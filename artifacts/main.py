import traceback
import time
import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
from awsiot.greengrasscoreipc.model import (
    IoTCoreMessage,
    QOS, 
    SubscribeToIoTCoreRequest  
)   

def respond(event):
        message = str(event.message.payload, "utf-8")
        topic_name = event.message.topic_name
        print(message)
        print(topic_name)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           


class StreamHandler(client.SubscribeToIoTCoreStreamHandler):
    def __init__(self):
        super().__init__()
      
    def on_stream_event(self, event: IoTCoreMessage) -> None:
        try:
            respond(event)
            
        except:
            traceback.print_exc()

   
ipc_client = awsiot.greengrasscoreipc.connect() # IPC Client greengrass client
print("The device is connected")
REQUEST_TOPIC = "Web Camera"
TIMEOUT = 10
request = SubscribeToIoTCoreRequest()
request.topic_name = REQUEST_TOPIC
request.qos = QOS.AT_MOST_ONCE
handler = StreamHandler()
operation = ipc_client.new_subscribe_to_iot_core(handler)
future = operation.activate(request)
future.result(TIMEOUT)

# Keep the main thread alive, or the process will exit.
while True:
    time.sleep(10)

# To stop subscribing, close the operation stream.
operation.close()
    
