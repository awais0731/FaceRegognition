from FRecognition.exception import FRException
import os, sys
from FRecognition.utils.main_utils import image_to_base64
from FRecognition.logger import logging
from FRecognition.FRProcess.face_match_api import FaceMatchAPIs
from FRecognition.constant import conn, procedure_name
from FRecognition.utils.main_utils import execute_stored_procedure

class RequestProcess:

    faceTypeList  = execute_stored_procedure(conn, procedure_name)

    # @classmethod
    # def set_face_type_list(cls, face_type_list):
    #     cls._face_type_list = face_type_list

    # @classmethod
    # def get_face_type_list(cls):
    #     return cls._face_type_list

    def __init__(self, request_obj):
        self.request_obj = request_obj
        self.myProcess()

    def myProcess(self):
        
        
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
                    print(item)
                logging.info("Picture path before matching: " + imagefile)
                data = FaceMatchAPIs.MatchedFace(float(0.58), base64, "search_dlmisdb")
                logging.info("Picture path after matching: " + imagefile)
                print("result is",data)
                print("here")
     
        except Exception as e:
            raise FRException(e, sys)


    

    
    

    