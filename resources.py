from pygame import image, transform
import os

#FIXME gdyby tylko wszystko tak wyglądało...
class Resources:
    def __init__(self):
        self.matej_model = image.load(os.path.join('./textures/', 'matej_cropped.png'))
        self.bullet_model = image.load(os.path.join('./textures/', 'bullet.png'))
        self.playership_model = image.load(os.path.join('./textures/', 'playership.png'))
