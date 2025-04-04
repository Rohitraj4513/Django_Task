Virtual Android System Simulation

1. How to Run the Script

Prerequisites

Before running the script, ensure you have:

# ADB (Android Debug Bridge) installed and added to the system PATH
# Python 3.x installed
# A Running Virtual Android Emulator (Android Studio Emulator or QEMU)

Steps to Execute the Script
Start the Android Emulator

If using Android Studio:

Open Android Studio → Device Manager → Launch Emulator

If using QEMU:

Start the virtual Android system manually.

Verify ADB Connection
Run the following command to check if the emulator is detected:

adb devices

Expected output:

List of devices attached
emulator-5554   device

Run the Python Script

Open Command Prompt (CMD) or PowerShell in the project directory.

Execute the script:


python android_simulation.py

Expected output:

System info logged successfully! File saved at: D:\Assignments\logs\system_info.txt

2. How to Install an App on the Virtual System

Place the APK file in the project folder (e.g., D:\Assignments\app\HelloWorld.apk).

Run the installation command in the terminal:

adb install -r "D:\Assignments\app\HelloWorld.apk"
Verify installation by running:


adb shell pm list packages | findstr "helloworld"
Expected output:


package:com.example.helloworld

3. Summary of the System Information Logged

The script logs key system details, including:

OS Version
Device Model
Total Memory
Available Memory

Example Log (system_info.txt)

OS Version: 11
Device Model: sdk_gphone_x86_64
Total Memory: MemTotal:        2028176 kB
Available Memory: MemAvailable:    1073768 kB