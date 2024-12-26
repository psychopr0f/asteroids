import pygame
from constants import *
import player
import asteroidfield
import asteroid
import shot

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shootables = pygame.sprite.Group()
    player.Player.containers = (updatables, drawables)
    asteroid.Asteroid.containers = (asteroids, updatables, drawables)
    asteroidfield.AsteroidField.containers = (updatables),
    shot.Shot.containers = (shootables, drawables, updatables)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield1 = asteroidfield.AsteroidField()



    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for updatable in updatables:
            updatable.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid1 in asteroids:
            if asteroid1.collide(player1) <= float(player1.radius + asteroid1.radius):
                print("Game over!")
                exit(0) 
            for shootable in shootables:
                if shootable.collide(asteroid1) <= float(shootable.radius + asteroid1.radius):
                    asteroid1.split()
                    shootable.kill()
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()