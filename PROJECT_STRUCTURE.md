# Project Structure Overview

This document explains the complete structure of the project and the purpose of each file.

## 📁 Complete Project Structure

```
SupplyChainGHG/
│
├── README.md                          # Main project documentation
├── QUICKSTART.md                      # 5-minute quick start guide
├── PROJECT_STRUCTURE.md               # This file - detailed structure
├── MIGRATION_GUIDE_EN.md              # Migration guidance from old structure
├── LICENSE                            # MIT license
├── requirements.txt                   # Python dependency list
├── setup.py                           # Package installation config
├── .gitignore                         # Git ignore rules
│
├── src/ghg_analysis/                  # Core Python library 📦
│   ├── __init__.py                    # Package initialization
│   │   └── Exports: GHGDataLoader, GHGAnalyzer, GHGVisualizer
│   │
│   ├── loader.py                      # Data loading module (250+ lines)
│   │   └── GHGDataLoader class
│   │       ├── load() - Load CSV file
│   │       ├── validate() - Validate data structure
│   │       ├── clean() - Clean and normalize data
│   │       ├── get_data() - Get data copy
│   │       └── get_summary() - Get data summary
│   │
│   ├── analyzer.py                    # Analysis module (350+ lines)
│   │   └── GHGAnalyzer class
│   │       ├── load_and_prepare() - One-step loading
│   │       ├── summary_statistics() - Statistical summary
│   │       ├── top_emitters() - Top N industries
│   │       ├── emission_by_sector() - Sector-level analysis
│   │       ├── filter_by_naics() - Filter by NAICS code
│   │       ├── filter_by_industry() - Filter by industry name
│   │       ├── get_statistics_table() - Statistics table
│   │       ├── compare_industries() - Industry comparison
│   │       └── export_to_csv() - Export to CSV
│   │
│   ├── visualizer.py                  # Visualization module (350+ lines)
│   │   └── GHGVisualizer class
│   │       ├── plot_top_emitters() - Top emitters bar chart
│   │       ├── plot_distribution() - Distribution histogram
│   │       ├── plot_sector_comparison() - Sector comparison chart
│   │       ├── plot_margin_comparison() - Margin impact chart
│   │       └── plot_custom() - Custom plot support
│   │
│   └── utils.py                       # Utility functions module (250+ lines)
│       ├── get_naics_sector_name() - Convert NAICS code to sector
│       ├── calculate_emissions() - Calculate total emissions
│       ├── convert_emissions_unit() - Convert between units
│       ├── aggregate_by_sector() - Aggregate data by sector
│       ├── print_summary_report() - Print text summary
│       └── export_analysis_results() - Export complete results
│
├── data/                              # Data directory
│   ├── raw/                           # Raw data
│   │   └── SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv
│   │       (1,500+ rows, ~15 MB)
│   └── processed/                     # Processed output data
│
├── notebooks/                         # Jupyter notebooks 📓
│   └── 01_exploratory_analysis.ipynb  # Complete exploratory analysis
│       ├── Data loading and summary
│       ├── Statistical analysis
│       ├── Visualization examples
│       ├── Filtering and comparisons
│       ├── Emissions calculations
│       └── Results export
│
├── scripts/                           # Executable scripts 🔧
│   └── process_data.py                # Complete data processing pipeline
│       ├── Auto data loading
│       ├── Generate summary reports
│       ├── Create visualizations
│       ├── Export result files
│       └── Support command-line execution
│
├── tests/                             # Unit tests ✓
│   ├── __init__.py
│   ├── test_loader.py                 # GHGDataLoader tests
│   │   ├── test_load_csv
│   │   ├── test_file_not_found
│   │   ├── test_validate_data
│   │   ├── test_clean_data
│   │   └── test_get_summary
│   └── test_analyzer.py               # GHGAnalyzer tests
│       ├── test_initialization
│       ├── test_summary_statistics
│       ├── test_top_emitters
│       ├── test_filter_by_naics
│       ├── test_filter_by_industry
│       ├── test_get_statistics_table
│       └── test_compare_industries
│
└── output/                            # Output directory (generated)
    ├── emission_statistics.csv        # Statistics data table
    ├── sector_analysis.csv            # Sector analysis results
    ├── top_emitters.png               # Top emitters chart
    ├── distribution.png               # Distribution chart
    └── sector_comparison.png          # Sector comparison chart
```

