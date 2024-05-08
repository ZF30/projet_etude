import subprocess
import json
import nmap


def run_nmap_scan(target, scan_type):
    nm = nmap.PortScanner()
    if scan_type == 'O':
        nm.scan(target, arguments='-O')
    else:
        nm.scan(target, arguments='-s' + scan_type)
    return {f"{scan_type}_scan": nm[target]}

def run_all_scans(target):
    scan_types = [ 'A', 'V', 'O']
    results = {}
    for scan_type in scan_types:
        results.update(run_nmap_scan(target, scan_type))
    return results

def export_to_json(results, filename):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)




    