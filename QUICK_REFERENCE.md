# 快速参考卡 - Supply Chain GHG Analysis

## 🚀 5 分钟快速开始

```bash
# 1. 进入项目
cd SupplyChainGHG_Refactored

# 2. 创建虚拟环境
python -m venv venv && source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行
python scripts/process_data.py
```

## 📚 关键命令

```bash
# 运行脚本
python scripts/process_data.py

# 运行测试
pytest tests/ -v

# Jupyter
jupyter notebook notebooks/01_exploratory_analysis.ipynb

# Python 包安装
pip install -e .
```

## 💻 常见代码

### 基本使用
```python
from ghg_analysis import GHGAnalyzer

# 加载数据
analyzer = GHGAnalyzer('data/raw/SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv')

# 统计
stats = analyzer.summary_statistics()
print(f"平均: {stats['mean_emission']:.4f}")

# 排行
top_10 = analyzer.top_emitters(top_n=10)
```

### 数据筛选
```python
# NAICS 代码筛选 (农业: 11)
agriculture = analyzer.filter_by_naics('11')

# 行业名称搜索
farming = analyzer.filter_by_industry('Farming')

# 行业对比
comp = analyzer.compare_industries(['Farming', 'Mining'])
```

### 可视化
```python
from ghg_analysis import GHGVisualizer

viz = GHGVisualizer(analyzer)
viz.plot_top_emitters(top_n=20, save_path='output/top.png')
viz.plot_distribution()
viz.plot_sector_comparison()
```

### 工具函数
```python
from ghg_analysis.utils import calculate_emissions, convert_emissions_unit

# 计算排放
total_kg = calculate_emissions(1_000_000, 1.5)  # $1M, 1.5 kg CO2e/USD
tonnes = convert_emissions_unit(total_kg, 'tonnes')

# 导出结果
analyzer.export_to_csv('output/analysis.csv')
```

## 📂 文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 项目文档 |
| `QUICKSTART.md` | 快速开始 |
| `src/ghg_analysis/` | 核心库 |
| `tests/` | 单元测试 |
| `data/raw/` | 原始数据 |
| `notebooks/` | 示例代码 |
| `scripts/` | 脚本 |

## 🔧 API 速查

### GHGAnalyzer

```python
analyzer = GHGAnalyzer(filepath)
analyzer.load_and_prepare()              # 加载准备
analyzer.summary_statistics()            # 统计摘要
analyzer.top_emitters(top_n=20)         # 排放排行
analyzer.emission_by_sector()           # 按部门分析
analyzer.filter_by_naics('11')          # NAICS 筛选
analyzer.filter_by_industry('Farming')  # 行业筛选
analyzer.get_statistics_table()         # 统计表
analyzer.compare_industries([...])      # 行业对比
analyzer.export_to_csv('file.csv')      # 导出
```

### GHGVisualizer

```python
viz = GHGVisualizer(analyzer)
viz.plot_top_emitters(top_n=20)                    # 排行图
viz.plot_distribution()                           # 分布图
viz.plot_sector_comparison()                      # 部门对比
viz.plot_margin_comparison(top_n=15)             # 边际对比
viz.plot_custom(df, 'col1', 'col2', 'scatter')   # 自定义
```

### 工具函数

```python
from ghg_analysis.utils import *

calculate_emissions(amount_usd, emission_factor)        # 计算排放
convert_emissions_unit(kg, 'tonnes')                    # 单位转换
get_naics_sector_name('11')                            # NAICS 转换
aggregate_by_sector(df)                                # 按部门聚合
print_summary_report(analyzer)                         # 打印报告
export_analysis_results(analyzer, 'output/')           # 导出结果
```

## 📊 NAICS 代码速查

| 代码 | 行业 |
|------|------|
| 11 | 农业、林业、捕鱼 |
| 21 | 采矿、采石 |
| 22 | 公用事业 |
| 23 | 建筑 |
| 31-33 | 制造业 |
| 42 | 批发贸易 |
| 44-45 | 零售贸易 |
| 48-49 | 运输和仓储 |
| 51 | 信息产业 |
| 52 | 金融保险 |
| 54 | 专业服务 |
| 72 | 酒店和食品 |
| 92 | 政府管理 |

## ⚙️ 依赖包

```
pandas >= 1.3.0          # 数据处理
numpy >= 1.21.0          # 数值计算
matplotlib >= 3.4.0      # 绘图
seaborn >= 0.11.0        # 统计图
jupyter >= 1.0.0         # Notebook
pytest >= 6.2.0          # 测试
```

## 🐛 常见问题

**Q: 数据文件位置？**  
A: `data/raw/SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv`

**Q: 如何运行测试？**  
A: `pytest tests/ -v`

**Q: 如何保存图表？**  
A: `visualizer.plot_top_emitters(save_path='output/top.png')`

**Q: 如何导入为包？**  
A: `pip install -e .` 然后 `from ghg_analysis import GHGAnalyzer`

## 🔗 文档链接

- 项目文档: `README.md`
- 快速开始: `QUICKSTART.md`
- 架构说明: `PROJECT_STRUCTURE.md`
- 整理总结: `REFACTORING_SUMMARY.md`

---
**版本**: 1.0.0 | **更新**: 2026-09-17
