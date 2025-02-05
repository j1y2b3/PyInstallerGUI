'''各打包参数的细节
name
icon
console
filestyle
distpath
workpath
specpath
coverdist
coverwork
loglevel              # TRACE DEBUG INFO WARN ERROR CRITICAL
data                  # [(编译时文件位置, 运行时文件位置), ...]
binary                # 同上
moreimportpaths       # 额外导入的包
morehiddenimports     # 额外隐藏导入的包
excludemodules        # 排除的包
runtimetmpdir         # 运行时临时目录，用于onefile且有data或binary时
'''

from gui.details import name

__all__ = ['name', 'icon']
