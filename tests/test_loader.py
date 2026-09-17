"""Unit tests for the loader module."""

import pytest
import pandas as pd
import tempfile
import os
from pathlib import Path
import sys

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ghg_analysis.loader import GHGDataLoader


@pytest.fixture
def sample_csv():
    """Create a sample CSV file for testing."""
    data = {
        '2017 NAICS Code': ['111110', '111120', '111130'],
        '2017 NAICS Title': ['Soybean Farming', 'Oilseed Farming', 'Dry Pea Farming'],
        'GHG': ['All GHGs', 'All GHGs', 'All GHGs'],
        'Unit': ['kg CO2e/2021 USD', 'kg CO2e/2021 USD', 'kg CO2e/2021 USD'],
        'Supply Chain Emission Factors without Margins': [1.223, 1.223, 2.874],
        'Margins of Supply Chain Emission Factors': [0.103, 0.103, 0.134],
        'Supply Chain Emission Factors with Margins': [1.326, 1.326, 3.007],
        'Reference USEEIO Code': ['1111A0', '1111A0', '1111B0']
    }

    df = pd.DataFrame(data)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        df.to_csv(f.name, index=False)
        temp_path = f.name

    yield temp_path

    # Cleanup
    if os.path.exists(temp_path):
        os.unlink(temp_path)


class TestGHGDataLoader:
    """Test suite for GHGDataLoader class."""

    def test_load_csv(self, sample_csv):
        """Test loading CSV file."""
        loader = GHGDataLoader(sample_csv)
        df = loader.load()

        assert df is not None
        assert len(df) == 3
        assert '2017 NAICS Code' in df.columns

    def test_file_not_found(self):
        """Test error handling for non-existent file."""
        with pytest.raises(FileNotFoundError):
            GHGDataLoader('/non/existent/path.csv')

    def test_validate_data(self, sample_csv):
        """Test data validation."""
        loader = GHGDataLoader(sample_csv)
        loader.load()

        assert loader.validate() == True

    def test_clean_data(self, sample_csv):
        """Test data cleaning."""
        loader = GHGDataLoader(sample_csv)
        loader.load()
        df_clean = loader.clean()

        assert df_clean is not None
        assert len(df_clean) >= 0

    def test_get_summary(self, sample_csv):
        """Test getting data summary."""
        loader = GHGDataLoader(sample_csv)
        loader.load()
        summary = loader.get_summary()

        assert 'total_rows' in summary
        assert 'total_columns' in summary
        assert summary['total_rows'] == 3


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
