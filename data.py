'''获取datas文件夹内的文件'''

import os
import json

root = os.path.join(os.path.dirname(__file__), 'datas')

def getIconPath(style: str = 'console') -> str:
    '''获取图标路径'''

    if style == 'console':
        return os.path.join(root, r'icon-console.ico')
    elif style == 'windowed':
        return os.path.join(root, r'icon-windowed.ico')
    else:
        raise ValueError('style must be "console" or "windowed"')

def getRecentPaths(file: str = 'recent.json') -> list[str]:
    '''获取最近打开的Python文件路径'''

    path = os.path.join(root, file)
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as file:
        return list(json.load(file))

def writeRecentPaths(paths: list[str], file: str = 'recent.json'):
    '''写入最近打开的Python文件路径'''

    path = os.path.join(root, file)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(paths, file, ensure_ascii=False, indent=4)