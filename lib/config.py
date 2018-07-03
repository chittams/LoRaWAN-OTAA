import machine
import binascii
import ubinascii

# Get the WiFi MAC address
WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

# The Things Network Settings
SERVER = 'router.eu.thethings.network'
PORT = 1700

# NTP Settings
NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

# WiFi settings
WIFI_SSID = 'xxxxxxxxxxxxxxxx'
WIFI_PASS = 'xxxxxxxxxxxxxxxx'

DHCP = True
if not DHCP:
    IP_ADDR = '192.168.0.x'
    IP_MASK = '255.255.255.0'
    IP_GATE = '192.168.0.1'
    IP_DNS  = '192.168.0.1'

#LoRa Application keys
LORA_APP_EUI = binascii.unhexlify('xxxxxxxxxxxxxxxx')
LORA_APP_KEY = binascii.unhexlify('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

#LoRa frequency for AU915
LORA_FREQUENCY = 923300000

