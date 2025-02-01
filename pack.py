import PyInstaller.__main__
from PyInstaller import Analysis, PYZ, EXE, COLLECT


class Pack:

    def __init__(self,
                 path: str,
                 script: str,
                 name: str):
        
        # 分析Python脚本及其依赖项
        analysis = Analysis(
            [script],  # 要分析的Python脚本
            pathex=[],  # 额外的路径，用于查找依赖项
            binaries=[],  # 二进制文件
            datas=[],  # 数据文件
            hiddenimports=[],  # 隐藏的导入，有些模块在运行时动态导入，PyInstaller可能无法自动检测到，需要手动添加
            hookspath=[],  # 钩子脚本路径
            runtime_hooks=[],  # 运行时钩子脚本
            excludes=[],  # 要排除的模块
            win_no_prefer_redirects=False,  # Windows特定选项：用于控制是否在Windows系统中不使用重定向
            win_private_assemblies=False,  # Windows特定选项：用于控制是否在Windows系统中将程序集设置为私有
            cipher=3,  # 加密级别
        )

        # 创建PYZ归档文件
        pyz = PYZ(analysis.pure, analysis.zipped_data, cipher=3)

        # 创建可执行文件
        exe = EXE(
            pyz,
            analysis.scripts,
            [], # 额外的模块列表，这里为空
            exclude_binaries=True, # 排除二进制文件
            name=name,  # 最终的可执行文件名
            debug=False, # 不开启调试模式
            bootloader_ignore_signals=False, # 引导程序不忽略信号，确保信号处理正常
            strip=False, # 不剥离符号信息，保留符号信息以便调试
            upx=True, # 使用UPX压缩，减小可执行文件的大小
            upx_exclude=[], # UPX压缩排除的文件列表
            runtime_tmpdir=None, # 运行时临时目录，默认为None
            console=True, # 创建控制台应用程序
        )

        # 收集所有文件并创建最终的可执行文件
        collect = COLLECT(
            exe,
            analysis.binaries,
            analysis.zipfiles,
            analysis.datas,
            strip=False, # 不剥离符号信息 ，保留调试信息
            upx=True, # 使用UPX压缩，减小可执行文件体积
            upx_exclude=[], # UPX压缩排除的文件列表
            name=name,  # 最终的可执行文件名
        )

        # 将收集到的文件写入指定路径，生成最终的可执行文件
        collect.write(path)
        print()

if __name__ == '__main__':
    Pack('main', 'dist/main.exe')