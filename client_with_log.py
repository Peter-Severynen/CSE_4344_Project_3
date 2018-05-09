from socket import *
import sys
import struct

# import urllib.request

# making a client
clientSocket = socket(AF_INET, SOCK_STREAM)

new_path1 = 'agent001.txt'
log001 = open(new_path1, 'a')
new_path2 = 'agent100.txt'
log100 = open(new_path2, 'a')
new_path3 = 'agent111.txt'
log111 = open(new_path3, 'a')
log001.write("Client Message Incomning")
log100.write("Client Message Incomning")
log111.write("Client Message Incomning")


if (len(sys.argv) == 4):
    hostName = sys.argv[1]
    port = int(sys.argv[2])
    file = sys.argv[3]
else:
    hostName = sys.argv[1]
    port = 8080
    file = sys.argv[2]

try:
    # Connect the client socket to the host.
    clientSocket.connect((hostName, port))
    print('\nConnecting...\n')
except:
    print("\nHost name invalid.\n")
    sys.exit(1)

print("Socket Information:")
log001.write("Socket Information:")
log100.write("Socket Information:")
log111.write("Socket Information:")
print(clientSocket)
log001.write(str(clientSocket))
log100.write(str(clientSocket))
log111.write(str(clientSocket))

# Prompt the user to enter the path of the file/page.
#filePath = input("Please specify the file path:")

# Create a HTTP GET request to retrieve the file.
request = "GET " + file + " HTTP 1.1\n\n"

# Send to server
clientSocket.send(str.encode(request))

result = clientSocket.recv(4096)

if (len(result) == 0):
    print("\nNothing was received from the server.\n\n")

# This loop will recieve all the data from the server and display it.
while (len(result) > 0):

    try:
        result.decode()
        print(result)
        log001.write(result)
        log100.write(result)
        log111.write(result)

        result = clientSocket.recv(4096)

    except UnicodeDecodeError:
        print("Error in decoding file to Unicode.")
        break

clientSocket.close()  # Close the socket and inform the user.

print("\nConnection is now closed.\n\n")
log001.close()
log100.close()
log111.close()
