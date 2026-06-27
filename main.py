# Imports

import os
import time
import datetime
from logging import exception
from discord_webhook import DiscordWebhook
import requests
from colorama import Fore
from tools import nmap
import subprocess

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

def main():
    os.system('clear')
    print(banner)
    target = input('\n[+] Target URL: ')
    try:
        nmap.nmapdns(target)
    except TypeError as e:
        print(e)
main()
