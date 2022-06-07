# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/05/31 15:44
import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)


def check_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)


def update_screen(ai_setting, screen, ship, aliens, bullets):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_setting, screen, ship, bullets):
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def get_numbers(ai_setting, alien_width):
    a_space_x = ai_setting.screen_width - 2 * alien_width
    n_aliens_x = int(a_space_x / (2 * alien_width))
    return n_aliens_x


def get_number_rows(ai_setting, ship_heigh, alien_heigh):
    a_space_y = (ai_setting.screen_heigh - (3*alien_heigh)-ship_heigh)
    number_rows = int(a_space_y / (2*alien_heigh))
    return number_rows


def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height+2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_setting, screen, ship, aliens):
    alien = Alien(ai_setting, screen)
    n_aliens_x = get_numbers(ai_setting, alien.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(n_aliens_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)

