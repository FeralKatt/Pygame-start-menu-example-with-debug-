import sys
import pygame
import gui
from pygame import *
from images.images import *
import ptext
from global_variables import *
from gui import Gui
from main import *


def title_screen():
    menu_scroll = 1480
    start_color = 1
    option_color = 1
    quit_color = 1
    mousex = 0
    mousey = 0

    while True:  # TODO DEBUG can be removed later
        mouseClicked = False
        SCREEN.blit(Images.main_menu0, (0, 0))

        if not pygame.mixer_music.get_busy():
            if global_variables.MUSIC:
                pygame.mixer_music.load('sounds\\space_walk.ogg')
                pygame.mixer_music.play(-1, 0.0)

        ptext.draw('Start Menu', center=(screen_width / 2, screen_height / 10),
                   fontname='fonts\\grandnational.ttf', fontsize=175, color='NAVY',
                   gcolor='PURPLE', owidth=1.0, ocolor='BLACK', underline=True)

        ptext.draw('Example', center=(screen_width / 2, screen_height / 4),
                   fontname='fonts\\grandnational.ttf', fontsize=125, color='PURPLE',
                   gcolor='NAVY', owidth=1.0, ocolor='BLACK')

        ptext.draw('Credits currently in credits file', (menu_scroll, 880))  # Displays credit txt
        menu_scroll -= 2

        if menu_scroll < -20:  # scrolls credit text
            menu_scroll = 1480

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

    # checks for mouse position and menus
        if DEBUGMENU:  # DEBUG MENU
            ptext.draw('DEBUG', (900, 720), fontname='fonts\\deadman.ttf', fontsize=50,
                       color='red')
            if 890 <= mousex <= 1100 and 720 <= mousey <= 760:
                if global_variables.DEBUG == 1:
                    if mouseClicked:
                        global_variables.DEBUG = 0
                elif global_variables.DEBUG == 0:
                    if mouseClicked:
                        global_variables.DEBUG = 1

        if option_color == 1:  ######## OPTIONS
            ptext.draw('OPTIONS', (605, 495),
                       fontname='fonts\\deadman.ttf', fontsize=50, color='white',
                       owidth=0.5, ocolor='black', shadow=(.5, .5), scolor='black')
            if 600 <= mousex <= 845 and 495 <= mousey <= 540:
                option_color = 2

        if start_color == 1:  ####### START MENU
            ptext.draw('START', (630, 422),
                       fontname='fonts\\deadman.ttf', fontsize=50, color='white',
                       owidth=0.5, ocolor='black', shadow=(.5, .5), scolor='black')
            if 610 <= mousex <= 820 and 420 <= mousey <= 470:
                start_color = 2

        elif start_color == 2:
            ptext.draw('START', (630, 422.5),
                       fontname='fonts\\deadman.ttf', fontsize=50, color='purple',
                       owidth=0.5, ocolor='black')
            if mouseClicked:
                pygame.mixer_music.stop()
                return
            if mousex < 610 or mousex > 820 or mousey < 420 or mousey > 470:
                start_color = 1

        if option_color == 1:  ######## OPTIONS
            ptext.draw('OPTIONS', (605, 495),
                       fontname='fonts\\deadman.ttf', fontsize=50, color='white',
                       owidth=0.5, ocolor='black', shadow=(.5, .5), scolor='black')
            if 600 <= mousex <= 845 and 495 <= mousey <= 540:
                option_color = 2

        elif option_color == 2:  #
            ptext.draw('OPTIONS', (605, 495.5),
                       fontname='fonts\\deadman.ttf', fontsize=50, color='purple',
                       owidth=0.5, ocolor='black', scolor='black')
            if mouseClicked:
                options_menu()

            elif mousex < 600 or mousex > 845 or mousey < 495 or mousey > 540:
                option_color = 1

        if quit_color == 1:  ####### QUIT MENU
            ptext.draw("QUIT", (658, 567.5),
                       fontname='fonts\\deadman.ttf', fontsize=50, color='white',
                       owidth=0.5, ocolor='black', shadow=(.5, .5), scolor='black')
            if 650 <= mousex <= 790 and 580 <= mousey <= 620:
                quit_color = 2

        elif quit_color == 2:
            ptext.draw("QUIT", (658, 567),
                       fontname='fonts\\deadman.ttf', fontsize=50, color='purple',
                       owidth=0.5, ocolor='black')
            if 650 <= mousex <= 790 and 580 <= mousey <= 620:  # if within bounds and clicked activate
                if mouseClicked:
                    pygame.quit()
                    sys.exit()
            elif mousex < 650 or mousex > 790 or mousey < 580 or mousey > 620:  # if not within bounds revert
                quit_color = 1

        if global_variables.DEBUG == 1:  # TODO DEBUG
            fpsClock.tick(FPS)
            debugFps = str(fpsClock)
            debugW = str(screen_width / 2) ### CHANGE FOR VALUE NEEDED
            debugH = str(screen_height / 2)
            debugMH = str(mousey)
            debugMW = str(mousex)

            ### DEBUG FONT

            debugFont = pygame.font.SysFont('comicsansms', 10)
            debugFontColor = RED

            if mouseClicked:
                print(debugMW, debugMH)

            fpsSurfObj = debugFont.render(debugFps, True, debugFontColor)
            # fpsRect = fpsSurfObj.get_rect()
            fpsDB = fpsSurfObj

            widthSurfObj = debugFont.render(debugW, True, debugFontColor)
            # widthRect = widthSurfObj.get_rect()
            widthDB = widthSurfObj

            heightSurfObj = debugFont.render(debugH, True, debugFontColor)
            # heightRect = heightSurfObj.get_rect()
            heightDB = heightSurfObj

            mousexSurfObj = debugFont.render(debugMW, True, debugFontColor)
            # mousexRect = mousexSurfObj.get_rect()
            mousexDB = mousexSurfObj

            mouseySurfObj = debugFont.render(debugMH, True, debugFontColor)
            # mousexRect = mouseySurfObj
            mouseyDB = mouseySurfObj

            SCREEN.blit(fpsDB, (250, 200)) # TODO CHANGE AS NEEDED
            SCREEN.blit(widthDB, (250, 220))
            SCREEN.blit(heightDB, (250, 240))
            SCREEN.blit(mousexDB, (250, 260))
            SCREEN.blit(mouseyDB, (250, 280))

        pygame.display.flip()
        fpsClock.tick(FPS)




