"""
Carlos Bustos
1001317137
Project 1
"""

from socket import * #Import socket module to use sockets.
from _thread import * #Import _thread module to use multithreading functions
import time
import tcp_packet

#Making a socket using the socket constructor
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a HTTP server socket
serverSocket.bind(('', 80))
serverSocket.listen(10)

print("Waiting for connection...")

#function handles a request from the server socket.
def thread(socket):
    counter  = 1
    new_path1 = 'agent001.txt'
    log001 = open(new_path1, 'w')

    new_path2 = 'agent100.txt'
    log100 = open(new_path2, 'w')

    new_path3 = 'agent111.txt'
    log111 = open(new_path3, 'w')

    while True:
        #Getting a connection
        #receive host and ip address
        print("\nConnection Socket information:")
        log001.write("\nConnection Socket information:")
        log100.write("\nConnection Socket information:")
        log111.write("\nConnection Socket information:")
        connectionSocket, addr = serverSocket.accept()
        log001.write(str(connectionSocket))
        log100.write(str(connectionSocket))
        log111.write(str(connectionSocket))
        log001.write("\n\n")
        log100.write("\n\n")
        log111.write("\n\n")
        print(connectionSocket)
        try:
            #Receive a HTTP get request from a client/host.
            message = connectionSocket.recv(4096)
            print(type(message))
            #getting the message from the client and decoding it
            print("\nMessage from client:")
            log001.write("\nMessage from client:")
            log100.write("\nMessage from client:")
            log111.write("\nMessage from client:")
            print(message.decode('utf-8'))
            log001.write(message.decode('utf-8'))
            log100.write(message.decode('utf-8'))
            log111.write(message.decode('utf-8'))
            log001.write("\n\n")
            log100.write("\n\n")
            log111.write("\n\n")
            #Parse get request to receive filename
            start = time.time()

            filename = message.split()[1] 
            f = open(filename[1:])
            outputdata = f.readlines()
            #Make all the lines in the file to a list so that we can send the information to the client.
            #Send one HTTP header line into socket.
            message = 'HTTP/1.1 200 OK\n\n'
            end = time.time()
            interval = end - start
            if(interval > 1 or counter % 4 == 0):
                print("retransmit")
            counter = counter + 1
            connectionSocket.send(str.encode(message))
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                #The data is encoded to bytes so that the client can interpret it.
                connectionSocket.send(str.encode(outputdata[i])) 
            connectionSocket.close() 
            #Close the socket once the data is sent. This is a non-persisten connection.
            print("Connection Closed")
            log001.write("Connection Closed")
            log100.write("Connection Closed")
            log111.write("Connection Closed")
        except (IOError, IndexError): 
             #Send response message for file not found or there is an index error.
             message = 'HTTP/1.1 404 Not Found\n\n'
             connectionSocket.send(str.encode(message))
             log001.write(message)
             log100.write(message)
             log111.write(message)             #Close client socket
             connectionSocket.close()
             print("\nConnection Closed\n\n")
             log001.write("Connection Closed")
             log100.write("Connection Closed")
             log111.write("Connection Closed")
    serverSocket.close() #Close serversocket
    print("\nServer Socket Closed\n\n")
    log001.write("\nServer Socket Closed\n\n")
    log100.write("\nServer Socket Closed\n\n")
    log111.write("\nServer Socket Closed\n\n")
    log001.close()
    log100.close()
    log111.close()
#Start a thread
start_new_thread(thread,(serverSocket,))
