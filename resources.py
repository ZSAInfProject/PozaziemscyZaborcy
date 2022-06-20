from pygame import image, transform
import os


class Resources:
    matej_model = image.load(os.path.join('./textures/', 'matej_cropped.png'))
    bullet_model = image.load(os.path.join('./textures/', 'bullet.png'))
    playership_model = image.load(
        os.path.join('./textures/', 'playership.png'))
    first_intro_path = 'videos/intro_1.mp4'
