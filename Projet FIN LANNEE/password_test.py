import re
import json

def check_password_complexity(password):
    # Password complexity rules
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+=\-[\]{};:\'",.<>?`~|\\/]', password))
    length = len(password)

    # Calculate complexity level
    complexity = 0
    if length >= 8:
        complexity += 1
    if has_lower:
        complexity += 1
    if has_upper:
        complexity += 1
    if has_digit:
        complexity += 1
    if has_special:
        complexity += 1

    # Define complexity labels
    complexity_labels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong"
    }

    # Return password and its complexity
    return password, complexity_labels[min(complexity, 4)]

def read_passwd_file():
    try:
        with open("./Exports/found_credentials.json", "r") as f:
            data = json.load(f)
            return [(username, data[username]["password"]) for username in data]
    except FileNotFoundError:
        print("Error: passwd_copy.json file not found.")
        return []

def analyze_passwords():
    passwords = read_passwd_file()
    results = []
    for username, password in passwords:
        password, complexity = check_password_complexity(password)
        results.append((username, password, complexity))
    return results

def export_results(data):
    results_dict = {}
    for username, password, complexity in data:
        results_dict[username] = {
            "password": password,
            "password_complexity": complexity
        }
    output_file = "./Exports/password_complexity.json"
    with open(output_file, "w") as f:
        json.dump(results_dict, f, indent=4)

        
