from FRecognition.utils.main_utils import check_record_del_or_not, getPicPAthFromFrLOG
from FRecognition.constant import conn
from FRecognition.utils.main_utils import execute_stored_procedure
from FRecognition.constant import conn, InsertFRData, DashBoard_Values
from FRecognition.utils.main_utils import GetNameandWatchListType, GetWatchListType, GetCameralocation
from datetime import datetime

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

                    name_and_watchlist_type = GetNameandWatchListType(conn, data['result']['paths'][i])

                    watchType = GetWatchListType(conn, name_and_watchlist_type.type)

                    loc = GetCameralocation(conn, int(request_obj['cam_id']))

                    message = f"Blacklist: Suspect Person: {name_and_watchlist_type.name} included in the blacklist {watchType.txtval} spotted <br> Location: {loc.location} <br>Time: {datetime.now()} "

                    WatchList.InsertIntoWatchList(int(request_obj['LogId'], i+1, message, file.file_path, data['result']['paths'][i]))
                

    def InsertIntoWatchList(RefKeyId, RefKeySrNo, message, filepath, faceId):
        DashboardId = 1
        InfoAbout = 'F'
        InfoType = 'W'
        RefTypeId = int(faceId)
        status = True
        StatusTimestamp = datetime.now()
        Description = message
        FilePath = filepath


        parameters = {}

        parameters["DashboardId"] = DashboardId
        parameters["InfoAbout"] = InfoAbout
        parameters["InfoType"] =  InfoType
        parameters["RefKeyId"] = RefKeyId
        parameters["RefKeySrNo"] = RefKeySrNo
        parameters["RefTypeId"] = RefTypeId
        parameters["Status"] = status
        parameters["StatusTimestamp"] = StatusTimestamp
        parameters["Description"] = Description
        parameters["FilePath"] = FilePath

        params_list = list(parameters.values())

        execute_stored_procedure(conn, DashBoard_Values, params=params_list, fetch=False)


