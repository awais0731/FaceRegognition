import base64


def image_to_base64(image_path):
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            base64_encoded = base64.b64encode(image_data).decode('utf-8')
        return base64_encoded


def execute_stored_procedure(conn, procedure_name, *params):
    cursor = conn.cursor()
    cursor.execute("EXEC " + procedure_name + " " + ",".join(["?"] * len(params)), params)
    rows = cursor.fetchall()
    cursor.close()
    return rows