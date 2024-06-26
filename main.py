from FRecognition.RabbitMQ.rabbitmq_keys import RabbitMQKeys
import pyodbc
from FRecognition.utils.main_utils import execute_stored_procedure


if __name__ == "__main__":

    input = input("Enter (q) to run fr matching from Que :")

    if input.lower() == 'q':
        RabbitMQKeys.StartListner()
        print("You are here")
    