import machine
import utime

print('Pin TEST')
p = input('bitte gebe den Pin ein: ') or '26'
p = int(p)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(p, machine.Pin.OUT)
internLed = machine.Pin(1, machine.Pin.OUT)
internLed.value(1)


def ButtonPress():
    led.value(1)
    utime.sleep(10)
    led.value(0)


while True:

    if button.value() == 0:
        ButtonPress()
        utime.sleep_ms(25)

    utime.sleep_ms(50)
