import utime
import dht
import machine


class TemperatureSensor:
    """
    representation für den DHT22
    """

    def __init__(self, pin):
        """Te
        initialisiert den DHT22
        :param pin: DataPIn des DHT
        :type pin: int
        """
        self.d = dht.DHT22(machine.Pin(pin))

    def read_data(self):
        """
        Read temperatur and humidity
        :return temperatur, humidity
        :rtype: list
        """
        utime.sleep_ms(100)
        self.d.measure()
        temp = self.d.temperature()
        hum = self.d.humidity()
        return temp, hum
