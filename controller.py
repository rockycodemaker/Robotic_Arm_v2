import pygame

"""""
this file is dependent on pygame being initialized in the main file
the joystick module is dependent on pygame's events, which only work when it is initialized
may initializing the screen as well is enough tho...
"""

pygame.joystick.init()


def initialize():
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    gamepad_names = []
    for joystick in joysticks:
        gamepad_names.append(joystick.get_name())
        print(joystick.get_numbuttons())
    print(gamepad_names)
    return joysticks


def event_handler (event):
    if event.type == pygame.JOYAXISMOTION:
        print("xaxis\n")
    if event.type == pygame.JOYBALLMOTION:
        print("ball\n")
    if event.type == pygame.JOYHATMOTION:
        print("hat\n")
    if event.type == pygame.JOYBUTTONUP:
        print("btn up\n")
    if event.type == pygame.JOYBUTTONDOWN:
        print("btn down\n")
