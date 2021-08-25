import os
import getpass
import time

os.system("espeak-ng Hello Welcome to your menu program")
x = "Welcome to your menu program"
y = x.center(80)
print(y)

while True :
  os.system("clear")
  print("\t\t --------------Welcome to menu program for Linux commands-------------- \n\n")
  print("Press 1 To Install Package \t\t\t\t\t Press 2 To print Date")
  print("Press 3 To check list of and file and directory \t\t\t Press 4 To Find/Search")
  print("Press 5 To Handling Services \t\t\t\t\t Press 6 To Adding user")
  print("Press 7 To Create Partition \t\t\t\t\t Press 8 To create a webserver")
  print("Press 9 To setting up different cronjobs \t\t\t Press 10 To Mount Disk")
  print("Press 11 To fstab for mounting \t\t\t\t\t Press 12 To create physical volumes")
  print("Press 13 To create a volume group \t\t\t\t Press 14 To check logical volumes")
  print("Press 0 To Exit")
  
  os.system("espeak-ng 'How may I help you'")
  p=int(input("How may I help you "))
  if p==1:
    packagename=input("Enter package to install: ")
    os.system("sudo yum install {} -y ".format(packagename))
    os.system("espeak-ng 'packages installed'")
    time.sleep(5)
    
  elif p==2:
    os.system("espeak-ng 'Date is'")
    os.system("date")
    time.sleep(5)
  
  elif p==3:
    os.system("espeak-ng 'Current Directory list is'")
    os.system("ls -l")
    time.sleep(5)
    
  elif p==4:
    option=input("How you want to find ")
    file=input("Enter Filename ")
    os.system("ls | grep {} {}".format(option, file))
  
  elif p==5:
    service=input("Enter Service Name ")
    os.system("sudo systemctl start {}".format(service))
    os.system("espeak-ng 'service started'")
    time.sleep(5)

  elif p==6:
    name=input("Enter new user name: ")
    passwd = getpass.getpass(prompt="Enter password: ")
    os.system("sudo useradd {}".format(name))
    os.system("sudo passwd {}".format(name))
    os.system("espeak-ng 'user is now created'")
    time.sleep(5)
  
  elif p==7:
    disk=input("enter your disk name ")
    os.system("sudo fdisk /dev/{}".format(disk))
    
  elif p==8:
    webserver=input("Enter which webserver is installed ")
    if webserver=="httpd":
        os.system("systemctl stop firewalld")
        print("Starting the apache services")
        os.system("systemctl start httpd")
        print("Copy your index.html files in /var/www/html/ folder ")
        time.sleep(2)
        os.system("ifconfig enp0s3")
        print("Enter the local vm ip in webbrowser for checking site")
        os.system("espeak-ng 'Enter the local vm ip in webbrowser for checking site'")
        time.sleep(5)
    else:
        os.system("systemctl stop firewalld")
        print("Starting the nginx services")
        os.system("systemctl start nginx")
        print("Copy your index.html files in /usr/bin/share/html/ folder ")
        time.sleep(2)
        os.system("ifconfig enp0s3")
        print("Enter the local vm ip in webbrowser for checking site")
        os.system("espeak-ng 'Enter the local vm ip in webbrowser for checking site'")
        time.sleep(5)
	      
  elif p==9:
    os.system("crontab –e")
    time.sleep(5)

  elif p==10:
    initdisk=input("Enter the destination where to mount ")
    finaldisk=input("Enter the disk path ")
    os.system("sudo mount -t ntfs {}  {}".format(initdisk, finaldisk))
    time.sleep(5)
	      
  elif p==11:
    os.system("vim /etc/fstab")
    time.sleep(5)
	
  elif p==12:
    initdisk=input("Enter the destination where to mount ")
    finaldisk=input("Enter the disk path ")
    os.system("sudo pvcreate {}  {}".format(initdisk, finaldisk))
    time.sleep(5)
	      
  elif p==13:
    grname=input("Enter your group name ")
    initdisk=input("Enter the destination where to mount ")
    finaldisk=input("Enter the disk path ")
    os.system("sudo vgcreate {}  {} {}".format(grname,initdisk, finaldisk))
    time.sleep(5)
	      
  elif p==14:
    os.system("sudo lvdisplay")
    time.sleep(5)
    
  elif p==0:
    break
