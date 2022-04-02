import os
from colorama import init, Fore
from time import sleep
import csv
import time
import random
import os
import pickle
import sys
scam = '@notoscam'
init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.LIGHTGREEN_EX
w = Fore.LIGHTGREEN_EX
cy = Fore.LIGHTGREEN_EX
ye = Fore.LIGHTGREEN_EX
gr = Fore.LIGHTGREEN_EX
colors = [lg, lg, lg, lg, lg, lg]

os.makedirs("sessions")

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    

  
    '██╗  ██╗██╗███╗   ██╗██████╗ ███████╗██╗   ██╗██╗██╗     ███████╗' ,
    '██║ ██╔╝██║████╗  ██║██╔══██╗██╔════╝██║   ██║██║██║     ██╔════╝' ,
    '█████╔╝ ██║██╔██╗ ██║██║  ██║█████╗  ██║   ██║██║██║     ███████╗' ,
    '██╔═██╗ ██║██║╚██╗██║██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║     ╚════██║' ,
    '██║  ██╗██║██║ ╚████║██████╔╝███████╗ ╚████╔╝ ██║███████╗███████║' ,
    '╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝╚══════╝' ,
 


    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    print(f'{r}   {r}')
    print(f'{r} Channel: @kindevilsorg{r}')
    print(f'{cy} Group : @kindevils{cy}')
    print(f'{r}   {r}')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
while True:
    clr()
    banner()
    print(ye+'Choose an Option:'+n)
    print(cy+'            [1] Setup Script'+n)
    print(cy+'            [2] Exit'+n)
    a = int(input('\n Enter your choice: '))
    if a == 1:
    
       print("[+] Installing requierments ...")
       os.system('pip install telethon==1.24.0')
       os.system('pip install colorama==0.4.3')

       print("[+] setup complete !")
       print("[+] now you can run any tool !")
       input(f'\n Press enter to goto main menu...')
       
    if a == 2:
        clr()
        banner()
        exit()
