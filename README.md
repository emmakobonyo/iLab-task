 # IP Address Publisher for MQTT

This script publishes the Raspberry Pi's IP address to an MQTT broker, allowing remote services to locate the device on the network.

## Overview

The script performs the following functions:
- Connects to a public MQTT broker (EMQX)
- Retrieves the device's IP address
- Publishes the IP address to a specific MQTT topic
- Can be used with MQTTX client to receive the published data

## Dependencies

- `paho-mqtt` library:  https://github.com/eclipse-paho/paho.mqtt.python
- Python 3.x
- Working internet connection

## Installation

```bash
pip install paho-mqtt
```

## Configuration
The script uses the following default settings:

- Broker: broker.emqx.io
- Port: 1883
- Topic: gateway/carpark/ip
- Client ID: gateway0

## Usage

- Save the script as [text](ip-address-pub-test.py)
- Run the script:

```bash
python ip-address-pub-test.py
```
The script will:

- Connect to the MQTT broker
- Retrieve the device's IP address
- Publish the IP to the specified topic
- Print connection status to the console


## Receiving Data with MQTTX

To receive the published IP address:
- Install and open MQTTX
- Configure a new connection:
-- Host: broker.emqx.io
-- Port: 1883
-- Client ID: (any unique ID)
- Subscribe to the topic gateway/carpark/ip
- Run the script, and the IP address will appear in MQTTX
