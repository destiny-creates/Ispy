# Written by Nulled_Ash
# Imports

import os
import subprocess
import json

from colorama import Fore
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
import datetime
from configparser import ConfigParser

# Variables

nuclei_file = 'config_files/nuclei_results.json'
# if not os.path.exists(nuclei_file):
#     os.system(f'touch {nuclei_file}')
# else:
#     with open(nuclei_file) as nf:
#         if len(nf.read()) <= 0:
#             os.system("echo  '{}' > config_files/nuclei_results.json")
#             json.load(nf)
#         else:
#             nuclei_results = json.load(nf)
#             nuclei_results = nuclei_results['dns','waf','dmarc','spf','http']
#             print(nuclei_results)

def find_nuclei():
    paths = [
        '/usr/local/nuclei'
    ]
    for p in paths:
        if os.path.exists(p):
            print(p)
            return p
    return 'nuclei not found, please install.'


config = ConfigParser()
config.read('config_files/settings.ini')
nuclei_webhook = (config.get('SETTINGS', 'Nuclei_webhook'))
webhook = DiscordWebhook(url=nuclei_webhook)

def load_nuclei_json(path):
    try:
        with open(path, "r") as f:
            lines = f.read().strip().splitlines()

            # JSONL format (multiple JSON objects)
            if len(lines) > 1:
                return [json.loads(line) for line in lines]

            # Single JSON object
            return json.loads(lines[0])

    except Exception as e:
        return {"error": f"Nuclei returned non‑JSON output: {e}"}


def nucleiscan(target):
    separator = '-----------------------\n'
    print(Fore.GREEN + f"[+] Running Nuclei scan against: {target}...\n")

    # Normalize target
    if not target.startswith("http"):
        target = f"https://{target}"

    # Ensure temp file exists
    if not os.path.exists(nuclei_file):
        open(nuclei_file, "w").close()

    # Run nuclei (JSONL supported on older versions)
    cmd = f'proxychains4 nuclei -target {target} -jsonl -o {nuclei_file}'
    subprocess.run(cmd, shell=True)

    # Load results
    results = load_nuclei_json(nuclei_file)

    # Save results to config_files
    with open('config_files/nuclei_results.json', 'w') as out:
        json.dump(results, out, indent=4)

    # Prepare JSON text
    pretty = json.dumps(results, indent=2)
    if len(pretty) > 4000:
        pretty = pretty[:4000] + "\n... (truncated)"

    # Build embed
    embed = DiscordEmbed(
        title=f'[+] SCAN RESULT: {datetime.datetime.now()}\n[+] Target: {target}',
        description=f'[+] Nuclei module\n```json\n{pretty}\n```',
        color="03b2f8"
    )

    # Send
    webhook = DiscordWebhook(url=nuclei_webhook)
    webhook.add_embed(embed)
    response = webhook.execute()

    print(f"[+] Webhook response: {response.status_code}")

    # Cleanup
    os.remove(nuclei_file)
    print(f'[+] Report sent\n{separator}')
