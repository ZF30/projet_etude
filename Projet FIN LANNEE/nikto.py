import subprocess
import json
import shutil
import os

def ensure_https(url):
    # Check if the URL starts with 'https://'
    if url.startswith('https://'):
        return url
    # If not, add 'https://' to the beginning of the URL
    else:
        return 'https://' + url

def run_nikto_scan(target):
    # Run Nikto scan
    try:
        # Run Nikto with detailed scan options and JSON output
        nikto_cmd = f"nikto -host {target} -Format json -output './Exports/nikto_results.json' -Tuning 123bde"
        subprocess.run(nikto_cmd, shell=True, check=True)
        print("Nikto scan completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Nikto: {e}")
