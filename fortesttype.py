# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/06/01 17:25
import pygame
import sys
from setting import Setting


def run_game():
    pygame.init()
    ai_setting = Setting()

    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_heigh))
    pygame.display.set_caption("aline")
    # ship = Ship(ai_setting, screen)
    while True:
        check_events()


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)

if __name__ == '__main__':
    run_game()