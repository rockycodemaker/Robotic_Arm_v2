import pygame

"""""
this file is dependent on pygame being initialized in the main file
the joystick module is dependent on pygame's events, which only work when it is initialized
may initializing the screen as well is enough tho...
"""


def initialize():
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    gamepad_names = []
    for joystick in joysticks:
        gamepad_names.append(joystick.get_name())
    print(gamepad_names)
    return joysticks


def event_handler(event, micro_controller):
    if event.type == pygame.JOYAXISMOTION:
        if event.axis <= 1:
            if event.value < -0.2 or event.value > 0.2:
                print(event)
        elif 2 <= event.axis <= 3:
            if event.value < -0.2 or event.value > 0.2:
                print(event)

    if event.type == pygame.JOYBALLMOTION:
        print(event)
    if event.type == pygame.JOYHATMOTION:
        print(event)
    if event.type == pygame.JOYBUTTONUP:
        print(event)
        micro_controller.serial_write("OFF")
    if event.type == pygame.JOYBUTTONDOWN:
        print(event)
        micro_controller.serial_write("ON")