def options_menu():
    screen_erase = True
    mousex = 0
    mousey = 0

    while True:
        mouseClicked = False

        if screen_erase:
            SCREEN.fill((0, 0, 0)) ### Erases screen
            pygame.display.flip()
            screen_erase = False

        SCREEN.blit(Images.main_menu0, (0, 0))

        ptext.draw('HyperSpace:', center=(screen_width / 2, screen_height / 10),
                   fontname='fonts\\grandnational.ttf', fontsize=175, color='NAVY',
                   gcolor='PURPLE', owidth=1.0, ocolor='BLACK', underline=True)

        ptext.draw('Transport', center=(screen_width / 2, screen_height / 4),
                   fontname='fonts\\grandnational.ttf', fontsize=125, color='PURPLE',
                   gcolor='NAVY', owidth=1.0, ocolor='BLACK')

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        if DEBUGMENU:  # DEBUG MENU
            ptext.draw('DEBUG', (900, 720), fontname='fonts\\deadman.ttf', fontsize=50,
                       color='red')
            if 890 <= mousex <= 1100 and 720 <= mousey <= 760:
                if global_variables.DEBUG == 1:
                    if mouseClicked:
                        global_variables.DEBUG = 0
                elif global_variables.DEBUG == 0:
                    if mouseClicked:
                        global_variables.DEBUG = 1

        ptext.draw('MUSIC:', (630, 422),
                   fontname='fonts\\deadman.ttf', fontsize=50, color='white',
                   owidth=0.5, ocolor='black', shadow=(.5, .5), scolor='black')

        if global_variables.MUSIC:
            ptext.draw('ON', (825, 422),
                       fontname='fonts\\deadman.ttf', fontsize=50, color='white',
                       owidth=0.5, ocolor='black', shadow=(.5, .5), scolor='black')

            if 632 <= mousex <= 905 and 425 <= mousey <= 465:
                if mouseClicked:
                    global_variables.MUSIC = False
                    pygame.mixer_music.stop()

        elif not global_variables.MUSIC:
            ptext.draw('OFF', (825, 422),
                       fontname='fonts\\deadman.ttf', fontsize=50, color='white',
                       owidth=0.5, ocolor='black', shadow=(.5, .5), scolor='black')
            if 632 <= mousex <= 905 and 425 <= mousey <= 465:
                if mouseClicked:
                    global_variables.MUSIC = True
                    pygame.mixer_music.play(-1, 0.0)
        ptext.draw('RETURN', (625, 500),
                   fontname='fonts\\deadman.ttf', fontsize=50, color='white',
                   owidth=0.5, ocolor='black', shadow=(.5, .5), scolor='black')
        if 625 <= mousex <= 850 and 500 <= mousey <= 540:
            if mouseClicked:
                return global_variables.MUSIC

        if global_variables.DEBUG == 1:  # TODO DEBUG MENU
            fpsClock.tick(FPS)
            debugFps = str(fpsClock)
            debugW = str(screen_width / 2) ### CHANGE FOR VALUE NEEDED
            debugH = str(screen_height / 2)
            debugMH = str(mousey)
            debugMW = str(mousex)

            ### DEBUG FONT

            debugFont = pygame.font.SysFont('comicsansms', 10)
            debugFontColor = RED
            if mouseClicked:
                print(debugMW, debugMH)
            fpsSurfObj = debugFont.render(debugFps, True, debugFontColor)
            fpsRect = fpsSurfObj.get_rect()
            fpsDB = fpsSurfObj

            widthSurfObj = debugFont.render(debugW, True, debugFontColor)
            widthRect = widthSurfObj.get_rect()
            widthDB = widthSurfObj

            heightSurfObj = debugFont.render(debugH, True, debugFontColor)
            heightRect = heightSurfObj.get_rect()
            heightDB = heightSurfObj

            mousexSurfObj = debugFont.render(debugMW, True, debugFontColor)
            mousexRect = mousexSurfObj.get_rect()
            mousexDB = mousexSurfObj

            mouseySurfObj = debugFont.render(debugMH, True, debugFontColor)
            mousexRect = mouseySurfObj
            mouseyDB = mouseySurfObj

            SCREEN.blit(fpsDB, (250, 200)) # TODO CHANGE AS NEEDED
            SCREEN.blit(widthDB, (250, 220))
            SCREEN.blit(heightDB, (250, 240))
            SCREEN.blit(mousexDB, (250, 260))
            SCREEN.blit(mouseyDB, (250, 280))

        pygame.display.flip()


def new_game():  # TODO figure this shit out
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        #pygame.draw.rect(SCREEN, BLACK, Gui.SCREENONEIN)
        #SCREEN.blit(DISPLAYONE, (5, 5))
        #pygame.display.update(Gui.SCREENONERect)

        pygame.display.flip()  #DEBUG