import machine
from machine import ADC
from machine import I2C
from network import LoRa
import ustruct
from ustruct import pack
import Adafruit_BME280
import Adafruit_CCS811
import Adafruit_TSL2591
import LTC2946
import binascii
import pycom
import socket
import time

adc = machine.ADC(0)

def battery():
    numADCreadings = const(100)
    adcread  = adc.channel(attn=3, pin='P16')
    samplesADC = [0.0]*numADCreadings; meanADC = 0.0
    count = 0
    while (count < numADCreadings):
        adcint = adcread()
        samplesADC[count] = adcint
        meanADC += adcint
        count += 1
    meanADC /= numADCreadings
    varianceADC = 0.0
    for adcint in samplesADC:
        varianceADC += (adcint - meanADC)**2
    varianceADC /= (numADCreadings - 1)
    mV = meanADC*1400/1024
    return mV

pycom.heartbeat(False) #needs to be disabled for LED functions to work
pycom.rgbled(0x0f0000) #red

#Set the LoRa to the local region
lora = LoRa(mode=LoRa.LORAWAN, public=1,  adr=0, tx_retries=0, region=LoRa.AU915)

#Set AppEUI and AppKey - use your values from the device settings --> https://console.thethingsnetwork.org/
dev_eui = lora.mac()
app_eui = binascii.unhexlify('70B3D57ED000FF15')
app_key = binascii.unhexlify('1486F238D7545DF185BC45C9E75D15CF')

# Remove default channels
for index in range(0, 72):
    lora.remove_channel(index)

# Set  AU ISM 915 channel plan for TTN Australia
for index in range(0, 7):
    lora.add_channel(index, frequency=923300000+index*600000, dr_min=0, dr_max=3)


for index in range(8, 15):
    lora.add_channel(index, frequency=915200000+index*200000, dr_min=0, dr_max=3)


lora.add_channel(65, frequency=917500000,  dr_min=4,  dr_max=4)

lora.frequency(923300000)

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

sensor1 = Adafruit_BME280.BME280(t_mode=Adafruit_BME280.BME280_OSAMPLE_8, p_mode=Adafruit_BME280.BME280_OSAMPLE_8, h_mode=Adafruit_BME280.BME280_OSAMPLE_8,i2c=i2c)
sensor2 = Adafruit_TSL2591.TSL2591(i2c=i2c)
#sensor3 = Adafruit_CCS811.CCS811(i2c=i2c)
sensor4 = LTC2946.LTC2946(i2c=i2c)

def main():
    while lora.has_joined():
        pycom.rgbled(0x00000f) #blue

        voltage = battery()
        degrees = sensor1.read_temperature()
        pascals = sensor1.read_pressure()
        hectopascals = pascals / 100
        humidity = sensor1.read_humidity()

        packet = pack("ffff",voltage,degrees,hectopascals,humidity)

        print('Battery     = {0:0.3f} mV'.format(voltage))
        print('Temp        = {0:0.3f} deg C'.format(degrees))
        print('Pressure    = {0:0.2f} hPa'.format(hectopascals))
        print('Humidity    = {0:0.2f} %'.format(humidity))
        print('Lux:        = {}'.format(sensor2.lux))
        print('------------------------------')

        time.sleep(1)
        pycom.heartbeat(False)
        time.sleep(1)
        s.setblocking(True)
        s.send(bytes(packet))
        s.setblocking(False)
        time.sleep(1)

main()