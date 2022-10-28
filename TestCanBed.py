import can_bed
import json
import time
from machine import Pin
from merg_widgets import merg_input, merg_led, merg_led2

config = {
    "manufacturer": 165,
    "cpuManufId": 3,
    "module": 58,
    "name": "TEST",
    "major_version":  1,
    "minor_version": "B",
    "beta": 1,
    "consumer": True,
    "producer": True,
    "flim": True,
    "bootloader": False,
    "consume_own_events": False,
    "node_variables": 2,
    "event_variables": 3,
    "data_file": "TestCanBed.json"
}


class Test(can_bed.can_bed):
    def __init__(self):
        can_bed.can_bed.__init__(self, config)
        self.debug = False
       
    def my_function(self, event):
        print('my_function ' + str(self.data['variables']) + ' : ' + str(event))
        
    def run(self):
        print("TestCanPico RUN")
        while True:
            self.process()
            time.sleep(0.001)
