from FRecognition.utils.main_utils import check_record_del_or_not, getPicPAthFromFrLOG
from FRecognition.constant import conn
from FRecognition.utils.main_utils import execute_stored_procedure
from FRecognition.constant import conn, InsertFRData

class WatchList:

    def insert_FrMatch(request_obj, data, MatchedFromDb, MatchingThreshold):
        
        parameters = {}

        for i in range(5):
            if(i < len(data['result']['paths'])):
                
                obj = check_record_del_or_not(conn, data['result']['paths'][i])
                file = getPicPAthFromFrLOG(conn, int(request_obj['LogId']))

                if(obj.status):
                    parameters["LogId"] = request_obj['LogId']
                    parameters["SrNo"] = i + 1
                    parameters["MatchedScore"] =  round(data['result']['score'][i], 2)
                    parameters["MatchSource"] = MatchedFromDb
                    parameters["MatchRefId"] = data['result']['paths'][i]
                    parameters["MatchRefIdTxt"] = None

                
                    parameters["TagInfo"] = obj.file_path
                    parameters["Status"] = 'F'
                    parameters["Timestamp"] = request_obj['timestamp']
                    parameters["MatchThreshold"] = round(MatchingThreshold, 2)

                    params_list = list(parameters.values())

                    execute_stored_procedure(conn, InsertFRData, params=params_list, fetch=False)
