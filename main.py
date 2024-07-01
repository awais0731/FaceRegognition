from FRecognition.RabbitMQ.rabbitmq_keys import RabbitMQKeys
from FRecognition.utils.main_utils import execute_stored_procedure
from FRecognition.constant import DlimisRecord, conn
from FRecognition.singleton import Singleton


if __name__ == "__main__":


    dlims_distict_list = execute_stored_procedure(conn, DlimisRecord,fetch=True)
    singleton = Singleton()
    singleton.set_dlims_distict_list(dlims_distict_list) 

    input = input("Enter (q) to run fr matching from Que :")

    if input.lower() == 'q':
        RabbitMQKeys.StartListner()
        print("You are here")