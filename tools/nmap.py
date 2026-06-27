#Imports

import nmap3
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime
from colorama import Fore

#Variables
nmap = nmap3.Nmap()
webhookurl = 'REDACT'
embed = DiscordEmbed(title="ISPY TOOL", description=f"SCAN RESULT: {datetime.datetime.now()}", color="03b2f8")
global hostname, IPaddress, separation

#Functions

def nmapdns(target):
    print(Fore.GREEN + '[+] Running NMAP DNS scan\n')
    dns_results = nmap.nmap_dns_brute_script(target)
    print(Fore.GREEN + '[+] Sorting NMAP DNS scan\n')
    for item in dns_results:
        hostname = ('[+] Hostname: ' + item['hostname'])
        print(hostname)
        IPaddress = ('[+] IP Address: ' + item['address'] + '\n')
        print(IPaddress)
        separation = ('-----------------------')
        print(Fore.GREEN + f'[+] Sending NMAP DNS scan over webhook: {webhookurl}\n')
        webhook = DiscordWebhook(url=webhookurl, content=hostname + IPaddress + separation)
        webhook.add_embed(embed)
        webhook.execute()

def nmapversion(target):
    version_results = nmap.nmap_version_detection(target)
    ip_address = next(iter(version_results))
    version = version_results[ip_address]
    for port in version['ports']:
        print('[+] Protocol: ' + port['protocol'])
        print('[+] Port: ' + port['portid'])
        print('[+] State: ' + port['state'])
        print('[+] Name: ' + port['service']['name'])
        print('-----------------------')


def nmaptopports(target):
    top_ports = nmap.scan_top_ports(target)
    ports_results = next(iter(top_ports))
    port = top_ports[ports_results]
    for port in port['ports']:
        print('[+] Port: ' + port['portid'])
        print('[+] Protocol: ' + port['protocol'])
        print('[+] State: ' + port['state'])
        print('[+] Service: ' + port['service']['name'])
        print('-----------------------')


def nmapos(target):
    os_results = nmap.nmap_os_detection(target)
    ip_address = next(iter(os_results))
    os_version = os_results[ip_address]
    for item in os_version['osmatch']:
        print('[+] OS: ' + item['name'])
        print('[+] Family: ' + item['osclass']['osfamily'])
        print('[+] Type: ' + item['osclass']['type'])
        print('[+] Generation: ' + item['osclass']['osgen'])
        print('[+] Accuracy: ' + item['accuracy'])
        print('-----------------------')