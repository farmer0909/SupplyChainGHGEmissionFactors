# Project Structure Overview

本文档说明项目的完整结构和各文件的用途。

## 📁 完整项目结构

```
SupplyChainGHG/
│
├── README.md                          # 项目主文档（中英文）
├── QUICKSTART.md                      # 快速开始指南
├── PROJECT_STRUCTURE.md               # 本文件 - 项目结构说明
├── LICENSE                            # MIT 许可证
├── requirements.txt                   # Python 依赖列表
├── setup.py                           # 包安装配置
├── .gitignore                         # Git 忽略规则
│
├── src/ghg_analysis/                  # 核心 Python 库 📦
│   ├── __init__.py                    # 包初始化，导出主类
│   │   └── 导出: GHGDataLoader, GHGAnalyzer, GHGVisualizer
│   │
│   ├── loader.py                      # 数据加载模块 (250+ 行)
│   │   └── GHGDataLoader 类
│   │       ├── load() - 加载 CSV 文件
│   │       ├── validate() - 验证数据结构
│   │       ├── clean() - 清理数据
│   │       ├── get_data() - 获取数据副本
│   │       └── get_summary() - 数据摘要
│   │
│   ├── analyzer.py                    # 分析模块 (350+ 行)
│   │   └── GHGAnalyzer 类
│   │       ├── load_and_prepare() - 一步加载
│   │       ├── summary_statistics() - 统计摘要
│   │       ├── top_emitters() - 排放排行
│   │       ├── emission_by_sector() - 按部门分析
│   │       ├── filter_by_naics() - NAICS 代码筛选
│   │       ├── filter_by_industry() - 行业名称筛选
│   │       ├── get_statistics_table() - 统计表
│   │       ├── compare_industries() - 行业对比
│   │       └── export_to_csv() - 导出 CSV
│   │
│   ├── visualizer.py                  # 可视化模块 (350+ 行)
│   │   └── GHGVisualizer 类
│   │       ├── plot_top_emitters() - 排放排行图
│   │       ├── plot_distribution() - 分布直方图
│   │       ├── plot_sector_comparison() - 部门对比
│   │       ├── plot_margin_comparison() - 边际对比
│   │       └── plot_custom() - 自定义图表
│   │
│   └── utils.py                       # 工具函数模块 (250+ 行)
│       ├── get_naics_sector_name() - NAICS 代码转换
│       ├── calculate_emissions() - 排放计算
│       ├── convert_emissions_unit() - 单位转换
│       ├── aggregate_by_sector() - 按部门聚合
│       ├── print_summary_report() - 打印摘要报告
│       └── export_analysis_results() - 导出结果
│
├── data/                              # 数据目录
│   ├── raw/                           # 原始数据
│   │   └── SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv
│   │       (1,500+ 行，15 MB)
│   └── processed/                     # 处理后的数据（输出用）
│
├── notebooks/                         # Jupyter 笔记本 📓
│   └── 01_exploratory_analysis.ipynb  # 完整的探索性分析
│       ├── 数据加载和摘要
│       ├── 统计分析
│       ├── 可视化演示
│       ├── 筛选和比较
│       ├── 排放计算示例
│       └── 结果导出
│
├── scripts/                           # 执行脚本 🔧
│   └── process_data.py                # 完整的数据处理管道
│       ├── 自动加载数据
│       ├── 生成摘要报告
│       ├── 创建可视化
│       ├── 导出结果文件
│       └── 支持命令行执行
│
├── tests/                             # 单元测试 ✓
│   ├── __init__.py
│   ├── test_loader.py                 # Loader 类测试
│   │   ├── test_load_csv
│   │   ├── test_file_not_found
│   │   ├── test_validate_data
│   │   ├── test_clean_data
│   │   └── test_get_summary
│   └── test_analyzer.py               # Analyzer 类测试
│       ├── test_initialization
│       ├── test_summary_statistics
│       ├── test_top_emitters
│       ├── test_filter_by_naics
│       ├── test_filter_by_industry
│       ├── test_get_statistics_table
│       └── test_compare_industries
│
└── output/                            # 输出目录（生成）
    ├── emission_statistics.csv        # 统计数据表
    ├── sector_analysis.csv            # 部门分析结果
    ├── top_emitters.png               # 排行图
    ├── distribution.png               # 分布图
    └── sector_comparison.png          # 部门对比图
```

## 📊 文件统计

