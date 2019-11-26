import global_variables, gui, key_press, os, ptext, pygame, screens, sys
from global_variables import *
from gui import *
from key_press import *

"""A more than horrible example of a title screen using Pygame and Ptext
Written by FeralKatt

I'll try to come back to it to clarify thing but for the moment it's done
I did this just to teach myself some things so if it helps you learn some things that's awesome

This does use some assets I did not create so the credit file attributes those as per the requirements (I hope)

"""


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300, 100)
SCREEN = pygame.display.set_mode((global_variables.screen_width, global_variables.screen_height), 0, 0)

pygame.init()


def main():
    pygame.display.set_caption('Start Menu Example')
    screens.title_screen()

    if global_variables.MUSIC:
        pygame.mixer_music.load('sounds\\space_walk.ogg')
        pygame.mixer_music.play(-1, 0.0)

    screens.new_game()

    while True:

        pygame.display.flip()  # DEBUG
        fpsClock.tick(FPS)


def event_check(): # Currently not being called

    key_press.key()


if __name__ == '__main__':
    main()
