import json

def parse_json_data(json_files, output_file):
    parsed_data = {}

    # Loop through each JSON file
    for json_file in json_files:
        with open(json_file, 'r') as f:
            data = json.load(f)

        # Loop through each scan type (e.g., 'S_scan', 'T_scan')
        for scan_type, scan_data in data.items():
            if scan_type not in parsed_data:
                parsed_data[scan_type] = {}

            # Check if the 'tcp' key exists in the scan data
            if 'tcp' in scan_data:
                # Loop through each port in the scan data
                for port, port_data in scan_data['tcp'].items():
                    # If port is not already in parsed data, add it
                    if port not in parsed_data[scan_type]:
                        parsed_data[scan_type][port] = port_data

    # Write parsed data to output file
    with open(output_file, 'w') as outfile:
        json.dump(parsed_data, outfile, indent=4)

    print(f"Parsed data exported to '{output_file}'.")

