import utime
import machine
import _thread

led_onboard = machine.Pin(25, machine.Pin.OUT)
launch_button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

est_fly_time = 30

global launch_startdel
launch_startdel = True

def launch_read_thread():
    global launch_startdel
    while True:
        if launch_button.value() == 1:
            launch_startdel = False
            print("launched signal received")
    utime.sleep(0.01)
    
def countdowntostart():
    for i in range(25):
        led_onboard.toggle()
        utime.sleep(1)
    for i in range(5):
        led_onboard.toggle()
        utime.sleep(0.5)
    for i in range(25):
        led_onboard.toggle()
        utime.sleep(0.1)
    led_onboard.value(1)
    
    
    
    
_thread.start_new_thread(launch_read_thread, ())
while launch_startdel == True:
    led_onboard.value(1)
    utime.sleep(0.1)
    
countdowntostart()
print("launch")
utime.sleep(est_fly_time)
print("deploying parachute")