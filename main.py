# Imports

import os
import datetime
import logging
import sys

from colorama import Fore
from tools import nmap, whois, setup, nuclei

#Variables
# @TODO need to make the logger actually handle data.
LOGGER = logging.getLogger('logs.log')
if not os.path.exists('logs'):
    os.mkdir('logs')
    logging.basicConfig(filename='logs/logs.log')
time = datetime.datetime.now()
banner = (Fore.RED + f'''                                                                      
                                                                      
IIIIIIIIII   SSSSSSSSSSSSSSS PPPPPPPPPPPPPPPPP   YYYYYYY       YYYYYYY
I::::::::I SS:::::::::::::::SP::::::::::::::::P  Y:::::Y       Y:::::Y
I::::::::IS:::::SSSSSS::::::SP::::::PPPPPP:::::P Y:::::Y       Y:::::Y
II::::::IIS:::::S     SSSSSSSPP:::::P     P:::::PY::::::Y     Y::::::Y
  I::::I  S:::::S              P::::P     P:::::PYYY:::::Y   Y:::::YYY
  I::::I  S:::::S              P::::P     P:::::P   Y:::::Y Y:::::Y   
  I::::I   S::::SSSS           P::::PPPPPP:::::P     Y:::::Y:::::Y    
  I::::I    SS::::::SSSSS      P:::::::::::::PP       Y:::::::::Y     
  I::::I      SSS::::::::SS    P::::PPPPPPPPP          Y:::::::Y      
  I::::I         SSSSSS::::S   P::::P                   Y:::::Y       
  I::::I              S:::::S  P::::P                   Y:::::Y       
  I::::I              S:::::S  P::::P                   Y:::::Y       
II::::::IISSSSSSS     S:::::SPP::::::PP                 Y:::::Y       
I::::::::IS::::::SSSSSS:::::SP::::::::P              YYYY:::::YYYY    
I::::::::IS:::::::::::::::SS P::::::::P              Y:::::::::::Y    
IIIIIIIIII SSSSSSSSSSSSSSS   PPPPPPPPPP              YYYYYYYYYYYYY    
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      {time}\n''')

#Functions

def setupcheck():
    if os.path.exists('config_files/settings.ini'):
        return
    else:
        print(Fore.GREEN + '[!] settings.ini does not exist. Running setup...')
        setup.setup()
        main()

def main():

    if sys.platform == "Linux":
        os.system('clear')
    elif sys.platform == "Windows":
        os.system('cls')
    elif sys.platform == "Darwin":
        os.system('clear')

    setupcheck()
    print(banner)
    target = input('\n[+] Target URL: ')
    if target == '':
        print('[!] Target URL must not be empty')
    else:
        try:
            # OSINT
            whois.whoisscan(target)
            print('\n')

            # Scan for services and their respective information
            nmap.nmapversion(target)
            print('\n')

            # Get intel on the top 1000 ports
            nmap.nmaptopports(target)
            print('\n')

            # Check DNS
            nmap.nmapdns(target)
            print('\n')

            # Vulnerability Scan
            nuclei.nucleiscan(target)
            print('\n[+] Scans completed')

            # Moved exit to ensure full execution, error handling included
        except ModuleNotFoundError as  m:
            logging.log(logging.ERROR, f'Module: {m} failed to load!') # Track module errors
        except Exception as e:
            logging.log(logging.ERROR, f'General error: {e}') # General error catch
        finally:
            exit()

if __name__ == '__main__':
    main()
    exit()
