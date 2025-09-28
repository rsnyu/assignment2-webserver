# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket 
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen()
  #Fill in end


  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024)#Fill in start -a client is sending you a message   #Fill in end 
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], 'rb')     #fill in start              #fill in end   )
      body = f.read()
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
              
      #Content-Type is an example on how to send a header as bytes. There are more!
      headers = (
          b"HTTP/1.1 200 OK\r\n"
          b"Content-Type: text/html; charset=UTF-8\r\n"
          b"Server: RsCloudServer/1.0\r\n"
          b"Connection: close\r\n"
          + f"Content-Length: {len(body)}\r\n".encode('ascii')
          + b"\r\n"
      )

      connectionSocket.sendall(headers + body)


      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
 
      #Fill in end
               
      #for line in file
      #Fill in start - append your html file contents #Fill in end 
      
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start

      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      body = b"<!doctype html><html><body><h1>404 Not Found</h1></body></html>"
      headers = (
          b"HTTP/1.1 404 Not Found\r\n"
          b"Content-Type: text/html; charset=UTF-8\r\n"
          b"Server: RsCloudServer/1.0\r\n"
          b"Connection: close\r\n"
          + f"Content-Length: {len(body)}\r\n".encode('ascii')
          + b"\r\n"
      )

      connectionSocket.sendall(headers + body)
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)