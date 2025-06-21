# 🔐 Wi-Fi Password Extractor (Windows)

This Python script extracts all **saved Wi-Fi network names and their passwords** from a Windows system using `netsh` and writes them to a text file.

---

## ⚙️ Features

- 📡 Lists all saved Wi-Fi profiles
- 🔑 Retrieves saved passwords (if available)
- 📁 Saves the output to a `.txt` file
- ✅ Pure Python and native Windows command usage
- 🪄 Works without any third-party libraries

---

## 📋 Requirements

- Python 3.x
- Windows OS (uses `netsh` command)
- Admin privileges may be required on some systems

---

## 🚀 Usage

When executed, the script will:

- Find all saved Wi-Fi profiles on your system
- Attempt to retrieve the passwords for each (if they exist)
- Save the names and passwords in a file named:

  ```
  nothing_to_see_here420869.txt
  ```

- Then, it reads and prints the contents of a file named:

  ```
  nothing_to_see_here.txt
  ```

  > 📝 This second file read is for **testing purposes**. You may remove that part of the code when deploying.

---

- If no password is saved, the value will be `None`.

---

## 📦 Recommended: Convert to Executable (.exe)

To run this on another Windows system without Python installed:

1. Install [`pyinstaller`](https://www.pyinstaller.org/):

   ```bash
   pip install pyinstaller
   ```

2. Convert the script to an executable:

   ```bash
   pyinstaller --onefile wifi_password_extractor.py
   ```

   The generated `.exe` will be found in the `dist` folder.

---

## ⚠️ Disclaimer

This tool is for **educational and recovery purposes only**.  
Use it **only on systems and networks you own or have permission to access**.

---
