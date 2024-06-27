import base64
from FRecognition.exception import FRException
import os, sys
import pyodbc


def image_to_base64(image_path):
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            base64_encoded = base64.b64encode(image_data).decode('utf-8')
        return base64_encoded


def execute_stored_procedure(conn, procedure_name, *params):
    try:
         
        cursor = conn.cursor()
        cursor.execute("EXEC " + procedure_name + " " + ",".join(["?"] * len(params)), params)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except Exception as e:
         raise FRException(e, sys)
    
def execute_stored_procedure1(conn,procedure_name, params=None):
     try:
        cursor = conn.cursor()
        if params:
            if isinstance(params, dict):
                params = list(params.values())
            cursor.execute(f"EXEC {procedure_name} " + ', '.join(['?'] * len(params)), params)
        else:
            cursor.execute(f"EXEC {procedure_name}")
        
        if cursor.description:
            data = cursor.fetchall()  # Adjust fetch method based on your need
        else:
            data = None

        conn.commit()
        return data

     except pyodbc.Error as e:
          raise FRException(e, sys)
     
     finally:
        cursor.close()
        conn.close()
     
    
