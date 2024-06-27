from FRecognition.exception import FRException
import os, sys
from FRecognition.utils.main_utils import image_to_base64
from FRecognition.logger import logging
from FRecognition.FRProcess.face_match_api import FaceMatchAPIs
from FRecognition.constant import conn, DBInfo, sourceWatchList
from FRecognition.utils.main_utils import execute_stored_procedure_to_get_DBInfo
from FRecognition.singleton import Singleton

class RequestProcess:

    faceTypeList  = execute_stored_procedure_to_get_DBInfo(conn, DBInfo)

    def __init__(self, request_obj):
      
        self.request_obj = request_obj
        self.myProcess()

    def myProcess(self):

        # singleton = Singleton()
        # dlims_distict_list = singleton.get_dlims_distict_list() #this retunr list of dlimis district list
        
        base64 = ""

        self.request_obj['directory_path'] = "D:/test_images/20240611132956402.jpg"
        imagefile = self.request_obj['directory_path']

        #imagefile = self.request_obj['directory_path']
        try:
            
            if base64 == "":

                if  os.path.exists(imagefile):
                    base64 = image_to_base64(imagefile)
                else:
                    logging.info("image file path does not found :" + imagefile)
                    

            if base64 != "":
                for item in RequestProcess.faceTypeList:
                    data = FaceMatchAPIs.MatchedFace(float(item.MatchingThreshold), base64, item.ApiEndPoint)
                    
                    if data is not None:
                        if 'result' in data and data['result'] is not None:
                            if 'paths' in data['result'] and len(data['result']['paths']) > 0:
                                if item.ApiEndPoint == str(sourceWatchList):
                                    print("fda")
                                else:
                                    print("watch list")
                            else:
                                print("data not found from", item.ApiEndPoint)
                        else:
                            print("data not found from", item.ApiEndPoint)
                    else:
                        print("data not found from", item.ApiEndPoint, imagefile)
                    
                
        except Exception as e:
            raise FRException(e, sys)


    

    
    

    