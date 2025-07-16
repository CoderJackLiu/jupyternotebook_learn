# -*- coding: utf-8 -*-
"""
修复后的seaborn图表代码
解决中文字体显示问题
"""

# 导入必要的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import matplotlib.font_manager as fm
import warnings

# 完整的字体修复函数
def setup_chinese_font():
    """
    设置中文字体，解决matplotlib和seaborn中文显示问题
    """
    # 获取系统可用的中文字体
    def get_chinese_fonts():
        chinese_fonts = []
        common_fonts = ['Microsoft YaHei', 'SimHei', 'SimSun', 'KaiTi', 'FangSong', 'STHeiti']
        system_fonts = [f.name for f in fm.fontManager.ttflist]
        for font in common_fonts:
            if font in system_fonts:
                chinese_fonts.append(font)
        return chinese_fonts
    
    # 设置字体
    available_fonts = get_chinese_fonts()
    
    if available_fonts:
        # 设置matplotlib和seaborn字体
        font_list = available_fonts + ['DejaVu Sans']
        
        # 更新所有相关的字体设置
        plt.rcParams.update({
            'font.sans-serif': font_list,
            'font.family': 'sans-serif',
            'axes.unicode_minus': False
        })
        
        mpl.rcParams.update({
            'font.sans-serif': font_list,
            'font.family': 'sans-serif', 
            'axes.unicode_minus': False
        })
        
        # 清除字体缓存
        try:
            mpl.font_manager._rebuild()
        except:
            pass
            
        print(f'✅ 中文字体设置成功: {available_fonts[0]}')
        
    else:
        print('⚠️  警告: 未找到中文字体')
    
    # 抑制字体警告
    warnings.filterwarnings('ignore', category=UserWarning)
    
    # 设置seaborn样式
    sns.set_style('whitegrid')
    
    return available_fonts

# 创建修复后的seaborn图表
def create_seaborn_charts_fixed(df_students, df_sales):
    """
    创建修复中文字体问题后的seaborn图表
    """
    # 首先设置中文字体
    setup_chinese_font()
    
    # 创建seaborn图表
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # 1. 箱线图 - 各班级成绩分布
    sns.boxplot(data=df_students, x='班级', y='数学', ax=axes[0, 0])
    axes[0, 0].set_title('各班级数学成绩分布', fontsize=14, fontweight='bold')
    
    # 2. 小提琴图 - 成绩分布
    df_scores = df_students[['数学', '语文', '英语']].melt(var_name='科目', value_name='成绩')
    sns.violinplot(data=df_scores, x='科目', y='成绩', ax=axes[0, 1])
    axes[0, 1].set_title('各科目成绩分布', fontsize=14, fontweight='bold')
    
    # 3. 热力图 - 科目相关性
    correlation = df_students[['数学', '语文', '英语']].corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, 
               square=True, ax=axes[1, 0])
    axes[1, 0].set_title('科目成绩相关性', fontsize=14, fontweight='bold')
    
    # 4. 分组柱状图 - 地区产品销售
    region_product = df_sales.groupby(['地区', '产品'])['销售额'].sum().reset_index()
    sns.barplot(data=region_product, x='地区', y='销售额', hue='产品', ax=axes[1, 1])
    axes[1, 1].set_title('各地区产品销售情况', fontsize=14, fontweight='bold')
    axes[1, 1].legend(title='产品', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    plt.show()
    
    print('🎯 如果图表中文显示正常，说明问题已解决！')

if __name__ == '__main__':
    # 示例用法
    print('请在Jupyter Notebook中运行以下代码：')
    print('\n# 导入修复模块')
    print('exec(open("fix_chinese_font.py").read())')
    print('fix_chinese_font()')
    print('\n# 然后重新运行seaborn图表代码')
    print('# 或者使用:')
    print('exec(open("seaborn_fixed.py").read())')
    print('create_seaborn_charts_fixed(df_students, df_sales)')