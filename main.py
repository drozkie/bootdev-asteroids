import pygame
from asteroid import *
from asteroidfield import *
from constants import *
from lives import *
from player import *
from scoreboard import *
from shot import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")

    pygame.init()

    #CREATE GROUPS
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    #CONFIGURE GROUPS
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    #SET VARIABLES
    game_clock = pygame.time.Clock()
    dt = 0
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #GROUP (UPDATABLE, DRAWABLE)
    field = AsteroidField()
    lives = Lives()

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0), rect=None, special_flags=0)

        dt = game_clock.tick(60) / 1000

        for object in updatable:
            object.update(dt)

        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if p.check_collision(asteroid):
                print("Game over!")
                return

        for shot in shots:
            for asteroid in asteroids:
                if shot.check_collision(asteroid):
                    asteroid.split()
                    p.add_points(asteroid)
                    shot.kill()

        current_score = p.get_score()

        scoreboard(screen, current_score)

        pygame.display.flip()

if __name__ == "__main__":
    main()