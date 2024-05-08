import subprocess
import json
import shutil
import os

def check_install_nikto():
    # Check if Nikto is installed
    try:
        subprocess.run(['nikto', '-Version'], check=True)
        print("Nikto is already installed.")
    except FileNotFoundError:
        # Nikto not found, install it
        print("Nikto is not installed. Installing...")
        subprocess.run(['sudo', 'apt-get', 'install', 'nikto'], check=True)
        print("Nikto installed successfully.")

def run_nikto_scan(target):
    # Run Nikto scan
    try:
        # Run Nikto with detailed scan options and JSON output
        nikto_cmd = f"nikto -host {target} -Format json -output './Exports/nikto_results.json' -Tuning 123bde"
        subprocess.run(nikto_cmd, shell=True, check=True)
        print("Nikto scan completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Nikto: {e}")

        
def delete_nikto():
    # Delete Nikto executable if it was not installed initially
    if not shutil.which('nikto'):
        os.remove('/usr/bin/nikto')
        print("Nikto deleted.")
