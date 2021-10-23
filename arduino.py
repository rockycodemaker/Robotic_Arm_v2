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
        if self.ser.is_open:
            written = self.ser.write(message.encode('utf8'))
            return written
        else:
            return 0

    def serial_read(self, read_bytes=1, time_out=1):
        if self.ser.is_open:

            # change timeout temporarily if necessary
            if self.ser.timeout != time_out:
                self.ser.timeout = time_out

            reply = self.ser.read(read_bytes)

            # change back timeout
            if self.timeout != self.ser.timeout:
                self.ser.timeout = self.timeout

            return reply.decode('utf-8')
        else:
            return "ERROR: serial port is not open"

    def init(self):
        connected = False
        self.ser = serial.Serial(self.comport_name, self.baud_rate, timeout=self.timeout)  # open comport connection
        # send the magic message
        if self.ser.is_open:
            self.ser.timeout = 3
            reply1 = self.ser.read(26)
            print(reply1.decode('utf-8'))

            written = self.serial_write('magic_message!\n')
            if written > 0:
                answer = self.serial_read(18, 2)
                print(answer)
                if answer == "message_received!\n":  # check for the magic answer
                    connected = True
                else:
                    connected = False
                    print("ERROR: init failed")
                    if self.ser.is_open:
                        self.close_comport()
        return connected

    def close_comport(self):
        self.ser.close()
