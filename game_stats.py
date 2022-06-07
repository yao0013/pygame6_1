# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/06/07 16:35
class GameStats:

    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_setting.ship_limit
