import pygame
import sys
import sprites

pygame.init()

WIDTH = 1920/2
HEIGHT = 1080/2
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

velocityX = 0
velocityY = 0

spriteList = pygame.sprite.Group()

jetSprite = sprites.Jet(1.5) 
jetSprite.rect.centerx = WIDTH//2
jetSprite.rect.centery = HEIGHT//2

backgound = sprites.TiledBackgrounds("graphics/stars.jpeg", 0.5)
backgound.rect.x = 0
backgound.rect.y = 0

backgound2 = sprites.TiledBackgrounds("graphics/stars.jpeg", 0.5)
backgound2.rect.x = WIDTH
backgound2.rect.y = 0

spriteList.add(backgound)
spriteList.add(backgound2)
spriteList.add(jetSprite)

keys = []

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
    
    spriteList.update(screen, keys)
    screen.fill((255, 255, 255))
    spriteList.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()