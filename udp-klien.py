from socket import *
from random import randint
import time, json, sys

def dummyData():
    return randint(1, 100)

serverName = "192.168.10.1"
serverPort = 8989
MAX = 65535
counter = 1
clientSocket = socket(AF_INET, SOCK_DGRAM)

try:
    while 1:
        timestamp = time.strftime("%d/%m/%y-%H:%M:%S")
        message = {'id': counter, 'temp': dummyData(), 'hum': dummyData(), 'smoke': dummyData(), 'carbon': dummyData(), 'timestamp': timestamp}
        data = json.dumps(message)
        print data
        clientSocket.sendto(data ,(serverName, serverPort))
        ackMessage, serverAddress = clientSocket.recvfrom(MAX)
        print ackMessage + "\n"
        counter = counter + 1
        time.sleep(3)

except KeyboardInterrupt:
    clientSocket.close()
    print('\n\nOPERATION HAS BEEN CANCELED!\n')
    sys.exit()
