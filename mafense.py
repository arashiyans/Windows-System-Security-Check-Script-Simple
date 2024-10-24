import subprocess
import psutil
import os

def check_windows_defender():
    try:
        # Cek status Windows Defender
        cmd = "powershell -Command \"Get-MpComputerStatus | Select-Object -Property AntivirusEnabled, RealTimeProtectionEnabled\""
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        output = result.stdout.strip().splitlines()

        if "True" in output:
            print("[INFO] Windows Defender Real-time Protection is Active.")
        else:
            print("[WARNING] Real-time Protection Windows Defender dinonaktifkan!")
    except Exception as e:
        print(f"[ERROR] Gagal memeriksa Windows Defender: {e}")

def run_sfc():
    try:
        # Jalankan sfc /scannow
        print("[INFO] Memulai pemeriksaan file sistem...")
        subprocess.run("sfc /scannow", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("[ERROR] Gagal menjalankan sfc: Anda mungkin perlu menjalankan skrip ini sebagai administrator.")
    except Exception as e:
        print(f"[ERROR] Gagal menjalankan sfc: {e}")


def check_processes():
    suspicious_processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            # Tambahkan logika untuk mendeteksi proses mencurigakan
            if proc.info['name'] in ["example_malware.exe"]:  # Ganti dengan nama file yang relevan
                suspicious_processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    if suspicious_processes:
        print("[WARNING] Proses mencurigakan ditemukan:")
        for process in suspicious_processes:
            print(f"  PID: {process['pid']}, Name: {process['name']}")

def main():
    print("[INFO] Memulai pemeriksaan keamanan sistem...")
    check_windows_defender()
    run_sfc()
    check_processes()
    # Tambahkan pemeriksaan lainnya sesuai kebutuhan

if __name__ == "__main__":
    main()
