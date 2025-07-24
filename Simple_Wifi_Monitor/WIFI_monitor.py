import socket
import subprocess
from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11Elt, Dot11, RadioTap
from tabulate import tabulate
import os
# If you want to understand it more easily. Start looking from the main() and follow what it does.

#This will list all the interfaces available on the device.
def list_interfaces():

    interfaces = [i[1] for i in socket.if_nameindex()] # This makes a tuple where all the interface names are put.
    return interfaces
#We return the interfaces so that we can use it again

#This will Let the user select the desired interface.
def selecting_interface(interfaces): #Its using the interface acquired by the first function.
        
    for index, name in enumerate(interfaces, 1): #Prints the interfaces with the number and name.
        print(index, name)

    user_input = int(input("Select your interface: ")) 
    print('Using Interface: ' + str(interfaces[user_input -1])) #Since its a tuple we have to -1 to get the correct selection.

    return interfaces [user_input -1]
    
def turning_monitor_mode_on(interface):
        
        #Turns it off
        os.system(f"sudo ifconfig {interface} down")
        print(f"\033[92m[+]\033[0m Turning off {interface}... ")
        #Tries to turn on monitor mode.
        #Here it is important to use subprocess.run since we want to capture the output and look for errors
        output2 = subprocess.run(
            ["sudo","iwconfig", interface ,"mode" ,"monitor"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text = True
        )
        
        #Dont get scared of \033[92m[+]\033[ this part its just me adding colors. Completely Optional. But it looks Great!
        print(f"\033[92m[+]\033[0m Turning on Monitor mode...")
        #Just like before we store the output to check if any error occurred
        checking2 = output2.stdout + output2.stderr
        #This looks if checking2 has anything inside it.
        if checking2:
            #Turns it on
            os.system(f"sudo ifconfig {interface} up")
            return False #This is used later in main()
        else:

            os.system(f"sudo ifconfig {interface} up")
            print(f"\033[92m[+]\033[0m Turning on {interface}...")

            return True #This is used later in main()  

#This function sets network information.
def wifi_info(packet):

    if packet.haslayer(Dot11Beacon):

        SSID = packet[Dot11Elt].info.decode()                   #|
        BSSID = packet[Dot11].addr3                             #|
        STATS = packet[Dot11Beacon].network_stats()             #|
        CHANNEL = STATS.get("channel")                          #| Stores all the values to its respective variables.
        CRYPTO = STATS.get("crypto")                            #|
        signal_strength = packet.dBm_AntSignal                  #|
        freq = packet[RadioTap].ChannelFrequency                #|
        data_rate = packet[RadioTap].Rate                       #|

        if BSSID not in networks:
            networks[BSSID] = (SSID, CHANNEL, CRYPTO, signal_strength, freq, data_rate)

#This will sniff out all the information of the networks available.
def sniff_networks(interface):
    try:
        global networks
        networks = {} 

        print(f"\033[92m[+]\033[0m Scanning for WiFi networks using {interface}...\n")
        print(f"\033[92m[+]\033[0m Press Ctrl+C to stop scanning...\n")
        sniff(prn=wifi_info, iface=interface, timeout=10, store=0)
        # This part makes the chart.
        headers = ["SSID", "BSSID", "Channel", "CRYPTO", "Signal Strength (dBm)", "Frequency (MHz)", "Data Rate (Mbps)"]
        table = []
        for BSSID, (SSID, CHANNEL, CRYPTO, signal_strength, freq, data_rate) in networks.items():
            table.append([
            SSID, BSSID, CHANNEL,
            ', '.join(CRYPTO) if isinstance(CRYPTO, list) else str(CRYPTO),
            signal_strength, freq, data_rate
            ])
        print(tabulate(table, headers=headers, tablefmt="fancy_grid")) # Prints the table
        #It turns off the monitor mode in the end
        print(f"\033[92m[+]\033[0m Turning off Monitor mode...")
        os.system(f"sudo ifconfig {interface} down")
        os.system(f"sudo iwconfig {interface} mode managed")
        os.system(f"sudo ifconfig {interface} up")
        print(f"\033[92m[+]\033[0m Exiting...")
    #It turns off the monitor mode in the end even if the process is stopped using ctrl+c
    except KeyboardInterrupt:
        print(f"\033[92m[+]\033[0m Turning off Monitor mode...")
        os.system(f"sudo ifconfig {interface} down")
        os.system(f"sudo iwconfig {interface} mode managed")
        os.system(f"sudo ifconfig {interface} up")

#All the functions are called out in order
def all_interface_work():
    #If the interface doesn't support monitor mode. Which means "turning_monitor_mode_on(selected_interface)" will return False. It will keep looping till it has the right interface.
    while True:

        interfaces = list_interfaces()                              #|
        selected_interface = selecting_interface(interfaces)        #|This is the main skeleton of the entire script. It runs functions stores the return values and passes it to other functions.
        TRUEorFALSE = turning_monitor_mode_on(selected_interface)   #|
        #If its True then the loop will break and run the last function in the main().
        if TRUEorFALSE:
             break
        else:
            print(f"\033[91m[-]\033[0m Failed. Your interface probably doesn't support Monitor mode. Please choose another interface or try again.")

    return selected_interface    
    #It returns the interface name that is selected which is used in sniff_networks() as parameter.

def main():

    selected_interface = all_interface_work()
    sniff_networks(selected_interface)       

if __name__ == "__main__":
    main()
       



   