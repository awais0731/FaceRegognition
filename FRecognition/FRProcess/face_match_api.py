import requests.cookies
from FRecognition.constant import UseProxy, FaceMatchAPIURL, FaceMatchAPIDBURL,proxy_url
import requests
from FRecognition.exception import FRException
import os, sys
from requests.auth import HTTPProxyAuth
import json
import time

class FaceMatchAPIs:

    @staticmethod

    def MatchedFace(threshold, base64, search_db):
        
        useProxy = bool(UseProxy)

        FaceMatch_API_URL = FaceMatchAPIURL
        FaceMatch_API_DBURL  = FaceMatchAPIDBURL + search_db

        print("in matching")

        proxy = proxy_url
        print(proxy)
        http_proxy = {
            "http": proxy,
            "https": proxy
        }

        session = requests.session()

        if useProxy:
            session.proxies = http_proxy
            session.auth = HTTPProxyAuth('','')
        
        match_result = None

        try:
            payload = {
                "thresh": str(threshold),
                "img": base64
            }

            print("in middle")

            response = session.post(FaceMatch_API_URL + FaceMatch_API_DBURL, data=payload)
            if response.status_code == 202:
                print(response.text)
                location_obj = response.json()
                task_url = location_obj["location"]
                print(task_url)
                print("after task_url")

                keep_searching = True

                while(keep_searching):
                    print("in searching")
                    task_response = session.get(FaceMatch_API_URL+task_url)
                    result = task_response.text
                    print(result)
                    match_result = json.loads(result)

                    if match_result["state"] in ["SUCCESS", "FAILURE"]:
                        print("State " + match_result["state"])
                        keep_searching = False
                    else:
                        print("in pending")
                        time.sleep(1)
   
                
        except Exception as e:
            raise FRException(e, sys)
        
        print(match_result)
        return match_result

       