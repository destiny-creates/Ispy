#Imports

import nmap3
import requests
from discord_webhook import DiscordWebhook

#Variables
nmap = nmap3.Nmap()
webhookurl = 'REDACTED'

#Functions

def nmapdns(target):
    dns_results = nmap.nmap_dns_brute_script(target)
    for item in dns_results:
        print('[+] Hostname: ' + item['hostname'])
        print('[+] IP Address: ' + item['address'] + '\n')
        print('-----------------------')
    webhook = DiscordWebhook(url=webhookurl, content=f'''[+] Hostname: ' + item['hostname']''')
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