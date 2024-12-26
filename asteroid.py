import pygame
import circleshape
import constants
import random

class Asteroid(circleshape.CircleShape):

    containers = (),
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    
    def split(self):
        self.kill()
        if (self.radius <= constants.ASTEROID_MIN_RADIUS):
            return
        else:
            random_angle = random.uniform(20, 50)
            angle1 = random_angle
            angle2 = -random_angle
            velocity1 = self.velocity.rotate(angle1) * 1.2
            velocity2 = self.velocity.rotate(angle2) * 1.2
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
            asteroid1.velocity = velocity1
            asteroid2.velocity = velocity2

