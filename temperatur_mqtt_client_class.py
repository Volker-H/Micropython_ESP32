import utime
from dht_class import TemperatureSensor
from umqtt.robust import MQTTClient


class TemperatureClient:
    """
    represents mqtt client which publish temperature data on an interval
    """

    def __init__(self, client_id, server, pin, topic=None):
        """

        :param client_id: Unique Mqtt Client ID
        :type client_id: str
        :param server: mqtt server (ip or domain)
        :type server: str
        :param pin: Pin for DHT Sensor
        :type pin: int
        :param topic: topic for posting the temp
        :type topic: str
        """
        self.sensor = TemperatureSensor(pin)
        self.client = MQTTClient(client_id, server)
        if not topic:
            self.topic = '/sensor/unspecified/temp'
        else:
            self.topic = topic
        self.client.connect()

    def publishTemperature(self):
        """
        reads the temperature and publishes it

        """
        t = self.sensor.read_data()[0]
        self.client.publish(self.topic, str(t))

    def start(self,interval):
        """
        non ending posting of temperature at the given interval
        :param interval: time in sec
        :type interval: int
        :return:
        """
        while True:
            self.publishTemperature()
            utime.sleep(interval)

