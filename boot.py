import machine
from network import WLAN
wlan = WLAN() # get current object, without changing the mode

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)
    # configuration below MUST match your home router settings!!
    #wlan.ifconfig(config=('192.168.0.7', '255.255.255.0', '192.168.0.1', '8.8.8.8'))

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('router', auth=(WLAN.WPA2, 'LetMeInAgain'), timeout=5000)
    print('Connected to WiFi router...')
    while not wlan.isconnected():
        machine.idle() # save power while waiting