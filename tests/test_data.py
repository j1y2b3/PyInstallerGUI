import os
import pytest

from data import root
from data import getIconPath, getRecentFiles, writeRecentFiles

def test_getIconPath():

    assert os.path.exists(getIconPath())
    assert os.path.exists(getIconPath('console'))
    assert os.path.exists(getIconPath('windowed'))
    with pytest.raises(ValueError):
        getIconPath('unknown')


class TestRecentFiles:

    def setup_class(self):
        
        # 初始化参数
        self.jsonfile = 'temp.json'
        self.recentfiles = ['file1', 'file2', 'file3']

        # 清除上一次错误遗留的文件
        if os.path.exists(os.path.join(root, self.jsonfile)):
            os.remove(os.path.join(root, self.jsonfile))
    
    def teardown_class(self):

        # 清除文件
        os.remove(os.path.join(root, self.jsonfile))
    
    @pytest.mark.run(order=1)
    def test_getRecentFiles(self):

        assert getRecentFiles(self.jsonfile) == []

    @pytest.mark.run(order=2)
    def test_writeRecentFiles(self):

        # 第一次写入
        writeRecentFiles(self.recentfiles, self.jsonfile)
        assert getRecentFiles(self.jsonfile) == self.recentfiles

        # 第二次写入，顺序改变
        self.recentfiles[0] , self.recentfiles[1] = self.recentfiles[1], self.recentfiles[0]
        writeRecentFiles(self.recentfiles, self.jsonfile)
        assert getRecentFiles(self.jsonfile) == self.recentfiles
        assert getRecentFiles(self.jsonfile)[0] == self.recentfiles[0]
