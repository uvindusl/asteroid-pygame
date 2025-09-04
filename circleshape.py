import pygame

# base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, raduis):
        if hasattr(self, 'containers'):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = raduis

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
        