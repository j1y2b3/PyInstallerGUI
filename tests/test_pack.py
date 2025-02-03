import os
import unittest

from pack import Pack


class TestPack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 创建Pack对象
        cls.pack = Pack()
        cls.pack.maxresultdirs = 5

        # 生成文件夹
        cls.root = r'D:\jyb\MyProgram\PyInstallerGUI\tests'
        cls.pack.root = cls.root # 为使用makeResultDir方法，不用makePackage的path参数而是改root
        cls.srcpath = os.path.join(cls.root, 'examples')
        cls.runpath = cls.pack.makeResultDir()

        # 定义参数
        cls.args = (
            (os.path.join(cls.srcpath, r'ex_tkinter\main.py'),
             {'name' : 'ex_tkinter',
              'datas' : [(os.path.join(cls.srcpath, r'ex_tkinter\datas'), r'.\datas')],
              'loglevel' : 'ERROR'}
              ),

            (os.path.join(cls.srcpath, r'ex_pygame\main.py'),
             {'name' : 'ex_pygame',
              'icon' : os.path.join(cls.srcpath, r'ex_pygame\datas\icon.ico'),
              'nonconsole' : True,
              'datas' : [(os.path.join(cls.srcpath, r'ex_pygame\datas'), r'.\datas')],
              'loglevel' : 'ERROR'}
              )
        )
        
    def test_pack_then_copy(self):

        for arg in self.args:

            # 打包
            self.pack.getArgs(arg[0], **arg[1])
            self.pack.makePackage(self.runpath)

            # 复制
            '''
            match arg[0]:
                case ...:
                   self.pack.copyOtherTings(src)
            '''