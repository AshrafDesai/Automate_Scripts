##Develop a script to monitor and alert if disk space falls below a certain threshold.
##Retrieve System Architecture:

import shutil
import time
import platform

def get_system_architecture():
    return platform.architecture()[0]

def check_disk_space(threshold_gb):
    while True:
        total, used, free = shutil.disk_usage("/")
        free_gb = free // (2**30) 
        print(f"System Architecture: {get_system_architecture()}")
        print(f"Free disk space: {free_gb} GB")
        
        if free_gb < threshold_gb:
            print("\033[91mDisk space is running low!\033[0m")  
        else:
            print("Disk space is sufficient.")
        
        time.sleep(60) 

if __name__ == "__main__":
    threshold_gb = 5  
    check_disk_space(threshold_gb)
