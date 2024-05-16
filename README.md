ienvenue sur l'outil de test de pénétration de cybersécurité Recon-NG.

Pour l'instant, la version 1.0 se concentre sur la première étape de la chaîne d'exécution, la reconnaissance.

Avec des aspects futurs développés pour tirer profit des résultats trouvés en utilisant des charges utiles ou des exploits.

Le toolkit devrait installer toutes les bibliothèques ou paquets nécessaires, mais dans le cas où ce ne serait pas le cas, je vais les lister afin que vous puissiez les installer manuellement.

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

Il est conseillé de lancer l'outil en utilisant sudo, en utilisant la commande suivante
sudo python main.py

La première fonction du premier menu propose deux options pour l'énumération des DNS/réseaux.

L'empreinte DNS est réalisée à l'aide de la bibliothèque dnspython qui fait appel au module resolver, qui effectue une requête DNS sur le domaine indiqué par l'utilisateur et renvoie tous les enregistrements du type : TXT, A ,AAAA ,MX ,CNAME ,SOA ,NS.

Pour l'analyse du réseau, la boîte à outils utilise le module python-nmap qui prend une adresse IP saisie par l'utilisateur.

Pour les tests de l'application web, nous avons trois tests :

Gobuster qui prend une URL ex(https://www.example.org/) et liste ensuite tous les répertoires trouvés à partir de cette URL. Toutes les URL doivent être écrites dans ce format.

Ensuite, Nikto est utilisé pour analyser les vulnérabilités trouvées pour une URL spécifique dans le même format que précédemment.

Enfin, le scan analytique parcourt le code source d'une application web donnée et recherche des variables ou des mots-clés tels ques password, user, username, apikey, secret, pour voir s'il y a des informations confidentielles dans le code source.

Pour le dernier menu, les tests machine, il est nécessaire d'effectuer d'abord l'énumération des utilisateurs avant d'effectuer le test SSH Brutefore, si une connexion réussie est notée, il effectue ensuite une analyse du mot de passe pour juger de la complexité de celui-ci. Pour finir, l'analyse des vulnérabilités se fait en utilisant nmap avec le paramètre --script vulners en ciblant toutes les CVE avec un score de 5.0 ou plus.

Une fois tout cela terminé, retournez au menu de démarrage pour générer le rapport.
