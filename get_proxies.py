from platform import system as iden
from bs4 import BeautifulSoup
from random import choice
from colorama import Fore
from requests import get
from sys import argv
c = Fore.CYAN
g = Fore.GREEN
w = Fore.WHITE
r = Fore.RED
if iden() != "Windows":
 from readline import parse_and_bind
 parse_and_bind('tab:complete')
def banner():
 colors = [w , r , g , c]
 print (f"""{choice(colors)}          
                                     _           
                                    (_)          
                _ __  _ __ _____  ___  ___ _ __ 
                | '_ \| '__/ _ \ \/ / |/ _ \ '__|
                | |_) | | | (_) >  <| |  __/ |   
                | .__/|_|  \___/_/\_\_|\___|_|   
                | |                              
                |_|                              

			Coded By : Ali Mansour""")

def get_proxies():
    names = ['http' , 'socks4' , 'socks5']
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"}
    html_doc = get("https://free-proxy-list.net/")
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    ip = ''
    f_r = open("proxies-list_all.txt" , 'a')
    f_r1 = open("proxies-list_socks4.txt" , 'w')
    f_r2 = open("proxies-list_socks5.txt" , 'w')
    f_r3 = open("proxies-list_http.txt" , 'w')
    for ip_d in soup.find_all("td"):
        if "mins" in ip_d.text:
            continue
        if ip_d.text.count('.') > 2:
            ip += ip_d.text
        if ip_d.text.isnumeric():
            if ip != '':
                ip += ':' + str(ip_d.text)
                print (f'{w}[{g}+{w}] {c}{ip}')
                f_r.write(ip + '\n')
            ip = ''
    f_r.write(get("https://api.proxyscrape.com/v2/?request=getproxies").text)
    req = get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http")
    req2 = get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4")
    req3 = get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5")
    f_r1.write(req2.text)
    f_r2.write(req3.text)
    f_r3.write(req.text)
    f_r.close()
    f_r1.close()
    f_r2.close()
    f_r3.close()
def addToProxtchain():
    f_r1 = open("proxies-list_socks4.txt" , 'r')
    f_r2 = open("proxies-list_socks5.txt" , 'r')
    f_r3 = open("proxies-list_http.txt" , 'r')
    with open("/etc/proxychains.conf" , 'a') as f_a:
        for socks4 in f_r1.readlines():
            socks4 = socks4.rstrip()
            f_a.write(f"socks4 {socks4.split(':')[0]} {socks4.split(':')[1]}\n")
        for socks5 in f_r2.readlines():
            socks5 = socks5.rstrip()
            f_a.write(f"socks5 {socks5.split(':')[0]} {socks5.split(':')[1]}\n")
        for http in f_r3.readlines():
            http = http.rstrip()
            f_a.write(f"http {http.split(':')[0]} {http.split(':')[1]}\n")
    print (f"{w}[{g}+{w}] {r}Added To /etc/proxychains.conf Successfully")
banner()
if len(argv) == 1:
    print ('Usages:')
    print ("""
-n Number Of Function

Example:

1. ./{0} -n 1  -> Fetch All Fresh proxies
2. ./{0} -n 2  -> Add This Proxies to /etc/proxychains.conf
3. ./{0} -n 3  -> All Of Them

""".format(argv[0]))
else:
    try:
        if "-n" in argv[1:]:
            number = str(argv[argv.index('-n')+1])
        if "-n" not in argv[1:]:
            exit(f"{w}[{r}!{w}] Number Not Inserted")
        if number == '1':
             get_proxies()
        elif number == '2':
            addToProxtchain()
        elif number == '3':
            get_proxies()
            addToProxtchain()
        else :
            exit (f"{w}[{r}!{w}] Incorrect Select")
    except Exception as e:
        print (e)
