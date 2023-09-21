# Import necessary modules
from pyats import aetest
from pyats.topology import loader

# Load the testbed configuration
testbed = loader.load('my_testbed.yaml')

# Define a testcase class
class MyTestcase(aetest.Testcase):

    # Connect to the device
    @aetest.setup
    def connect_to_device(self):
        self.device = testbed.devices['Cat8000V']
        self.device.connect()

    # Check if the device is reachable
    @aetest.test
    def check_device_reachability(self):
        if self.device.is_connected():
            self.passed(f"Device is reachable.")
        else:
            self.failed(f"Device is not reachable.")

    # Get device information
    @aetest.test
    def get_device_info(self):
        output = self.device.execute('show version')
        self.passed(f"Device Info:\n{output}")

    # Disconnect from the device
    @aetest.cleanup
    def disconnect_from_device(self):
        self.device.disconnect()

# Run the testcases
if __name__ == '__main__':
    aetest.main()
