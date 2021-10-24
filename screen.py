import pygame


class PygameDisplay:
    def __init__(self):
        self.done = False
        self.fullscreen = False
        self.monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.currentResolution = [1200, 700]


def initialize():

    pygame.display.init()

    screen_class = PygameDisplay()

    # Loop until the user clicks the close button.
    screen_class.done = False

    # keep track if fullscreen or not
    screen_class.fullscreen = False

    pygame.display.set_caption("Robotic Arm v2")

    screen_class.screen = pygame.display.set_mode(screen_class.currentResolution, pygame.RESIZABLE)
    return screen_class


def update_start(screen_class):
    screen_class.screen.fill((0, 0, 50))
    return screen_class


def event_handler(screen_class):
    for event in pygame.event.get():  # User did something.
        if event.type == pygame.QUIT:  # If user clicked close.
            screen_class.done = True  # Flag that we are done so we exit this loop.
        if event.type == pygame.VIDEORESIZE:
            if not screen_class.fullscreen:
                screen_class.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                screen_class.currentResolution = [event.w, event.h]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                screen_class.done = True
            if event.key == pygame.K_F11:
                screen_class.fullscreen = not screen_class.fullscreen
                if screen_class.fullscreen:
                    screen_class.screen = pygame.display.set_mode(screen_class.monitor_size, pygame.FULLSCREEN)
                else:
                    screen_class.screen = pygame.display.set_mode(screen_class.currentResolution, pygame.RESIZABLE)

    return screen_class


def update_end():
    pygame.display.update()
    pygame.time.Clock().tick(60)


def close():
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
