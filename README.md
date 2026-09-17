# Supply Chain GHG Emission Factors Analysis

A Python project for analyzing supply chain greenhouse gas (GHG) emission factors across different industries. Leverages NAICS classification to quantify environmental impact by economic sector.

## 📋 Project Overview

This project provides comprehensive analysis of supply chain GHG emission factors, enabling detailed understanding of environmental impact across different economic sectors. By combining industry-specific emission data with cost analysis, it supports sustainable procurement decisions and carbon accounting.

### 🎯 Key Features
- **Industry Classification**: NAICS (North American Industry Classification System) organized data
- **Emission Factors**: CO2e (Carbon Dioxide Equivalent) measurements  
- **Cost Analysis**: Economic comparison in USD 2021 baseline
- **Data Processing**: Modular Python library for loading, analyzing, and visualizing data
- **Visualization**: Interactive charts and statistical analysis

## 📂 Project Structure

```
SupplyChainGHG/
├── README.md                          # Main project documentation
├── QUICKSTART.md                      # Quick start guide
├── PROJECT_STRUCTURE.md               # Detailed structure documentation
├── MIGRATION_GUIDE_EN.md              # Migration guidance
├── requirements.txt                   # Python dependencies
├── setup.py                           # Package installation config
├── .gitignore                         # Git ignore rules
│
├── data/                              # Data directory
│   ├── raw/
│   │   └── SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv
│   └── processed/                     # Processed output data
│
├── src/                               # Source code
│   └── ghg_analysis/
│       ├── __init__.py                # Package initialization
│       ├── loader.py                  # Data loading module
│       ├── analyzer.py                # Analysis engine
│       ├── visualizer.py              # Visualization module
│       └── utils.py                   # Utility functions
│
├── notebooks/                         # Jupyter notebooks
│   └── 01_exploratory_analysis.ipynb  # Complete exploratory analysis
│
├── tests/                             # Unit tests
│   ├── __init__.py
│   ├── test_loader.py
│   └── test_analyzer.py
│
└── scripts/                           # Executable scripts
    └── process_data.py                # Data processing pipeline
```

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/farmer0909/SupplyChainGHGEmissionFactors.git
cd SupplyChainGHGEmissionFactors

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from ghg_analysis import GHGAnalyzer, GHGVisualizer

# Initialize analyzer
analyzer = GHGAnalyzer('data/raw/SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv')

# Get summary statistics
stats = analyzer.summary_statistics()
print(f"Average emission: {stats['mean_emission']:.4f} kg CO2e/USD")

# Get top emitters
top_10 = analyzer.top_emitters(top_n=10)
print(top_10)

# Filter by NAICS code (agriculture)
agriculture = analyzer.filter_by_naics('11')

# Create visualizations
viz = GHGVisualizer(analyzer)
viz.plot_top_emitters(top_n=20, save_path='output/top_emitters.png')
```

## 📊 Data Description

**File**: `SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv`

| Column Name | Description |
|------|------|
| 2017 NAICS Code | Industry classification code |
| 2017 NAICS Title | Industry classification title |
| GHG | Type of greenhouse gas |
| Unit | Measurement unit |
| Supply Chain Emission Factors without Margins | Emission factor without margins |
| Margins of Supply Chain Emission Factors | Margin value for emission factor |
| Supply Chain Emission Factors with Margins | Emission factor with margins included |
| Reference USEEIO Code | USEEIO reference code |

## 💡 Use Cases

- **Corporate Sustainability**: Track supply chain emissions for procurement
- **Environmental Impact Assessment**: Quantify sector-level emissions
- **Policy Analysis**: Support climate-related policy development
- **Academic Research**: Empirical analysis of supply chain GHG impacts
- **Carbon Accounting**: Calculate product carbon footprint

## 🔧 Core Modules

### `GHGDataLoader` (loader.py)
- `load()` - Load CSV data
- `validate()` - Validate data structure
- `clean()` - Clean and normalize data
- `get_data()` - Get data copy
- `get_summary()` - Get data summary

### `GHGAnalyzer` (analyzer.py)
- `load_and_prepare()` - One-step data loading
- `summary_statistics()` - Statistical summary
- `top_emitters(top_n)` - Top N industries by emission
- `emission_by_sector()` - Aggregate by sector
- `filter_by_naics(code)` - Filter by NAICS code
- `filter_by_industry(name)` - Filter by industry name
- `compare_industries(names)` - Compare multiple industries
- `export_to_csv(path)` - Export results to CSV

### `GHGVisualizer` (visualizer.py)
- `plot_top_emitters()` - Bar chart of top emitters
- `plot_distribution()` - Distribution histogram
- `plot_sector_comparison()` - Sector-level comparison
- `plot_margin_comparison()` - Margin impact visualization
- `plot_custom()` - Custom plot support

## 📈 Dataset Version

- **Version**: 1.2
- **Reference Year**: 2021 (USD)
- **Last Updated**: 2026
- **Format**: CSV
- **Source**: USEEIO Supply Chain Emission Factors

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_loader.py -v

# Run with coverage
pytest tests/ --cov=src/ghg_analysis
```

## 📝 Jupyter Notebook

- `01_exploratory_analysis.ipynb` - Complete exploratory data analysis example
  - Data loading and summary
  - Statistical analysis
  - Visualizations
  - Filtering and comparisons
  - Emissions calculations
  - Results export

## 🚀 Running the Pipeline

```bash
# Run the complete data processing pipeline
python scripts/process_data.py

# This will:
# - Load and validate data
# - Generate summary reports
# - Create visualizations
# - Export results to output/
```

## 🤝 Contributing

Contributions are welcome! You can:
- Report issues or data errors
- Suggest improvements
- Add new visualizations or analyses
- Update to latest dataset versions
- Improve documentation

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 📧 Contact & Support

For questions or issues, please open an issue on GitHub.

---

**Last Updated**: 2026-09-17  
**Author**: farmer0909  
**Repository**: https://github.com/farmer0909/SupplyChainGHGEmissionFactors  
**Python**: 3.8+
