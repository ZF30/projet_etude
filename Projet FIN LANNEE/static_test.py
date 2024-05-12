import requests
import re
import json

def analyze_webpage(url):
    try:
        # Fetch the web page source code
        response = requests.get(url)
        source_code = response.text

        # Define patterns for sensitive information
        sensitive_patterns = {
            'username': re.compile(r'(?i)username(?:\s*[:=]\s*)([^\s]+)'),
            'login': re.compile(r'(?i)login(?:\s*[:=]\s*)([^\s]+)'),
            'user': re.compile(r'(?i)user(?:\s*[:=]\s*)([^\s]+)'),
            'mdp': re.compile(r'(?i)mdp(?:\s*[:=]\s*)([^\s]+)'),
            'password': re.compile(r'(?i)password(?:\s*[:=]\s*)([^\s]+)'),
            'apikey': re.compile(r'(?i)apikey(?:\s*[:=]\s*)([^\s]+)'),
            'secret': re.compile(r'(?i)secret(?:\s*[:=]\s*)([^\s]+)')
        }

        # Search for sensitive information in the source code
        sensitive_data = {}
        for key, pattern in sensitive_patterns.items():
            matches = pattern.findall(source_code)
            if matches:
                sensitive_data[key] = matches

        # Write results to JSON file
        with open('./Exports/analysis_report.json', 'w') as json_file:
            json.dump(sensitive_data, json_file, indent=4)

        # Print completion message
        print(f"Analysis completed. Results saved to the file analysis_report.json")
    except requests.RequestException as e:
        print(f"Error fetching web page: {e}")

