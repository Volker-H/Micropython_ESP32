import utime
import dht
import machine

d = dht.DHT22(machine.Pin(25))


def get_dht_data():
    d.measure()
    utime.sleep_ms(100)
    temp = d.temperature()
    hum = d.humidity()
    return temp, hum


print('DHT Testprogramm')

while True:
    data = []
    data = get_dht_data()

    print('Temperatur: ', end='')
    print(data[0])
    print('Humidity: ', end='')
    print(data[1])
    utime.sleep(5)
