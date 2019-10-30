#!/usr/bin/python3

import pygame
import main_game

# pylint: disable=no-member
pygame.init()


def main():

    main_game.game_loop()
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
