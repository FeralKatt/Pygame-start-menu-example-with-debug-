import pygame
from pygame import *

"""This is not generally how you use a class but it works and I was learning it at the time"""


class Images:
    main_menu = pygame.image.load('images\\back0.jpg')  # .convert()
    main_menu0 = pygame.transform.smoothscale(main_menu, (1440, 900))


""" Still learning it too btw"""
