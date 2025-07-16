@echo off
echo ========================================
echo    Jupyter Notebook 学习环境启动脚本
echo ========================================
echo.

echo 正在检查 Python 环境...
python --version
if %errorlevel% neq 0 (
    echo 错误：未找到 Python，请先安装 Python
    pause
    exit /b 1
)

echo.
echo 正在安装依赖包...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo 警告：部分包安装失败，但可以继续使用基础功能
)

echo.
echo 正在启动 Jupyter Notebook...
echo 浏览器将自动打开，如果没有请手动访问显示的地址
echo.
echo 学习文件说明：
echo   01_基础入门.ipynb     - Jupyter Notebook 基础操作
echo   02_Python基础.ipynb   - Python 编程基础
echo   03_数据分析入门.ipynb - 数据分析入门
echo   04_可视化示例.ipynb   - 数据可视化实践
echo.
echo 按 Ctrl+C 可以停止 Jupyter Notebook
echo ========================================
echo.

jupyter notebook

echo.
echo Jupyter Notebook 已关闭
pause