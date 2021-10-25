"""
this file will contains the main code
3 modules are combined here:
Controller: pygame controller module called 'joystick'
Screen: pygame GUI module called 'display'
arduino: pyserial serial communication module
"""

import arduino
import controller
import screen


def main():
    # initialize screen
    screen_class = screen.initialize()

    # initialize controller connection
    joysticks = controller.initialize()

    # initialize serial connection
    port_names = arduino.find_comports()                # get a list of port names
    for port in port_names:
        print(str(port))
    print('\n')
    # choose a port, should get a dropdown button (or something like that) later
    port_name = 'COM3'
    # create a Serial communication class to setup serial communication
    micro_controller = arduino.SerialCom(port_name)

    # initialize the serial communication
    micro_controller.initialize()

    while not screen_class.done:
        screen_class.screen = screen.update_start(screen_class.screen)
        screen_class = screen.event_handler(screen_class, micro_controller)
        screen.update_end()

    micro_controller.close_comport()


if __name__ == '__main__':
    main()
