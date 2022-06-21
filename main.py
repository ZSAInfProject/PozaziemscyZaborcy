#!/usr/bin/python3

import main_game
from resources import Resources

from moviepy.editor import *
import pygame


def play_first_intro() -> None:
    with VideoFileClip(Resources.first_intro_path) as clip:
        clip.preview()

    pygame.mixer.music.load('./sounds/codex.mp3')
    pygame.mixer.music.play(-1)


def main():
    # play_first_intro()
    #
    # is_won = main_game.play_first_level()
    # if is_won:
    main_game.boss_level_loop()

    quit()


if __name__ == "__main__":
    # pylint: disable=no-member
    pygame.init()

    main()
