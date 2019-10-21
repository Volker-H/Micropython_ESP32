"""
publish temperature every 60 sec.
uses the classes from temperatur_mqtt_client_class.py which uses dht_class.py
"""

from temperatur_mqtt_client_class import TemperatureClient

tc = TemperatureClient('microPythTest', '10.253.247.26', 25, topic='/sensor/test/temp')
tc.start(60)
