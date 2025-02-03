'''将python文件打包为可执行文件'''

import os
import shutil
import subprocess
#import PyInstaller.__main__


class Pack:
    '''生成完整的应用程序'''

    def __init__(self,
                 pythonfile: str, *,
                 path: str | None = None,
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
                 runtimetmpdir: str | None = None # 运行时临时目录，用于onefile且有datas或binary时
                 ):
        
        self.pythonfile = pythonfile
        self.path = path
        self.name = name
        self.icon = icon
        self.nonconsole = nonconsole
        self.filestyle = filestyle
        self.distpath = distpath
        self.workpath = workpath
        self.specpath = specpath
        self.coverdist = coverdist
        self.coverwork = coverwork
        self.loglevel = loglevel
        self.datas = datas
        self.binaries = binaries
        self.moreimportpaths = moreimportpaths
        self.morehiddenimports = morehiddenimports
        self.excludemodules = excludemodules
        self.runtimetmpdir = runtimetmpdir

    def pack(self):
        '''用pyinstaller打包exe文件'''

        # 生成命令
        self.commands = [self.pythonfile]

        self.cwd={}
        if self.path is not None:
            self.cwd['cwd'] = self.path

        if self.name is not None:
            self.commands.append('-n ' + self.name)
        if self.icon is not None:
            self.commands.append('-i ' + self.icon)
        if self.nonconsole:
            self.commands.append('--noconsole')

        if self.filestyle == 'onefile':
            self.commands.append('--onefile')
        elif self.filestyle == 'onedir':
            self.commands.append('--onedir')
        else:
            raise ValueError('filestyle must be onefile or onedir')

        if self.distpath is not None:
            self.commands.append('--distpath ' + self.distpath)
        if self.workpath is not None:
            self.commands.append('--workpath ' + self.workpath)
        if self.specpath is not None:
            self.commands.append('--specpath ' + self.specpath)

        if self.coverdist:
            self.commands.append('-y')
        if self.coverwork:
            self.commands.append('-clean')
        
        if self.loglevel != 'INFO':
            self.commands.append('--log-level ' + self.loglevel)

        if self.datas:
            for data in self.datas:
                self.commands.append(f'--add-data "{data[0]}:{data[1]}"')
        if self.binaries:
            for binary in self.binaries:
                self.commands.append(f'--add-binary "{binary[0]}:{binary[1]}"')
        
        if self.moreimportpaths:
            for importpath in self.moreimportpaths:
                self.commands.append('--paths ' + importpath)
        if self.morehiddenimports:
            for module in self.morehiddenimports:
                self.commands.append('--hidden-import ' + module)
        if self.excludemodules:
            for module in self.excludemodules:
                self.commands.append('--exclude-module ' + module)
        
        if self.runtimetmpdir is not None:
            self.commands.append('--runtime-tmpdir ' + self.runtimetmpdir)

        # 执行命令
        #PyInstaller.__main__.run(self.commands)
        self.commands = ['pyinstaller'] + self.commands
        self.commands = ' '.join(self.commands)
        subprocess.run(self.commands, **self.cwd)

    def copy(self, src: str):
        '''复制文件或文件夹到exe文件同目录下
        弥补pyinstaller的不足
        '''

        # 生成目标路径
        if self.name is not None:
            name = self.name
        else:
            name = os.path.basename(self.pythonfile).split('.')[0]

        if self.distpath is not None:
            dst = os.path.join(self.distpath, name)
        else:
            dst = os.path.join(self.path, 'dist', name)

        dst = os.path.join(dst, os.path.basename(src))
        
        # 复制
        if os.path.isfile(src):
            shutil.copyfile(src, dst)
        elif os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            raise ValueError('src must be a file or a directory')