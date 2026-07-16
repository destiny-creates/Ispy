# Imports

import os
import datetime
from colorama import Fore
from tools import nmap
from tools import nuclei
from tools import whois
from tools import setup

#Variables

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
    print(banner)
    if os.path.exists('settings.ini'):
        main()
    else:
        print(Fore.GREEN + '[!] settings.ini does not exist. Running setup...')
        setup.setup()
        main()

def main():
    os.system('clear')
    print(banner)
    target = input('\n[+] Target URL: ')
    try:
        whois.whoisscan(target)
        print('\n')
        nmap.nmapversion(target)
        print('\n')
        nmap.nmaptopports(target)
        print('\n')
        nuclei.nucleiscan(target)
        print('\n[+] Scans completed')
        exit()
    except Exception as e:
        print(e)

setupcheck()
