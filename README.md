# Windows-System-Security-Check-Script-#1

This Python script automates basic security checks on a Windows system. It helps users monitor their system for potential security issues by performing the following tasks:

## Features:
- **Windows Defender Status Check**: Verifies whether Windows Defender's real-time protection is enabled, ensuring your system is actively protected.
- **System File Check (SFC)**: Runs the `sfc /scannow` command to check and repair any corrupt or missing system files, improving system integrity.
- **Suspicious Process Detection**: Scans currently running processes for suspicious activity (e.g., malware), which can be customized based on specific process names.

## Usage:
1. Clone the repository.
2. Run the script in a Python environment with administrative privileges for accurate results.
3. The script will automatically check the system's security status and display any issues found.

## Requirements:
- Python 3.x
- `psutil` library (Install with `pip install psutil`)

## ⚠️ Warning:
The code contains **example malware names** which are not real. To test the detection feature, you can replace the example name with actual malware process names if available.

- **DO NOT** run this script on a real operating system if you are testing with real malware.
- **Use a virtual environment** like VirtualBox or VMware to safely run tests with malware.



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
