import pygame
import global_variables

"""This is not generally how you use a class but it works and I was learning it at the time"""


class Gui:

    """ Sets the parameters for each SCREEN size, NOTE if you run this the borders
    wont be exactly what you might think. the code below works to fix that as long as the window X, Y is not changed
    """

    # SCREENONE = pygame.Rect(0, 0, global_variables.screen_width / 2, global_variables.screen_height)
    # SCREENTWO = pygame.Rect(0, 600, global_variables.screen_width, global_variables.screen_height / 2)

    """NOTE: As of writing this 11/2019 I have been learning Python and Pygame for about a month
    so why this works better than the above I'm still learning as I write this"""

    """ To use this comment out the code above with "#"  and un-comment this, with this there is now a lot of 
    space to the bottom and right this is because this calls a per pixel display and above just halves it"""
    SCREENONE = pygame.Rect(2, 2, 960, 715)  # Left Display
    SCREENTWO = pygame.Rect(960, 2, 424, 715)  # Right Display


""" Still learning it too btw"""
