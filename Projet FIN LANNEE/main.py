import os
import time
import sys
import start_menu
import subprocess
import requests

def install_dependencies(requirements_file):
    try:
        subprocess.run(["pip", "install", "-r", requirements_file], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        
def is_package_installed(package):
    try:
        subprocess.check_output(['dpkg', '-l', package], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def install_packages():
    packages = ['gobuster', 'enum4linux','nikto','hydra','pip']  # Replace with your package names
    
    try:
        subprocess.check_call(['sudo', 'apt', 'update'])
        for package in packages:
            if not is_package_installed(package):
                subprocess.check_call(['sudo', 'apt', 'install', '-y', package])
            else:
                print(f"{package} is already installed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")
        raise SystemExit(1)

def is_nmap_installed():
    try:
        subprocess.check_output(['nmap', '-V'])
        return True
    except subprocess.CalledProcessError:
        return False

def is_vulners_script_installed():
    return os.path.isfile('/usr/share/nmap/scripts/vulners.nse')

def download_vulners_script():
    url = 'https://raw.githubusercontent.com/vulnersCom/nmap-vulners/master/vulners.nse'
    script_path = '/usr/share/nmap/scripts/vulners.nse'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(script_path, 'wb') as f:
                f.write(response.content)
            os.chmod(script_path, 0o755)
            print("vulners.nse script downloaded successfully.")
        else:
            print("Failed to download vulners.nse script.")
    except Exception as e:
        print(f"An error occurred while downloading vulners.nse script: {e}")

def install_nmap_and_vulners_script():
    try:
        if not is_nmap_installed():
            subprocess.check_call(['sudo', 'apt', 'update'])
            subprocess.check_call(['sudo', 'apt', 'install', '-y', 'nmap'])
        
        if not is_vulners_script_installed():
            download_vulners_script()
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        raise SystemExit(1)
    
if __name__ == "__main__":

    requirements_file = "requirements.txt"
    #install_packages()
    install_dependencies(requirements_file)
    #install_nmap_and_vulners_script()
    start_menu.start_menu()
