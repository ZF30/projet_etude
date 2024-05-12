import subprocess
import platform
import shutil
import os
import re
import time 
import sys
import password_test
import enum_scan
import vulner_scanner
import start_menu
import vulner_parser

def machine_menu():
    while True:
        start_menu.clear_screen()
        print("Machine Enumeration\n")
        print("1. Enumeration des utilisateurs")
        print("2. Bruteforce test et Test de mot de passe")
        print("3. Vulnerability Scan")
        print("4. Retour au menu prinicpal")
        print('5. Exist')
        
        response = input('\n Que voulez-vous faire? \n')
        if response == '1':
            print('Perfom a complete machine enumeration, by providing the target IP address')
            target_ip = input("Enter l'adresse IP de la machine à scanner: ")
            try:
                
                # Run enum4linux with the -U argument to enumerate users
                usernames = enum_scan.run_enum4linux(target_ip)
                enum_scan.save_to_json(usernames)
            finally:
                pass
        elif response == '2':
            target_ip = input("Enter l'adresse IP de la machine à tester le bruteforce: ")
            usernames = enum_scan.run_enum4linux(target_ip)
            try:
                
                # Use Hydra to brute force SSH using the extracted usernames
                found_credentials = enum_scan.hydra_bruteforce_ssh(target_ip, usernames)
                    # Save the found credentials to a JSON file
                save_creds = enum_scan.save_credentials_to_json(found_credentials)
                '''
                if found_credentials:
                    enum_scan.copy_shadow_file(target, found_credentials)
                    hash_file = "./Exports/shadow_copy.txt"
                    cracked_passwords = enum_scan.crack_passwords(hash_file)
                    if cracked_passwords:
                        for password in cracked_passwords:
                            print(password.strip())
                '''
            finally:
                password_results = password_test.analyze_passwords()
                password_test.export_results(password_results)
        elif response == '3':
            print('Le script nmap Vulners est utilisé pour le test des vulnerabilités.')
            target = input("Enter l'URL / adresse IP à tester: ")
            try:
                vulners_results= vulner_scanner.scan_target(target)
            finally:
                vulner_scanner.export_json(vulners_results)
                vulner_parser.json_load()
        elif response == '4':
            print('Retour au menu principal')
            break
        elif response == '5':
            print("L'application s'arret")
            time.sleep(5)
            sys.exit()
        else:
            print('Votre choix est invalide')

