# Written by Nulled_Ash
# Imports

import os
from colorama import Fore
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
import datetime
from configparser import ConfigParser

# Variables

config = ConfigParser()
config.read('../settings.ini')
nuclei_webhookurl = (config.get('SETTINGS','nuclei_webhook'))
webhook = DiscordWebhook(url=nuclei_webhookurl)


def nucleiscan(target):
    separator = '-----------------------\n'
    print(Fore.GREEN + f"[+] Running Nuclei scan against: {target}...\n")
    if not target.startswith('http'):
        target = f'http://{target}'
        os.system(f'''proxychains4 nuclei -u {target} -sa -as -o nuclei_results.txt''')
        print(f'[+] Sending scan over {nuclei_webhookurl}')
        with open('nuclei_results.txt', 'r') as file:
            results = file.read()
            embed = DiscordEmbed(title=f'[+] SCAN RESULT: {datetime.datetime.now()}\n[+] Target: {target}',
                                 description='[+] Nuclei module' + f'\n{results}', color="03b2f8")
            webhook.add_embed(embed)
            webhook.execute()
        os.system('rm nuclei_results.txt')
        print(f'[+] Report sent' + f'\n{separator}')
    else:
        os.system(f'''proxychains4 nuclei -u {target} -sa -as -o nuclei_results.txt''')
        print(f'[+] Sending scan over {nuclei_webhookurl}')
        with open('nuclei_results.txt', 'r') as file:
            results = file.read()
            embed = DiscordEmbed(title=f'[+] SCAN RESULT: {datetime.datetime.now()}\n[+] Target: {target}',
                                 description='[+] Nuclei module' + f'\n{results}', color="03b2f8")
            webhook.add_embed(embed)
            webhook.execute()
        os.system('rm nuclei_results.txt')
        print(f'[+] Report sent' + f'\n{separator}')