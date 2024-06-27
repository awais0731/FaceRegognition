import base64
from FRecognition.exception import FRException
import os, sys


def image_to_base64(image_path):
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            base64_encoded = base64.b64encode(image_data).decode('utf-8')
        return base64_encoded


def execute_stored_procedure_to_get_DBInfo(conn, procedure_name, *params):
    try:
         
        cursor = conn.cursor()
        cursor.execute("EXEC " + procedure_name + " " + ",".join(["?"] * len(params)), params)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except Exception as e:
         raise FRException(e, sys)

def execute_stored_procedure_to_get_DlimisDistricit(conn, procedure_name, *params):
    try:     
        cursor = conn.cursor()
        cursor.execute("EXEC " + procedure_name + " " + ",".join(["?"] * len(params)), params)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except Exception as e:
         raise FRException(e, sys)
         