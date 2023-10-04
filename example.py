# Import the StrideClient class from the library
from StrideModbusDriver.StrideClient import StrideClient

def main():
    # Initialize the StrideClient with the host IP address
    modbus_device = StrideClient(host="192.168.1.127")
    # Make the units Celsius
    modbus_device.write_units('C')



    try:
        # Call the read_firmware function and store the result
        result = modbus_device.read_samples()
        # Print the result of the read_firmware function
        print(f"{result}")
    except Exception as e:
        # Print an error message if reading fails
        print(f"Error reading firmware version: {e}")


if __name__ == '__main__':
    main()
