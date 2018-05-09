from socket import * #Import socket module to use sockets.
from _thread import * #Import _thread module to use multithreading functions
import time
new_path = 'agent001.txt'
new_path1 = 'agent100.txt'
new_path2 = 'agent111.txt'

#Making a socket using the socket constructor
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a HTTP server socket
serverSocket.bind(('', 80))
serverSocket.listen(10)
print("Waiting for connection...")

#function handles a request from the server socket.
def thread(socket):
    count = 1
    while True:
        log001 = open(new_path, 'a')
        log100 = open(new_path1, 'a')
        log111 = open(new_path2, 'a')
        #Getting a connection
        #receive host and ip address
        connectionSocket, addr = serverSocket.accept()
        
        print("\nConnection Socket information:")
        print(connectionSocket)
        print("\n\n")
        #log001.write(connectionSocket)
        
        try:
            #Begining the timer
            start = time.time()
            #Receive a HTTP get request from a client/host.
            message = connectionSocket.recv(4096)
            end = time.time()
            interval = end - start
            if(interval > 1 or count % 5 == 0):
                 message = connectionSocket.recv(4096)
            count = count + 1
            #getting the message from the client and decoding it and saving it in a log
            print("\nMessage from client:")
            print(message.decode('utf-8'))
            log001.write("\nMessage from client:\n")
            log001.write(message.decode('utf-8'))
            log100.write("\nMessage from client:\n")
            log100.write(message.decode('utf-8'))
            log111.write("\nMessage from client:\n")
            log111.write(message.decode('utf-8'))
            print("\n\n")
            #Parse get request to receive filename
            filename = message.split()[1] 
            f = open(filename[1:])
            outputdata = f.readlines()
            #Make all the lines in the file to a list so that we can send the information to the client.
            #Send one HTTP header line into socket.
            message = 'HTTP/1.1 200 OK\n\n'
            connectionSocket.send(str.encode(message))
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                #The data is encoded to bytes so that the client can interpret it.
                connectionSocket.send(str.encode(outputdata[i])) 
            connectionSocket.close() 
            #Close the socket once the data is sent. This is a non-persisten connection.
            print("Connection Closed")
        except (IOError, IndexError): 
             #Send response message for file not found or there is an index error.
             message = 'HTTP/1.1 404 Not Found\n\n'
             connectionSocket.send(str.encode(message))
             #Close client socket
             connectionSocket.close()
             print("\nConnection Closed\n\n")
    serverSocket.close() #Close serversocket
    print("\nServer Socket Closed\n\n")
    log001.close()
    log100.close()
    log111.close()
#Start a thread
start_new_thread(thread,(serverSocket,))
