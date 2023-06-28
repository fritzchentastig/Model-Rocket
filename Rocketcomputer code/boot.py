# boot.py -- run on boot-up
launch_button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
global armed
armed = False
for i in range(10):
     if launch_button.value() == 1:
            armed = True
            print("armed")

if armed:
    import main
else:
    print("Not armed ready for programming")