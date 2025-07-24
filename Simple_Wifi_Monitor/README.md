# WiFi Network Scanner
### This is made for beginners/amateurs to learn while building code. Every line of code is explained thoroughly.
### It scans nearby wireless networks using monitor mode and displays detailed info in a clean table. With error handling.




## ⚙️ Requirements

- Python 3  
- Root privileges  
- Linux OS  
- Wireless card supporting monitor mode  

Install dependencies:

```
pip3 install -r requirements.txt
```

## ✅ Features

- Lists available network interfaces  
- Enables monitor mode on selected interface  
- Captures and displays:  all the wifi info
- Auto-disables monitor mode after scan or on Ctrl+C  
- Colorized console output  
- Results shown in a tabulated format using `tabulate`

---
## 📝 Notes
- Only works on Linux
- Requires monitor-mode capable wireless adapter


