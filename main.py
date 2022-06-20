#!/usr/bin/python3

import main_game
from game_exit import GameExit
from resources import Resources

from moviepy.editor import *
import pygame


def play_first_intro() -> None:
    with VideoFileClip(Resources.first_intro_path) as clip:
        clip.preview()

    pygame.mixer.music.load('./sounds/codex.mp3')
    pygame.mixer.music.play(-1)


def main():
    play_first_intro()

    game_exit = GameExit.FALSE

    while game_exit is not GameExit.TO_DESKTOP:
        main_game.restart_game()
        game_exit = main_game.game_loop()

    quit()


if __name__ == "__main__":
    # pylint: disable=no-member
    pygame.init()

    main()
