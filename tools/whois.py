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
whois_webhookurl = (config.get('SETTINGS','whois_webhook'))
webhook = DiscordWebhook(url=whois_webhookurl)

def whoisscan(target):
    separator = '-----------------------\n'
    print(Fore.GREEN + f"[+] Running WHOIS scan against: {target}...\n")
    os.system(f'''proxychains4 whois {target} > whois.txt''')
    print(f'[+] Sending scan over {whois_webhookurl}')
    with open('whois.txt', 'r') as file:
        results = file.read()
        embed = DiscordEmbed(title=f'[+] SCAN RESULT: {datetime.datetime.now()}\n[+] Target: {target}',
                             description='[+] WHOIS module' + f'\n{results}', color="03b2f8")
        webhook.add_embed(embed)
        webhook.execute()
    os.system(f'''rm whois.txt''')
    print(f'[+] Report sent' + f'\n{separator}')