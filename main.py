#!/usr/bin/python3

import pygame
import main_game

pygame.init()

#FIXME no co tu dużo gadać, zjebane i tyle xd
def main():

    main_game.game_loop()
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
