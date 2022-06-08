# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/06/07 16:35
class GameStats:

    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0

