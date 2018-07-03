import machine
import config
import time
from machine import RTC
from network import WLAN

rtc  = RTC()  # Real Time Clock
wlan = WLAN() # get current object, without changing the mode

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)
    # configuration below MUST match your home router settings!!
    if not DHCP:
        wlan.ifconfig(config=(IP_ADDR, IP_MASK, IP_GATE, IP_DNS))

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect(config.WIFI_SSID, auth=(WLAN.WPA2, config.WIFI_PASS), timeout=5000)
    print('Connected to WiFi router on IP:',wlan.ifconfig()[0])
    while not wlan.isconnected():
        machine.idle() # save power while waiting

while not rtc.synced():
    rtc.ntp_sync(config.NTP)
    print('Trying to sync time to %s!' %  config.NTP)
    time.sleep(1)
    pass