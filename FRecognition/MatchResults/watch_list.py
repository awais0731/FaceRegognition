from FRecognition.utils.main_utils import execute_stored_procedure
from FRecognition.singleton import Singleton
from FRecognition.constant import conn, InsertFRData

class WatchList:

    def __init__(self) -> None:
        pass

    def insert_FrMatch():
        pass

    def Insert_Details(request_obj, data, MatchedFromDb, isCro, MatchedFromDbName, MatchingThreshold):

        parameters = {}
        count = 0

        print("Congratulation you are here")

        for i in range(5):
            if(i < len(data['result']['paths'])):

                
                parameters["LogId"] = request_obj['LogId']
                parameters["SrNo"] = i + 1
                parameters["MatchedScore"] =  round(data['result']['score'][i], 2)
                parameters["MatchSource"] = MatchedFromDb
                parameters["MatchRefId"] = None
                parameters["MatchRefIdTxt"] = None

                picture = WatchList.GetFileNameOrCroNoFromPath(str(data['result']['paths'][i]),MatchedFromDb, isCro, MatchedFromDbName)

                parameters["TagInfo"] = picture
                parameters["Status"] = 'A'
                parameters["Timestamp"] = request_obj['timestamp']
                parameters["MatchThreshold"] = round(MatchingThreshold, 2)


                # parameters["MatchedPictureInfo"] = None

                # if isCro:
                #     parameters["CroNo"] = WatchList.encryption_cro_no(picture)
                # else:
                #     parameters["CroNo"] = None
                params_list = list(parameters.values())

                execute_stored_procedure(conn, InsertFRData, params=params_list, fetch=True)



    def GetFileNameOrCroNoFromPath(pa, DBtype, isCro, MatchedFromDbName):
        
        singleton = Singleton()
        dlims_distict_list = singleton.get_dlims_distict_list() #this retunr list of dlimis district list
        
        data = ""
        path = str(pa)
        if isCro:
            listData = path.replace("./", "").split('/')
            crono = listData[3].split('-')[1]
            data = f"{crono}-{listData[1]}"
        
        elif MatchedFromDbName == "DLIMS":
            listData = path.replace("./", "").replace("../", "").split('\\')
            distid = 0

            frm = next((m for m in dlims_distict_list if m.District_Name == listData[1].upper()), None)

            if frm:
                distid = frm.District_Id
            
            data = f"{listData[-1]}-{listData[1]}-{distid}"
        
        else:
            listData = path.replace("./", "").replace("../", "").split('\\')
            data = listData[-1]
        
        return data


    def encryption_cro_no(input_string):
        string_bytes = input_string.encode('utf-16le')
        sb_bytes = []
        for b in string_bytes:
            sb_bytes.append(f"{b:02X}")
        
        return ''.join(sb_bytes)