| 类别 | 文件数 | 代码行数 |
|------|--------|---------|
| 核心库 | 5 | 1,200+ |
| 数据文件 | 1 | 1,500+ 行 |
| 测试 | 2 | 200+ |
| Notebook | 1 | - |
| 脚本 | 1 | 100+ |
| 文档 | 4 | - |
| **总计** | **14** | **3,000+** |

## 🎯 模块依赖关系

```
users
  ↓
setup.py
  ↓
src/ghg_analysis/
  ├── __init__.py (导出接口)
  ├── loader.py (数据加载)
  │   └── pandas, pathlib
  ├── analyzer.py (数据分析)
  │   ├── loader.py
  │   └── pandas, numpy
  ├── visualizer.py (可视化)
  │   ├── analyzer.py
  │   └── matplotlib, seaborn
  └── utils.py (工具函数)
      ├── analyzer.py
      ├── visualizer.py
      └── pandas, pathlib

tests/
  ├── test_loader.py → loader.py
  └── test_analyzer.py → analyzer.py

scripts/
  └── process_data.py → 所有模块

notebooks/
  └── 01_exploratory_analysis.ipynb → 所有模块
```

## 🚀 使用流程

### 方式1: 命令行运行
```bash
python scripts/process_data.py
```

### 方式2: Python 脚本
```python
from src.ghg_analysis import GHGAnalyzer

analyzer = GHGAnalyzer('data/raw/...csv')
analyzer.load_and_prepare()
# 使用 analyzer 进行分析
```

### 方式3: Jupyter Notebook
```bash
jupyter notebook notebooks/01_exploratory_analysis.ipynb
```

### 方式4: 作为库导入
```bash
pip install -e .
python -c "from ghg_analysis import GHGAnalyzer; ..."
```

## 📦 依赖包

### 必需 (requirements.txt)
- pandas >= 1.3.0 - 数据处理
- numpy >= 1.21.0 - 数值计算
- matplotlib >= 3.4.0 - 绘图
- seaborn >= 0.11.0 - 统计可视化
- jupyter >= 1.0.0 - Notebook 环境
- pytest >= 6.2.0 - 单元测试
- pytest-cov >= 2.12.0 - 覆盖率报告

## 📝 关键设计特点

### 1. 模块化设计
- 每个功能独立成模块
- 低耦合，高内聚
- 易于扩展和维护

### 2. 生产级代码质量
- 完整的文档字符串
- 类型提示
- 错误处理和验证
- 单元测试覆盖

### 3. 灵活的数据访问
- 支持多种筛选方式
- NAICS 代码匹配
- 行业名称搜索
- 自定义过滤

### 4. 多样化的可视化
- 5 种预构建图表类型
- 自定义绘图支持
- 高分辨率输出
- 支持保存为 PNG/PDF

### 5. 文档完整
- 中英文 README
- 快速开始指南
- 在线 Jupyter 示例
- 代码注释详细

## 🔄 数据流

```
CSV 数据文件
    ↓
GHGDataLoader (加载、验证、清理)
    ↓
GHGAnalyzer (分析、筛选、计算)
    ↓
    ├─→ GHGVisualizer (可视化)
    ├─→ export_to_csv() (导出表格)
    └─→ utils 工具函数 (计算、转换)
    ↓
输出结果 (CSV、PNG、统计)
```

## ✅ 质量保证

- **测试覆盖**: loader.py 和 analyzer.py 完整测试
- **代码风格**: 遵循 PEP 8 规范
- **文档**: 所有公共函数都有文档字符串
- **错误处理**: 完善的异常捕获和提示

## 🎓 学习路径

1. **初学者**: 阅读 README.md 和 QUICKSTART.md
2. **使用者**: 运行 scripts/process_data.py 脚本
3. **研究者**: 打开 notebooks/01_exploratory_analysis.ipynb
4. **开发者**: 阅读 src/ 中的源代码和 tests/ 中的测试

## 📄 配置文件说明

- **setup.py** - 包元数据和依赖定义
- **requirements.txt** - pip 依赖列表
- **.gitignore** - Git 忽略规则（__pycache__、.pyc、venv 等）
- **LICENSE** - MIT 许可证

## 🔗 相关链接

- GitHub: https://github.com/farmer0909/SupplyChainGHGEmissionFactors
- 数据源: USEEIO Supply Chain Emission Factors
- NAICS 分类: https://www.census.gov/naics/

---

**创建日期**: 2026-09-17  
**版本**: 1.0.0  
**维护者**: farmer0909
