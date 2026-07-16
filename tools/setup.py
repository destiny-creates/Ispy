from colorama import Fore
from configparser import ConfigParser
config = ConfigParser()

def setup():
    whois = input(Fore.GREEN + '[+] Whois Discord webhook URL:')
    NMAP = input(Fore.GREEN + '[+] NMAP Discord webhook URL:')
    Nuclei = input(Fore.GREEN + '[+] Nuclei Discord webhook URL:')
    config.add_section('SETTINGS')
    config.set('SETTINGS', 'whois_webhookurl', whois)
    config.set('SETTINGS', 'nmap_webhook', NMAP)
    config.set('SETTINGS', 'nuclei_webhook', Nuclei)
    with open("settings.ini", 'w') as file:
        config.write(file)