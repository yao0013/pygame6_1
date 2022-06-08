# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/05/30 16:20
import sys
import pygame
from pygame.sprite import Group
from button import Button
from setting import Setting
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_setting = Setting()

    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_heigh))
    pygame.display.set_caption("aline")
    play_button = Button(ai_setting, screen, "Start")
    stats = GameStats(ai_setting)
    sb = Scoreboard()
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_setting, screen, ship, aliens)

    while True:
        gf.check_events(ai_setting, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_setting, screen, stats, ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()

# TODO 12-5 侧面射击：编写一个游戏，将一艘飞船放在屏幕左边，并允许玩家上下移动飞船。在玩家按空格键时，让飞船发射一颗在屏幕中向右穿
#  行的子弹，并在子弹离开屏幕而消失后将其删除，即改成横版游戏！！！
