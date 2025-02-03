'''获取datas文件夹内的文件'''

import os

def get_icon_path(style: str = 'console') -> str:
    '''获取图标路径'''

    if style == 'console':
        return os.path.join(os.path.dirname(__file__), r'datas\icon-console.ico')
    elif style == 'windowed':
        return os.path.join(os.path.dirname(__file__), r'datas\icon-windowed.ico')
    else:
        raise ValueError('style must be "console" or "windowed"')