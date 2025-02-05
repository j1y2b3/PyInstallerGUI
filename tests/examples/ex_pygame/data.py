import os

import pygame

def get_icon():
    path = os.path.join(os.path.dirname(__file__), r'datas\icon.ico')
    return pygame.image.load(path)