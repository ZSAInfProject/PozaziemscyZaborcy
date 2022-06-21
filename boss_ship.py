from __future__ import annotations

import random
from enum import Enum, auto

from pygame import transform, Surface

import boss_bullet
import ship

from boss_bullet import BossBullet

# this inspection is an error in PyCharm when dealing with auto
# noinspection PyArgumentList
from player_ship import PlayerShip

# this inspection is an error in PyCharm when dealing with auto
# noinspection PyArgumentList
class BossState(Enum):
    IDLING = auto()
    SHOOTING = auto()
    SLAMMING = auto()
    MOVING = auto()
    RETURNING = auto()

    @classmethod
    def get_random_state(cls) -> BossState:
        return random.choice([cls.IDLING, cls.SHOOTING, cls.SLAMMING, cls.MOVING])


# this inspection is an error in PyCharm when dealing with auto
# noinspection PyArgumentList
class BossDirection(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    @classmethod
    def get_random_direction(cls) -> BossDirection:
        return random.choice([cls.UP, cls.DOWN, cls.LEFT, cls.RIGHT])


class BossStateMachine:
    IDLING_BASE_DURATION: int = 360
    IDLING_BASE_VARIATION: int = 120

    SHOOTING_BASE_COUNT: int = 3
    SHOOTING_BASE_VARIATION: int = 1
    SHOOTING_COOLDOWN: int = 30

    MOVING_DISTANCE: int = 150

    def __init__(self) -> None:
        super().__init__()

        self.current_state: BossState = BossState.IDLING

        # in frames
        self.idling_timer: int = 0
        self.idling_current_duration: int = self.calculate_idling_duration()

        self.shooting_current_bullets_to_shoot: int = self.calculate_shooting_bullet_count()
        self.shooting_bullets_shot: int = 0
        self.shooting_timer: int = 0

        self.slamming_done: bool = False

        self.moving_current_distance: float = 0
        self.moving_current_direction: BossDirection = BossDirection.get_random_direction()
        self.is_returning: bool = False

    def update(self):
        if self.current_state == BossState.IDLING:
            self.idling_timer += 1
        elif self.current_state == BossState.SHOOTING:
            self.shooting_timer += 1

        self.try_change_state()

    def try_change_state(self):
        match self.current_state:
            case BossState.IDLING if self.idling_timer == self.idling_current_duration:
                self.idling_timer = 0
                self.idling_current_duration = self.calculate_idling_duration()

                # can go back to idling (as per design)!
                self.current_state = BossState.get_random_state()
            case BossState.SHOOTING if self.shooting_bullets_shot == self.shooting_current_bullets_to_shoot:
                self.shooting_bullets_shot = 0
                self.shooting_current_bullets_to_shoot = self.calculate_shooting_bullet_count()

                self.current_state = BossState.IDLING
            case BossState.SLAMMING if self.slamming_done:
                self.current_state = BossState.IDLING
            case BossState.MOVING if self.moving_current_distance == self.MOVING_DISTANCE:
                self.moving_current_distance = 0

                self.current_state = BossState.RETURNING
            case BossState.RETURNING if self.moving_current_distance == self.MOVING_DISTANCE:
                self.moving_current_distance = 0
                self.moving_current_direction = BossDirection.get_random_direction()

                self.current_state = BossState.IDLING

    @staticmethod
    def calculate_idling_duration():
        idling_variation = random.randint(
            -BossStateMachine.IDLING_BASE_VARIATION, BossStateMachine.IDLING_BASE_VARIATION)

        return BossStateMachine.IDLING_BASE_DURATION + idling_variation

    @staticmethod
    def calculate_shooting_bullet_count():
        count_variation = random.randint(
            -BossStateMachine.SHOOTING_BASE_VARIATION, BossStateMachine.SHOOTING_BASE_VARIATION)

        return BossStateMachine.SHOOTING_BASE_COUNT + count_variation


# this inspection is an error in PyCharm when dealing with auto
# noinspection PyArgumentList
class SlammingDirection(Enum):
    LEFT = auto()
    MIDDLE = auto()
    RIGHT = auto()
    NONE = auto()

    @classmethod
    def get_random_slamming_direction(cls) -> SlammingDirection:
        return random.choice([cls.LEFT, cls.MIDDLE, cls.RIGHT])

class BossShip(ship.Ship):
    MOVING_VELOCITY: float = 2.5
    SLAMMING_VELOCITY: float = 10

    def __init__(self, given_x: float, given_y: float, given_width: int, boss_model: Surface, player: PlayerShip,
                 screen_x: int, screen_y: int):
        super().__init__(given_x, given_y)

        self.width: int = given_width
        self.height: int = self.width
        self.is_enemy: bool = True
        self.enemy_model: Surface = transform.scale(boss_model, (self.width, self.height))
        self.state_machine: BossStateMachine = BossStateMachine()
        self.bullets: list[BossBullet] = []

        self.player = player
        self.screen_x = screen_x
        self.screen_y = screen_y

        self.original_x = given_x
        self.original_y = given_y
        self.slamming_direction = SlammingDirection.NONE

        self.health = 10
        self.exists = True

    def shoot(self):
        return boss_bullet.BossBullet(
            self.s_x, self.s_y + self.width, -4545, self.width * 0.1, self.bullet_width, self.bullet_height,
            self.player, self.screen_y)

    def update(self) -> None:
        self.state_machine.update()

        for bullet in self.bullets:
            bullet.update()

        match self.state_machine.current_state:
            case BossState.MOVING:
                self.state_machine.moving_current_distance += BossShip.MOVING_VELOCITY

                match self.state_machine.moving_current_direction:
                    case BossDirection.UP:
                        self.s_y -= BossShip.MOVING_VELOCITY
                    case BossDirection.DOWN:
                        self.s_y += BossShip.MOVING_VELOCITY
                    case BossDirection.LEFT:
                        self.s_x -= BossShip.MOVING_VELOCITY
                    case BossDirection.RIGHT:
                        self.s_x += BossShip.MOVING_VELOCITY
            case BossState.RETURNING:
                self.state_machine.moving_current_distance += BossShip.MOVING_VELOCITY

                match self.state_machine.moving_current_direction:
                    case BossDirection.UP:
                        self.s_y += BossShip.MOVING_VELOCITY
                    case BossDirection.DOWN:
                        self.s_y -= BossShip.MOVING_VELOCITY
                    case BossDirection.LEFT:
                        self.s_x += BossShip.MOVING_VELOCITY
                    case BossDirection.RIGHT:
                        self.s_x -= BossShip.MOVING_VELOCITY
            case BossState.SHOOTING if self.state_machine.shooting_timer == BossStateMachine.SHOOTING_COOLDOWN:
                self.state_machine.shooting_timer = 0
                self.state_machine.shooting_bullets_shot += 1

                self.shoot()
            case BossState.SLAMMING:
                match self.slamming_direction:
                    case SlammingDirection.NONE:
                        self.slamming_direction = SlammingDirection.get_random_slamming_direction()
                    case SlammingDirection.LEFT:
                        if self.s_x == self.width / 2:
                            if self.s_y >= self.screen_y - self.width / 2:
                            # if self.s_y >= self.screen_y:
                                self.s_x = self.original_x
                                self.s_y = self.original_y

                                self.state_machine.slamming_done = True
                            else:
                                self.s_y = min(self.screen_y - self.width / 2, self.s_y + BossShip.SLAMMING_VELOCITY)
                        else:
                            self.s_x = max(self.width / 2, self.s_x - BossShip.SLAMMING_VELOCITY)
                    case SlammingDirection.RIGHT:
                        if self.s_x == self.screen_x - self.width / 2:
                            if self.s_y == self.screen_y - self.width / 2:
                            # if self.s_y == self.screen_y:
                                self.s_x = self.original_x
                                self.s_y = self.original_y

                                self.state_machine.slamming_done = True
                            else:
                                self.s_y = min(self.screen_y - self.width / 2, self.s_y + BossShip.SLAMMING_VELOCITY)
                        else:
                            self.s_x = min(self.screen_x - self.width / 2, self.s_x + BossShip.SLAMMING_VELOCITY)
                    case SlammingDirection.MIDDLE:
                        if self.s_y == self.screen_y - self.width / 2:
                        # if self.s_y == self.screen_y:
                            self.s_x = self.original_x
                            self.s_y = self.original_y

                            self.state_machine.slamming_done = True
                        else:
                            self.s_y = min(self.screen_y - self.width / 2, self.s_y + BossShip.SLAMMING_VELOCITY)

    def damage(self):
        self.health -= 1

        if self.health <= 0:
            self.exists = False

    def draw_for_boss(self, game_display):
        game_display.blit(self.enemy_model, [
            self.s_x, self.s_y, self.width, self.width])

        for player_bullet in self.bullets:
            game_display.blit(player_bullet.bullet_model, [
                player_bullet.x_pos, player_bullet.y_pos])

        for i in reversed(range(len(self.bullets))):
            if not self.bullets[i].exists:
                del self.bullets

    def check_player(self, player):  # wykraczy sie jesli kiedykolwiek gracz/enemy nie bedzie kwadratem
        if ((self.s_x <= player.s_x <= self.s_x + self.width) or (self.s_x <= player.s_x + player.width <= self.s_x + self.width)) and \
                ((self.s_y <= player.s_y <= self.s_y + self.width) or (self.s_y <= player.s_y + player.width <= self.s_y + self.width)):
            player.exists = False
