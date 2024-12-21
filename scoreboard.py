import pygame
from constants import *

def scoreboard(screen, score):
    font = pygame.font.SysFont("Arial", 36)
    render_score = font.render(f"Score: {score}", True, GREEN)
    screen.blit(render_score,(100 - render_score.get_width() // 2, 50 - render_score.get_height() // 2))