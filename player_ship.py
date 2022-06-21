import pygame
import ship
import bullet
import os

from player_bullet import PlayerBullet


class PlayerShip(ship.Ship):
    def __init__(self, given_x, given_y, playership_model, player_hp=1):
        super().__init__(given_x, given_y)

        self.width = int(674/10)
        self.height = int(1507/10)
        self.player_model = pygame.transform.scale(playership_model, (self.width, self.height))

        self.player_hp = player_hp
        self.exists = True

        self.base_velocity = 2.5

        self.bullets_for_boss: list[PlayerBullet] = []

    def check_walls(self, screen_x):
        if (round(self.s_x, 0) == 0 and self.velocity < 0)\
                or (round(self.s_x, 0) == screen_x - self.width and self.velocity > 0):
            return False
        else:
            return True

    def shoot(self):
        return bullet.Bullet(self.s_x, self.s_y - self.bullet_height,
                             6, self.width * 0.5, self.bullet_width, self.bullet_height)

    def shoot_player_bullet(self, enemy, screen_y):
        self.bullets_for_boss.append(PlayerBullet(self.s_x, self.s_y - self.bullet_height,
                             6, self.width * 0.5, self.bullet_width, self.bullet_height, enemy, screen_y))

    def touched_wall(self, screen_x):
        if self.check_walls(screen_x):
            self.s_x += self.velocity

    def start_moving_left(self):
        self.velocity = -self.base_velocity

    def start_moving_right(self):
        self.velocity = self.base_velocity

    def stop_moving(self):
        self.velocity = 0

    def damage(self):
        self.player_hp -= 1

        if self.player_hp <= 0:
            self.exists = False

    def draw_for_boss(self, game_display):
        game_display.blit(self.player_model, [
            self.s_x, self.s_y, self.width, self.width])

        for player_bullet in self.bullets_for_boss:
            game_display.blit(player_bullet.bullet_model, [
                player_bullet.x_pos, player_bullet.y_pos])

    def update(self):
        self.s_x += self.velocity

        for playerBullet in self.bullets_for_boss:
            playerBullet.update()

        for i in reversed(range(len(self.bullets_for_boss))):
            if not self.bullets_for_boss[i].exists:
                del self.bullets_for_boss[i]
