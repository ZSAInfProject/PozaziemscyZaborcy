import os
import pygame
import menu
from game import Game
from task import Task

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)

pygame.init()
GAME = Game()


def event_catch():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME.game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                GAME.entities[0].add_velocity(-2.5)
            if event.key == pygame.K_d:
                GAME.entities[0].add_velocity(2.5)
            if event.key == pygame.K_RETURN and GAME.bullets[0] is None and not GAME.game_end:
                GAME.bullets[0] = GAME.entities[0].shoot()
            if event.key == pygame.K_q:
                GAME.game_exit = True
        if event.type == pygame.KEYUP and not GAME.game_end:
            if event.key == pygame.K_a:
                GAME.entities[0].add_velocity(2.5)
            if event.key == pygame.K_d:
                GAME.entities[0].add_velocity(-2.5)


def draw_objects():
    for bullet in GAME.bullets:
        if bullet is not None:
            GAME.game_display.blit(bullet.bullet_model, [bullet.x_pos, bullet.y_pos, bullet.width, bullet.width])
    GAME.game_display.blit(GAME.entities[0].player_model, [GAME.entities[0].s_x, GAME.entities[0].s_y, GAME.entities[0].width, GAME.entities[0].width])
    for enemy in range(1, len(GAME.entities)):
        GAME.game_display.blit(GAME.entities[enemy].enemy_model, [GAME.entities[enemy].s_x, GAME.entities[enemy].s_y, GAME.entities[enemy].width, GAME.entities[enemy].width])
        if GAME.entities[enemy].check_player(GAME.entities[0]):
            GAME.points = 0
            GAME.game_end = True
            GAME.game_lost = True
            del GAME.entities
            del GAME.field
            break

def check_bullet_condition():
    for i, bullet in enumerate(GAME.bullets):
        if bullet is not None:
            bullet_exists, GAME.points = bullet.draw(GAME)
            if not bullet_exists:
                if i >= 1:
                    del GAME.bullets[i]
                else:
                    GAME.bullets[i] = None


def check_field_existence():
    if not GAME.field.exists:
        del GAME.field
        GAME.game_end = True
        GAME.game_won = True


def draw_game_won():
    if GAME.game_won:
        GAME.game_display.blit(GAME.label_game_won, (200, 220))
    else:
        check_field_existence()


def check_field():
    if not GAME.game_won:
        GAME.field.move_enemies(GAME.screen_x, GAME.entities)


def draw_game_lost():
    if GAME.game_lost:
        GAME.game_display.blit(GAME.label_game_lost, (200, 220))


def init_tasks():
    tasks = []
    enemy_shoot_interval = 0.65  # 0.65
    enemy_shot_offset = (0, 0.2)  # 0.2
    tasks.append(Task("enemy shot", enemy_shoot_interval, enemy_shot_offset, GAME.tickrate))
    return tasks


def parse_tasks(tasks):
    for task in tasks:
        if task.check_ticks(GAME.tickrate):
            if task.name == "enemy shot":
                shooter = GAME.field.find_shooter(GAME.entities)
                GAME.bullets.append(GAME.entities[shooter].shoot())


def progress_game(tasks):
    if GAME.game_end:
        if GAME.game_won:
            draw_game_won()
        else:
            draw_game_lost()
    else:
        # Move enemies (name = pain)
        check_field()

        # Check if player won the game (name hurts my eyes so fckin much)
        draw_game_won()

        #Check if player touched wall
        GAME.entities[0].touched_wall(GAME.screen_x)

        # Draw every object on screen
        draw_objects()

        # Check if any task happens this tick
        parse_tasks(tasks)

        # Check bullet condition
        check_bullet_condition()


def game_loop():

    menu.menu(GAME)

    # Initialize tasks
    tasks = init_tasks()

    while not GAME.game_exit:

        # Event-catching loop
        event_catch()

        # Fill screen with white colour
        GAME.game_display.fill((255, 255, 255))

        # Status of the game (win/lose/in progress)
        progress_game(tasks)

        # Update display, maintain stable framerate
        label = GAME.myfont.render("Points: " + str(GAME.points), 1, (0, 0, 0))
        GAME.game_display.blit(label, (10, 10))
        pygame.display.update()
        GAME.clock.tick(GAME.tickrate)
        print(GAME.clock)
