#!/bin/bash

echo -e "Mise à jour de système encours .. ...\n"
apt update -y > /dev/null 2>&1
apt upgrade -y > /dev/null 2>&1

echo -e "Installation de Python 3 encours .. ...\n"
apt install python3 -y > /dev/null 2>&1

echo -e "Installation de pip encours .. ...\n"
apt install pip -y > /dev/null 2>&1

echo -e "Suppresion des packages inutiles des updates ..\n"
apt autoremove -y > /dev/null 2>&1

echo -e "Installation des libraires python de SOC de PIKS encours .. ...\n"
pip install -r requirements.txt > /dev/null 2>&1

echo -e "Tout est bien terminée =)"
echo -e "Maintenant, vous pouvez aussi lancer le script avec 'sudo python3 SOC_DE_PIKS.py' si, le script n'est pas lancé.\n"

sudo python3 SOC_DE_PIKS.py
