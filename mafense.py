import subprocess
import psutil
import os

def check_windows_defender():
    try:
        # Check Windows Defender status
        cmd = "powershell -Command \"Get-MpComputerStatus | Select-Object -Property AntivirusEnabled, RealTimeProtectionEnabled\""
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        output = result.stdout.strip().splitlines()

        if "True" in output:
            print("[INFO] Windows Defender Real-time Protection is Active.")
        else:
            print("[WARNING] Windows Defender Real-time Protection is disabled!")
    except Exception as e:
        print(f"[ERROR] Failed to check Windows Defender status: {e}")

def run_sfc():
    try:
        # Run sfc /scannow
        print("[INFO] Starting system file check...")
        subprocess.run("sfc /scannow", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("[ERROR] Failed to run sfc: You might need to run this script as administrator.")
    except Exception as e:
        print(f"[ERROR] Failed to run sfc: {e}")

def check_processes():
    suspicious_processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            # Add logic to detect suspicious processes
            if proc.info['name'] in ["example_malware.exe"]:  # Replace with relevant file name
                suspicious_processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    if suspicious_processes:
        print("[WARNING] Suspicious processes found:")
        for process in suspicious_processes:
            print(f"  PID: {process['pid']}, Name: {process['name']}")

def main():
    print("[INFO] Starting system security check...")
    check_windows_defender()
    run_sfc()
    check_processes()
    # Add other checks as needed

if __name__ == "__main__":
    main()
