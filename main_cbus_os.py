import test_python_os
import json

# nodeId = 1200  # Node Id

node = test_python_os.test_python_os()  # Create cbus module


# Start the CBus Module
if __name__ == '__main__':
    print('Test_picow')
    node.run()