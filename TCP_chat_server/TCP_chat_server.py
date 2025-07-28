import socket
import threading

Host = input("IP:")                     #Select the ip address you are hosting on. If you want to use your local network use 127.0.0.1
Port = int(input("PORT:"))              #Select the port you want to use.

nicknames = []                          #Dictionary for all the nicknames set by the users.
users = []                              #Dictionary for all the users socket.


# This send the message 
def messages_sender(message,Csocket):
# It broadcasts the message to everyone except the person who sent it.
    for user in users:
        if user != Csocket:
            user.send(message) 
            

def disconnection_messages_sender(disconnection_message):
# It will send everyone the disconnection message. If a user disconnects
    for user in users: 
        user.send(disconnection_message)
          
                    
                     
def handling_users(Csocket):
      
      while True:
            try:

                raw_message = Csocket.recv(1024)                                #Receives the message.
                index = users.index(Csocket)                                    #Selects the current user from the dictionary.
                nickname_of_current_user = nicknames[index]                     #Selects the nickname from the dictionary
                message = nickname_of_current_user + b":"+ raw_message          #We send everything in bytes as it will be decoded on the user side.   
                messages_sender(message,Csocket)                                #Tells the function to send the message.

            except:

                index2 = users.index(Csocket)
                disconnected_user = nicknames[index2]                           #Selects the disconnected user from the dictionary.
                print(disconnected_user + b" has disconnected.")
                Csocket.close()                                                 #Closes the Connection.
                users.pop(index2)                                               #Removes it from the dictionary.
                disconnection_message = disconnected_user + b" has disconnected..."
                disconnection_messages_sender(disconnection_message)            #Tells the function to send this message.
                nicknames.pop(index2)
                break
       

      
            
def socket_receiver(Host, Port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.bind((Host, Port))                                                    #Uses the Port and Host to set up the listener
        s.listen()
        print("--------------------SERVER STARTED-----------------------")

        while True:

            Csocket, Caddr = s.accept()                                         #Accepts incoming connections
            nickname = Csocket.recv(1024)
            encoded_nickname = nickname.decode("utf-8")                         #The user.py sends the nickname first so it accepts the first message and saved it as the nickname.
            users.append(Csocket)                                               #Writes the name in the dictionary.
            nicknames.append(nickname)
            print(f"Connected to {Caddr}")
            message = nickname + b" has joined the server!"
            messages_sender(message,Csocket)                                    #Tells the function to send join message to everyone.
            print("Username is " + encoded_nickname)
            threading.Thread(target = handling_users, args = (Csocket,)).start()# This runs the handling_users function on the background. Without it the code wont work.
    
socket_receiver(Host, Port)

    
    
   



