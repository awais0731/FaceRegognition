import datetime
import json
from FRecognition.exception import FRException
import sys, os
from FRecognition.FRProcess.request_process import RequestProcess

class MessageReceiver:
    
    def __init__(self,channel):
        self._channel = channel

    
    def handle_basic_deliver(self, ch, method, properties, body):
        try:

            queue_detect = f"In queue function detected from queue: {datetime.datetime.now()}"
            print(queue_detect)

            data = body.decode('utf-8')
            request_obj = json.loads(data)

            # print("LogId is :", request_obj['LogId'])
            # print("Directory path is: ",request_obj['directory_path'])
            # print("Cam Id is: ",request_obj['cam_id'])
            # print("Timestamp is: ",request_obj['timestamp'])
            # print("Location id is: ",request_obj['loc_id'])

            directory_path = request_obj['directory_path']
            
            if directory_path is not None:
                request_process = RequestProcess(request_obj)
                
        except Exception as e:
            raise FRException(e,sys)
