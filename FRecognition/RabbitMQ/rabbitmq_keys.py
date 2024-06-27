from FRecognition.constant import RabbitMQ_username, RabbitMQ_Password, RabbitMQ_HostName, RabbitMQ_QueueName
import pika
from FRecognition.RabbitMQ.message_receiver import MessageReceiver
from FRecognition.exception import FRException
import sys, os


class RabbitMQKeys:

    def StartListner():


        try:
            credentials = pika.PlainCredentials(RabbitMQ_username, RabbitMQ_Password)
            parameters = pika.ConnectionParameters(host=RabbitMQ_HostName, credentials=credentials)
            connection = pika.BlockingConnection(parameters)

            # If no exception is raised, the connection was successful

            print("Connection to RabbitMQ successful.")
            channel = connection.channel()

            channel.basic_qos(0,1,False)

            message_receiver = MessageReceiver(channel)

            channel.basic_consume(queue=RabbitMQ_QueueName, on_message_callback=message_receiver.handle_basic_deliver, auto_ack=False)

            print('Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()
            
        except Exception as e:
            raise FRException(e, sys)
        


