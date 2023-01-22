import random
import os
import threading
import requests
import win32console as wc
import colorama
from colorama import Fore
colorama.init()

while True:
    os.system("cls")
    wc.SetConsoleTitle("discord Dev wiss#7258")
    genorcheck = input(f"{Fore.BLUE}> Generate or Check? (g/c): {Fore.RED}")

    def generate():
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWYYZ"
        numbers = "0123456789"

        amount = int(input(f"{Fore.BLUE}> Amount to Generate: {Fore.RED}"))
        upper, lower, nums = True, True, True
        all = ""

        if upper:
            all += uppercase
        if lower:
            all += lowercase
        if nums:
            all += numbers

            count = 0
            length = 16
            n = open('nitros.txt', 'w+')
            for x in range(amount):
                code = "".join(random.sample(all, length))
                n.write(code + "\n")
                count += 1
                print(f"{Fore.RED}{code}{Fore.BLUE} | Code Written ({Fore.RED}nitros.txt{Fore.BLUE}){Fore.RED} - x{count}{Fore.BLUE}/{Fore.RED}{amount}{Fore.BLUE}")
    vc = open("validcodes.txt", "w")
    def check():
        with open("nitros.txt", "r") as nitrofile:
            nitros = nitrofile.read().split("\n")
        nitrofile.close()
        count = 0
        with open("validcodes.txt", "w+") as vc:
            for i in range(len(nitros)):
                nitro = nitros[i]
                try:
                    checkurl = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}")
                    if checkurl.status_code not in [200, 201, 204]:
                        requests.post(webhook_url, json={"content": f"https://discord.gift/{nitro}", "username": "Nitro Checker - dsc.gg/devs"})
                        count += 1
                        vc.write(nitro + "\n")
                        print(f"{Fore.BLUE}[+] {Fore.RED}{nitro}{Fore.BLUE} | Valid Code{Fore.RED} - x{count}{Fore.BLUE}/{Fore.RED}{len(nitros)-1}")
                    else:
                        count+=1
                        print(f"{Fore.BLUE}[-] {Fore.RED}{nitro}{Fore.BLUE} | Invalid Code{Fore.RED} - x{count}{Fore.BLUE}/{Fore.RED}{len(nitros)-1}")
                except:
                    pass

    # def scrapeproxies():
    #     input(f"{Fore.BLUE}> Press ENTER To Scrape HTTP Proxies")
    #     url = requests.get("https://api.openproxylist.xyz/http.txt")
    #     urlresult = url.text
    #     linecount = 0
    #     with open('proxies.txt', 'w') as proxyscrapelist:
    #         proxyscrapelist.write(urlresult)
    #         file = open('proxies.txt')
    #         for line in file:
    #             if line != "\n":
    #                 linecount += 1
    #         print(f"{Fore.BLUE}[+] Scraped {Fore.RED}{linecount}{Fore.BLUE} Proxies ({Fore.RED}proxies.txt{Fore.BLUE})")
    #         file.close()
    #         input(f"{Fore.BLUE}> Press ENTER To Start Checking")

    if genorcheck == "g":
        generate()
    if genorcheck == "c":
        webhook_url = input(f"{Fore.BLUE}\n> Webhook URL (valid codes will be sent to webhook): {Fore.RED}")
        threading.Thread(target=check).start()