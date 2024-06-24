from FRecognition.RabbitMQ.rabbitmq_keys import RabbitMQKeys

if __name__ == "__main__":


    input = input("Enter (q) to run fr matching from Que :")

    if input.lower() == 'q':
        RabbitMQKeys.StartListner()
        print("You are here")
    