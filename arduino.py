import serial
import serial.tools.list_ports


def find_comports():
    # search available com ports
    ports = serial.tools.list_ports.comports()
    return ports


class SerialCom:
    def __init__(self, comport_name, baud_rate=9600, time_out=1):
        self.comport_name = comport_name
        self.baud_rate = baud_rate
        self.timeout = time_out
        self.ser = serial.Serial()

    def serial_write(self, message):
        if self.ser.is_open:
            message = message + '\n'
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

    def initialize(self):
        connected = False
        self.ser = serial.Serial(self.comport_name, self.baud_rate, timeout=self.timeout)  # open comport connection
        # send the magic message
        if self.ser.is_open:
            self.ser.timeout = 10
            reply1 = self.ser.read(21)
            reply1 = reply1.decode('utf-8')
            if reply1 == "Serial port started!\n":
                print(reply1)
                self.ser.flush()
                written = self.serial_write('magic_message!')
                if written > 0:
                    answer = self.serial_read(18, 10)
                    print(answer)
                    if answer == "message_received!\n":  # check for the magic answer
                        print("successfully connected to microcontroller!")
                        connected = True
                    else:
                        connected = False
                        print("ERROR: init failed")
                        if self.ser.is_open:
                            self.close_comport()
        return connected

    def close_comport(self):
        self.ser.close()
