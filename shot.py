import pygame
import circleshape
import constants

class Shot(circleshape.CircleShape):

    containers = (),

    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt