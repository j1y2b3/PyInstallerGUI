import os
import shutil
import time
import unittest

from pack import Pack


class TestPack(unittest.TestCase):

    def makeResultDir(self):
        
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
        if len(resultdirs) > 5:
            for resultdir in resultdirs[:-5]:
                shutil.rmtree(os.path.join(resultspath, resultdir))
        
        return resultpath

    @classmethod
    def setUpClass(cls):

        # 生成文件夹
        cls.root = r'D:\jyb\MyProgram\PyInstallerGUI\tests'
        cls.srcpath = os.path.join(cls.root, 'examples')
        cls.runpath = cls.makeResultDir(cls)

        # 定义参数
        cls.args1 = (os.path.join(cls.srcpath, r'ex_tkinter\main.py'),
                      {'path' : cls.runpath,
                       'name' : 'ex_tkinter',
                       'datas' : [(os.path.join(cls.srcpath, r'ex_tkinter\datas'), r'.\datas')],
                       'loglevel' : 'ERROR'}
                     )
        cls.args2 = (os.path.join(cls.srcpath, r'ex_pygame\main.py'),
                      {'path' : cls.runpath,
                       'name' : 'ex_pygame',
                       'icon' : os.path.join(cls.srcpath, r'ex_pygame\datas\icon.ico'),
                       'nonconsole' : True,
                       'datas' : [(os.path.join(cls.srcpath, r'ex_pygame\datas'), r'.\datas')],
                       'loglevel' : 'ERROR'}
                     )

        # 创建Pack对象
        cls.pack1 = Pack(cls.args1[0], **cls.args1[1])
        cls.pack2 = Pack(cls.args2[0], **cls.args2[1])

    def test_pack_and_copy(self):
        
        # 打包
        self.pack1.pack()
        self.pack2.pack()

        # 复制

if __name__ == '__main__':
    unittest.main()