import requests
from colorama import Fore
from bs4 import BeautifulSoup
import os

def logo():
    a = f"""{Fore.RED}
    ███╗   ███╗ ██████╗███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
    ████╗ ████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██╔████╔██║██║     ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
    ██║╚██╔╝██║██║     ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
    ██║ ╚═╝ ██║╚██████╗███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
    ╚═╝     ╚═╝ ╚═════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                           
 [{Fore.BLUE}+{Fore.RED}] https://github.com/hypostat1c [{Fore.BLUE}+{Fore.RESET}]
"""
    print(a)

def skins():
    print('\n' + f'{Fore.GREEN}[+] Skins [+]\n' + Fore.RESET)
    content = soup.find_all('a', href=True)
    if not os.path.isdir(pseudomc):
        os.mkdir(pseudomc)
    for tag in content:
        if "/skin" in tag['href']:
            skin_id = tag['href'].split("/")[-1]
            img = requests.get("https://fr.namemc.com/texture/" + skin_id).content
            with open(pseudomc + "/" + skin_id + ".png", "wb") as handler:
                handler.write(img)
    print(f'{Fore.RED}Check in path > /' + pseudomc)

def old_nicknames():
    a = soup.find('main', attrs={'class': 'container'})
    content = a.find_all('a', attrs={'translate': 'no'})
    final = str(content).replace(',', '').replace('[', '').replace('<a href="/name/', '').replace(']', '').replace('"', '').replace('translate=no>', '').replace('</a>', '').replace('</a>]', '')
    arr = final.split()
    arr = list(set(arr))
    result = str(arr).replace('[', '').replace(']', '').replace("'", '').replace(', ', ' - ')
    print(Fore.BLUE + "\n[+] Old nicknames [+]\n\n" + Fore.RED + result + '\n')

def menu():
    logo()
    global pseudomc
    print(f'{Fore.RED}')
    pseudomc = input('[+] Pseudo [+] : ')
    print(f'{Fore.RESET}')
    if len(pseudomc) <= 2 or len(pseudomc) > 16:
        print(Fore.RED + "\n[+] Nothing found [+]" + Fore.RESET)
        exit()
    req = requests.get("https://fr.namemc.com/profile/" + pseudomc + ".1")
    page = req.content
    global soup
    soup = BeautifulSoup(page, features="lxml")
    old_nicknames()
    skins()

menu()
