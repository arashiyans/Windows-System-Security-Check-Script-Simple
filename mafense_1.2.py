import subprocess
import psutil
import os
import ctypes
import logging
import hashlib

# Setup logging
logging.basicConfig(filename='system_security_check.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def check_windows_defender():
    try:
        # Check Windows Defender status
        cmd = "powershell -Command \"Get-MpComputerStatus | Select-Object -Property AntivirusEnabled, RealTimeProtectionEnabled\""
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        output = result.stdout.strip().splitlines()

        if "True" in output:
            print("[INFO] Windows Defender Real-time Protection is Active.")
            logging.info("Windows Defender Real-time Protection is Active.")
        else:
            print("[WARNING] Windows Defender Real-time Protection is disabled!")
            logging.warning("Windows Defender Real-time Protection is disabled!")
    except Exception as e:
        print(f"[ERROR] Failed to check Windows Defender status: {e}")
        logging.error(f"Failed to check Windows Defender status: {e}")

def run_sfc():
    try:
        # Run sfc /scannow
        print("[INFO] Starting system file check...")
        logging.info("Starting system file check...")
        subprocess.run("sfc /scannow", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("[ERROR] Failed to run sfc: You may need to run this script as administrator.")
        logging.error(f"Failed to run sfc: {e}")
    except Exception as e:
        print(f"[ERROR] Failed to run sfc: {e}")
        logging.error(f"Failed to run sfc: {e}")

def check_processes():
    suspicious_processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            # Add logic to detect suspicious processes
            if proc.info['name'] in ["example_malware.exe"]:  # Replace with relevant file names
                suspicious_processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if suspicious_processes:
        print("[WARNING] Suspicious processes detected:")
        logging.warning("Suspicious processes detected:")
        for process in suspicious_processes:
            print(f"  PID: {process['pid']}, Name: {process['name']}")
            logging.warning(f"  PID: {process['pid']}, Name: {process['name']}")

def check_antivirus_status():
    try:
        # Check for third-party antivirus status
        cmd = 'wmic /namespace:\\\\root\\SecurityCenter2 path AntiVirusProduct get displayName,productState'
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        print("[INFO] Antivirus Status:\n", result.stdout.strip())
        logging.info("Antivirus Status:\n" + result.stdout.strip())
    except Exception as e:
        print(f"[ERROR] Failed to check antivirus status: {e}")
        logging.error(f"Failed to check antivirus status: {e}")

def check_firewall_status():
    try:
        # Check Windows Firewall status
        cmd = "netsh advfirewall show allprofiles state"
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        if "ON" in result.stdout:
            print("[INFO] Windows Firewall is enabled.")
            logging.info("Windows Firewall is enabled.")
        else:
            print("[WARNING] Windows Firewall is disabled!")
            logging.warning("Windows Firewall is disabled!")
    except Exception as e:
        print(f"[ERROR] Failed to check Windows Firewall status: {e}")
        logging.error(f"Failed to check Windows Firewall status: {e}")

def check_bitlocker_status():
    try:
        # Check BitLocker status
        cmd = "manage-bde -status"
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        print("[INFO] BitLocker Status:\n", result.stdout.strip())
        logging.info("BitLocker Status:\n" + result.stdout.strip())
    except Exception as e:
        print(f"[ERROR] Failed to check BitLocker status: {e}")
        logging.error(f"Failed to check BitLocker status: {e}")

def check_uac_status():
    try:
        # Check UAC status
        cmd = "reg query HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA"
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        if "0x1" in result.stdout:
            print("[INFO] UAC is enabled.")
            logging.info("UAC is enabled.")
        else:
            print("[WARNING] UAC is disabled!")
            logging.warning("UAC is disabled!")
    except Exception as e:
        print(f"[ERROR] Failed to check UAC status: {e}")
        logging.error(f"Failed to check UAC status: {e}")

def check_open_ports():
    try:
        # Check open ports
        cmd = "netstat -an | findstr LISTENING"
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        print("[INFO] Open Ports:\n", result.stdout.strip())
        logging.info("Open Ports:\n" + result.stdout.strip())
    except Exception as e:
        print(f"[ERROR] Failed to check open ports: {e}")
        logging.error(f"Failed to check open ports: {e}")

def check_windows_updates():
    try:
        # Check Windows Update logs
        cmd = "powershell -Command \"Get-WindowsUpdateLog\""
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        print("[INFO] Windows Update Log:\n", result.stdout.strip())
        logging.info("Windows Update Log:\n" + result.stdout.strip())
    except Exception as e:
        print(f"[ERROR] Failed to check Windows Update log: {e}")
        logging.error(f"Failed to check Windows Update log: {e}")

def hash_file(filepath):
    try:
        # Calculate file hash
        hasher = hashlib.sha256()
        with open(filepath, 'rb') as file:
            buffer = file.read()
            hasher.update(buffer)
        return hasher.hexdigest()
    except Exception as e:
        print(f"[ERROR] Failed to hash file: {e}")
        logging.error(f"Failed to hash file: {e}")
        return None

def check_process_integrity():
    for proc in psutil.process_iter(attrs=['pid', 'name', 'exe']):
        try:
            if proc.info['exe']:
                file_hash = hash_file(proc.info['exe'])
                print(f"[INFO] Process: {proc.info['name']}, Hash: {file_hash}")
                logging.info(f"Process: {proc.info['name']}, Hash: {file_hash}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

def main():
    if not is_admin():
        print("[ERROR] Script must be run as an administrator!")
        logging.error("Script must be run as an administrator!")
        return

    print("[INFO] Starting system security check...")
    logging.info("Starting system security check...")

    check_windows_defender()
    check_antivirus_status()
    check_firewall_status()
    check_bitlocker_status()
    check_uac_status()
    run_sfc()
    check_processes()
    check_process_integrity()
    check_open_ports()
    check_windows_updates()

if __name__ == "__main__":
    main()
