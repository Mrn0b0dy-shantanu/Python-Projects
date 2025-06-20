import subprocess
import time
import re
time_for_cooldown = int(input("only put number *second. Only whole numbers\n " + "cooldown time ----> "))
time_for_restart = int(input("Insert time to stop before restarting WIFI ----> ")) 
def turn_off_wifi():
    subprocess.call([
        'powershell',
        '-Command',
        ''f'netsh wlan disconnect'
    ])


def turn_on_wifi():
    subprocess.call([
        'powershell',
        '-Command',
        ''f'netsh wlan connect name=(netsh wlan show profiles | Select-String "All User Profile" | Select-Object -First 1).ToString().Split(":")[1].Trim()'
    ])


def ping_time(host="8.8.8.8"):
    try:
        output = subprocess.check_output(["ping", "-n", "1", host], stderr=subprocess.STDOUT, universal_newlines=True)
        # Extract the time from the ping output using regex
        match = re.search(r"time[=<]\s*(\d+)\s*ms", output)
        if match:
            return int(match.group(1))
        else:
            return None
    except subprocess.CalledProcessError:
            return None
def main():
    print("Monitoring....")
    while True:
        ping_time_taken = ping_time()
        if ping_time_taken is not None:
         print(f"Ping time: {ping_time_taken} ms")
         time.sleep(time_for_cooldown)
        else:
            turn_off_wifi()
            print("turning off")
            turn_on_wifi()
            print("on")
            time.sleep (time_for_restart)
         
      
            
if __name__ == "__main__":
    main()

