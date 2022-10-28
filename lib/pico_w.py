from machine import Pin, SPI, Timer
import CbusFlimNode
import network, time
import rp2
import socket
from merg_widgets import merg_input, merg_led2

class pico_w(CbusFlimNode.PicoNode):
    def __init__(self, config):
        CbusFlimNode.PicoNode.__init__(self, config)
        self.status_led = Pin("LED", Pin.OUT)
        self.status_led(1)
        
        self.status_led = Pin("LED", Pin.OUT)
        self.status_led(0)

        rp2.country('GB')

        self.SSID = 'GL-AR750S-5ae'
        self.PASSWORD = 'Sh@gg3r5'

        self.CBUS_HOST = '192.168.8.227'
        self.CBUS_PORT = 5550
        self.wlan = network.WLAN(network.STA_IF) #initialize the wlan object
        self.wlan.active(True)
        self.wlan.connect(self.SSID, self.PASSWORD)
        
        while not self.wlan.isconnected() and self.wlan.status() >= 0:
             print("Waiting to connect:")
             time.sleep(1)

        print(self.wlan.ifconfig())
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