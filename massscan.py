import os
import sys
from subprocess import call
ans=True
while ans:
    print("""
    1. Scan 1 lst
    2. Scan 2 lst
    3. Scan 3 lst
    4. Exit/Quit
    """)
    ans=raw_input("Cosa Vuoi Fare? ")
    if ans=="1":
	  call(["clear"])
	  os.system("ls *.lst")
	  lista1 = raw_input('nome lista 1: ')
	  os.system("screen -S Scan1 zmap -p22 -w {0}.lst  -o mfu.txt -B100M".format(lista1))
	  call(["clear"])
	  os.system("screen -S Update1 ./update 1500")
	  call(["clear"])
	  os.system("screen -S Slump1 perl slump.pl vuln.txt")
	  call(["clear"])
    elif ans=="2":
	  #input
	  os.system("ls *.lst")
	  lista1 = raw_input('nome lista 1: ')
	  os.system("ls *.lst")
	  lista2 = raw_input('nome lista 2: ')
	  #lista 1
	  call(["clear"])
	  os.system("screen -S Scan1 zmap -p22 -w {0}.lst  -o mfu.txt -B100M".format(lista1))
	  #lista 2
	  os.system("screen -S Scan2 zmap -p22 -w {0}.lst  -o /root/scan/2/mfu.txt -B100M".format(lista2))
	  call(["clear"])
	  #Update 1
	  os.system("screen -S Update1 ./update 1500")
	  call(["clear"])
	  #Slump 1
	  os.system("screen -S Slump1 perl slump.pl vuln.txt")
	  call(["clear"])
    elif ans=="3":
	  #input
	  os.system("ls *.lst")
	  lista1 = raw_input('nome lista 1: ')
	  os.system("ls *.lst")
	  lista2 = raw_input('nome lista 2: ')
	  os.system("ls *.lst")
	  lista3 = raw_input('nome lista 3: ')
	  #lista 1
	  call(["clear"])
	  os.system("screen -S Scan1 zmap -p22 -w {0}.lst -o mfu.txt -B100M".format(lista1))
	  call(["clear"])
	  #lista 2
	  os.system("screen -S Scan2 zmap -p22 -w {0}.lst -o /root/scan/2/mfu.txt -B100M".format(lista2))
	  call(["clear"])
	  #lista 3
	  os.system("screen -S Scan3 zmap -p22 -w {0}.lst -o /root/scan/3/mfu.txt -B100M".format(lista3))
	  call(["clear"])
	  #Update 1
	  os.system("screen -S Update1 ./update 1500")
	  call(["clear"])
	  call(["clear"])
	  #Slump 1
	  os.system("screen -S Slump1 perl slump.pl vuln.txt")
	  call(["clear"])
    elif ans=="4":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Scelta non valida")
