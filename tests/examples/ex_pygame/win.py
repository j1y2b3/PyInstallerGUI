import pygame

import data

class Win:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption('pygame example')
        pygame.display.set_icon(data.get_icon())
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.clock.tick(60)