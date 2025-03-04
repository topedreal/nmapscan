## Nmap Scanner

A simple Python-based Nmap scanning tool that allows users to perform different types of scans on a given target.

## 🔥 Features
- Supports **multiple scan types**:
  - `-sS` (SYN Scan)
  - `-sT` (TCP Connect Scan)
  - `-sU` (UDP Scan)
  - `-O` (OS Detection)
    
- **Automatic input validation** for scan type selection.
- Saves scan results to a **text file** for later review.
- **Error handling** for failed scans.

## Requirements
Before running the script, ensure you have:
- Python **3.7+** installed
- Nmap installed on your system:
  - **Linux/macOS**:  
    ```sh
    sudo apt install nmap  # Debian-based
    sudo yum install nmap  # Red Hat-based
    brew install nmap      # macOS
    ```
## How to Use

### **Run the Script Directly**
```
python Nmapscan.py
Enter the target IP address or domain name.
Select a scan type by entering 1, 2, 3, or 4.
The scan will start, and results will be saved in a text file.
```

📜 License
This project is licensed under the MIT License.

## Feedback & Suggestions

We value your input! If you have any feedback or suggestions on how to improve this script, please feel free to leave a comment. Your contributions are greatly appreciated and will help us enhance the script for everyone. [Issues](https://github.com/topedreal/nmapscan/issues/1)
