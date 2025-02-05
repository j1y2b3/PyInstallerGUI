import os
import subprocess
import unittest

from pack import Pack

class TestPack(unittest.TestCase):

    class _Pack(Pack):
        '''更改打包方式，以便于测试'''

        def makeResultDir(self):
            '''更改结果目录生成方式，以便于测试'''

            self.maxresultdirs = 5

            return super().makeResultDir()

    @classmethod
    def setUpClass(cls):
        
        # 设置测试用目录
        cls.root = r'D:\jyb\MyProgram\PyInstallerGUI\tests'
        cls.srcpath = os.path.join(cls.root, 'examples')
        
        # 设置打包参数
        cls.allcommands = (
            {'pythonfile': os.path.join(cls.srcpath, r'ex_tkinter\main.py'),
             'name': '-n ex_tkinter',
             'data': '--add-data ' + os.path.join(cls.srcpath, r'ex_tkinter\datas' + ';datas')
             },

            {'pythonfile': os.path.join(cls.srcpath, r'ex_pygame\main.py'),
             'name': '-n ex_pygame',
             'icon': '-i ' + os.path.join(cls.srcpath, r'ex_pygame\datas\icon.ico'),
             'console': '--noconsole',
             'data': '--add-data ' + os.path.join(cls.srcpath, r'ex_pygame\datas' + ';datas')
             }
        )
    
    def test_A_init(self):

        for commands in self.allcommands:
            
            # 过滤日志输出
            commands['loglevel'] = '--log-level ERROR'

            # 运行打包命令
            self.pack = self._Pack(commands)

            # 检查打包结果
            exepath = self.pack.findExePath()
            subprocess.run((exepath,), cwd=os.path.dirname(exepath), check=True)
