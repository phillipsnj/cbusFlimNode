#import sys
#sys.path.append('./lib')

from lib.python_os import cbus_os
import json
import time
import sys
# from merg_widgets import merg_button

config = {
    "manufacturer": 165,
    "cpuManufId": 3,
    "module": 58,
    "name": "PYTHON",
    "major_version":  1,
    "minor_version": "A",
    "beta": 1,
    "consumer": True,
    "producer": True,
    "flim": True,
    "bootloader": False,
    "consume_own_events": True,
    "node_variables": 2,
    "event_variables": 3,
    "data_file": "cbus_os_data.json"
}


class test_python_os(cbus_os):
    def __init__(self):
        cbus_os.__init__(self, config)
        self.debug = False
        self.acon(1)
        
    def my_function(self, event_variables):
        print('Test_picow my_function ' + str(self.data['variables']) + ' : ' + str(event_variables))
        
    def run(self):
        print("Test_cbus_os RUN")
        while True:
            self.process()
            #self.button.check()
            # self.amber_led.check()
            time.sleep(0.001)