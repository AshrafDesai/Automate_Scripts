
##python script to Determine if the system is running in a virtualized environment.


import platform

def is_virtualized():
    system_info = platform.uname()

    
    if "Microsoft" in system_info.release:  
        return True
    elif "hyperv" in system_info.machine.lower() or "virtual" in system_info.machine.lower():
        return True
    elif "VMware" in system_info.release or "VMware" in system_info.version:
        return True
    elif "VirtualBox" in system_info.release or "VirtualBox" in system_info.version:
        return True
    elif "Xen" in system_info.release or "Xen" in system_info.version:
        return True
    elif "KVM" in system_info.release or "KVM" in system_info.version:
        return True
    elif "Parallels" in system_info.release or "Parallels" in system_info.version:
        return True
    elif "docker" in system_info.release.lower() or "docker" in system_info.version.lower():
        return True
    elif "container" in system_info.machine.lower():
        return True
    else:
        return False

if __name__ == "__main__":
    if is_virtualized():
        print("The system is running in a virtualized environment.")
    else:
        print("The system is running on a physical machine.")
