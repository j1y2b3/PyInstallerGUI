import unittest
from pack import Pack

print('Test pack...')
class TestPack(unittest.TestCase):

    def setUp(self):

        print('Setup test...')

        self.path = r'D:\jyb\MyProgram\PyInstallerGUI\temp'

        self.args1 = (r'D:\jyb\MyProgram\BallRunning\main.py',
                      {'path' : self.path,
                       'name' : 'BallRunning',
                       'icon' : r'D:\jyb\MyProgram\BallRunning\files\ricon.ico',
                       'nonconsole' : True,
                       'datas' : [(r'D:\jyb\MyProgram\BallRunning\files', r'.\files'),
                                  (r'D:\jyb\MyProgram\BallRunning\levels', r'.\levels')]}
                      )
        
        self.args2 = (r'D:\jyb\MyProgram\FunctionGraphPainter\函数图像绘制器.pyw', 
                      {'path' : self.path,
                       'name' : 'FunctionGraphPainter',
                       'icon' : r'D:\jyb\MyProgram\FunctionGraphPainter\文件\图标.ico',
                       'nonconsole' : True,
                       'datas' : [(r'D:\jyb\MyProgram\FunctionGraphPainter\文件', r'.\文件')]}
                      )

    def test_pack(self):

        Pack(self.args1[0], **self.args1[1])
        Pack(self.args2[0], **self.args2[1])
        print('Pack test passed.')

if __name__ == '__main__':
    unittest.main()