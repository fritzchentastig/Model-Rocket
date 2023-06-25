import rp2
import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
input1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

print("Starting shit")

led_onboard.value(0)
