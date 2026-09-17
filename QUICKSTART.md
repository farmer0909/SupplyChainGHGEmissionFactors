# Quick Start Guide

快速开始使用供应链 GHG 排放系数分析工具。

## 🚀 5分钟快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行分析脚本

```bash
python scripts/process_data.py
```

### 3. 在 Python 中使用

```python
from ghg_analysis import GHGAnalyzer

# 初始化分析器
analyzer = GHGAnalyzer('data/raw/SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv')

# 获取统计摘要
stats = analyzer.summary_statistics()
print(f"平均排放系数: {stats['mean_emission']:.4f} kg CO2e/USD")

# 获取排放最高的行业
top_20 = analyzer.top_emitters(top_n=20)
print("\n排放最高的20个行业:")
print(top_20)

# 按 NAICS 代码筛选
agriculture = analyzer.filter_by_naics('11')
print("\n农业部门:")
print(agriculture)

# 创建可视化
from ghg_analysis import GHGVisualizer

visualizer = GHGVisualizer(analyzer)
visualizer.plot_top_emitters(top_n=20)
visualizer.plot_distribution()
visualizer.plot_sector_comparison()
```

## 📊 常用命令

### 获取摘要统计

```python
stats = analyzer.summary_statistics()
# 返回: mean, median, std, min, max, q25, q75
```

### 按行业查询

```python
# 按名称搜索
farming = analyzer.filter_by_industry('Farming')

# 按 NAICS 代码搜索
sector_11 = analyzer.filter_by_naics('11')  # 农业
sector_21 = analyzer.filter_by_naics('21')  # 采矿业
```

### 导出数据

```python
# 导出为 CSV
analyzer.export_to_csv('output/my_analysis.csv')

# 导出为图表
visualizer.plot_top_emitters(save_path='output/top_emitters.png')
```

## 🔧 主要类和方法

### GHGAnalyzer 类

| 方法 | 说明 |
|------|------|
| `load_and_prepare()` | 加载并准备数据 |
| `summary_statistics()` | 获取统计摘要 |
| `top_emitters(top_n)` | 获取排放最高的行业 |
| `emission_by_sector()` | 按部门分析 |
| `filter_by_naics(code)` | 按 NAICS 代码筛选 |
| `filter_by_industry(name)` | 按行业名称筛选 |
| `get_statistics_table()` | 获取统计表 |
| `compare_industries(list)` | 行业对比 |

### GHGVisualizer 类

| 方法 | 说明 |
|------|------|
| `plot_top_emitters()` | 绘制排放排行 |
| `plot_distribution()` | 显示分布直方图 |
| `plot_sector_comparison()` | 部门对比图 |
| `plot_margin_comparison()` | 边际对比图 |
| `plot_custom()` | 自定义图表 |

## 📁 项目结构

```
SupplyChainGHG/
├── src/ghg_analysis/          # 核心库
│   ├── loader.py              # 数据加载
│   ├── analyzer.py            # 分析类
│   ├── visualizer.py          # 可视化
│   └── utils.py               # 工具函数
├── data/raw/                  # 原始数据
├── output/                    # 分析输出
├── scripts/                   # 脚本
├── tests/                     # 测试
└── notebooks/                 # Jupyter Notebooks
```

## 💡 示例分析

### 示例1: 查找排放最高的农业行业

```python
analyzer = GHGAnalyzer('data/raw/...csv')

# 筛选农业部门
agriculture = analyzer.filter_by_naics('11')

# 排序获取排放最高的
top_ag = agriculture.nlargest(10, 'Supply Chain Emission Factors with Margins')
print(top_ag)
```

### 示例2: 比较不同部门

```python
# 获取各部门平均排放
sectors = analyzer.emission_by_sector()
print(sectors)

# 可视化部门对比
viz = GHGVisualizer(analyzer)
viz.plot_sector_comparison()
```

### 示例3: 导出供应链排放计算

```python
from ghg_analysis.utils import calculate_emissions, convert_emissions_unit

# 计算某行业的总排放
industry_emission = 1.5  # kg CO2e/USD
spending = 1_000_000  # USD

total_emissions_kg = calculate_emissions(spending, industry_emission)
total_emissions_tonnes = convert_emissions_unit(total_emissions_kg, 'tonnes')

print(f"支出: ${spending:,}")
print(f"排放: {total_emissions_kg:,.0f} kg CO2e")
print(f"      {total_emissions_tonnes:,.1f} 公吨 CO2e")
```

## 🧪 运行测试

```bash
# 运行所有测试
python -m pytest tests/ -v

# 运行特定测试
python -m pytest tests/test_analyzer.py -v

# 生成覆盖率报告
python -m pytest tests/ --cov=src/ghg_analysis
```

## 🆘 常见问题

**Q: 数据文件在哪里?**  
A: 应该在 `data/raw/SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv`

**Q: 如何添加新数据?**  
A: 将新的 CSV 文件放在 `data/raw/` 目录，确保列名匹配。

**Q: 如何自定义图表?**  
A: 使用 `GHGVisualizer.plot_custom()` 方法或直接使用 matplotlib。

## 📞 联系与支持

如有问题，请通过 GitHub Issues 或邮件联系。

---

**最后更新**: 2026-09-17  
**版本**: 1.0.0
