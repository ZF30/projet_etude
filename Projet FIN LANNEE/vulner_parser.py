import json

def parse_vulnerabilities(json_data):
    parsed_data = {}

    for ip, ip_data in json_data.items():
        for protocol, protocol_data in ip_data['protocols'].items():
            for port, port_data in protocol_data['ports'].items():
                if 'scripts' in port_data:
                    if 'vulners' in port_data['scripts']:
                        vulners_data = port_data['scripts']['vulners'].strip()
                        if vulners_data:
                            vulnerabilities = []
                            vulners_lines = vulners_data.split('\n')
                            for line in vulners_lines:
                                line = line.strip()
                                if line:
                                    parts = line.split('\t')
                                    if len(parts) >= 3:
                                        cpe, score, link = parts[:3]
                                        vulnerabilities.append({'cpe': cpe, 'score': score, 'link': link})
                            if vulnerabilities:
                                if ip not in parsed_data:
                                    parsed_data[ip] = {}
                                if port not in parsed_data[ip]:
                                    parsed_data[ip][port] = vulnerabilities
    return parsed_data

def json_load():
    with open('./Exports/vulners_data_results.json', 'r') as f:
        json_data = json.load(f)

    parsed_data = parse_vulnerabilities(json_data)
    
    with open('./Exports/vulners_parsed_results.json', 'w') as f:
        json.dump(parsed_data, f, indent=4)

