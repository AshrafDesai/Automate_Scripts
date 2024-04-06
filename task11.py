import os
import subprocess

class SystemInfo:
    
    def check_temperature(self):
        try:
            
            ohm_path = "D:\\ZeroThreat\\openhardwaremonitor-v0.9.6\\OpenHardwareMonitor\\OpenHardwareMonitor.exe"
            
            
            if not os.path.exists(ohm_path):
                print("OpenHardwareMonitor executable not found.")
                return None
            
            
            output = subprocess.check_output([ohm_path, "-c", "sensors"])
            
            
            temperature_lines = [line for line in output.split('\n') if "Temperature" in line]
            if temperature_lines:
                temperature = temperature_lines[0].split(':')[1].strip()
                cpu_temp_info = {
                    "Temperature": temperature
                }
                return cpu_temp_info
            else:
                print("No CPU temperature information found.")
                return None
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return "CPU temperature information not available."


sys_info = SystemInfo()


cpu_temperature = sys_info.check_temperature()


print("CPU Temperature Information:")
if cpu_temperature:
    print(cpu_temperature)
else:
    print("CPU temperature information not available.")
