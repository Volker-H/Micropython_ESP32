import machine
import utime

print('Rotary Button TEST')
button_a = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
button_b = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

lastA = False
x = 0
lastx = 0

while True:
    a = button_a.value()
    b = button_b.value()
    if x != lastx:
        print(x)
        lastx = x
    if not a and lastA:
        if b:
            x = x - 1
        else:
            x = x + 1
    x = max(0, min(x, 10))
    lastA = a
    utime.sleep_ms(25)
