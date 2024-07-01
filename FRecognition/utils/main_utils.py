import base64
from FRecognition.exception import FRException
import os, sys
import pyodbc
from FRecognition.Entity.entity_model import CheckStatusWatchList, CheckLogIdFilePathStatus
from FRecognition.Entity.entity_model import NameandWatchListType, WatchListType, Cameralocation
from FRecognition.constant import q_checkRecordDelOrNot, q_getPicPAthFromFrLOG
from FRecognition.constant import q_getNameandWatchListType, q_getWatchListType, q_getCameralocation



def image_to_base64(image_path):
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            base64_encoded = base64.b64encode(image_data).decode('utf-8')
        return base64_encoded


def execute_stored_procedure(conn, procedure_name, params=None, fetch=False):
    try:
        cursor = conn.cursor()

        # Ensure params is a list or tuple
        if params:
            if isinstance(params, dict):
                params = list(params.values())
            query = f"EXEC {procedure_name} " + ', '.join(['?'] * len(params))
            cursor.execute(query, params)
        else:
            query = f"EXEC {procedure_name}"
            cursor.execute(query)

        # Fetch results if required
        if fetch:
            if cursor.description:
                data = cursor.fetchall()
            else:
                data = None
        else:
            data = None
            conn.commit()  # Commit changes if any
        

        return data

    except pyodbc.Error as e:
        print(f"Error executing stored procedure: {e}")
        return None

    finally:
        # Clean up resources
        cursor.close()




def check_record_del_or_not(conn, valid_id):

    obj = CheckStatusWatchList()

    query = q_checkRecordDelOrNot

    try:
        cursor = conn.cursor()
        cursor.execute(query, valid_id)
        row = cursor.fetchone()
        if row:
            obj.file_path = row[0]
            obj.status = row[1]
        else:
            print("No rows found.")

        cursor.close()
    
    except Exception as e:
        raise FRException(e, sys)
    
    return obj


def getPicPAthFromFrLOG(conn, LogId):

    file = CheckLogIdFilePathStatus()

    query = q_getPicPAthFromFrLOG

    try:
        cursor = conn.cursor()
        cursor.execute(query, LogId)
        row = cursor.fetchone()
        if row:
            file.file_path = row[0]
        else:
            print("No rows found.")

        cursor.close()
    
    except Exception as e:
        raise FRException(e, sys)
    
    return file


def GetNameandWatchListType(conn, faceId):

    watchListData = NameandWatchListType()

    query = q_getNameandWatchListType

    try:
        cursor = conn.cursor()
        cursor.execute(query, faceId)
        row = cursor.fetchone()
        if row:
            watchListData.type = row[0]
            watchListData.name = row[1]
        else:
            print("No rows found.")

        cursor.close()
    
    except Exception as e:
        raise FRException(e, sys)
    
    return watchListData


def GetWatchListType(conn, type):
    
    typeObj = WatchListType()

    query = q_getWatchListType

    try:
        cursor = conn.cursor()
        cursor.execute(query, type)
        row = cursor.fetchone()

        if row:
            typeObj.txtval = row[0]
        else:
            print("No rows found.")

        cursor.close()

    except Exception as e:
        raise FRException(e, sys)
    
    return typeObj


def GetCameralocation(conn,camId):
    camLocation = Cameralocation()
    
    query = q_getCameralocation

    try:
        cursor = conn.cursor()
        cursor.execute(query, type)
        row = cursor.fetchone()

        if row:
            camLocation.location = row[0]
        else:
            print("No rows found.")

        cursor.close()

    except Exception as e:
        raise FRException(e, sys)
    
    return camLocation