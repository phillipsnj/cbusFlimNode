from lib.CbusFlimNode import PicoNode
import socket
# from merg_widgets import merg_input, merg_led2


class cbus_os(PicoNode):
    def __init__(self, config):
        PicoNode.__init__(self, config)

        self.CBUS_HOST = 'localhost'
        self.CBUS_PORT = 5550

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
        self.s.connect((self.CBUS_HOST, self.CBUS_PORT))
        
        if self.nodeId == 0:
            self.rqnn()
    
    def my_function(self, event_variables):
        print('PicoW my_function ' + str(self.data['variables']) + ' : ' + str(event_variables))
    
    def send(self, msg):
        # print("Pico Node Send : " + msg)
        self.s.send(msg.encode())
        
    def process(self):
        data = self.s.recv(1024)
        output = data.decode()
        messages = output.split(';')
        del messages[-1]
        for msg in messages:
            self.action_opcode(msg+";")
            # print(msg + ";")