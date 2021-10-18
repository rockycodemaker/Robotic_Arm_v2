import serial

def initcomport():
    # search available com ports
    # choose first one (for now)
    return ['COM3']

#comment
class Serialcom:
    def __init__(self, comport_name):
        self.comport_name = comport_name
        self.baud_rate = 9600
        self.timeout = 1
        self.ser = serial.Serial()

    def open_comport(self):  # receive comport name and baud rate
        # open the serial com port
        self.ser = serial.Serial(self.comport_name, self.baud_rate, timeout=self.timeout)

    def serial_write(self, message):
        print(message)
        #self.ser.write(message)

    def close_comport(self):
        self.ser.close()

# print(serial.tools.list_ports)

a = Serialcom('COM3')
a.open_comport()
a.serial_write('hello world!')
a.close_comport()
