"""
Data loader module for GHG emission factors.

This module handles loading, validating, and cleaning the supply chain GHG data.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Union, Optional, Dict, Any


class GHGDataLoader:
    """Load and validate GHG emission factors data."""

    # Expected columns in the dataset
    EXPECTED_COLUMNS = {
        '2017 NAICS Code': 'NAICS_Code',
        '2017 NAICS Title': 'Industry_Name',
        'GHG': 'GHG_Type',
        'Unit': 'Unit',
        'Supply Chain Emission Factors without Margins': 'Emission_Without_Margins',
        'Margins of Supply Chain Emission Factors': 'Margins',
        'Supply Chain Emission Factors with Margins': 'Emission_With_Margins',
        'Reference USEEIO Code': 'USEEIO_Code'
    }

    def __init__(self, filepath: Union[str, Path], verbose: bool = True):
        """
        Initialize the data loader.

        Args:
            filepath: Path to the CSV file
            verbose: Print status messages
        """
        self.filepath = Path(filepath)
        self.verbose = verbose
        self.data: Optional[pd.DataFrame] = None

        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {self.filepath}")

    def load(self) -> pd.DataFrame:
        """
        Load the CSV data file.

        Returns:
            DataFrame with loaded data
        """
        if self.verbose:
            print(f"Loading data from {self.filepath}...")

        try:
            self.data = pd.read_csv(self.filepath)
            if self.verbose:
                print(f"✓ Loaded {len(self.data)} rows")
            return self.data
        except Exception as e:
            raise ValueError(f"Error loading CSV file: {e}")

    def validate(self) -> bool:
        """
        Validate the data structure.

        Returns:
            True if valid, raises exception otherwise
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load() first.")

        # Check required columns exist
        missing_cols = set(self.EXPECTED_COLUMNS.keys()) - set(self.data.columns)
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")

        # Check for empty data
        if self.data.empty:
            raise ValueError("Dataset is empty")

        # Check numeric columns
        numeric_cols = [
            'Supply Chain Emission Factors without Margins',
            'Margins of Supply Chain Emission Factors',
            'Supply Chain Emission Factors with Margins'
        ]

        for col in numeric_cols:
            if not pd.api.types.is_numeric_dtype(self.data[col]):
                raise ValueError(f"Column '{col}' should be numeric")

        if self.verbose:
            print("✓ Data validation passed")

        return True

    def clean(self) -> pd.DataFrame:
        """
        Clean and standardize the data.

        Returns:
            Cleaned DataFrame
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load() first.")

        df = self.data.copy()

        # Remove duplicate rows
        initial_rows = len(df)
        df = df.drop_duplicates()
        duplicates_removed = initial_rows - len(df)

        if duplicates_removed > 0 and self.verbose:
            print(f"✓ Removed {duplicates_removed} duplicate rows")

        # Handle missing values
        missing_before = df.isnull().sum().sum()

        # For numeric columns, fill with 0 if needed (or drop rows)
        numeric_cols = [
            'Supply Chain Emission Factors without Margins',
            'Margins of Supply Chain Emission Factors',
            'Supply Chain Emission Factors with Margins'
        ]

        df[numeric_cols] = df[numeric_cols].fillna(0)

        missing_after = df.isnull().sum().sum()
        if missing_before > missing_after and self.verbose:
            print(f"✓ Handled {missing_before - missing_after} missing values")

        # Ensure NAICS codes are strings (with leading zeros preserved)
        if '2017 NAICS Code' in df.columns:
            df['2017 NAICS Code'] = df['2017 NAICS Code'].astype(str)

        self.data = df
        return df

    def get_data(self) -> pd.DataFrame:
        """
        Get the loaded data.

        Returns:
            DataFrame
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load() first.")
        return self.data.copy()

    def get_summary(self) -> Dict[str, Any]:
        """
        Get summary statistics of the data.

        Returns:
            Dictionary with summary information
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load() first.")

        return {
            'total_rows': len(self.data),
            'total_columns': len(self.data.columns),
            'industries': self.data['2017 NAICS Title'].nunique(),
            'ghg_types': self.data['GHG'].nunique() if 'GHG' in self.data.columns else 0,
            'memory_usage_mb': self.data.memory_usage(deep=True).sum() / 1024**2,
        }
