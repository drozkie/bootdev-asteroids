import pygame
from constants import *
from circleshape import *

class Lives(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 270

    def draw(self, screen):
        x = screen.get_width() - 20
        y = screen.get_height() - 20
        pygame.draw.polygon(screen, WHITE, ((x, y), (x + 10, y - 15), (x - 10, y - 15)), 2)