# Supply Chain GHG Emission Factors Analysis

一个用于分析供应链温室气体（GHG）排放系数的 Python 项目。通过 NAICS 分类系统分析不同行业的环境影响。

**中文 | [English](#english)**

## 📋 项目概述

本项目对供应链 GHG 排放系数进行深入分析，量化不同经济部门的环保影响。通过组合行业特定排放数据与成本分析，为可持续性规划和碳会计提供见解。

### 🎯 主要功能
- **行业分类**：基于 NAICS（北美行业分类系统）的数据组织
- **排放系数**：CO2e（二氧化碳当量）测量
- **成本分析**：2021年美元基准的经济比较
- **数据处理**：模块化 Python 库用于加载、分析和可视化
- **可视化**：交互式图表和统计分析

## 📂 项目结构

```
SupplyChainGHG/
├── README.md                          # 项目文档
├── requirements.txt                   # 项目依赖
├── setup.py                           # 包安装配置
├── .gitignore                         # Git 忽略规则
│
├── data/                              # 数据目录
│   ├── raw/
│   │   └── SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv
│   └── processed/                     # 处理后的数据
│
├── src/                               # 源代码
│   └── ghg_analysis/
│       ├── __init__.py
│       ├── loader.py                  # 数据加载模块
│       ├── analyzer.py                # 分析模块
│       ├── visualizer.py              # 可视化模块
│       └── utils.py                   # 工具函数
│
├── notebooks/                         # Jupyter notebooks
│   └── 01_exploratory_analysis.ipynb
│
├── tests/                             # 单元测试
│   ├── __init__.py
│   ├── test_loader.py
│   └── test_analyzer.py
│
└── scripts/                           # 独立脚本
    └── process_data.py
```

## 🚀 快速开始

### 安装

```bash
# 克隆项目
git clone https://github.com/farmer0909/SupplyChainGHGEmissionFactors.git
cd SupplyChainGHGEmissionFactors

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

### 基本使用

```python
from ghg_analysis import GHGAnalyzer

# 初始化分析器
analyzer = GHGAnalyzer('data/raw/SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv')

# 加载数据
df = analyzer.load_data()

# 基本统计
print(analyzer.summary_statistics())

# 按行业分类
print(analyzer.emission_by_sector())

# 可视化
analyzer.plot_top_emitters(top_n=20)
analyzer.show_distribution()
```

## 📊 数据说明

**文件**：`SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv`

| 列名 | 描述 |
|------|------|
| 2017 NAICS Code | 行业代码 |
| 2017 NAICS Title | 行业名称 |
| GHG | 温室气体类型 |
| Unit | 测量单位 |
| Supply Chain Emission Factors without Margins | 不含边际成本的排放系数 |
| Margins of Supply Chain Emission Factors | 供应链排放系数的边际值 |
| Supply Chain Emission Factors with Margins | 含边际成本的排放系数 |
| Reference USEEIO Code | 参考代码 |

## 💡 使用场景

- **企业可持续发展**：跟踪供应链排放
- **环境影响评估**：量化部门级排放
- **政策分析**：支持气候相关政策发展
- **学术研究**：供应链 GHG 影响的实证分析

## 🔧 主要模块

### `ghg_analysis.loader`
- `load_csv()` - 加载 CSV 数据
- `validate_data()` - 数据验证
- `clean_data()` - 数据清理

### `ghg_analysis.analyzer`
- `GHGAnalyzer` - 主分析类
- `summary_statistics()` - 统计摘要
- `emission_by_sector()` - 按行业分析
- `filter_by_naics()` - 按 NAICS 代码筛选

### `ghg_analysis.visualizer`
- `plot_top_emitters()` - 绘制排放排行
- `show_distribution()` - 显示分布
- `sector_comparison()` - 行业对比图

## 📈 数据版本

- **版本**：1.2
- **基准年份**：2021 (USD)
- **最后更新**：2026
- **格式**：CSV

## 🧪 测试

```bash
# 运行所有测试
python -m pytest tests/

# 运行特定测试
python -m pytest tests/test_loader.py -v
```

## 📝 Notebook

- `01_exploratory_analysis.ipynb` - 探索性数据分析

## 🤝 贡献

欢迎贡献！你可以：
- 报告 issue 或数据错误
- 提出改进建议
- 增加新的可视化或见解
- 更新最新数据版本

## 📄 许可

本项目遵循 MIT 许可证。详见 LICENSE 文件。

## 📧 联系

如有问题，请通过 GitHub Issues 联系。

---

## English

### Overview
This project analyzes supply chain GHG emission factors to understand environmental impact across different economic sectors using NAICS classification.

### Key Features
- Industry classification by NAICS codes
- CO2e (Carbon Dioxide Equivalent) measurements
- Cost analysis in USD 2021
- Modular Python library for data processing and analysis
- Interactive visualizations and statistical analysis

### Quick Start
```bash
pip install -r requirements.txt
python -c "from ghg_analysis import GHGAnalyzer; a = GHGAnalyzer('data/raw/...csv'); print(a.summary_statistics())"
```

### License
MIT License

---

**Last Updated**: 2026-09-17  
**Author**: farmer0909  
**Repository**: https://github.com/farmer0909/SupplyChainGHGEmissionFactors
