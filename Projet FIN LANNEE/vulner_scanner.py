import nmap
import json

def scan_target(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-p 1-65535 -sV --script vulners --script-args mincvss=5.5')

    results = {}

    if nm.all_hosts():
        for host in nm.all_hosts():
            results[host] = {}
            results[host]['protocols'] = {}
            for proto in nm[host].all_protocols():
                results[host]['protocols'][proto] = {}
                results[host]['protocols'][proto]['ports'] = {}
                ports = nm[host][proto].keys()
                for port in ports:
                    results[host]['protocols'][proto]['ports'][port] = {}
                    results[host]['protocols'][proto]['ports'][port]['state'] = nm[host][proto][port]['state']
                    if 'script' in nm[host][proto][port]:
                        results[host]['protocols'][proto]['ports'][port]['scripts'] = {}
                        for script in nm[host][proto][port]['script'].keys():
                            results[host]['protocols'][proto]['ports'][port]['scripts'][script] = nm[host][proto][port]['script'][script]
    return results

def export_json(results):
    output_file = './Exports/vulners_data_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)
