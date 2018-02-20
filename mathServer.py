# Author: Abdulsalam taofeek akintunde
from socket import *

serverPort = 22595




serverSocket = socket(AF_INET, SOCK_DGRAM)


serverSocket.bind(('', serverPort))
print("The server is ready to recieve")


ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
MODULUS = 5

def calculator(message): 
    """
    takes in a message string that contains an operation as the first number
    and two operands as the second and the third
    and returns the result of the operation on them
    """
    
    message = message.split(' ')
    operator =  int(message[0]) 
    operand1 = int(message[1])
    operand2 = int(message[2])
    
    
   
    if(operator == ADDITION):
        return operand1 + operand2
    elif(operator == SUBTRACTION):
        return operand1 - operand2
    elif(operator == MULTIPLICATION):
        return operand1 * operand2
    elif(operator == DIVISION ):
        return operand1 / operand2
    elif(operator == MODULUS):
        return operand1 % operand2
    else:
        return ' error: no valid operation'

while True:
    message, clientAddress = serverSocket.recvfrom(4096)
    resultMessage = str(calculator(message))
    serverSocket.sendto(resultMessage, clientAddress)

