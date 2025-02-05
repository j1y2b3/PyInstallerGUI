'''将python文件打包为可执行文件
打包参数：
pythonfile
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

import os
import subprocess
import shutil
import time
#import PyInstaller.__main__


class Pack:
    '''打包生成应用程序'''

    def __init__(self, commands: dict[str, str], runpath: str | None = None):
        
        # makeResultDirs
        self.root = os.path.dirname(__file__)
        self.maxresultdirs = 15

        # 生成命令
        self.commands = commands
        self.command = ' '.join(self.commands.values())

        self.runpath = runpath
        self.cwd={}
        if self.runpath is not None:
            self.cwd['cwd'] = self.runpath
        else:
            self.cwd['cwd'] = self.makeResultDir()
            self.runpath = self.cwd['cwd']
        
        # 执行命令
        #PyInstaller.__main__.run(self.commands.values())
        subprocess.run('pyinstaller ' + self.command, check=True, **self.cwd)
    
    def makeResultDir(self) -> str:
        '''生成结果目录
        当path为None时将结果保存在此
        '''
        
        # 确保存在results文件夹
        resultspath = os.path.join(self.root, 'results')
        if not os.path.exists(resultspath):
            os.makedirs(resultspath)
        
        # 生成唯一的result文件夹
        resultname = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        resultpath = os.path.join(resultspath, resultname)
        while os.path.exists(resultpath):
            resultname = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
            resultpath = os.path.join(resultpath, resultname)
        os.makedirs(resultpath)

        # 删除过多的result文件夹
        resultdirs = os.listdir(resultspath)
        if len(resultdirs) > self.maxresultdirs:
            for resultdir in resultdirs[:-self.maxresultdirs]:
                shutil.rmtree(os.path.join(resultspath, resultdir))
        
        return resultpath
    
    def findExePath(self) -> str:
        '''查找exe文件路径'''

        if 'distpath' in self.commands:
            distpath = self.commands['distpath'].split(' ')[1]
        else:
            distpath = os.path.join(self.runpath, 'dist')

        if 'name' in self.commands:
            name = self.commands['name'].split(' ')[1]
        else:
            name = os.path.basename(self.commands['pythonfile']).split('.')[0]

        return os.path.join(distpath, name, name + '.exe')
    
    def copyIn(self, src: str):
        '''复制文件或文件夹到exe文件同目录下
        弥补有时pyinstaller的不足
        '''

        # 找到目标路径
        dst = os.path.join(os.path.dirname(self.findExePath()), os.path.basename(src))
        
        # 复制
        if os.path.isfile(src):
            shutil.copyfile(src, dst)
        elif os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            raise ValueError('src must be a file or a directory')
    
    def copyOut(self, dst: str | None = None):
        '''复制结果文件到指定目录'''

        pass