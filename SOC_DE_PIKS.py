#!/usr/bin/env python3
#	 ____   ___   ____   ____  _____   ____ ___ _  ______  
#	/ ___| / _ \ / ___| |  _ \| ____| |  _ \_ _| |/ / ___| 
#	\___ \| | | | |     | | | |  _|   | |_) | || ' /\___ \ 
#	 ___) | |_| | |___  | |_| | |___  |  __/| || . \ ___) |
#	|____/ \___/ \____| |____/|_____| |_|  |___|_|\_\____/ 
#
#		Script de Pentest Codé par Kavi & Pierre
#			   Projet MSI 1 CS B
#			          © 
#			     Sup de Vinci
#
#
# Soc de PIKS version : 8.6 - BETA
#
from termcolor import colored
from pyfiglet import Figlet
#
import sys, signal, os, socket
#
def def_handler(sig, frame):
    print("\n\n[!] Going out...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
# menu d'accueil SOC de PIKS
print("\n")
f = Figlet(font='standard')
print(colored(f.renderText('	SOC de PIKS'), 'red', attrs=['blink', 'bold']))
print(colored('	Script de Pentest codé par :', 'white'), colored('Pierre CHEREAU & Kavirajan SARAVANANE', 'cyan'))
print(colored('		Projet MSI-1-CS-B', 'white'), colored(' © ', 'red'), colored('Sup de Vinci', 'green'))
print(colored('			Happy Hacking =) ', 'yellow'))
print("\n")
while True:
    # Chercher l'adresse IP de la machine
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(colored('Votre adresse IP  est: ', 'red'), s.getsockname()[0]+'\n')
    s.close()

    # Affiche le menu principal
    print("""Choisir une catégorie:
            1 - Reconnaissance
            2 - Enumeration
            3 - Scanning & Exploitation
            4 - Recherche Exploits
            5 - Aide
            6 - Quitter
            """)
    option = input("Option: ")

    if option == "1": # Reconnaissance - menu 1.x       
    
        print("""Choisir un outil de Reconnaissance:
                1 - Maltego
                2 - Host to IP
                3 - SpiderFoot
                4 - TheHarvester
                5 - Google Dorking
                6 - Quitter\n """)
        opt1 = input("Votre choix: " )

        if opt1 == "1": # 1.1 Outil Maltego
            
            print("Maltego")
            # Install l'application Maltego
            cmd = os.system("apt install maltego > /dev/null 2>&1")
            print("Maltego Démarre dans quelques secondes .. ...  ....")
            cmd = os.system("maltego > /dev/null 2>&1")
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal
    
        elif opt1 == "2": # 1.2 Outil Host to IP
             
            print("Host to IP")
            host = input("Saisir un nom de domaine ou un hostname: ")
            ip = socket.gethostbyname(host)
            print(" %s a comme adresse IP de %s" % (host, ip))
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal
        
        elif opt1 == "3": # 1.3 Outil Spider
                           
            print("SpiderFoot")
            cmd = os.system("apt install spiderfoot > /dev/null 2>&1")
            print("SpiderFoot Démarre dans quelques secondes .. ...  ....")
            cmd = os.system("xdg-open http://127.0.0.1:5001")
            cmd = os.system("spiderfoot -l 127.0.0.1:5001 > /dev/null 2>&1") 
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal
        
        elif opt1 == "4": # 1.4 Outil TheHarvester
                           
            print("TheHarvester : Listing des employés - Linkedin")
            cmd = os.system("apt-get install theharvester > /dev/null 2>&1")
            print("Entrez le nom de domaine de l'entreprise.")
            url = input("Nom de domaine: ")
            cmd = os.system("theHarvester -d %s -l 200 -b linkedin" % url)      
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal

        elif opt1 == "5": # 1.5 Outil Google Dorking
                           
            print("Google Dorking")
            cmd = os.system("apt-get install git -y > /dev/null 2>&1")
            cmd = os.system("git clone https://github.com/IvanGlinkin/Fast-Google-Dorks-Scan.git > /dev/null 2>&1")
            cmd = os.system("chmod 777 Fast-Google-Dorks-Scan/FGDS.sh ")
            print("Entrez un nom de domaine pour faire une recherche Google dorking. Attention, une utilisation répétée peut engendrer un blocage par Google.")
            url = input("Nom de domaine: ")
            cmd = os.system("Fast-Google-Dorks-Scan/FGDS.sh %s " % url)      
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal    
            
        else:
            print("Retour au menu principal.\n\n\n")
            # Retour au menu principal
              
                
            
    elif option == "2": # Enumeration - menu 2.x 
            
          
       print("""Choisir un outil de Reconnaissance:
                            1 - Nmap
                            2 - Enumeration de sous-domaine
                            3 - Enumeration d'un site web
                            4 - Enumeration des repertoires d'un site web
                            5 - Quitter\n """)
       opt2 = input("Votre choix: " )    
    
       if opt2 == "1": # Nmap - menu 2.1.x
           
           print("""Choisir un outil:
                        1 - Scanner un réseau entier.
                        2 - Scanner les ports communs.
                        3 - Scanner les services.
                        4 - Scanner tous les ports.
                        5 - Scanner les ports TCP ouverts.
                        6 - Scanner les ports UDP ouverts.
                        7 - Effectuer un scan agressif. 
                        8 - Quitter\n """)
           opt21 = input("Votre choix: " )  
           
           if opt21 == "1":
              
            print("Scanner un réseau entier - NMAP") # 2.1.1 network scan
            cmd = os.system("apt-get install nmap > /dev/null 2>&1")
            print("Entrez le réseau à scanner. Exemple: 192.168.1.0/24")
            ip = input("IP du réseau: ")
            cmd = os.system("nmap -sP %s " % ip)
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal                  
          
           elif opt21 == "2":
                
            print("Scanner les ports - Mode rapide - NMAP") # 2.1.2 network scan
            cmd = os.system("apt-get install nmap > /dev/null 2>&1")
            print("Entrez l'adresse IP à scanner. Exemple: 192.168.1.1")
            ip = input("Adresse IP: ")
            cmd = os.system("nmap -Pn -F %s " % ip)
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal
                  
           elif opt21 == "3":
        
            print("Scanner les services - NMAP")
            cmd = os.system("apt-get install nmap > /dev/null 2>&1")
            print("Entrez l'adresse IP à scanner. Exemple: 192.168.1.1")
            ip = input("Adresse IP: ")
            cmd = os.system("nmap -sV %s " % ip)
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal            

           elif opt21 == "4":
        
            print("Scanner tous les ports - NMAP")
            cmd = os.system("apt-get install nmap > /dev/null 2>&1")
            print("Entrez l'adresse IP à scanner. Exemple: 192.168.1.1")
            ip = input("Adresse IP: ")
            cmd = os.system("nmap -p- %s " % ip)
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal

           elif opt21 == "5":
        
            print("Scanner les ports TCP ouverts - NMAP")
            cmd = os.system("apt-get install nmap > /dev/null 2>&1")
            print("Entrez l'adresse IP à scanner. Exemple: 192.168.1.1")
            ip = input("Adresse IP: ")
            cmd = os.system("nmap -sT %s " % ip)
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal

           elif opt21 == "6":
        
            print("Scanner les ports UDP ouverts - NMAP")
            cmd = os.system("apt-get install nmap > /dev/null 2>&1")
            print("Entrez l'adresse IP à scanner. Exemple: 192.168.1.1")
            ip = input("Adresse IP: ")
            cmd = os.system("nmap -sU %s " % ip)
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal

           elif opt21 == "7":
        
            print("Scan agressif - NMAP")
            cmd = os.system("apt-get install nmap > /dev/null 2>&1")
            print("Entrez l'adresse IP à scanner. Exemple: 192.168.1.1")
            ip = input("Adresse IP: ")
            cmd = os.system("nmap -A %s " % ip)
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal


           else:
                print("Retour au menu principal.\n\n\n")       
            
       elif opt2 == "2":
                                
            print("Enumeration de sous-domaine - Amass")
            print("Enumeration de sous domaine démarre dans quelques secondes ..")
            cmd = os.system("apt install amass -y > /dev/null 2>&1")
            print("Entrez le nom de domaine. Exemple: example.com")
            url = input("Nom de domaine: ")
            cmd = os.system("amass enum -d %s " % url)
            input("Appuyez sur entrée pour continuer\n\n\n")
            # Retour au menu principal
     
       elif opt2 == "3":
       
                print("Scanneur de site web - WhatWeb")
                print("Scanneur de site web/serveur démarre dans quelques secondes ..")
                cmd = os.system("apt install whatweb > /dev/null 2>&1")
                url = input("Saisir un nom de domaine à scanner: ") 
                cmd = os.system("whatweb -v %s" % url)      
                input("Appuyez sur entrée pour continuer\n\n\n")
                # Retour au menu principal
                                           
       elif opt2 == "4":
                               
               print("Enumeration de repertoire de site web")
               print("Scanneur de répertoire site web démarre dans quelques secondes ..")
               cmd = os.system("apt install dirb > /dev/null 2>&1")
               url = input("Saisir l'URL à scanner: ")
               cmd = os.system("dirb %s /usr/share/wordlists/dirb/common.txt" % url)
               input("Appuyez sur entrée pour continuer\n\n\n")
               # Retour au menu principal
               
       else:
                 print("Retour au menu principal.\n\n\n")
        
    elif option == "3": #Scan de vulnérabilité  - menu 3.x 
                             
       print("""Choisir un outil de Scanning ou Exploitation:
                             1 - Scan de vulnerabilités de serveur web
                             2 - ClickJacking testeur
                             3 - XSS scanneur
                             4 - SQL injection testeur
                             5 - CVE detection avec Nmap
                             6 - DDOS attack
                             7 - Detection de malware sur les hôtes distants
                             8 - Quitter\n """)
       opt3 = input("Votre choix: " )   


       if opt3 == "1":
                            
        
                print("Scan de vulnerabilités de serveur web - Nikto")
                print("Scanneur de vulnerabilités de serveur web démarre dans quelques secondes ..")
                cmd = os.system("apt install nikto > /dev/null 2>&1")
                url = input("Saisir une URL d'un site web à scanner: ") 
                cmd = os.system("nikto -h %s" % url)      
                input("Appuyez sur entrée pour continuer\n\n\n")
                # Retour au menu principal
                         
       elif opt3 == "2":
                            
        
                print("Votre choix est 2 - ClickJacking testeur")
                print("Clickjacking testeur démarre dans quelques secondes ..")
                cmd = os.system("apt install git > /dev/null 2>&1")
                cmd = os.system("git clone https://github.com/D4Vinci/Clickjacking-Tester.git  > /dev/null 2>&1")
                url = input("Saisir un nom de domaine à tester: ")
                cmd = os.system("echo %s > Clickjacking-Tester/url.txt" % url)
                cmd = os.system("python3 Clickjacking-Tester/Clickjacking_Tester.py Clickjacking-Tester/url.txt")      
                input("Appuyez sur entrée pour continuer\n\n\n")
                # Retour au menu principal
                                     
       elif opt3 == "3":
                            
        
                print("Votre choix est 3 - XSS scanneur - XSStrike")
                print("XSS testeur démarre dans quelques secondes ..")
                cmd = os.system("apt install git > /dev/null 2>&1")
                cmd = os.system("git clone https://github.com/s0md3v/XSStrike.git  > /dev/null 2>&1")
                url = input("Saisir l'URL à scanner: ") 
                cmd = os.system("python3 XSStrike/xsstrike.py -u %s --crawl" % url)      
                input("Appuyez sur entrée pour continuer\n\n\n")
                # Retour au menu principal
                         
       elif opt3 == "4":
                             
         
                print("Votre choix est 4 - SQL injection testeur - SQL Map")
                print("SQL injection testeur démarre dans quelques secondes ..")
                cmd = os.system("apt install git > /dev/null 2>&1")
                cmd = os.system("git clone https://github.com/sqlmapproject/sqlmap.git  > /dev/null 2>&1")
                url = input("Saisir l'URL à tester: ") 
                cmd = os.system("python3 sqlmap/sqlmap.py -u %s --batch" % url)      
                input("Appuyez sur entrée pour continuer\n\n\n")
                # Retour au menu principal                 

       elif opt3 == "5":
                             
         
                print("Votre choix est 5 - CVE detection - Nmap")
                print("CVE detection démarre dans quelques secondes ..")
                cmd = os.system("apt install nmap > /dev/null 2>&1")
                ip = input("Saisir l'adresse IP à tester: ") 
                cmd = os.system("nmap -Pn --script vuln %s " % ip)      
                input("Appuyez sur entrée pour continuer\n\n\n")
                # Retour au menu principal

       elif opt3 == "6":
                             
         
                print("Votre choix est 6 - DDOS attack - Nmap - SlowLoris")
                print("DDOS attack démarre dans quelques secondes ..")
                cmd = os.system("apt install nmap > /dev/null 2>&1")
                ip = input("Saisir l'adresse IP à attaquer: ") 
                cmd = os.system("nmap %s -max-parallelism 800 -Pn --script http-slowloris --script-args http-slowloris.runforever=true " % ip)      
                input("Appuyez sur entrée pour continuer\n\n\n")
                # Retour au menu principal

       elif opt3 == "7":
                             
         
                print("Votre choix est 7 - detection de malware sur les hôtes distants -Nmap")
                print("Détection de malware démarre dans quelques secondes ..")
                cmd = os.system("apt install nmap > /dev/null 2>&1")
                ip = input("Saisir l'IP à scanner: ") 
                cmd = os.system("nmap -sV --script=http-malware-host %s " % ip)      
                input("Appuyez sur entrée pour continuer\n\n\n")
                # Retour au menu principal
       else:
                print("Retour au menu principal.\n\n\n")
                # Retour au menu principal
        
    elif option == "4": #Recherche d'exploit 
                             
       print("Choisir un outil de Scanning ou Exploitation:")
       print("Rerchercher les exploits - Searchsploit")
       print("Recherche des exploits dans quelques secondes ..")
       cmd = os.system("apt install searchsploit > /dev/null 2>&1")
       cmd = os.system("searchsploit -u > /dev/null 2>&1")
       print("Rechercher des exploits récents et connus depuis la base de données de Exploit-DB. Exemple: Tomcat 3.1")
       exploit = input("Chercher un exploit: ") 
       cmd = os.system("searchsploit %s " % exploit)
       input("Appuyez sur entrée pour continuer\n\n\n")
       # Retour au menu principal

    elif option == "5": # Aide
                 
        print(""" Arborescence Soc de PIKS :
                1 - Reconnaissance
                    1 - Maltego
                    2 - Host to IP
                    3 - SpiderFoot
                    4 - TheHarvester
                    5 - Google Dorking
                2 - Enumeration
                    1 - Nmap
                        1 - Scanner un réseau entier.
                        2 - Scanner les ports communs.
                        3 - Scanner les services.
                        4 - Scanner tous les ports.
                        5 - Scanner les ports TCP ouverts.
                        6 - Scanner les ports UDP ouverts.
                        7 - Effectuer un scan agressif.
                    2 - Enumeration de sous-domaine
                    3 - Enumeration d'un site web
                    4 - Enumeration des repertoires d'un site web
                3 - Scanning & Exploitation
                    1 - Scan de vulnerabilités de serveur web
                    2 - ClickJacking testeur
                    3 - XSS scanneur
                    4 - SQL injection testeur
                    5 - CVE detection avec Nmap
                    6 - DDOS attack
                    7 - Detection de malware sur les hôtes distants
                4 - Recherche Exploits
                5 - Aide
                6 - Quitter
                            """)
        input("Appuyez sur entrée pour continuer\n\n\n")
        # Retour au menu principal
     
    elif option == "6": # Quitter
    
        print("Au revoir et à bientôt =)")
        sys.exit(0)
    # Si choix=invalide, alors: message + retour au menu principal 
    else:
        print("Choix invalide. S'il vous plait choissisez parmis les options de 1 à 6.\n\n\n")
