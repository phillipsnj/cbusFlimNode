import TestCanBed
import json

# nodeId = 1500  # Node Id

node = TestCanBed.Test()  # Create cbus module


# Start the CBus Module
if __name__ == '__main__':
    print('Test CanBed')
    node.run()

