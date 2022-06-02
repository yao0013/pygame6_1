# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/05/30 16:20
import sys
import pygame
from pygame.sprite import Group
from setting import Setting
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Setting()

    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_heigh))
    pygame.display.set_caption("aline")
    ship = Ship(ai_setting, screen)
    bullets = Group()

    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting, screen, ship, bullets)


if __name__ == '__main__':
    run_game()

# TODO 12-5 侧面射击：编写一个游戏，将一艘飞船放在屏幕左边，并允许玩家上下移动飞船。在玩家按空格键时，让飞船发射一颗在屏幕中向右穿
#  行的子弹，并在子弹离开屏幕而消失后将其删除，即改成横版游戏！！！
