import subprocess
import os

save_dir = r"D:\Assignments\logs"
os.makedirs(save_dir, exist_ok=True)
file_path = os.path.join(save_dir, "system_info.txt")

commands = {
    "OS Version": "adb shell getprop ro.build.version.release",
    "Device Model": "adb shell getprop ro.product.model",
}

system_info = {}
for key, cmd in commands.items():
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    system_info[key] = result.stdout.strip()

meminfo_output = subprocess.run("adb shell cat /proc/meminfo", shell=True, capture_output=True, text=True).stdout
mem_lines = meminfo_output.split("\n")

total_mem = next((line for line in mem_lines if "MemTotal" in line), "Total Memory: Not Found")
avail_mem = next((line for line in mem_lines if "MemAvailable" in line), "Available Memory: Not Found")

system_info["Total Memory"] = total_mem.strip()
system_info["Available Memory"] = avail_mem.strip()

with open(file_path, "w") as file:
    for key, value in system_info.items():
        file.write(f"{key}: {value}\n")

print(f"System info logged successfully! File saved at: {file_path}")
