import pygame
import controller


class PygameDisplay:
    def __init__(self):
        self.done = False
        self.fullscreen = False
        self.monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.currentResolution = [1200, 700]
        self.controllerEvents = [pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION,
                                 pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN]


class Button:
    def __init__(self, screen, h, w, x, y):
        self.rect = pygame.draw.rect(screen)

    def draw(selfself):
        screen.blit


def controller_event(event, screen_class):
    found = False
    for x in screen_class.controllerEvents:
        if event == x:
            found = True
            break
    return found


def initialize():

    pygame.display.init()
    pygame.font.init()

    screen_class = PygameDisplay()

    # Loop until the user clicks the close button.
    screen_class.done = False

    # keep track if fullscreen or not
    screen_class.fullscreen = False

    pygame.display.set_caption("Robotic Arm v2")

    screen_class.screen = pygame.display.set_mode(screen_class.currentResolution, pygame.RESIZABLE)
    return screen_class


def update_start(screen):
    screen.fill((0, 0, 50))

    default_font = pygame.font.get_default_font()
    font = pygame.font.Font(default_font, 36)
    surface = font.render("Settings", True, [255, 255, 255])
    title = screen.blit(surface, (25, 25))
    titlebox = pygame.draw.rect(screen, (155, 155, 155), [title.x-5, title.y-5, title.width+10, title.height+10], 0, 5)
    title = screen.blit(surface, (25, 25))

    return screen


def event_handler(screen_class, micro_controller):
    for event in pygame.event.get():  # User did something.
        if event.type == pygame.QUIT:  # If user clicked close.
            screen_class.done = True  # Flag that we are done so we exit this loop.
        elif event.type == pygame.VIDEORESIZE:
            if not screen_class.fullscreen:
                screen_class.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                screen_class.currentResolution = [event.w, event.h]
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                screen_class.done = True
            if event.key == pygame.K_F11:
                screen_class.fullscreen = not screen_class.fullscreen
                if screen_class.fullscreen:
                    screen_class.screen = pygame.display.set_mode(screen_class.monitor_size, pygame.FULLSCREEN)
                else:
                    screen_class.screen = pygame.display.set_mode(screen_class.currentResolution, pygame.RESIZABLE)
        elif controller_event(event.type, screen_class):
            controller.event_handler(event, micro_controller)
    return screen_class


def update_end():
    pygame.display.update()
    pygame.time.Clock().tick(60)


def close():
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
