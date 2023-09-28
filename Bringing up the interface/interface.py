from pyats import aetest
from pyats.topology import loader

# Create an AETest script
class CheckAndEnableInterface(aetest.Testcase):

    @aetest.setup
    def setup(self):
        # Load the testbed file 
        self.tb = loader.load('my_testbed.yaml')
        self.device = self.tb.devices['Cat8000V']  
        self.interface_name = 'GigabitEthernet3'  

        # Connect to the device
        self.device.connect()

    @aetest.test
    def test_interface_status(self):
        # Execute 'show interfaces' command
        show_interfaces = self.device.execute('show interface')

        # Parse the 'show interfaces' output
        if self.interface_name in show_interfaces:
            output_lines = show_interfaces.splitlines()
            for line in output_lines:
                if self.interface_name in line:
                    status = line.split()[-1].strip('(),')
                    if status.lower() == 'up':
                        self.passed(f'Interface {self.interface_name} is UP.')
                    else:
                        # Interface is down, try to bring it up
                        self.device.configure(f'interface {self.interface_name}\n'
                                             'no shutdown\n'
                                             'end\n')
                        self.passed(f'Interface {self.interface_name} has been enabled.')
                    break
            else:
                self.failed(f'Interface {self.interface_name} not found on the device.')
        else:
            self.failed(f'Interface {self.interface_name} not found on the device.')

    @aetest.cleanup
    def disconnect_from_device(self):
        self.device.disconnect()

if __name__ == '__main__':
    aetest.main()
