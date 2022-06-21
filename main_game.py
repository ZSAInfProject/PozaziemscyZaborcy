import os

import pygame

import boss_ship
import enemy_ship
import menu
import player_ship
from game import Game
from game_exit import GameExit
from player_action import PlayerAction
from resources import Resources
from task import Task

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)

GAME = Game()


def event_catch():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME.game_exit = GameExit.TO_DESKTOP
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                GAME.player.add_velocity(-2.5)
            elif event.key == pygame.K_d:
                GAME.player.add_velocity(2.5)
            elif event.key == pygame.K_RETURN and GAME.bullets[0] is None and not GAME.game_end:
                GAME.bullets[0] = GAME.player.shoot()
            elif event.key == pygame.K_q:
                GAME.game_exit = GameExit.TO_DESKTOP
            # quit is for the Escape key
            elif event.key == pygame.K_ESCAPE:
                GAME.game_exit = GameExit.TO_MENU
        elif event.type == pygame.KEYUP and not GAME.game_end:
            if event.key == pygame.K_a:
                GAME.player.add_velocity(2.5)
            elif event.key == pygame.K_d:
                GAME.player.add_velocity(-2.5)


def boss_event_catch() -> list[PlayerAction]:
    player_actions = []

    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                player_actions.append(PlayerAction.EXIT_TO_DESKTOP)
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_a:
                        player_actions.append(PlayerAction.START_MOVING_LEFT)
                    case pygame.K_d:
                        player_actions.append(PlayerAction.START_MOVING_RIGHT)
                    case pygame.K_RETURN:
                        player_actions.append(PlayerAction.SHOOT)
                    case pygame.K_q:
                        player_actions.append(PlayerAction.EXIT_TO_DESKTOP)
                    case pygame.K_ESCAPE:
                        player_actions.append(PlayerAction.EXIT_TO_MENU)
            case pygame.KEYUP:
                match event.key:
                    case pygame.K_a | pygame.K_d:
                        player_actions.append(PlayerAction.STOP_MOVING)

    return player_actions


def draw_objects():
    for bullet in GAME.bullets:
        if bullet is not None:
            GAME.game_display.blit(bullet.bullet_model, [
                                   bullet.x_pos, bullet.y_pos])
    GAME.game_display.blit(GAME.player.player_model, [
                           GAME.player.s_x, GAME.player.s_y, GAME.player.width, GAME.player.width])
    for enemy in range(0, len(GAME.enemies)):
        GAME.game_display.blit(GAME.enemies[enemy].enemy_model, [
                               GAME.enemies[enemy].s_x, GAME.enemies[enemy].s_y, GAME.enemies[enemy].width, GAME.enemies[enemy].width])
        if GAME.enemies[enemy].check_player(GAME.player):
            GAME.points = 0
            GAME.game_end = True
            GAME.game_lost = True
            del GAME.enemies
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
    if not GAME.bullets[0] is None and GAME.bullets[0].y_pos <= 0:
        GAME.bullets[0] = None


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
        GAME.field.move_enemies(GAME.screen_x, GAME.enemies)


def draw_game_lost():
    if GAME.game_lost:
        GAME.game_display.blit(GAME.label_game_lost, (200, 220))


def init_tasks():
    tasks = []
    enemy_shoot_interval = 2  # 0.65
    enemy_shot_offset = (0, 0.5)  # 0.2
    tasks.append(Task("enemy shot", enemy_shoot_interval,
                      enemy_shot_offset, GAME.tickrate))
    return tasks


def parse_tasks(tasks):
    for task in tasks:
        if task.check_ticks(GAME.tickrate):
            if task.name == "enemy shot":
                shooter = GAME.field.find_shooter(GAME.enemies, GAME.player)
                GAME.bullets.append(GAME.enemies[shooter].shoot())


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

        # Check if player touched wall
        GAME.player.touched_wall(GAME.screen_x)

        # Draw every object on screen
        draw_objects()

        # Check if any task happens this tick
        parse_tasks(tasks)

        # Check bullet condition
        check_bullet_condition()


def first_level_loop() -> GameExit:
    menu.menu(GAME)

    # Initialize tasks
    tasks = init_tasks()

    while GAME.game_exit is GameExit.FALSE:

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
        # print(GAME.clock)

    return GAME.game_exit


# modifies the player object!
def boss_handle_events(player_actions: list[PlayerAction], player: player_ship.PlayerShip,
                       enemy: boss_ship.BossShip, screen_y: int) -> GameExit:
    for action in player_actions:
        match action:
            case PlayerAction.EXIT_TO_MENU:
                return GameExit.TO_MENU
            case PlayerAction.EXIT_TO_DESKTOP:
                return GameExit.TO_DESKTOP
            case PlayerAction.START_MOVING_LEFT:
                player.start_moving_left()
            case PlayerAction.START_MOVING_RIGHT:
                player.start_moving_right()
            case PlayerAction.STOP_MOVING:
                player.stop_moving()
            case PlayerAction.SHOOT:
                player.shoot_player_bullet(enemy, screen_y)

    return GameExit.FALSE


def boss_level_loop() -> GameExit:
    GAME = Game()

    screen_x = GAME.screen_x
    screen_y = GAME.screen_y
    player_x = 220
    player_y = 0.9 * screen_y - GAME.width
    resources = Resources()
    game_display = GAME.game_display

    # TODO
    boss_x = screen_x / 2 * 1.15
    boss_y = screen_y / 3
    boss_width = 100
    boss_model = resources.matej_model

    player = player_ship.PlayerShip(player_x, player_y, resources.playership_model)
    boss = boss_ship.BossShip(boss_x, boss_y, boss_width, boss_model, player, screen_x, screen_y)

    while GAME.game_exit is GameExit.FALSE:
        # Fill the screen with blue colour
        game_display.fill((51, 102, 255))

        # Catch the events
        player_actions: list[PlayerAction] = boss_event_catch()
        # And handle them
        game_exit = boss_handle_events(player_actions, player, boss, screen_y)
        if game_exit != game_exit.FALSE:
            return game_exit

        # check if game won / lost
        if not boss.exists:
            GAME.game_display.blit(GAME.label_game_won, (200, 220))
        elif not player.exists:
            GAME.game_display.blit(GAME.label_game_lost, (200, 220))
        else:
            # update entities (they update their bullets)
            player.update()
            boss.update()

            # draw entities
            player.draw_for_boss(game_display)
            boss.draw_for_boss(game_display)

            # see if enemy touches player
            boss.check_player(player)

        # Update the display, maintain stable framerate
        pygame.display.update()
        GAME.clock.tick(GAME.tickrate)

    return GameExit.FALSE


def restart_game() -> None:
    global GAME
    GAME = Game()


def play_first_level():
    game_exit = GameExit.FALSE

    while game_exit is not GameExit.TO_DESKTOP:
        restart_game()
        game_exit = first_level_loop()

    return GAME.game_won

