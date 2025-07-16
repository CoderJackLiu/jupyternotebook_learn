import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import seaborn as sns
import warnings

def setup_chinese_font():
    chinese_fonts = []
    common_fonts = ['Microsoft YaHei', 'SimHei', 'SimSun', 'KaiTi', 'FangSong', 'STHeiti']
    system_fonts = [f.name for f in fm.fontManager.ttflist]
    for font in common_fonts:
        if font in system_fonts:
            chinese_fonts.append(font)
    
    if chinese_fonts:
        font_list = chinese_fonts + ['DejaVu Sans']
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
        try:
            mpl.font_manager._rebuild()
        except:
            pass
        print(f'Chinese font set successfully: {chinese_fonts[0]}')
    else:
        print('Warning: No Chinese fonts found')
    
    warnings.filterwarnings('ignore', category=UserWarning)
    sns.set_style('whitegrid')
    return chinese_fonts

if __name__ == '__main__':
    setup_chinese_font()