import os
from colorama import Fore
from configparser import ConfigParser
config = ConfigParser()

def setup():

    whois = config.get("SETTINGS","WHOIS_webhook")
    NMAP = config.get("SETTINGS","NMAP_webhook")
    Nuclei = config.get("SETTINGS","Nuclei_webhook")
    config_file = 'config_files/settings.ini'
    if os.path.exists(config_file):
        with open(config_file, 'w') as f:
            config.add_section('SETTINGS')
            f.writelines('[SETTINGS]\n')

            config.set('SETTINGS','whois_webhook',whois)
            f.writelines(f'WHOIS_webhook = "{whois}"\n')

            config.set('SETTINGS','NMAP_webhook',NMAP)
            f.writelines(f'NMAP_webhook = "{NMAP}"\n')

            config.set('SETTINGS','Nuclei_webhook',Nuclei)
            f.writelines(f'Nuclei_webhook = "{Nuclei}"\n')

            f.close()
            return config.items('SETTINGS')
    else:
        if not os.path.abspath(config_file):
            os.mkdir('../config_files')
            settings_file = open(config_file, 'c')
            settings_file.write(config_file)
            config_file.format(settings_file)
            print(settings_file)
            return settings_file
        return None

if __name__ == "__main__":
    setup()