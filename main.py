import global_variables, gui, key_press, os, ptext, pygame, screens, sys
from global_variables import *
from gui import *
from key_press import *




os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300, 100)
SCREEN = pygame.display.set_mode((global_variables.screen_width, global_variables.screen_height), 0, 0)



pygame.init()


def main():
    pygame.display.set_caption('Start Menu Example')
    screens.title_screen()

    SCREEN.fill((0, 0, 0))  ### Erases screen
    if global_variables.MUSIC:
        pygame.mixer_music.load('sounds\\space_walk.ogg')
        pygame.mixer_music.play(-1, 0.0)


    """ The following is only going to look stupid because its just demonstrating something"""

    """ Draws a NAVY rectangle on the top left, then draws another black one in the center of it"""

    pygame.draw.rect(SCREEN, NAVY, Gui.SCREENONE)
    pygame.draw.rect(SCREEN, BLACK, Gui.SCREENONEIN)

        # Bottom
    pygame.draw.rect(SCREEN, NAVY, Gui.SCREENTWO)

    display.flip()
    screens.new_game()

    while True:

        # event_check()
        pygame.display.flip()  # DEBUG
        fpsClock.tick(FPS)

def event_check():

    key_press.key()


if __name__ == '__main__':
    main()
