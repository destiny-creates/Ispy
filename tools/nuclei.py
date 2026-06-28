# Written by Nulled_Ash
# Imports

import os
from colorama import Fore
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
import datetime

# Variables
webhookurl = 'REDACTED'
webhook = DiscordWebhook(url=webhookurl)


def nucleiscan(target):
    print(Fore.GREEN + f"[+] Running Nuclei scan against: {target}...\n")
    if not target.startswith('http'):
        target = f'http://{target}'
        os.system(f'''nuclei -u {target} -sa -as -o nuclei_results.txt''')
        print(f'[+] Sending scan over {webhookurl}')
        with open('nuclei_results.txt', 'r') as file:
            results = file.read()
            embed = DiscordEmbed(title=f'[+] SCAN RESULT: {datetime.datetime.now()}\n[+] Target: {target}',
                                 description='[+] Nuclei module' + f'\n{results}', color="03b2f8")
            webhook.add_embed(embed)
            webhook.execute()
    else:
        os.system(f'''nuclei -u {target} -sa -as -o nuclei_results.txt''')
        print(f'[+] Sending scan over {webhookurl}')
        with open('nuclei_results.txt', 'r') as file:
            results = file.read()
            embed = DiscordEmbed(title=f'[+] SCAN RESULT: {datetime.datetime.now()}\n[+] Target: {target}',
                                 description='[+] Nuclei module' + f'\n{results}', color="03b2f8")
            webhook.add_embed(embed)
            webhook.execute()
