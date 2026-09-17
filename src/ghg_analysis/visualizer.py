"""
Visualization module for GHG analysis.

This module provides plotting and visualization functions for emission data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, List, Tuple


class GHGVisualizer:
    """Create visualizations for GHG emission analysis."""

    def __init__(self, analyzer, style: str = "seaborn-v0_8-darkgrid"):
        """
        Initialize the visualizer.

        Args:
            analyzer: GHGAnalyzer instance
            style: Matplotlib style to use
        """
        self.analyzer = analyzer
        try:
            plt.style.use(style)
        except:
            # Fallback if style not available
            plt.style.use('default')

        sns.set_palette("husl")

    def plot_top_emitters(
        self,
        top_n: int = 20,
        figsize: Tuple[int, int] = (14, 8),
        save_path: Optional[str] = None
    ) -> None:
        """
        Plot industries with highest emission factors.

        Args:
            top_n: Number of top industries to show
            figsize: Figure size (width, height)
            save_path: Path to save figure (optional)
        """
        data = self.analyzer.top_emitters(top_n=top_n)

        fig, ax = plt.subplots(figsize=figsize)

        colors = plt.cm.RdYlGn_r(np.linspace(0.3, 0.9, len(data)))
        bars = ax.barh(range(len(data)), data['Emission_Factor'], color=colors)

        ax.set_yticks(range(len(data)))
        ax.set_yticklabels(data['Industry'], fontsize=10)
        ax.set_xlabel('Emission Factor (kg CO2e / 2021 USD)', fontsize=12, fontweight='bold')
        ax.set_title(f'Top {top_n} Industries by GHG Emission Factors',
                     fontsize=14, fontweight='bold', pad=20)

        # Add value labels on bars
        for i, (idx, row) in enumerate(data.iterrows()):
            ax.text(row['Emission_Factor'], i, f" {row['Emission_Factor']:.3f}",
                   va='center', fontsize=9)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Figure saved to {save_path}")

        plt.show()

    def plot_distribution(
        self,
        figsize: Tuple[int, int] = (14, 6),
        save_path: Optional[str] = None
    ) -> None:
        """
        Plot distribution of emission factors.

        Args:
            figsize: Figure size
            save_path: Path to save figure (optional)
        """
        data = self.analyzer.data
        emission_col = 'Supply Chain Emission Factors with Margins'

        fig, axes = plt.subplots(1, 2, figsize=figsize)

        # Histogram
        axes[0].hist(data[emission_col], bins=50, color='steelblue', edgecolor='black', alpha=0.7)
        axes[0].set_xlabel('Emission Factor (kg CO2e / 2021 USD)', fontsize=11, fontweight='bold')
        axes[0].set_ylabel('Frequency', fontsize=11, fontweight='bold')
        axes[0].set_title('Distribution of Emission Factors', fontsize=12, fontweight='bold')
        axes[0].grid(axis='y', alpha=0.3)

        # Box plot
        axes[1].boxplot(data[emission_col], vert=True)
        axes[1].set_ylabel('Emission Factor (kg CO2e / 2021 USD)', fontsize=11, fontweight='bold')
        axes[1].set_title('Box Plot of Emission Factors', fontsize=12, fontweight='bold')
        axes[1].grid(axis='y', alpha=0.3)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Figure saved to {save_path}")

        plt.show()

    def plot_sector_comparison(
        self,
        figsize: Tuple[int, int] = (14, 8),
        save_path: Optional[str] = None
    ) -> None:
        """
        Compare emission factors by sector.

        Args:
            figsize: Figure size
            save_path: Path to save figure (optional)
        """
        data = self.analyzer.data.copy()
        data['Sector'] = data['2017 NAICS Code'].str[:2]

        emission_col = 'Supply Chain Emission Factors with Margins'
        sector_data = data.groupby('Sector')[emission_col].mean().sort_values(ascending=False)

        fig, ax = plt.subplots(figsize=figsize)

        colors = plt.cm.viridis(np.linspace(0, 1, len(sector_data)))
        bars = ax.bar(range(len(sector_data)), sector_data.values, color=colors, edgecolor='black')

        ax.set_xticks(range(len(sector_data)))
        ax.set_xticklabels(sector_data.index, fontsize=11, fontweight='bold')
        ax.set_ylabel('Average Emission Factor (kg CO2e / 2021 USD)',
                     fontsize=12, fontweight='bold')
        ax.set_title('Average GHG Emission Factors by Sector (NAICS 2-digit)',
                    fontsize=14, fontweight='bold', pad=20)

        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}',
                   ha='center', va='bottom', fontsize=9, fontweight='bold')

        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Figure saved to {save_path}")

        plt.show()

    def plot_margin_comparison(
        self,
        top_n: int = 15,
        figsize: Tuple[int, int] = (14, 8),
        save_path: Optional[str] = None
    ) -> None:
        """
        Compare emission factors with and without margins.

        Args:
            top_n: Number of industries to show
            figsize: Figure size
            save_path: Path to save figure (optional)
        """
        data = self.analyzer.data.copy()
        data = data.nlargest(top_n, 'Supply Chain Emission Factors with Margins')
        data = data[['2017 NAICS Title',
                     'Supply Chain Emission Factors without Margins',
                     'Supply Chain Emission Factors with Margins',
                     'Margins of Supply Chain Emission Factors']]

        fig, ax = plt.subplots(figsize=figsize)

        x = np.arange(len(data))
        width = 0.35

        bars1 = ax.bar(x - width/2, data['Supply Chain Emission Factors without Margins'],
                       width, label='Without Margins', color='skyblue', edgecolor='black')
        bars2 = ax.bar(x + width/2, data['Supply Chain Emission Factors with Margins'],
                       width, label='With Margins', color='coral', edgecolor='black')

        ax.set_xlabel('Industry', fontsize=12, fontweight='bold')
        ax.set_ylabel('Emission Factor (kg CO2e / 2021 USD)', fontsize=12, fontweight='bold')
        ax.set_title('Comparison of Emission Factors: With vs Without Margins',
                    fontsize=14, fontweight='bold', pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels(data['2017 NAICS Title'], rotation=45, ha='right', fontsize=9)
        ax.legend(fontsize=11)
        ax.grid(axis='y', alpha=0.3)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Figure saved to {save_path}")

        plt.show()

    @staticmethod
    def plot_custom(
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        plot_type: str = 'scatter',
        figsize: Tuple[int, int] = (12, 7),
        title: str = '',
        save_path: Optional[str] = None
    ) -> None:
        """
        Create custom plot from DataFrame.

        Args:
            df: DataFrame with data
            x_col: Column name for x-axis
            y_col: Column name for y-axis
            plot_type: 'scatter', 'line', or 'bar'
            figsize: Figure size
            title: Plot title
            save_path: Path to save figure (optional)
        """
        fig, ax = plt.subplots(figsize=figsize)

        if plot_type == 'scatter':
            ax.scatter(df[x_col], df[y_col], alpha=0.6, s=100)
        elif plot_type == 'line':
            ax.plot(df[x_col], df[y_col], marker='o', linewidth=2)
        elif plot_type == 'bar':
            ax.bar(df[x_col], df[y_col])

        ax.set_xlabel(x_col, fontsize=11, fontweight='bold')
        ax.set_ylabel(y_col, fontsize=11, fontweight='bold')
        if title:
            ax.set_title(title, fontsize=13, fontweight='bold')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Figure saved to {save_path}")

        plt.show()
