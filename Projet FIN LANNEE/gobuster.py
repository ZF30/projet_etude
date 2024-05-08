import subprocess
import shutil
import os
import json
    
def scan_directories(target):
    try:
        command = f"gobuster dir -u {target} -w '/usr/share/dirb/wordlists/common.txt' -q"
        result = subprocess.run(command, shell=True, capture_output=True, check=True, text=True)
        if result.returncode == 0:
            return result.stdout.split('\n')
        else:
            print("Error running Gobuster.")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def export_results_to_json(results):
    try:
        with open("./Exports/gobuster_results.json", "w") as f:
            json.dump(results, f, indent=4)
    except Exception as e:
        print(f"Error exporting results to JSON file: {e}")

        