from dataclasses import dataclass
import json
from paho.mqtt import client as mqtt_client

broker = 'mqtt.aws.innovation-hub.de'
port = 8883
topic = '/fischertechnik/sensordata'
client_id = 'mqttx_d0c12617'
username = 'aklues'
password = 'lRTQxtXHjLTdNT9RcI8b3FH2o6cOH3dm'



#!/usr/bin/env python
# -*- coding: utf8 -*-

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)            
    client = mqtt_client.Client(client_id)
    client.tls_set(tls_version=mqtt_client.ssl.PROTOCOL_TLS)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port, 60)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        json_data = msg.payload.decode()
        length_str = len(msg.payload.decode()) - 1
        datei = open('links_anomalie_sensor2.json','a')
        datei.write(str(msg.payload.decode())[1:length_str] + ",")
        datei.write("\n")
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    client.subscribe(topic, qos=0)
    client.on_message = on_message



def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
    
    
    
