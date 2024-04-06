##Create a script to list all installed software on the system.
import os
from datetime import datetime

def get_installed_software(drive):
    software_list = []

    def get_executables(directory):
        executables = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith((".exe", ".msi", ".bat", ".com")):
                    file_path = os.path.join(root, file)
                    executables.append(file_path)
        return executables


    executables = get_executables(drive)


    for exe_file in executables:
        install_date = datetime.fromtimestamp(os.path.getmtime(exe_file)).strftime('%d-%m-%Y')
        software_info = {
            "Name": os.path.basename(exe_file),
            "InstallDate": install_date,
            "InstallLocation": os.path.dirname(exe_file),
            "Publisher": "",
            "DisplayVersion": "",
            "EstimatedSize": os.path.getsize(exe_file) // (1024 * 1024)  # Convert bytes to MB
        }
        software_list.append(software_info)

    return software_list

drives = ["C:\\","D:\\", "E:\\", "F:\\"]


for drive in drives:
    print(f"Installed software on {drive}")
    installed_software = get_installed_software(drive)
    for software in installed_software:
        print(f"Name: {software['Name']}")
        print(f"InstallDate: {software['InstallDate']}")
        print(f"InstallLocation: {software['InstallLocation']}")
        print(f"Publisher: {software['Publisher']}")
        print(f"DisplayVersion: {software['DisplayVersion']}")
        print(f"EstimatedSize: {software['EstimatedSize']} MB")
        print("-" * 50)

    txt_filename = f"installed_software_{drive.strip(':').replace('/', '_')}.txt" 
    with open("list_software.txt", 'a') as txt_file:  
        for software in installed_software:
            txt_file.write(f"Name: {software['Name']}\n")
            txt_file.write(f"InstallDate: {software['InstallDate']}\n")
            txt_file.write(f"InstallLocation: {software['InstallLocation']}\n")
            txt_file.write(f"Publisher: {software['Publisher']}\n")
            txt_file.write(f"DisplayVersion: {software['DisplayVersion']}\n")
            txt_file.write(f"EstimatedSize: {software['EstimatedSize']} MB\n")
            txt_file.write("-" * 50 + "\n")

    print(f"Record saved to {txt_filename}")
