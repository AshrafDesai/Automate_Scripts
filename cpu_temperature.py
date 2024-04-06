##Use available tools or commands to monitor the CPU temperature

import subprocess
import datetime

def check_cpu_temperature():
    try:
        # Execute PowerShell command to get CPU temperature
        output = subprocess.check_output(['powershell', '-Command', 'Get-CimInstance -Namespace root/OpenHardwareMonitor -ClassName Sensor | Where-Object {$_.SensorType -eq "Temperature"} | Select-Object -ExpandProperty Value'], universal_newlines=True)
        return output.strip()  # Return CPU temperature
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"

def log_cpu_temperature():
    # Get CPU temperature information
    cpu_temperature = check_cpu_temperature()

    # Get current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write temperature information to a text file
    with open("cpu_temperature_log.txt", "a") as file:
        file.write(f"{current_datetime} - CPU temperature: {cpu_temperature} °C\n")

    # Display CPU temperature information
    print("CPU Temperature Information:")
    print(f"CPU temperature: {cpu_temperature} °C")

# Log CPU temperature and display information
log_cpu_temperature()
