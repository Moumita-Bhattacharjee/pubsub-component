import traceback
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
        print("ok")
        try:
            respond(event)
            
        except:
            traceback.print_exc()
       



if __name__ == "__main__":
    
    ipc_client = awsiot.greengrasscoreipc.connect() # IPC Client greengrass client
    print(f"The device is connected")
    REQUEST_TOPIC = "Web Camera"
    REQUEST_QOS = QOS.AT_MOST_ONCE
    request = SubscribeToIoTCoreRequest()
    request.topic_name = REQUEST_TOPIC
    request.qos = REQUEST_QOS
    handler = StreamHandler()
    operation = ipc_client.new_subscribe_to_iot_core(handler)
    operation.activate(request)
    future_response = operation.get_response() 
    future_response.result()
    
