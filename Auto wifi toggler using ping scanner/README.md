# 🛰️ Wi-Fi Auto Reconnect Monitor (Python)

A Python script that continuously monitors your internet connection and automatically **restarts the Wi-Fi** if connectivity is lost.

---

## 🚀 Usage

When the script runs, it will prompt you for two inputs:

- **Cooldown Time** – Time in seconds between each ping while the internet is active.
- **Restart Wait Time** – Time in seconds to wait after restarting Wi-Fi before continuing monitoring.

### 🔄 Example

```text
only put number *second. Only whole numbers
cooldown time ----> 5
Insert time to stop before restarting WIFI ----> 10
```

---
## ⚙️ How It Works

- Pings `8.8.8.8` once every cooldown interval.
- If a ping fails:
  - Runs `netsh wlan disconnect` (turns off Wi-Fi)
  - Reconnects to the most recently used Wi-Fi profile using PowerShell
  - Waits for the restart delay, then resumes pinging

---

## 🔧 Features

- 📡 Monitors internet connection via ping (`8.8.8.8` by default)
- 🔌 Automatically disconnects and reconnects Wi-Fi when connection is lost
- ⏲️ Customizable cooldown and restart delay times
- 🪟 Designed specifically for **Windows** (uses `netsh` and PowerShell)

---

## 📋 Requirements

- Python 3.x
- Windows operating system
- Existing saved Wi-Fi profile on the system

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Mrn0b0dy-shantanu/Python-Projects.git
   cd Python-Projects
   ```

2. **Run the script:**

   ```bash
   python wifi_auto_reconnect.py
   ```

   > Replace `wifi_auto_reconnect.py` with your actual filename if different.

---




## 🙋‍♂️ Author

**Shantanu (Mrn0b0dy-shantanu)**  
[GitHub Profile](https://github.com/Mrn0b0dy-shantanu)
