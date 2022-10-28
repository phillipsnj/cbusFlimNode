import Test_picow
import json

# nodeId = 1200  # Node Id

node = Test_picow.test_picow()  # Create cbus module


# Start the CBus Module
if __name__ == '__main__':
    print('Test_picow')
    node.run()