# Task 4: Basic Networking

This project demonstrates how to connect a virtual Android system to a backend API using a Python script. The script collects system information from the Android emulator and sends it to the backend API developed in Task 1.

---

## Features

- Establishes an HTTP connection with the backend server.
- Gathers mock device data such as:
  - OS Version
  - Device Model
  - Memory Info
- Sends data using HTTP POST to the backend API.
- Logs the response from the server.

---

## Files Included

- `task4_script.py` – Python script to send data from the Android emulator to the backend.
- `system_info.txt` – Log file containing the collected device information.

---

##  How to Run the Script

1. **Start the Android Emulator:**
   - Open Android Studio and launch the AVD emulator.

2. **Ensure ADB is Working:**
   - Run: `adb devices` to confirm the emulator is detected.

3. **Update the Script URL:**
   - Replace the placeholder API URL in the script:
     ```python
     url = "http://<your-server-ip>:<port>/api/add-app/"
     ```

4. **Run the Python Script:**
   ```bash
   python networking_script.py



Brief Explanation of How the Script Works


The script uses adb shell commands to collect:

OS version: adb shell getprop ro.build.version.release

Device model: adb shell getprop ro.product.model

Memory info: adb shell cat /proc/meminfo

These values are formatted into JSON:

{
  "name": "Android System Info",
  "version": "11",
  "description": "Device Model: sdk_gphone_x86_64, Total Memory: MemTotal: 2028176 kB, Available Memory: MemAvailable: 1181252 kB"
}

 Example Response from Server

Status Code: 201
{
  "id": 5,
  "name": "Android System Info",
  "version": "11",
  "description": "Device Model: sdk_gphone_x86_64, Total Memory: MemTotal: 2028176 kB, Available Memory: MemAvailable: 1181252 kB"
}