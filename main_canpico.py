import TestCanPico
import json

# nodeId = 1500  # Node Id

node = TestCanPico.Test()  # Create cbus module


# Start the CBus Module
if __name__ == '__main__':
    print('TestCanPico')
    node.run()

