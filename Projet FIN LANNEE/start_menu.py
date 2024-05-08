import dns_network_menu
import web_test
import machine_test
import generation_rapport
import os
import time
import sys

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


def start_menu():

    while True:
        clear_screen()
        print(
            """
                        *************************************************************************
                        **                  Welcome to danger zone !                           **
                        ** Remember this is only suppose to be used for ethical purposes only  **
                        *************************************************************************
                        """
        )
        print("Python Pentest Toolkit\n")
        print("What test do you want to run")
        print("1. Domain / Network Reconnaissance")
        print("2. Web Application")
        print("3. Machine")
        print("4. Generation du rapport")
        print("5. Exit")

        response = input("\n Que voulez-vous faire?: ")
        if response == "1":
            dns_network_menu.network_domain_menu()
        elif response == "2":
            web_test.web_menu()
        elif response == "3":
            machine_test.machine_menu()
        elif response == "4":
            # Example usage:
            output_pdf_file = "./Report/pentest_report_new.pdf"
            dns_json_file = "./Exports/dns_footprinting_results.json"
            nmap_json_file = "./Exports/nmap_parsed_results.json"
            users_json_file = "./Exports/enum_user_results.json"
            credentials_json_file = "./Exports/password_complexity.json"
            cve_json_file = "./Exports/vulners_parsed_results.json"
            gobuster_json_file = "./Exports/gobuster_parsed_results.json"
            nikto_json_file = "./Exports/nikto_parsed_results.json"

            generation_rapport.render_all_to_pdf(output_pdf_file, dns_json_file,nmap_json_file,cve_json_file, users_json_file, credentials_json_file, nikto_json_file,gobuster_json_file)
        elif response == "5":
            print("L'application s'arret")
            time.sleep(5)
            sys.exit()
            loop = False
            print("\nVous quitez le programme")
        else:
            print("Votre choix est invalide")
