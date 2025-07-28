import socket
import threading
import sys

Host = input("IP:")                     #Put the ip you put in the sever.py
Port = int(input("PORT:"))              #Put the port you put in the server.py

#Same decoder as in sever.py
def message_decoder(s):
        
        while True: 
            messages = s.recv(1024)
            decoded_msg =  messages.decode("utf-8") #All data on the sever side must be in bytes.
            print(decoded_msg)
    
def socket_connector(Host, Port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:          
            s.connect((Host, Port))
        except:
             print(f"Connection was not successful. Please try again")
             sys.exit(1)         

        print(f"Connected to {Host}")
        nickname = input("Enter your username: ")
        s.send(nickname.encode("utf-8"))
#This thread keep the message decoder running for incoming messages. Without it the code wont work.
        threading.Thread(target=message_decoder, args = (s,)).start()

        while True:
                #This loop accepts messages from user.
                input_message = input(f"{nickname}:")
                s.send(input_message.encode("utf-8"))
                
        
socket_connector(Host, Port)


