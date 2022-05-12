import time
from paho.mqtt import client as mqtt_client

broker = "192.168.50.168"
port = 1883
topic = "/home/raspberry"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect to MQTT Broker")

    client = mqtt_client.Client("RaspiTest")
    client.on_connect = on_connect
    client.connect(broker, port)

    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


print("Testinformation aufm Pi")
print("Der gibt jetzt noch mehr Zeilen aus!")
print("Haha wuhu morty good hahahaha")



client = connect_mqtt()
client.loop_start()
publish(client)
