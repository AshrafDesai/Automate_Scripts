##Write a script to automate the backup of critical files or directories.

import shutil
import os
import datetime

def backup_files(source_paths, destination_path):
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = os.path.join(destination_path, f"Backup_Test_{timestamp}")

    
    os.makedirs(backup_dir)

    
    all_contents_dir = os.path.join(backup_dir, "All_Contents")
    os.makedirs(all_contents_dir)

    
    for source_path in source_paths:
        if os.path.exists(source_path):
            if os.path.isfile(source_path):
                shutil.copy(source_path, all_contents_dir)
                print(f"File '{source_path}' backed up to '{all_contents_dir}'.")
            elif os.path.isdir(source_path):
                
                for root, dirs, files in os.walk(source_path):
                    for file in files:
                        src_file = os.path.join(root, file)
                        shutil.copy(src_file, all_contents_dir)
                        print(f"File '{src_file}' backed up to '{all_contents_dir}'.")
                    for directory in dirs:
                        src_dir = os.path.join(root, directory)
                        shutil.copytree(src_dir, os.path.join(all_contents_dir, os.path.relpath(src_dir, source_path)))
                        print(f"Directory '{src_dir}' backed up to '{all_contents_dir}'.")
            else:
                print(f"Skipping '{source_path}' as it is neither a file nor a directory.")
        else:
            print(f"Source path '{source_path}' does not exist.")

if __name__ == "__main__":
    
    source_paths = [
        
        "D:\\Camera"
    ]

    
    destination_path = "C:\\Backup_Test"

    backup_files(source_paths, destination_path)
