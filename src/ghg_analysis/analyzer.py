"""
Analyzer module for GHG emission factors analysis.

This module provides analysis functions for supply chain GHG data.
"""

import pandas as pd
import numpy as np
from typing import Optional, List, Dict, Any
from .loader import GHGDataLoader


class GHGAnalyzer:
    """Analyze supply chain GHG emission factors."""

    def __init__(self, filepath: str, auto_load: bool = True):
        """
        Initialize the analyzer.

        Args:
            filepath: Path to the CSV data file
            auto_load: Automatically load and clean data
        """
        self.loader = GHGDataLoader(filepath)
        self.data: Optional[pd.DataFrame] = None

        if auto_load:
            self.load_and_prepare()

    def load_and_prepare(self) -> pd.DataFrame:
        """
        Load, validate, and clean data in one step.

        Returns:
            Prepared DataFrame
        """
        self.data = self.loader.load()
        self.loader.validate()
        self.data = self.loader.clean()
        return self.data

    def summary_statistics(self) -> Dict[str, Any]:
        """
        Get summary statistics of emission factors.

        Returns:
            Dictionary with statistics
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_and_prepare() first.")

        emission_col = 'Supply Chain Emission Factors with Margins'

        return {
            'total_industries': len(self.data),
            'mean_emission': self.data[emission_col].mean(),
            'median_emission': self.data[emission_col].median(),
            'std_emission': self.data[emission_col].std(),
            'min_emission': self.data[emission_col].min(),
            'max_emission': self.data[emission_col].max(),
            'q25': self.data[emission_col].quantile(0.25),
            'q75': self.data[emission_col].quantile(0.75),
        }

    def top_emitters(self, top_n: int = 20, margin_type: str = 'with') -> pd.DataFrame:
        """
        Get industries with highest emission factors.

        Args:
            top_n: Number of top industries to return
            margin_type: 'with' or 'without' margins

        Returns:
            DataFrame with top emitters
        """
        if self.data is None:
            raise ValueError("Data not loaded.")

        if margin_type == 'with':
            col = 'Supply Chain Emission Factors with Margins'
        else:
            col = 'Supply Chain Emission Factors without Margins'

        result = self.data[['2017 NAICS Code', '2017 NAICS Title', col]].copy()
        result.columns = ['NAICS_Code', 'Industry', 'Emission_Factor']
        result = result.sort_values('Emission_Factor', ascending=False).head(top_n)

        return result.reset_index(drop=True)

    def emission_by_sector(self) -> pd.DataFrame:
        """
        Analyze emissions grouped by major sectors.

        Returns:
            DataFrame with sector-level statistics
        """
        if self.data is None:
            raise ValueError("Data not loaded.")

        # Extract sector from NAICS code (first 2-3 digits)
        df = self.data.copy()
        df['Sector_Code'] = df['2017 NAICS Code'].str[:2]

        emission_col = 'Supply Chain Emission Factors with Margins'

        sector_stats = df.groupby('Sector_Code').agg({
            emission_col: ['mean', 'median', 'min', 'max', 'std', 'count'],
            '2017 NAICS Title': 'count'
        }).round(4)

        return sector_stats

    def filter_by_naics(self, naics_code: str) -> pd.DataFrame:
        """
        Filter data by specific NAICS code (supports wildcards).

        Args:
            naics_code: NAICS code or partial code (e.g., '11' for agriculture)

        Returns:
            Filtered DataFrame
        """
        if self.data is None:
            raise ValueError("Data not loaded.")

        result = self.data[
            self.data['2017 NAICS Code'].astype(str).str.startswith(naics_code)
        ]

        return result[['2017 NAICS Code', '2017 NAICS Title',
                       'Supply Chain Emission Factors with Margins']].copy()

    def filter_by_industry(self, industry_name: str, case_sensitive: bool = False) -> pd.DataFrame:
        """
        Filter data by industry name (partial match).

        Args:
            industry_name: Industry name to search for
            case_sensitive: Whether to match case

        Returns:
            Filtered DataFrame
        """
        if self.data is None:
            raise ValueError("Data not loaded.")

        if case_sensitive:
            mask = self.data['2017 NAICS Title'].str.contains(industry_name)
        else:
            mask = self.data['2017 NAICS Title'].str.contains(
                industry_name, case=False
            )

        return self.data[mask].copy()

    def get_statistics_table(self) -> pd.DataFrame:
        """
        Get detailed statistics for all industries.

        Returns:
            DataFrame with statistics
        """
        if self.data is None:
            raise ValueError("Data not loaded.")

        emission_col = 'Supply Chain Emission Factors with Margins'

        result = self.data[[
            '2017 NAICS Code',
            '2017 NAICS Title',
            emission_col
        ]].copy()

        result.columns = ['NAICS_Code', 'Industry', 'Emission_Factor']
        result = result.sort_values('Emission_Factor', ascending=False)

        return result.reset_index(drop=True)

    def compare_industries(self, industry_list: List[str]) -> pd.DataFrame:
        """
        Compare emission factors between specific industries.

        Args:
            industry_list: List of industry names to compare

        Returns:
            DataFrame with comparison data
        """
        if self.data is None:
            raise ValueError("Data not loaded.")

        results = []
        emission_col = 'Supply Chain Emission Factors with Margins'

        for industry in industry_list:
            matches = self.data[
                self.data['2017 NAICS Title'].str.contains(industry, case=False)
            ]
            if not matches.empty:
                results.append({
                    'Industry': industry,
                    'Match_Count': len(matches),
                    'Mean_Emission': matches[emission_col].mean(),
                    'Min_Emission': matches[emission_col].min(),
                    'Max_Emission': matches[emission_col].max(),
                })

        return pd.DataFrame(results)

    def export_to_csv(self, output_path: str, data: Optional[pd.DataFrame] = None) -> str:
        """
        Export analysis results to CSV.

        Args:
            output_path: Path for output file
            data: DataFrame to export (uses self.data if None)

        Returns:
            Path to exported file
        """
        if data is None:
            if self.data is None:
                raise ValueError("No data to export.")
            data = self.data

        data.to_csv(output_path, index=False)
        return output_path
