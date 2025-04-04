from paho.mqtt import client as mqtt_client
import socket

broker = 'broker.emqx.io'
port = 1883
topic = "gateway/carpark/ip"
client_id = 'gateway0'

# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id=client_id, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def get_ip():
    #Gets the Raspberry Pi's IP address
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "0.0.0.0"
    
def publish(client):
    ip_address = get_ip()
    client.publish(topic, ip_address)

def main():
    client = connect_mqtt()
    publish(client)

if __name__ == '__main__':
    main()