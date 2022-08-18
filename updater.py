import subprocess
from urllib.request import urlopen
import banners
import time
from colorama import init
from colorama import Fore, Back, Style

def update_client_version(version):
    with open("version.txt", "r") as vnum:
        vers = vnum.read()
        if vnum.read() != version:
            return True
            vers.replace('\n','')
            vers.replace('\r','')
            first, second = vers.split('.')
            if second != 9:
                with open("version.txt", "w") as j:
                    j.write(f'{first}.{second}')
            else:
                second = 0
                first += 1
                with open("version.txt", "w") as j:
                    j.write(f'{first}.{second}')
        else:
            return False

def main():
    try:
        version = urlopen("https://raw.githubusercontent.com/httpshotmaker/technowlogger_with_cryptor/master/version.txt").read()
    except Exception as e:
        print(f"{Fore.RED}[!] Unable to Fletch Origin version.txt")
        print("[!] Please Check Your Internet Connection!")
        print("[*] Exiting ...")
        quit()
        
    if update_client_version(version) is True:
        subprocess.call(["git", "pull", "origin", "master"])
        return f"{Fore.GREEN}[+] Updated to latest version: v{version}.."
    else:
        return f"{Fore.GREEN}[*] You are already up to date with git origin master :)"


if __name__ == '__main__':
    print(f'{Fore.RED}')
    print(banners.get_banner())
    print("\t\tAuthor: httpshotmaker | Github: github.com/httpshotmaker\n")
    print("[*] Welcome to Technowlogger's Auto Updater")
    print("[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]")
    print(f"{Fore.GREEN}[*] Please Note : Git must be installed in order to use \"updater.py\"")
    time.sleep(5)
    print("[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]")
    print(f"{Fore.YELLOW}[*] Checking Technowlogger's version information..")
    print(main())
    print("[*] Exiting ...")
