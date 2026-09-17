"""Unit tests for the analyzer module."""

import pytest
import pandas as pd
import tempfile
import os
import sys

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ghg_analysis.analyzer import GHGAnalyzer


@pytest.fixture
def sample_csv():
    """Create a sample CSV file for testing."""
    data = {
        '2017 NAICS Code': ['111110', '111120', '111130', '211000', '221000'],
        '2017 NAICS Title': ['Soybean Farming', 'Oilseed Farming', 'Dry Pea Farming',
                             'Oil and Gas Extraction', 'Power Generation'],
        'GHG': ['All GHGs', 'All GHGs', 'All GHGs', 'All GHGs', 'All GHGs'],
        'Unit': ['kg CO2e/2021 USD'] * 5,
        'Supply Chain Emission Factors without Margins': [1.223, 1.223, 2.874, 0.5, 0.3],
        'Margins of Supply Chain Emission Factors': [0.103, 0.103, 0.134, 0.05, 0.03],
        'Supply Chain Emission Factors with Margins': [1.326, 1.326, 3.007, 0.55, 0.33],
        'Reference USEEIO Code': ['1111A0', '1111A0', '1111B0', '2110', '2211']
    }

    df = pd.DataFrame(data)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        df.to_csv(f.name, index=False)
        temp_path = f.name

    yield temp_path

    if os.path.exists(temp_path):
        os.unlink(temp_path)


class TestGHGAnalyzer:
    """Test suite for GHGAnalyzer class."""

    def test_initialization(self, sample_csv):
        """Test analyzer initialization."""
        analyzer = GHGAnalyzer(sample_csv)
        assert analyzer.data is not None
        assert len(analyzer.data) == 5

    def test_summary_statistics(self, sample_csv):
        """Test summary statistics calculation."""
        analyzer = GHGAnalyzer(sample_csv)
        stats = analyzer.summary_statistics()

        assert 'mean_emission' in stats
        assert 'median_emission' in stats
        assert 'std_emission' in stats
        assert stats['mean_emission'] > 0

    def test_top_emitters(self, sample_csv):
        """Test getting top emitters."""
        analyzer = GHGAnalyzer(sample_csv)
        top = analyzer.top_emitters(top_n=3)

        assert len(top) == 3
        assert 'Emission_Factor' in top.columns
        # Should be sorted descending
        assert top.iloc[0]['Emission_Factor'] >= top.iloc[1]['Emission_Factor']

    def test_filter_by_naics(self, sample_csv):
        """Test filtering by NAICS code."""
        analyzer = GHGAnalyzer(sample_csv)
        result = analyzer.filter_by_naics('11')  # Agriculture

        assert len(result) == 3  # Should find 3 agriculture entries

    def test_filter_by_industry(self, sample_csv):
        """Test filtering by industry name."""
        analyzer = GHGAnalyzer(sample_csv)
        result = analyzer.filter_by_industry('Farming')

        assert len(result) == 3

    def test_get_statistics_table(self, sample_csv):
        """Test getting statistics table."""
        analyzer = GHGAnalyzer(sample_csv)
        table = analyzer.get_statistics_table()

        assert 'Industry' in table.columns
        assert 'Emission_Factor' in table.columns
        assert len(table) == 5

    def test_compare_industries(self, sample_csv):
        """Test industry comparison."""
        analyzer = GHGAnalyzer(sample_csv)
        result = analyzer.compare_industries(['Farming', 'Extraction'])

        assert 'Industry' in result.columns
        assert 'Mean_Emission' in result.columns


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
