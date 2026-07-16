#Imports

import nmap3
from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime
from colorama import Fore
from configparser import ConfigParser

#Variables
nmap = nmap3.Nmap()
config = ConfigParser()
config.read('../settings.ini')
nmap_webhookurl = (config.get('SETTINGS','nmap_webhook'))
webhook = DiscordWebhook(url=nmap_webhookurl)

#Functions

# This definition takes too long to scan, looking into why, so temporarily commented out.
# def nmapdns(target):
#     print(Fore.GREEN + '[+] Running NMAP DNS scan\n')
#     dns_results = nmap.nmap_dns_brute_script(target)
#     results = ''
#     separator = '-----------------------\n'
#     webhook = DiscordWebhook(url=nuclei_webhook)
#     for item in dns_results:
#         hostname = '[+] Hostname: ' + item['hostname']
#         IPaddress = '[+] IP Address: ' + item['address'] + '\n'
#         results += hostname + IPaddress
#     results += separator
#     print(results)
#     print(f'[+] Sending scan over {nuclei_webhook}')
#     embed = DiscordEmbed(title=f'[+] SCAN RESULT: {datetime.datetime.now()}\n[+] Target: {target}',
#                          description='[+] NMAP DNS module' + f'\n{results}', color="03b2f8")
#     webhook.add_embed(embed)
#     webhook.execute()
#     print('[+] Report sent')

def nmapversion(target):
    print(Fore.GREEN + '[+] Running NMAP version scan\n')
    version_results = nmap.nmap_version_detection(target)
    ip_address = next(iter(version_results))
    version = version_results[ip_address]
    results = ''
    separator = '-----------------------\n'
    for port in version['ports']:
        if not port['state'] == 'open':
            pass
        else:
            versionprotocol = '[+] Protocol: ' + port['protocol']
            versionport = ' Port: ' + port['portid']
            versionstate = ' State: ' + port['state']
            versionname = ' Name: ' + port['service']['name']
            results += versionprotocol + versionport + versionstate + versionname + '\n'
    print(results)
    print(f'[+] Sending scan over {nmap_webhookurl}')
    embed = DiscordEmbed(title=f'[+] SCAN RESULT: {datetime.datetime.now()}\n[+] Target: {target}',
                         description='[+] NMAP version module' + f'\n{results}', color="03b2f8")
    webhook.add_embed(embed)
    webhook.execute()
    print(f'[+] Report sent' + f'\n{separator}')


def nmaptopports(target):
    print(Fore.GREEN + '[+] Running NMAP top ports scan\n')
    top_ports = nmap.scan_top_ports(target)
    ports_results = next(iter(top_ports))
    port = top_ports[ports_results]
    results = ''
    separator = '-----------------------\n'
    for port in port['ports']:
        if not port['state'] == 'open':
            pass
        else:
            portnum = '[+] Port: ' + port['portid']
            portprotocol = ' Protocol: ' + port['protocol']
            portstate = ' State: ' + port['state']
            portservice = ' Service: ' + port['service']['name']
            results += portnum + portprotocol + portstate + portservice +'\n'
    print(results)
    print(f'[+] Sending scan over {nmap_webhookurl}')
    embed = DiscordEmbed(title=f'[+] SCAN RESULT: {datetime.datetime.now()}\n[+] Target: {target}', description='[+] NMAP top ports module' + f'\n{results}', color="03b2f8")
    webhook.add_embed(embed)
    webhook.execute()
    print(f'[+] Report sent' + f'\n{separator}')

