import requests
import subprocess
import json
import os

API_URL = "http://127.0.0.1:8000/api/add-app/"

def get_system_info():
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

    app_data = {
        "name": "Android System Info",
        "version": system_info["OS Version"],
        "description": f"Device Model: {system_info['Device Model']}, Total Memory: {system_info['Total Memory']}, Available Memory: {system_info['Available Memory']}"
    }

    return app_data

def send_data_to_server(data):
    try:
        response = requests.post(API_URL, json=data)
        return response.status_code, response.text
    except Exception as e:
        return "Error", str(e)

if __name__ == "__main__":
    print("Collecting system info...")
    app_data = get_system_info()

    print("Sending data to server...")
    status, response = send_data_to_server(app_data)

    save_dir = r"D:\Assignments\Task4_logs"
    os.makedirs(save_dir, exist_ok=True)
    log_file_path = os.path.join(save_dir, "network_log.txt")

    with open(log_file_path, "w") as file:
        file.write("Sent Data:\n")
        file.write(json.dumps(app_data, indent=4))
        file.write("\n\nServer Response:\n")
        file.write(f"Status Code: {status}\n")
        file.write(response)

    print(f"Data sent! Server Response: {status}")
    print(f"Log saved at: {log_file_path}")
