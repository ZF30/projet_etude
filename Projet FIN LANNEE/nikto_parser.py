import json

def parse_and_export(input_file, output_file):
    # Read JSON data from input file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Extract relevant information
    host = data["host"]
    ip = data["ip"]
    port = data["port"]
    vulnerabilities = data["vulnerabilities"]

    # Process vulnerabilities
    processed_vulnerabilities = []
    for vulnerability in vulnerabilities:
        id = vulnerability.get("id", "")
        references = vulnerability.get("references", "")
        method = vulnerability.get("method", "")
        url = vulnerability.get("url", "")
        msg = vulnerability.get("msg", "")
        processed_vulnerabilities.append({
            "id": id,
            "references": references,
            "method": method,
            "url": url,
            "msg": msg
        })

    # Create output data
    output_data = {
        "host": host,
        "ip": ip,
        "port": port,
        "vulnerabilities": processed_vulnerabilities
    }

    # Write output data to JSON file
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=4)


