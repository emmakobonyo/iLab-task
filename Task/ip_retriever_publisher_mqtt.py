# mqtt_ip_publisher.py

import time
import socket
import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/ip_address"
RETRY_INTERVAL = 5  # seconds

def get_ip_address():
    #Get the machine's current IP ADDRESS
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google DNS
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print("Error getting IP address:", e)
        return None

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker.")
        ip = get_ip_address()
        if ip:
            client.publish(MQTT_TOPIC, ip)
            print(f"Published IP: {ip}")
        else:
            print("Could not retrieve IP.")
    else:
        print("Failed to connect, return code:", rc)

def connect_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect

    while True:
        try:
            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            client.loop_start()
            break  # Connected successfully
        except Exception as e:
            print(f"Connection failed: {e}. Retrying in {RETRY_INTERVAL}s...")
            time.sleep(RETRY_INTERVAL)

if __name__ == "__main__":
    connect_mqtt()
