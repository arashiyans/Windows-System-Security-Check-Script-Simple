# System Security Check Script#1

This Python script performs a comprehensive security check on a Windows system. It checks the status of various security mechanisms like Windows Defender, Firewall, UAC, and BitLocker, detects suspicious processes, and verifies the integrity of running processes using file hashing.

## Features:
- Checks if Windows Defender real-time protection is active.
- Runs `sfc /scannow` to detect and repair corrupted system files.
- Detects suspicious processes by comparing process names.
- Checks third-party antivirus status and Windows Firewall status.
- Inspects open ports and logs active network connections.
- Checks if BitLocker and UAC are enabled.
- Verifies the integrity of running processes by calculating SHA-256 hash of executables.
- Logs all operations to `system_security_check.log` for auditing.

## Usage:
- Ensure you are running the script as an administrator.
- This script is designed for Windows environments.
- Requires Python and the following packages:
  - `psutil`
  - `subprocess`
  - `logging`
  - `ctypes`

## Requirements:
- Python 3.x
- `psutil` library (Install with `pip install psutil`)

⚠ **Warning**: 
- This script contains example malware names and is for educational purposes. Replace "example_malware.exe" with real malware names if needed.
- Do not run real malware on your main operating system. Use virtual machines such as VBox or VMware to avoid compromising your system.
- The script is not fully complete yet, and some issues may arise, for instance, Windows Defender real-time protection occasionally may not be detected.

## 🛠 Known Issues:
This script is still a **work in progress**. There are some issues that may arise, such as:
- The **Windows Defender Real-Time Protection** status may not always be detected accurately in some environments.
  
Feel free to contribute or provide feedback to improve the script!

# Kontribusi
Kami sangat menghargai kontribusi Anda. Jika Anda ingin berkontribusi pada proyek ini, silakan ikuti langkah-langkah berikut:

1. Fork repositori ini.
2. Buat branch baru untuk fitur yang ingin Anda tambahkan: `git checkout -b fitur-anda`
3. Commit perubahan Anda: `git commit -m 'Menambahkan fitur baru'`
4. Push ke branch Anda: `git push origin fitur-anda`
5. Buat pull request untuk kita tinjau.

# Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat berkas [LISENSI](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) untuk detailnya.

---
Terima kasih telah mengunjungi proyek ini. Kami harap website ini menjadi sumber inspirasi untuk Anda dalam belajar Python
