# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/05/31 15:44
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


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


def check_events(ai_setting, screen, stats, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, screen, stats, play_button, ship, aliens, bullets,
                              mouse_x, mouse_y)


def check_play_button(ai_setting, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_setting.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()



def update_screen(ai_setting, screen, stats, ship, aliens, bullets, play_button):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(ai_setting, screen, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()
        create_fleet(ai_setting, screen, ship, aliens)


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


def check_fleet_edges(ai_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break


def change_fleet_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1


def ship_hit(ai_setting, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_setting, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets)


def check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stats, screen, ship, aliens, bullets)
            break

