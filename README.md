# STRIDE-driver
 a driver/reader for Stride thermocouple modules

To use, include the StrideClient.py file in your project.
The output of this code is a list of thermocouples 1-8.

# Example
```python
# Import the StrideClient class from the library
from StrideClient import StrideClient

def main():
    # Initialize the StrideClient with the host IP address
    modbus_device = StrideClient(host="192.168.1.126")
    # Make the units Celsius
    modbus_device.write_units('C')

    try:
        # Call the read_firmware function and store the result
        result = modbus_device.read_temps()
        # Print the result of the read_firmware function
        print(f"{result}")
    except Exception as e:
        # Print an error message if reading fails
        print(f"Error reading firmware version: {e}")


if __name__ == '__main__':
    main()

```

With one thermocouple attached to input 1, and the thermocouple in free air, the output will be:
```
[23.3, 1421.1, 1421.1, 1421.1, 1421.2, 1421.2, 1421.3, 1421.3]
```

# Changing thermocouple type

The thermocouple type is set by the set_input_type method. For example, setting input 0 to a 'K' type thermocouple will be:

'''python
    modbus_device.set_input_type(0, 'K')
''''

Supported thermocouple types are:
- Disabled
- Voltage
- K
- J
- R
- S
- T
- B
- E
- N

# Configuring Stride devices

Good luck. The Stride devices are only controllable through Ethernet. There's information written on the units themselves. If you change the IP address, please change the label.