## 📊 File Statistics

| Category | Files | Lines of Code |
|------|--------|---------|
| Core Library | 5 | 1,200+ |
| Data Files | 1 | 1,500+ rows |
| Tests | 2 | 200+ |
| Notebook | 1 | - |
| Scripts | 1 | 100+ |
| Documentation | 4 | - |
| **Total** | **14** | **3,000+** |

## 🎯 Module Dependencies

```
Users/CLI
  ↓
setup.py (package config)
  ↓
src/ghg_analysis/
  ├── __init__.py (exports main classes)
  ├── loader.py (data loading)
  │   └── pandas, pathlib
  ├── analyzer.py (data analysis)
  │   ├── loader.py
  │   └── pandas, numpy
  ├── visualizer.py (visualization)
  │   ├── analyzer.py
  │   └── matplotlib, seaborn
  └── utils.py (utility functions)
      ├── analyzer.py
      ├── visualizer.py
      └── pandas, pathlib

tests/
  ├── test_loader.py → loader.py
  └── test_analyzer.py → analyzer.py

scripts/
  └── process_data.py → all modules

notebooks/
  └── 01_exploratory_analysis.ipynb → all modules
```

## 🚀 Usage Methods

### Method 1: Command-line Execution
```bash
python scripts/process_data.py
```

### Method 2: Python Script Import
```python
from src.ghg_analysis import GHGAnalyzer

analyzer = GHGAnalyzer('data/raw/...csv')
analyzer.load_and_prepare()
# Use analyzer for analysis
```

### Method 3: Jupyter Notebook
```bash
jupyter notebook notebooks/01_exploratory_analysis.ipynb
```

### Method 4: Install as Package
```bash
pip install -e .
python -c "from ghg_analysis import GHGAnalyzer; ..."
```

## 📦 Dependencies

### Required (requirements.txt)
- pandas >= 1.3.0 - Data manipulation
- numpy >= 1.21.0 - Numerical computing
- matplotlib >= 3.4.0 - Plotting
- seaborn >= 0.11.0 - Statistical visualization
- jupyter >= 1.0.0 - Notebook environment
- pytest >= 6.2.0 - Unit testing
- pytest-cov >= 2.12.0 - Coverage reporting

## 📝 Design Features

### 1. Modular Design
- Each function in its own module
- Low coupling, high cohesion
- Easy to extend and maintain

### 2. Production-Quality Code
- Complete docstrings
- Type hints
- Error handling and validation
- Unit test coverage

### 3. Flexible Data Access
- Multiple filtering methods
- NAICS code matching
- Industry name search
- Custom filtering support

### 4. Multiple Visualizations
- 5 pre-built chart types
- Custom plotting support
- High-resolution output
- PNG/PDF export support

### 5. Complete Documentation
- English README
- Quick start guide
- Jupyter examples
- Detailed code comments

## 🔄 Data Flow

```
CSV Data File
    ↓
GHGDataLoader (load, validate, clean)
    ↓
GHGAnalyzer (analyze, filter, calculate)
    ↓
    ├─→ GHGVisualizer (create charts)
    ├─→ export_to_csv() (export tables)
    └─→ utils functions (compute, convert)
    ↓
Output Results (CSV, PNG, statistics)
```

## ✅ Quality Assurance

- **Test Coverage**: Comprehensive tests for loader.py and analyzer.py
- **Code Style**: Follows PEP 8 standards
- **Documentation**: All public functions have docstrings
- **Error Handling**: Robust exception handling and validation

## 🎓 Learning Path

1. **Beginner**: Read README.md and QUICKSTART.md
2. **User**: Run `scripts/process_data.py` script
3. **Researcher**: Open `notebooks/01_exploratory_analysis.ipynb`
4. **Developer**: Read source code in `src/` and tests in `tests/`

## 📄 Configuration Files

- **setup.py** - Package metadata and dependencies
- **requirements.txt** - pip dependencies list
- **.gitignore** - Git ignore rules (__pycache__, .pyc, venv, etc.)
- **LICENSE** - MIT license

## 🔗 Related Links

- GitHub: https://github.com/farmer0909/SupplyChainGHGEmissionFactors
- Data Source: USEEIO Supply Chain Emission Factors
- NAICS Classification: https://www.census.gov/naics/

---

**Created**: 2026-09-17  
**Version**: 1.0.0  
**Maintainer**: farmer0909
