Bienvenue sur l'outil de test de pénétration de cybersécurité Recon-NG.

Version 1.0
La version 1.0 de Recon-NG se concentre sur la première étape de la chaîne d'exécution : la reconnaissance. Des fonctionnalités futures seront développées pour tirer profit des résultats trouvés en utilisant des charges utiles ou des exploits.

Installation des dépendances
Le toolkit devrait installer automatiquement toutes les bibliothèques et paquets nécessaires. Cependant, dans le cas où cela ne fonctionnerait pas, voici la liste des dépendances que vous pouvez installer manuellement :

Paquets :
pip
hydra
nmap
gobuster
nikto
enum4linux

Bibliothèques :
paramiko
reportlab
dnspython
python-nmap

Licences
Veuillez noter que chaque bibliothèque et paquet utilisé dans cet outil est soumis à sa propre licence. Voici un résumé des licences associées aux principales dépendances :

pip : MIT License
hydra : AGPL-3.0
nmap : Nmap Public Source License (NPSL)
gobuster : Apache License 2.0
nikto : GPL-2.0
enum4linux : GPL-3.0
paramiko : LGPL-2.1
reportlab : BSD License
dnspython : Apache License 2.0
python-nmap : GPL-3.0
Il est de votre responsabilité de vous assurer que vous respectez les termes de ces licences lors de l'utilisation de Recon-NG.

Utilisation de l'outil
Il est conseillé de lancer l'outil avec des privilèges administratifs en utilisant la commande suivante :
sudo python main.py

Fonctionnalités
  Menu principal
La première fonction du menu principal propose deux options pour l'énumération des DNS/réseaux.
 DNS Footprinting :
    Utilise la bibliothèque dnspython pour effectuer une requête DNS sur le domaine indiqué par l'utilisateur.
Renvoie tous les enregistrements de type : TXT, A, AAAA, MX, CNAME, SOA, NS.
Analyse du réseau :
    Utilise le module python-nmap pour scanner une adresse IP saisie par l'utilisateur.

Tests d'application web
Pour les tests de l'application web, nous avons trois outils principaux :
Gobuster :
    Prend une URL (ex : https://www.example.org/) et liste tous les répertoires trouvés à partir de cette URL.
Toutes les URL doivent être écrites dans ce format.
Nikto :
    Analyse les vulnérabilités pour une URL spécifique dans le même format que précédemment.
Scan analytique :
    Parcourt le code source d'une application web donnée à la recherche de variables ou de mots-clés tels que password, user, username, apikey, secret pour détecter des informations confidentielles.

Tests machine
    Énumération des utilisateurs :
      Effectue une énumération des utilisateurs avant de procéder au test SSH Bruteforce.
    Test SSH Bruteforce :
      Si une connexion réussie est notée, une analyse du mot de passe est effectuée pour évaluer sa complexité.
    Analyse des vulnérabilités :
      Utilise nmap avec le paramètre --script vulners pour cibler toutes les CVE avec un score de 5.0 ou plus.
    
Rapport
Une fois toutes les étapes terminées, revenez au menu de démarrage pour générer le rapport.

Merci d'utiliser Recon-NG pour vos tests de pénétration de cybersécurité. Assurez-vous de respecter les lois et les règles en vigueur lors de l'utilisation de cet outil.






