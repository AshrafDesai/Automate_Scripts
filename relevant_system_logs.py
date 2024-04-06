##Create a script to gather and save relevant system logs.

import subprocess
import os
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def save_logs_to_file(logs, file_path):
    with open(file_path, 'a') as file:  
        for log in logs:
            file.write(f"===== {log.upper()} LOGS =====\n")
            try:
                output = subprocess.check_output(log, shell=True, text=True)
                file.write(output)
            except subprocess.CalledProcessError as e:
                file.write(f"Error occurred while collecting logs: {e}\n")
            file.write("\n\n")

def gather_system_logs():
    logs_to_collect = [
        "systeminfo",            
        "ipconfig /all",        
        "netsh wlan show profile",  
        "netsh advfirewall show allprofiles",  
    ]
    event_logs_to_collect = [
        "wevtutil qe System /c:5 /rd:true /f:text",  
        "wevtutil qe Application /c:5 /rd:true /f:text",  
        "wevtutil qe Security /c:5 /rd:true /f:text",     
        "wevtutil qe Setup /c:5 /rd:true /f:text",        
    ]
    file_path = "system_logs.txt"

    try:
        save_logs_to_file(logs_to_collect, file_path)
        
        if is_admin():
            save_logs_to_file(event_logs_to_collect, file_path)
            print(f"System logs saved to '{file_path}'.")
        else:
            print("Error: Insufficient privileges to access event logs.")
            print(f"System logs (excluding event logs) saved to '{file_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    gather_system_logs()
