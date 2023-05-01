import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
from awsiot.greengrasscoreipc.model import (
    QOS,
    SubscribeToIoTCoreRequest,
    IoTCoreMessage
)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                


class StreamHandler(client.SubscribeToIoTCoreStreamHandler):
    def __init__(self, topic, qos):
        super().__init__()
        self.topic = topic
        self.qos = qos
        
    def on_stream_event(self, event: IoTCoreMessage) -> None:
        message = event.message.payload.decode('utf-8')
        print(f"Received message: {message} on topic {self.topic} with QoS {self.qos}")



if __name__ == "__main__":
    
    REQUEST_TOPIC = "Web Camera"
    ipc_client = awsiot.greengrasscoreipc.connect() # IPC Client greengrass client
    print(f"The device is connected")
    subscribe_request = SubscribeToIoTCoreRequest()  # request instance
    print(dir(subscribe_request))
    subscribe_request.topic = REQUEST_TOPIC
    subscribe_request.qos = QOS.AT_MOST_ONCE
    stream_handler = StreamHandler(topic=subscribe_request.topic, qos=subscribe_request.qos)
    operation = ipc_client.new_subscribe_to_iot_core(stream_handler)
    operation.activate(subscribe_request)
    
