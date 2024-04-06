##Utilize system commands to list all available network interfaces.
##Modify Environment Variables:
import subprocess
import os

def list_network_interfaces():
    if os.name == "nt":  
        command = "ipconfig"
    else:  
        command = "ifconfig"
        
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Network Interfaces:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error occurred while listing network interfaces:", e)

def modify_environment_variable(variable, value):
    os.environ[variable] = value

if __name__ == "__main__":
    list_network_interfaces()
    
    
    modify_environment_variable("MY_VARIABLE", "my_value")
    print("Environment variable MY_VARIABLE modified.")
