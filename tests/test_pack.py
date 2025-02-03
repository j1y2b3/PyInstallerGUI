import os
import shutil
import time
import unittest
from pack import Pack


class TestPack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 创建文件夹run_results
        cls.root = r'D:\jyb\MyProgram\PyInstallerGUI\tests\results'
        if not os.path.exists(cls.root):
            os.makedirs(cls.root)

        # 创建文件夹
        cls.time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        cls.path = os.path.join(cls.root, cls.time)
        while os.path.exists(cls.path):
            cls.time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
            cls.path = os.path.join(cls.root, cls.time)
        os.makedirs(cls.path)

        # 删除过多的文件夹
        dirs = os.listdir(cls.root)
        if len(dirs) > 5:
            for dir in dirs[:-5]:
                shutil.rmtree(os.path.join(cls.root, dir))

        # 定义参数
        cls.args1 = (r'D:\jyb\MyProgram\BallRunning\main.py',
                      {'path' : cls.path,
                       'name' : 'BallRunning',
                       'icon' : r'D:\jyb\MyProgram\BallRunning\files\ricon.ico',
                       'nonconsole' : True,
                       'datas' : [(r'D:\jyb\MyProgram\BallRunning\files', r'.\files'),
                                  (r'D:\jyb\MyProgram\BallRunning\levels', r'.\levels')],
                       'loglevel' : 'ERROR'}
                      )
        
        cls.args2 = (r'D:\jyb\MyProgram\FunctionGraphPainter\函数图像绘制器.pyw', 
                      {'path' : cls.path,
                       'name' : 'FunctionGraphPainter',
                       'icon' : r'D:\jyb\MyProgram\FunctionGraphPainter\文件\图标.ico',
                       'nonconsole' : True,
                       'datas' : [(r'D:\jyb\MyProgram\FunctionGraphPainter\文件', r'.\文件')],
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
        self.pack1.copy(r'D:\jyb\MyProgram\BallRunning\files')
        self.pack1.copy(r'D:\jyb\MyProgram\BallRunning\levels')
        self.pack2.copy(r'D:\jyb\MyProgram\FunctionGraphPainter\文件')

if __name__ == '__main__':
    unittest.main()