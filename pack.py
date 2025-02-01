import subprocess
import sys
import PyInstaller.__main__

class Pack:

    def __init__(self,
                 pythonfile: str,
                 name: str | None = None,
                 icon: str | None = None,
                 nonconsole: bool = False,
                 filestyle: str = 'onedir', # 或 onefile
                 distpath: str | None = None,
                 workpath: str | None = None,
                 specpath: str | None = None,
                 coverdist: bool = False,
                 coverwork: bool = False,
                 loglevel: str = 'INFO', # 或 TRACE DEBUG INFO WARN ERROR CRITICAL
                 datas: list[(str, str)] = [], # [(编译时文件位置, 运行时文件位置), ...]
                 binaries: list[(str, str)] = [], # 同上
                 moreimportpaths: list[str] = [], # 额外导入的包
                 morehiddenimports: list[str] = [], # 额外隐藏导入的包
                 excludemodules: list[str] = [], # 排除的包
                 runtimetmpdir: str = None # 运行时临时目录，用于onefile且有datas或binary时
                 ):

        self.commands = [pythonfile]

        if name is not None:
            self.commands.append('-n ' + name)
        if icon is not None:
            self.commands.append('-i ' + icon)
        if nonconsole:
            self.commands.append('--noconsole')

        if filestyle == 'onefile':
            self.commands.append('--onefile')
        elif filestyle == 'onedir':
            self.commands.append('--onedir')
        else:
            raise ValueError('filestyle must be onefile or onedir')

        if distpath is not None:
            self.commands.append('--distpath ' + distpath)
        if workpath is not None:
            self.commands.append('--workpath ' + workpath)
        if specpath is not None:
            self.commands.append('--specpath ' + specpath)

        if coverdist:
            self.commands.append('-y')
        if coverwork:
            self.commands.append('-clean')
        
        if loglevel != 'INFO':
            self.commands.append('--log-level ' + loglevel)

        if datas:
            for data in datas:
                self.commands.append(f'--add-data "{data[0]};{data[1]}"')
        if binaries:
            for binary in binaries:
                self.commands.append(f'--add-binary "{binary[0]};{binary[1]}"')
        
        if moreimportpaths:
            for path in moreimportpaths:
                self.commands.append('--paths ' + path)
        if morehiddenimports:
            for hidden in morehiddenimports:
                self.commands.append('--hidden-import ' + hidden)
        if excludemodules:
            for module in excludemodules:
                self.commands.append('--exclude-module ' + module)
        
        if runtimetmpdir is not None:
            self.commands.append('--runtime-tmpdir ' + runtimetmpdir)

        #PyInstaller.__main__.run(self.commands)
        self.commands = ['pyinstaller'] + self.commands
        self.commands = ' '.join(self.commands)
        print(self.commands)
        retcode = subprocess.run(self.commands).returncode
        sys.exit(retcode)

if __name__ == '__main__':
    '''
    p = Pack(r'D:\jyb\MyProgram\BallRunning\main.py',
             name='BallRunning',
             icon=r'D:\jyb\MyProgram\BallRunning\files\ricon.ico',
             nonconsole=True,
             datas=[(r'D:\jyb\MyProgram\BallRunning\files', r'.\files'),
                    (r'D:\jyb\MyProgram\BallRunning\levels', r'.\levels')],
            distpath=r'D:\jyb\MyProgram\PyInstallerGUI'
             )
    '''
    p = Pack(r'D:\jyb\MyProgram\FunctionGraphPainter\函数图像绘制器.pyw',
             name='FunctionGraphPainter',
             icon=r'D:\jyb\MyProgram\FunctionGraphPainter\文件\图标.ico',
             nonconsole=True,
             datas=[(r'D:\jyb\MyProgram\FunctionGraphPainter\文件', r'.\文件')],
             distpath=r'D:\jyb\MyProgram\PyInstallerGUI'
             )