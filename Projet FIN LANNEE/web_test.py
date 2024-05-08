import subprocess
import platform
import os
import shutil
import sys
import time
import json
import nikto
import static_test 
import gobuster
import gobuster_parser
import nikto_parser
import start_menu

def web_menu():
    while True:
        start_menu.clear_screen()
        print("Web Application / Websites Testes \n")
        print("1. Directories Reconnaissance")
        print("2. Vulnerability Scan")
        print("3. Scan Analystic")
        print("4. Retour au menu prinicpal")
        print('5. Exist')
        
        response = input('\n Que voulez-vous faire? \n')
        if response == '1':
            target_url = input('veuillez saisir le target: ')  # Remplacer avec l'URL de votre choix
            try:
                gobuster.check_install_gobuster()
                gobuster_results = gobuster.scan_directories(target_url)
                gobuster.export_results_to_json(gobuster_results)
            finally:
                if os.path.isfile("./Exports/gobuster_results.json"): 
                    json_file = "./Exports/gobuster_results.json"
                    output_file = "./Exports/gobuster_parsed_results.json"
                    gobuster_parser.parse_json(json_file,output_file)
                else:
                    pass
                
        elif response == '2':
            print('Pour tester les vulernabilites l\'outil utilise la solution Nikto')
            target_url = input("Veuillez taper un url: ")  # Replace with your target URL
            try:
                nikto.run_nikto_scan(target_url)
            finally:
                if os.path.isfile("./Exports/nikto_results.json"):
                    input_file = "./Exports/nikto_results.json"
                    output_file = "./Exports/nikto_parsed_results.json"
                    nikto_parser.parse_and_export(input_file, output_file)
                else:
                    pass
        elif response == '3':
            print('''Pour tester le code source du site en question, pour voir s'il existe des information personnel ou confidential comme mot de passe, usernames ou api keys''')
            url = input("Enter l'URL à tester: ")
            try:
                static_test.analyze_webpage(url)
            except FileNotFoundError:
                # Handle file not found exception
                print("Error occured")
        elif response == '4':
            print('Retour au menu principal')
            break
        elif response == '5':
            print("L'application s'arret en quelques secondes")
            time.sleep(5)
            sys.exit()
        else:
            print('Votre choix est invalide')

