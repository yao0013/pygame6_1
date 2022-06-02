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
        bullets.update()
        gf.update_screen(ai_setting, screen, ship, bullets)


if __name__ == '__main__':
    run_game()
