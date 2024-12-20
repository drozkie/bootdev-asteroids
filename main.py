import pygame
from asteroid import *
from constants import *
from player import *
from asteroidfield import *

def main():
    print("Starting asteroids!")

    pygame.init()

    #CREATE GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #CONFIGURE GROUPS
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    #SET VARIABLES
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #GROUP (UPDATABLE, DRAWABLE)
    field = AsteroidField()

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

        pygame.display.flip()

if __name__ == "__main__":
    main()