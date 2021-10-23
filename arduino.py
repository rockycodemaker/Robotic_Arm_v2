import serial


def find_comports():
    # search available com ports
    # choose first one (for now)
    return ['COM3']

class Serialcom:
    def __init__(self, comport_name):
        self.comport_name = comport_name
        self.baud_rate = 9600
        self.timeout = 1
        self.ser = serial.Serial()

    def serial_write(self, message):
        print(message)
        #self.ser.write(message)

    def serial_read(self):
        # read until newline and return the string
        message = ""
        message = message + self.ser.read(1).decode('utf8')
        while message[-1] != "\n":
            message = message + self.ser.read(1).decode('utf8')
        return message

    def init(self):
        connected = False
        self.ser = serial.Serial(self.comport_name, self.baud_rate, timeout=self.timeout) # open comport connection

        # send the magic message
        if self.ser.is_open:
            self.serial_write('magic_message!')
            answer = self.serial_read()
            if answer == "message_received!":  # check for the magic answer
                connected = True
            else:
                connected = False
        return connected

    def close_comport(self):
        self.ser.close()
