"""
Utility functions for GHG analysis.
"""

import pandas as pd
from typing import Dict, Any, List, Optional


def get_naics_sector_name(naics_code: str) -> str:
    """
    Get sector name from NAICS code.

    Args:
        naics_code: 2-6 digit NAICS code

    Returns:
        Sector name
    """
    sector_map = {
        '11': 'Agriculture, Forestry, Fishing and Hunting',
        '21': 'Mining, Quarrying, and Oil and Gas Extraction',
        '22': 'Utilities',
        '23': 'Construction',
        '31': 'Manufacturing',
        '32': 'Manufacturing',
        '33': 'Manufacturing',
        '42': 'Wholesale Trade',
        '44': 'Retail Trade',
        '45': 'Retail Trade',
        '48': 'Transportation and Warehousing',
        '49': 'Transportation and Warehousing',
        '51': 'Information',
        '52': 'Finance and Insurance',
        '53': 'Real Estate and Rental and Leasing',
        '54': 'Professional, Scientific, and Technical Services',
        '55': 'Management of Companies and Enterprises',
        '56': 'Administrative and Support and Waste Services',
        '61': 'Educational Services',
        '62': 'Health Care and Social Assistance',
        '71': 'Arts, Entertainment, and Recreation',
        '72': 'Accommodation and Food Services',
        '81': 'Other Services (except Public Administration)',
        '92': 'Public Administration',
    }

    # Extract first 2 digits
    sector_code = str(naics_code)[:2]
    return sector_map.get(sector_code, f'Unknown Sector ({sector_code})')


def calculate_emissions(amount_usd: float, emission_factor: float) -> float:
    """
    Calculate total emissions for a given amount.

    Args:
        amount_usd: Amount in 2021 USD
        emission_factor: kg CO2e per USD

    Returns:
        Total emissions in kg CO2e
    """
    return amount_usd * emission_factor


def convert_emissions_unit(emissions_kg: float, target_unit: str = 'tonnes') -> float:
    """
    Convert emissions to different units.

    Args:
        emissions_kg: Emissions in kg
        target_unit: 'tonnes', 'metric_tonnes', 'lbs', 'oz'

    Returns:
        Converted emissions
    """
    conversions = {
        'tonnes': 1000,  # kg to metric tonnes
        'metric_tonnes': 1000,
        'lbs': 2.20462,  # kg to pounds
        'oz': 35.274,  # kg to ounces
        'kg': 1,  # kg to kg (no conversion)
    }

    if target_unit not in conversions:
        raise ValueError(f"Unknown unit: {target_unit}")

    return emissions_kg / conversions[target_unit]


def aggregate_by_sector(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate emission data by sector.

    Args:
        df: DataFrame with NAICS codes and emission factors

    Returns:
        Aggregated DataFrame by sector
    """
    if 'Sector' not in df.columns:
        df['Sector'] = df['2017 NAICS Code'].str[:2]

    emission_col = 'Supply Chain Emission Factors with Margins'

    result = df.groupby('Sector').agg({
        emission_col: ['mean', 'median', 'min', 'max', 'std'],
        '2017 NAICS Title': 'count'
    }).round(4)

    result.columns = ['Mean', 'Median', 'Min', 'Max', 'Std', 'Industry_Count']
    result['Sector_Name'] = [get_naics_sector_name(code) for code in result.index]

    return result


def print_summary_report(analyzer) -> None:
    """
    Print a comprehensive summary report.

    Args:
        analyzer: GHGAnalyzer instance
    """
    stats = analyzer.summary_statistics()

    print("\n" + "="*70)
    print(" GHG EMISSION FACTORS - SUMMARY REPORT")
    print("="*70)
    print(f"\nTotal Industries:        {stats['total_industries']}")
    print(f"Mean Emission Factor:    {stats['mean_emission']:.4f} kg CO2e/USD")
    print(f"Median Emission Factor:  {stats['median_emission']:.4f} kg CO2e/USD")
    print(f"Std Deviation:           {stats['std_emission']:.4f}")
    print(f"\nRange:")
    print(f"  Minimum:               {stats['min_emission']:.4f} kg CO2e/USD")
    print(f"  Maximum:               {stats['max_emission']:.4f} kg CO2e/USD")
    print(f"  Q1 (25th percentile):  {stats['q25']:.4f}")
    print(f"  Q3 (75th percentile):  {stats['q75']:.4f}")

    print("\n" + "-"*70)
    print("\nTop 10 Highest Emission Industries:")
    print("-"*70)

    top_10 = analyzer.top_emitters(top_n=10)
    for idx, row in top_10.iterrows():
        print(f"{idx+1:2d}. {row['Industry']:<45} {row['Emission_Factor']:>10.4f}")

    print("\n" + "="*70 + "\n")


def export_analysis_results(
    analyzer,
    output_dir: str = './output',
    include_plots: bool = True
) -> Dict[str, str]:
    """
    Export complete analysis results to files.

    Args:
        analyzer: GHGAnalyzer instance
        output_dir: Output directory path
        include_plots: Whether to generate plots

    Returns:
        Dictionary mapping file type to file paths
    """
    import os
    from pathlib import Path

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    exported_files = {}

    # Export statistics
    stats_df = analyzer.get_statistics_table()
    stats_file = output_path / 'emission_statistics.csv'
    stats_df.to_csv(stats_file, index=False)
    exported_files['statistics'] = str(stats_file)
    print(f"✓ Statistics exported to {stats_file}")

    # Export sector analysis
    sector_df = analyzer.emission_by_sector()
    sector_file = output_path / 'sector_analysis.csv'
    sector_df.to_csv(sector_file)
    exported_files['sector_analysis'] = str(sector_file)
    print(f"✓ Sector analysis exported to {sector_file}")

    # Generate plots if requested
    if include_plots:
        from .visualizer import GHGVisualizer
        viz = GHGVisualizer(analyzer)

        # Top emitters plot
        plot_file = output_path / 'top_emitters.png'
        viz.plot_top_emitters(top_n=20, save_path=str(plot_file))
        exported_files['top_emitters'] = str(plot_file)

        # Distribution plot
        dist_file = output_path / 'distribution.png'
        viz.plot_distribution(save_path=str(dist_file))
        exported_files['distribution'] = str(dist_file)

        # Sector comparison plot
        sector_file = output_path / 'sector_comparison.png'
        viz.plot_sector_comparison(save_path=str(sector_file))
        exported_files['sector_comparison'] = str(sector_file)

    return exported_files
