import os

stream = os.popen('netsh wlan show profile') #cmd command to show connected networks
networklist = stream.read()#reading output of cmd
networklist = networklist.split(":") #splitting to narrow down wifi names    
wifilist = list(map(lambda x:x[:x.index("\n")].strip(),networklist[2:]))   #stripping excess chars and just extracting wifi names
print(wifilist) 
passlist = {} #dictionary to hold wifiname:wifipassword
for i in wifilist: #iterates through wifi names list 
    stream = os.popen('netsh wlan show profile name="{}" key="clear"'.format(i)) #cmd command to view password
    passli = stream.read()#reading output of cmd
    passli = passli.split("Key Content            :") #splitting to narrow down password 
    passlist[i]=(list(map(lambda x:x[:x.index("\n")].strip(),passli[1:]))[0])#stripping excess chars and extracting only password
    #appending to the dictionary with wifiname and password
print(passlist) #printing output in console
f = open("wifipass.txt","w+") #saves in default directory 
f.write(str(passlist)) #converting to string to save to text file
f.close()




