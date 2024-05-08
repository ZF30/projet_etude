import subprocess
import sys
import time
import dns_test as dns
import nmap_scanner
import nmap_parser
import start_menu
import os

def network_domain_menu():
    while True:
        start_menu.clear_screen()
        print("Domain / Network Reconnaissance\n")
        print("1. DNS Enumeration / Footprinting")
        print("2. Network Scan")
        print("3. Retour au menu precedent")
        print("4. Quittez l'application")
        
        response = input('\n Que voulez-vous faire?: ')
        if response == '1':
            target = input("Enter the domain name to perform DNS footprinting: ")
            dns.get_dns_records(target)
        elif response == '2':
            target = input("Enter the target/network to be scanned: ")
            try:
                scan_results = nmap_scanner.run_all_scans(target)
                nmap_scanner.export_to_json(scan_results,"./Exports/nmap_scan_results.json")
            finally:
                if os.path.isfile("./Exports/nmap_scan_results.json"):   
                    json_files = ["./Exports/nmap_scan_results.json"]  
                    output_file = "./Exports/nmap_parsed_results.json"
                    nmap_parser.parse_json_data(json_files, output_file)
                else:
                    pass
        elif response == '3':
            print("Retourne au menu precedent")
            time.sleep(5)
            break
        elif response == '4':
            print("L'application s'arret")
            time.sleep(5)
            sys.exit()
        else:
            print('Votre choix est invalide')

