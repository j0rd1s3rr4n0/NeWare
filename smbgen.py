import os
import time
import sys
#Genera Llista d'usuaris
os.system('cat /etc/passwd | grep "administracio1" -A 9999 | cut -d ":" -f1 | tr "\n" " " > users.txt')
#Llegeix Contingut de l'arxiu i ho emmagatzema com a una cadena de text

with open('users.txt') as f:
    lines = f.readlines()

with open('pass.txt') as g:
    gines = g.readlines()

gine = str(gines[0])
line = str(lines[0])

userlist = line.split()
passlist = gine.split()

a = 0
#os.system('sudo su')
for x in userlist:
        time.sleep(1)
        awd = ('echo "'+passlist[int(a)]+'\\n'+passlist[int(a)]+'" | sudo smbpasswd -a -s '+userlist[int(a)])
        #print(awd)
        os.system(awd)
        a+=1
