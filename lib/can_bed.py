from machine import Pin, SPI, Timer
import time
import CbusFlimNode
import cbus2515
from merg_widgets import merg_input, merg_led2

class can_bed(CbusFlimNode.PicoNode):
    def __init__(self, config):
        CbusFlimNode.PicoNode.__init__(self, config)
        self.button = merg_input(21, self.button_on, self.button_off)
        self.green_led = merg_led2(1)
        self.green_led.on = False
        self.amber_led = merg_led2(0)
        self.amber_led.on = True
        self.red_led = merg_led2(2)
        self.red_led.on = False
        
        self.interface = 1  # 1 can, 2 ethernet
        
        # Setup the CAN Bus
        self.SPI_ID = 0
        self.SPI_CLK = Pin(2)
        self.SPI_MOSI = Pin(3)
        self.SPI_MISO = Pin(4)

        self.SPI_CS = Pin(9)
        self.SPI_INT = Pin(11)
        self.OSC_2515 = 16000000
        
        # self.spi = SPI(self.SPI_ID, sck=self.SPI_CLK, mosi=self.SPI_MOSI, miso=self.SPI_MISO)
        self.spi = SPI(self.SPI_ID, sck=self.SPI_CLK, mosi=self.SPI_MOSI, miso=self.SPI_MISO, baudrate=10000000)
        self.can = cbus2515.Cbus2515(self.spi, self.SPI_CS, self.SPI_INT, osc=self.OSC_2515, debug=self.debug)
        time.sleep(0.2)
        if self.debug:
            print("SPI Configuration: " + str(self.spi) + '\n')  # Display SPI config
            if self.can.initialised:
                print('CAN Initialised')
                print('CAN Id '+str(self.can.can_id))
            else:
                print('CAN NOT Initialised')
        
        self.can.change_mode(0)  # 0-Normal, 1-Sleep, 2-Loopback, 3-Listen Only, 4-Configuration
        if self.nodeId == 0:
            self.rqnn()
        
    def my_function(self, event_variables):
        print('CanPico my_function ' + str(self.data['variables']) + ' : ' + str(event_variables))
    
    def button_on(self):
        self.acon(2)
        self.green_led.on = True
        self.red_led.flash = True
        self.red_led.flash_duration = 1000
        self.amber_led.level = 10
        
    def button_off(self):
        self.asof(2)
        self.green_led.on = False
        self.red_led.flash = False
        self.amber_led.level = 5
        
    def send(self, msg):
        # print("Pico Node Send : " + msg)
        self.can.send(msg)
        
    def process(self):
        while self.can.in_waiting():
                # print(self.can.receive())
                self.execute(self.can.receive())
                # print("Check")
                time.sleep(0.01)