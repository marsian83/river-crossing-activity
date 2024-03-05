import config, utils, pygame
from random import random 

class Wolf:
    def __init__(self, x, bottom, w = None, h = None):
        self.gameDisplay = pygame.display.get_surface()

        self.image = utils.scale_image_maintain_ratio(config.images.get("wolf"), w = w, h = h)
        self.image_idle = utils.scale_image_maintain_ratio(config.images.get("wolf_idle"), w = w, h = h)

        self.x = x
        self.y = bottom - self.image.get_height()

        self.step = 0

        self.on_click = None

    def draw(self):
        if self.step > 240:
            self.gameDisplay.blit(self.image_idle, (self.x, self.y))
        else:
            self.gameDisplay.blit(self.image, (self.x, self.y))

    def update(self):
        self.draw()
        self.step += random() * 0.5
        if self.step > 300:
            self.step = 0
