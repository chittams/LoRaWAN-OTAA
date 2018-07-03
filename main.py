import machine
from machine import I2C
from network import LoRa
import ustruct
from ustruct import pack
import Adafruit_BME280
import Adafruit_CCS811
import Adafruit_TSL2591
import battery
import config
import LTC2946
import pycom
import socket
import time

pycom.heartbeat(False) #needs to be disabled for LED functions to work
pycom.rgbled(0x0f0000) #red

#Set the LoRa to the local region
lora = LoRa(mode=LoRa.LORAWAN, public=1,  adr=0, tx_retries=0, region=LoRa.AU915)

#Set AppEUI and AppKey - use your values from the device settings --> https://console.thethingsnetwork.org/
dev_eui = lora.mac()
app_eui = config.LORA_APP_EUI
app_key = config.LORA_APP_KEY

# Remove default channels
for index in range(0, 72):
    lora.remove_channel(index)

# Set  AU ISM 915 channel plan for TTN Australia
for index in range(0, 7):
    lora.add_channel(index, frequency=923300000+index*600000, dr_min=0, dr_max=3)

for index in range(8, 15):
    lora.add_channel(index, frequency=915200000+index*200000, dr_min=0, dr_max=3)

lora.add_channel(65, frequency=917500000,  dr_min=4,  dr_max=4)

lora.frequency(config.LORA_FREQUENCY)

#Join TTN Network via OTAA
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    pycom.rgbled(0x0f0f00) #yellow
    time.sleep(5)
    print('Trying to join TTN Network!')
    pass

print('Network joined!')
pycom.rgbled(0x000f00) #green

#setup i2c internface
i2c = I2C(0, I2C.MASTER, baudrate=100000)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# set the BME280 sensor 
sensor1 = Adafruit_BME280.BME280(t_mode=Adafruit_BME280.BME280_OSAMPLE_8, p_mode=Adafruit_BME280.BME280_OSAMPLE_8, h_mode=Adafruit_BME280.BME280_OSAMPLE_8,i2c=i2c)
# set the TSL2591 sensor
sensor2 = Adafruit_TSL2591.TSL2591(i2c=i2c)
# set the CCS811 sensor
#sensor3 = Adafruit_CCS811.CCS811(i2c=i2c)
#set the LTC2946 sensor
sensor4 = LTC2946.LTC2946(i2c=i2c)

def main():
    while lora.has_joined():
        pycom.rgbled(0x00000f) #blue

        #Collect the sensor data ready to send out
        voltage = battery.status()
        degrees = sensor1.read_temperature()
        pascals = sensor1.read_pressure()
        hectopascals = pascals / 100
        humidity = sensor1.read_humidity()

        #Create the packet word in Hex
        packet = pack("ffff",voltage,degrees,hectopascals,humidity)

        print('Battery     = {0:0.3f} mV'.format(voltage))
        print('Temp        = {0:0.3f} deg C'.format(degrees))
        print('Pressure    = {0:0.2f} hPa'.format(hectopascals))
        print('Humidity    = {0:0.2f} %'.format(humidity))
        print('Lux:        = {}'.format(sensor2.lux))
        print('------------------------------')

        time.sleep(config.TIMEOUT)
        # Turn the LED off
        pycom.heartbeat(False)
        # Set the LoRa radio to send
        s.setblocking(True)
        # Send the packet out over the LoRa network
        s.send(bytes(packet))
        # Set the LoRa radio to recive
        s.setblocking(False)
        time.sleep(config.TIMEOUT)

main()