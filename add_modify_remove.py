##Write a script to add, modify, or remove environment variables.
##Check for Software Updates

import os
import subprocess

def add_or_modify_environment_variable(variable, value):
    os.environ[variable] = value
    print(f"Environment variable '{variable}' set to '{value}'.")

def remove_environment_variable(variable):
    if variable in os.environ:
        del os.environ[variable]
        print(f"Environment variable '{variable}' removed.")
    else:
        print(f"Environment variable '{variable}' does not exist.")

def check_for_updates():
    try:
        result = subprocess.run(["pip", "list", "--outdated"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Updates available for the following packages:")
            print(result.stdout)
        else:
            print("Failed to check for updates.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while checking for updates: {e}")

def check_for_updates():
    try:
        result = subprocess.run(["pip", "list", "--outdated"], capture_output=True, text=True, check=True)
        outdated_packages = result.stdout.split("\n")[2:-1]  
        if outdated_packages:
            print("Updates available for the following packages:")
            print("\n".join(outdated_packages))
            upgrade_packages = input("Do you want to upgrade these packages? (yes/no): ").strip().lower()
            if upgrade_packages == "yes":
                subprocess.run(["pip", "install", "--upgrade"] + outdated_packages, capture_output=True, text=True, check=True)
                print("Packages successfully upgraded.")
            else:
                print("No packages were upgraded.")
        else:
            print("No updates available for installed packages.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while checking for updates: {e}")

if __name__ == "__main__":
    # Example usage
    add_or_modify_environment_variable("MY_VARIABLE", "my_value")
    remove_environment_variable("MY_VARIABLE")
    
    check_for_updates()
