# Supply Chain GHG Emission Factors Analysis

A comprehensive analysis of supply chain greenhouse gas (GHG) emission factors across different industries using the NAICS classification system.

## 📋 Project Overview

This project analyzes supply chain GHG emission factors to understand and quantify the environmental impact of different economic sectors. It combines industry-specific emission data with cost analysis to provide insights for sustainability planning and carbon accounting.

### Key Features
- **Industry Classification**: Data organized by NAICS (North American Industry Classification System)
- **Emission Factors**: CO2e (Carbon Dioxide Equivalent) measurements
- **Cost Analysis**: USD 2021 baseline for economic comparison
- **Jupyter Notebook**: Interactive analysis and visualizations

## 📂 Repository Structure

```
SupplyChainGHGEmissionFactors/
├── README.md                                                    # Project documentation
├── SupplyChainGHGEmissionFactors_Analyst.ipynb                 # Main analysis notebook
└── SupplyChainGHGEmissionFactors_v1_2_NAICS_CO2e_USD2021.csv   # Dataset
```

## 📊 Dataset Description

**File**: `SupplyChainGHGEmissionFactors_v1_2_NAICS_CO2e_USD2021.csv`

- **Source**: Supply chain GHG emission factors database
- **Classification**: NAICS industry codes
- **Measurement Unit**: CO2e (metric tons per USD 2021)
- **Version**: 1.2
- **Scope**: Comprehensive supply chain emissions across sectors

### Dataset Columns (Typical)
- Industry Name & NAICS Code
- Emission Factor (CO2e per USD)
- Sector Classification
- Data Year (2021 baseline)

## 📓 Notebook Contents

**File**: `SupplyChainGHGEmissionFactors_Analyst.ipynb`

The notebook includes:
- Data loading and exploration
- Emission factor analysis by industry
- Visualization of emission patterns
- Statistical insights
- Comparative analysis across sectors

### How to Use

1. **View on GitHub**: Click the notebook file to preview in the browser
2. **Download & Run Locally**:
   ```bash
   git clone https://github.com/farmer0909/SupplyChainGHGEmissionFactors.git
   cd SupplyChainGHGEmissionFactors
   jupyter notebook SupplyChainGHGEmissionFactors_Analyst.ipynb
   ```
3. **Requirements**:
   ```
   pandas
   numpy
   matplotlib
   seaborn
   jupyter
   ```

## 🔍 Key Insights

This analysis helps to:
- Identify high-emission industries
- Compare emission factors across sectors
- Support carbon accounting and reporting
- Inform sustainable supply chain decisions
- Benchmark against industry standards

## 💡 Use Cases

- **Corporate Sustainability**: Track supply chain emissions
- **Environmental Impact Assessment**: Quantify sector-level emissions
- **Policy Analysis**: Support climate-related policy development
- **Research**: Empirical analysis of supply chain GHG impacts

## 📈 Data Version

- **Version**: 1.2
- **Baseline Year**: 2021 (USD)
- **Last Updated**: 2026
- **Format**: CSV (easily importable to Excel, Python, R, etc.)

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report issues or data errors
- Suggest improvements to the analysis
- Add new visualizations or insights
- Update with newer data versions

## 📄 License

Please check the license file for usage terms. This data is provided for analytical and research purposes.

## 📧 Contact

For questions or inquiries about this project, please reach out through GitHub Issues.

---

**Last Updated**: August 2026  
**Author**: farmer0909  
**Repository**: https://github.com/farmer0909/SupplyChainGHGEmissionFactors
