import json

def parse_json(json_file,output_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    parsed_data = []

    # Parse each line
    for line in data:
        # Remove "\u001b[2K" from each line
        line = line.replace("\u001b[2K", "")

        # Split the line into parts
        parts = line.split()

        # Filter out lines without a status code
        if "(Status:" not in line:
            continue

        # Extract the path and status code
        path = parts[0]
        status_code = parts[2][:-1]  # Remove the trailing parenthesis

        # Extract the link if available
        link = None
        if parts[-1].startswith("[-->"):
            link = parts[-1][4:-1]  # Remove "[-->" and "]"

        # Append to the parsed data list
        parsed_data.append({"path": path, "status_code": status_code, "link": link})

     # Write parsed data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(parsed_data, f, indent=4)
