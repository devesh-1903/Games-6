import pygame
#pylint: disable=no-member


class player_ship:

    def __init__(self):
        self.player_img = pygame.image.load('resorces/ship.png')
        self.img_width = 70
        self.img_height = 80
        self.draw_position_x = 265
        self.draw_position_y = 600
        self.lives = 5

    def fire(self):
        self.damage = 5
        self.bullet_count = 1
