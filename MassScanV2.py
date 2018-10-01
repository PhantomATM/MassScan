import os
import sys
from time import sleep
from subprocess import call

ans=True

def yes_no(answer):
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])

    while True:
        choice = raw_input(answer).lower()
        if choice in yes:
           scan()
           sys.exit("END")
        elif choice in no:
           call(["clear"])
           sys.exit("Rerun the Code")
        else:
           print "Please respond with 'yes' or 'no'\n"

def scan():
    sleep(0.5)
    print("5")
    sleep(1)
    print("4")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    os.system("rm -r mfu*")
    call(["clear"])
    os.system("screen -S ScanGlobal-1 zmap -p22 -o mfu.txt -N 250000")
    call(["clear"])
    os.system("screen -S Update1 ./update 1500")
    call(["clear"])
    os.system("screen -S Slump1 perl slump.pl vuln.txt")
    call(["clear"])
    
while ans:
    print("""
    1. Scan 1 lst
    2. Scan 2 lst
    3. Scan 3 lst
    4. Scan Global
    5. Exit/Quit
    """)
    ans=raw_input("Cosa Vuoi Fare? ")
    if ans=="1":
	  call(["clear"])
	  os.system("ls *.lst")
	  lista1 = raw_input('nome lista 1: ')
	  os.system("rm -r mfu*")
	  call(["clear"])
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
	  os.system("rm -r mfu*")
	  call(["clear"])
	  #lista 1
	  call(["clear"])
	  print "Scanning Lista 1"
	  sleep(0.5)
	  os.system("screen -S Scan1 zmap -p22 -w {0}.lst  -o mfu1.txt -B100M".format(lista1))
	  #lista 2
	  print "Scanning Lista 2"
	  sleep(0.5)
	  os.system("screen -S Scan2 zmap -p22 -w {0}.lst  -o mfu2.txt -B100M".format(lista2))
	  #Unisci liste
	  os.system("cat mfu1.txt mfu2.txt > mfu.txt")
	  #Rimuove mfu vecchi
	  os.system("rm mfu1.txt")
	  os.system("rm mfu2.txt")
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
	  os.system("rm -r mfu*")
	  call(["clear"])
	  #lista 1
	  call(["clear"])
	  print "Scanning Lista 1"
	  sleep(0.5)
	  os.system("screen -S Scan1 zmap -p22 -w {0}.lst -o mfu1.txt -B100M".format(lista1))
	  call(["clear"])
	  #lista 2
	  print "Scanning Lista 2"
	  sleep(0.5)
	  os.system("screen -S Scan2 zmap -p22 -w {0}.lst -o mfu2.txt -B100M".format(lista2))
	  call(["clear"])
	  #lista 3
	  print "Scanning Lista 3"
	  sleep(0.5)
	  os.system("screen -S Scan3 zmap -p22 -w {0}.lst -o mfu3.txt -B100M".format(lista3))
	  #Unisci liste
	  os.system("cat mfu1.txt mfu2.txt mfu3.txt > mfu.txt")
	  #Rimuove mfu vecchi
	  os.system("rm mfu1.txt")
	  os.system("rm mfu2.txt")
	  os.system("rm mfu3.txt")
	  call(["clear"])
	  #Update 1
	  os.system("screen -S Update1 ./update 1500")
	  call(["clear"])
	  #Slump 1
	  os.system("screen -S Slump1 perl slump.pl vuln.txt")
	  call(["clear"])
    elif ans=="4":
      print("Scanning Global is hazardous")
      yes_no('Scan? [y] or [n]: ')
    elif ans=="5":
      print("\n Goodbye")
      ans = None
    else:
       print("\n Scelta non valida")
