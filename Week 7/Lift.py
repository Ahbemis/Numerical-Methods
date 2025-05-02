import serial
import time

# Serial port config
ser = serial.Serial(
    port='COM5',        # Change as needed
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

if not ser.is_open:
    ser.open()

# Send 'VR' command with carriage return
command = '$FL25000$'  # Version Request
ser.write(command.encode('ascii'))
print(f"Sent: {command.strip()}")

# Wait briefly and read response
time.sleep(0.1)
response = ser.read_all().decode('ascii').strip()

if response:
    print(f"Response: {response}")
else:
    print("No response. Check wiring, COM port, or baud rate.")

ser.close()
