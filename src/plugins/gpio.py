import RPi.GPIO as GPIO
from smbus2 import SMBus


TEMPERATURE_REGISTER = 0x00
I2C_BUS = 1
TC74_ADDRESS = 0x48
READ_INTERVAL = 1
GPIO.setmode(GPIO.BOARD)

def read_temperature(address: int = TC74_ADDRESS, bus_number: int = I2C_BUS) -> dict:
    with SMBus(bus_number) as bus:
        value = bus.read_byte_data(address, TEMPERATURE_REGISTER)
    celsius = value - 256 if value >= 128 else value
    return {"temperature_c": celsius}

def activate_pin():
    GPIO.output(8, GPIO.HIGH)


def read_pin():
    GPIO.input