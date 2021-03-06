# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/05/30 17:10
class Setting:
    def __init__(self):
        self.screen_width = 800
        self.screen_heigh = 600
        self.bg_color = (230, 230, 230)

        # self.ship_speed_factor = 1
        self.ship_limit = 3

        # self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_heigh = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 6

        # self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 8
        # self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.2
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

