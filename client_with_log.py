"""
Carlos Bustos
1001317137
Project 1
"""

from socket import *
import sys
import struct

# import urllib.request

# making a client
clientSocket = socket(AF_INET, SOCK_STREAM)

new_path1 = 'agent001.txt'
log001 = open(new_path1, 'w')

new_path2 = 'agent100.txt'
log100 = open(new_path2, 'w')

new_path3 = 'agent111.txt'
log111 = open(new_path3, 'w')


if (len(sys.argv) == 3):
    hostName = sys.argv[1]
    port = int(sys.argv[2])
    #file = sys.argv[3]
else:
    hostName = sys.argv[1]
    port = 8080
    #file = sys.argv[2]

try:
    # Connect the client socket to the host.
    clientSocket.connect((hostName, port))
    print('\nConnecting...\n')
    log.write('\nConnecting...\n')
except:
    print("\nHost name invalid.\n")
    log.write("\nHost name invalid.\n")
    sys.exit(1)

print("Socket Information:")
log.write("Socket Information:")
print(clientSocket)
log.write(clientSocket)

"""
url = 'http://'+hostName+'/'+file
with urllib.request.urlopen(url) as response:
    html = response.read()
"""
# Prompt the user to enter the path of the file/page.
filePath = input("Please specify the file path:")

# Create a HTTP GET request to retrieve the file.
request = "GET " + filePath + " HTTP 1.1\n\n"

# Send to server
clientSocket.send(str.encode(request))

result = clientSocket.recv(4096)

if (len(result) == 0):
    print("\nNothing was received from the server.\n\n")
    log.write("\nNothing was received from the server.\n\n")

# This loop will recieve all the data from the server and display it.
while (len(result) > 0):

    try:
        result.decode()
        print(result)
        log.write(result)
        result = clientSocket.recv(4096)

    except UnicodeDecodeError:
        print("Error in decoding file to Unicode.")
        log.write("Error in decoding file to Unicode.")
        break

clientSocket.close()  # Close the socket and inform the user.

print("\nConnection is now closed.\n\n")
log.write("\nConnection is now closed.\n\n")
log.close()
