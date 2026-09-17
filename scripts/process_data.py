"""
Script to process and analyze GHG emission factors data.

This script demonstrates the full pipeline from loading to analysis.
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ghg_analysis import GHGAnalyzer, GHGVisualizer
from ghg_analysis.utils import print_summary_report, export_analysis_results


def main():
    """Main execution function."""

    # Define data path
    project_root = Path(__file__).parent.parent
    data_path = project_root / 'data' / 'raw' / 'SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv'

    # Check if data file exists
    if not data_path.exists():
        print(f"❌ Data file not found: {data_path}")
        print("Please ensure the CSV file is in data/raw/ directory")
        return

    print(f"📊 Loading data from: {data_path}\n")

    # Initialize analyzer
    analyzer = GHGAnalyzer(str(data_path))

    # Print summary report
    print_summary_report(analyzer)

    # Get top emitters
    print("\nTop 10 Highest Emission Industries:")
    print("-" * 70)
    top_10 = analyzer.top_emitters(top_n=10)
    print(top_10.to_string(index=False))

    # Sector analysis
    print("\n\nEmission Factors by Sector:")
    print("-" * 70)
    sector_stats = analyzer.emission_by_sector()
    print(sector_stats)

    # Filter by sector
    print("\n\nAgriculture Sector (NAICS 11):")
    print("-" * 70)
    agriculture = analyzer.filter_by_naics('11')
    print(agriculture.head(10).to_string(index=False))

    # Industry comparison
    print("\n\nIndustry Comparison:")
    print("-" * 70)
    comparison = analyzer.compare_industries([
        'Farming', 'Mining', 'Manufacturing', 'Retail', 'Utilities'
    ])
    print(comparison.to_string(index=False))

    # Create visualizations
    print("\n\n📈 Generating visualizations...\n")
    visualizer = GHGVisualizer(analyzer)

    output_dir = project_root / 'output'
    output_dir.mkdir(exist_ok=True)

    try:
        print("Creating top emitters plot...")
        visualizer.plot_top_emitters(top_n=20, save_path=str(output_dir / 'top_emitters.png'))

        print("Creating distribution plot...")
        visualizer.plot_distribution(save_path=str(output_dir / 'distribution.png'))

        print("Creating sector comparison plot...")
        visualizer.plot_sector_comparison(save_path=str(output_dir / 'sector_comparison.png'))

        print("\n✅ Visualizations saved to output/ directory\n")
    except Exception as e:
        print(f"⚠️  Note: Could not generate plots (matplotlib backend issue): {e}")
        print("   Plots can be generated in an interactive environment\n")

    # Export results
    print("📁 Exporting analysis results...")
    exported = export_analysis_results(
        analyzer,
        output_dir=str(output_dir),
        include_plots=False  # Already created above
    )

    print("\n✅ Analysis complete!")
    print(f"\nExported files in {output_dir}:")
    for key, path in exported.items():
        print(f"  - {key}: {path}")


if __name__ == '__main__':
    main()
