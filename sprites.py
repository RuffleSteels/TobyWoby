import pygame

class Jet(pygame.sprite.Sprite):
    def rotateJet(self, angle):
        self.targetAngle += angle
        self.targetAngle = max(min(self.targetAngle, 45), -45) 



    def __init__(self, scaleFac):
        super().__init__()
        self.angle = 0
        self.targetAngle = 0
        self.original = pygame.image.load("graphics/Boeing747.png").convert_alpha()
        self.original = pygame.transform.flip(self.original, True, False)
        self.original = pygame.transform.scale(self.original,
                                                      (self.original.get_width() * scaleFac,
                                                       self.original.get_height() * scaleFac))
        self.image = self.original
        self.rect = self.image.get_rect()

    def update(self,screen,keys):
        smoothingFactor = 0.01
        if keys[pygame.K_w]:
            self.rotateJet(2)
        if  keys[pygame.K_s]:
            self.rotateJet(-2)
            
        self.angle += (self.targetAngle - self.angle) * smoothingFactor

        self.image = pygame.transform.rotate(self.original, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

class TiledBackgrounds(pygame.sprite.Sprite):
    def __init__(self, image, scaleFac):
        super().__init__()
        self.original = pygame.image.load(image).convert_alpha()
        self.original = pygame.transform.scale(self.original,
                                                      (self.original.get_width() * scaleFac,
                                                       self.original.get_height() * scaleFac))
        self.image = self.original
        self.rect = self.image.get_rect()

    def update(self, surface, keys):
        self.rect.x -= 8

        if self.rect.right <= 0:
            self.rect.x = 1080/2