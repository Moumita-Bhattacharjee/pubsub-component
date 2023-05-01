
from datetime import datetime
import time
import traceback
import json
import boto3
import botocore
import sys
import os

import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
from awsiot.greengrasscoreipc.model import (
    IoTCoreMessage,
    QOS,
    SubscribeToIoTCoreRequest
)

TIMEOUT = 10
REQUEST_TOPIC = "Web Camera"


ipc_client = awsiot.greengrasscoreipc.connect()


def respond(event):
    print(type(event))

class StreamHandler(client.SubscribeToIoTCoreStreamHandler):
    def __init__(self):
        super().__init__()

    def on_stream_event(self, event: IoTCoreMessage) -> None:
        try:
            respond(event)
        except:
            traceback.print_exc()

    def on_stream_error(self, error: Exception) -> bool:
        print("ERROR")
        return True  # Return True to close stream, False to keep stream open.

    def on_stream_closed(self) -> None:
        # Handle close.
        pass

# Setup the MQTT Subscription


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