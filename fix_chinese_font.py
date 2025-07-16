#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
中文字体修复工具
解决matplotlib和seaborn中文显示问题

使用方法:
1. 直接运行: python fix_chinese_font.py
2. 在notebook中导入: 
   import fix_chinese_font
   fix_chinese_font.fix_chinese_font()
3. 或者使用exec加载:
   exec(open('fix_chinese_font.py', encoding='utf-8').read())
   fix_chinese_font()
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import seaborn as sns
import warnings

def fix_chinese_font():
    """
    修复matplotlib和seaborn的中文字体显示问题
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
        # 设置matplotlib全局字体参数
        plt.rcParams['font.sans-serif'] = available_fonts + ['DejaVu Sans']
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['axes.unicode_minus'] = False
        
        # 设置matplotlib底层字体参数
        mpl.rcParams['font.sans-serif'] = available_fonts + ['DejaVu Sans']
        mpl.rcParams['font.family'] = 'sans-serif'
        mpl.rcParams['axes.unicode_minus'] = False
        
        # 清除字体缓存并重建
        try:
            mpl.font_manager._rebuild()
        except:
            pass
        
        # 设置seaborn样式并确保字体继承
        sns.set_style('whitegrid')
        sns.set_context('notebook')
        
        # 强制应用字体设置
        plt.rcdefaults()
        plt.rcParams.update({
            'font.sans-serif': available_fonts + ['DejaVu Sans'],
            'font.family': 'sans-serif',
            'axes.unicode_minus': False,
            'figure.figsize': (10, 6)
        })
        
        print(f'✅ 中文字体设置成功: {available_fonts[0]}')
        print(f'📋 可用字体列表: {", ".join(available_fonts)}')
        
    else:
        # 如果没有找到中文字体，使用备用方案
        plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
        mpl.rcParams['font.sans-serif'] = ['DejaVu Sans']
        print('⚠️  警告: 未找到中文字体，建议安装中文字体包')
        print('💡 建议: 安装 Microsoft YaHei 或 SimHei 字体')
    
    # 抑制所有字体相关警告
    warnings.filterwarnings('ignore', category=UserWarning, module='matplotlib')
    warnings.filterwarnings('ignore', category=UserWarning, module='seaborn')
    warnings.filterwarnings('ignore', category=UserWarning, module='IPython')
    warnings.filterwarnings('ignore', message='.*Glyph.*missing.*')
    
    return available_fonts

def test_chinese_display():
    """
    测试中文显示效果
    """
    import numpy as np
    
    # 创建测试数据
    x = ['数学', '语文', '英语', '物理', '化学']
    y = [85, 78, 92, 88, 76]
    
    # 创建测试图表
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # matplotlib测试
    ax1.bar(x, y, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
    ax1.set_title('matplotlib中文测试', fontsize=14, fontweight='bold')
    ax1.set_xlabel('科目', fontsize=12)
    ax1.set_ylabel('成绩', fontsize=12)
    
    # seaborn测试
    import pandas as pd
    df_test = pd.DataFrame({'科目': x, '成绩': y})
    sns.barplot(data=df_test, x='科目', y='成绩', ax=ax2, palette='viridis')
    ax2.set_title('seaborn中文测试', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    print('🎯 如果上面的图表中文显示正常，说明字体设置成功！')

if __name__ == '__main__':
    # 修复字体
    fonts = fix_chinese_font()
    
    # 测试显示效果
    test_chinese_display()