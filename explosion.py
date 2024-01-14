import pygame
import math
import random
from pygame.locals import *

pygame.init()

class Animation:
    image_sprite = [pygame.image.load(f"graphics/explosion/explosion 3_{i+1}.png") for i in range(64)]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = 0

    def update(self, window, speed, up_speed):
        if self.value >= len(Animation.image_sprite):
            return True  # Animation has finished
        else:
            image = Animation.image_sprite[math.floor(self.value)]
            window.blit(image, (self.x, self.y))
            self.x -= speed
            self.y += up_speed
            self.value += 0.67
            return False  # Animation still in progress

def startExplosion(animations, x, y):
    animations.append(Animation(x, y))

# animations = []
# clock = pygame.time.Clock()
# run = True

# while run:
#     clock.tick(60)

#     for event in pygame.event.get():
#         if event.type == QUIT:
#             run = False
#         elif event.type == KEYDOWN and event.key == K_f:
#             startExplosion(0, 0)

#     window.fill((0, 0, 0))

#     animations_to_remove = []
#     for animation in animations:
#         if animation.update():
#             animations_to_remove.append(animation)

#     for animation in animations_to_remove:
#         animations.remove(animation)

#     pygame.display.update()

# pygame.quit()
