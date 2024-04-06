##Create a script to check the availability of an internet connection.
##Monitor Disk Space:

import urllib.request
import shutil
import psutil

def check_internet_connection():
    try:
        urllib.request.urlopen('http://google.com', timeout=1)
        print("Internet connection is available.")
    except:
        print("Internet connection is not available.")

def monitor_disk_space():
    total, used, free = shutil.disk_usage("/")
    print("Total disk space:", total / (2**30), "GB")
    print("Used disk space:", used / (2**30), "GB")
    print("Free disk space:", free / (2**30), "GB")

if __name__ == "__main__":
    check_internet_connection()
    monitor_disk_space()
