# this file will contain the main code
import arduino


def Main():
    # initialize serial connection
    port_names = arduino.find_comports()                # get a list of port names
    port_name = port_names[0]                           # choose a port
    micro_controller = arduino.Serialcom(port_name)     # create a 'Serialcom' class to setup serial communication
    if micro_controller.init():                         # initialize the serial communication
        micro_controller.close_comport()


if __name__ == '__main__':
    Main()
