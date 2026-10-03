#This is a simple python script to collect details of your linux system
#!/usr/bin/env python 

import os
import re
import sys
import datetime
import subprocess



from subprocess import Popen, PIPE
process = Popen(['ls', '/var/tmp/sap'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print stdout
x = stderr
y = stdout

if y != '':
	 print("the sap directory already exists,the folder will be backup to '/var/tmp/sapold.tar.gz' and then deleted")
 	 os.system("tar -cvzf /var/tmp/sapold.tar.gz /var/tmp/sap")
         os.system("rm -r /var/tmp/sap")

os.system("mkdir /var/tmp/sap")
def oskernel():
    x = subprocess.check_output(["uname","-a"])
    with open('/var/tmp/sap/oskernel1', "w") as f:
   	 f.write(x)
         print(' ')
	 print("The hostname,kernel,current time is listed below")
         print("================================================")
	 print(x)
         print("================================================")
         print('') 

def osrelease():
	x = subprocess.check_output(["cat", "/etc/os-release"])
	with open('/var/tmp/sap/osrelease', "w") as f:
                print("The os-release is listed below")
                print("======================================")
	        f.write(x)
	        print(x)
                print("======================================")
                print('')


def systemmem():
        x = subprocess.check_output(["free", "-tm"])
        with open('/var/tmp/sap/memdetails', "w") as f:
                print("The memory details of the system in MB is ")
                print("==========================================")
                f.write(x)
                print(x)
                print("==========================================")
                print('')

def systemcpu():
        x = subprocess.check_output(["lscpu"])
        with open('/var/tmp/sap/cpudetails', "w") as f:
                print("The CPU details of the system are listed below ")
                print("===============================================")
                f.write(x)
                print(x)
                print("===============================================")
                print('')

def systemnuma():
        x = subprocess.check_output(["numactl","-s"])
        with open('/var/tmp/sap/numadetails', "w") as f:
                print("The NUMA details of the system are listed below ")
                print("================================================")
                f.write(x)
                print(x)
                print("================================================")
                print('')


def systemIP():
        x = subprocess.check_output(["ifconfig","-a"])
        with open('/var/tmp/sap/ipconfigdetails', "w") as f:
                print("The IPconfig  details of the system are listed below ")
                print("================================================")
                f.write(x)
                print(x)
                print("================================================")
                print('')

def systemHostfile():
        x = subprocess.check_output(["cat","/etc/hosts"])
        with open('/var/tmp/sap/hostfile', "w") as f:
                print("The Host file  details of the system are listed below ")
                print("================================================")
                f.write(x)
                print(x)
                print("================================================")
                print('')

def iptables():
        x = subprocess.check_output(["iptables","-L"])
        with open('/var/tmp/sap/iptables', "w") as f:
                print("The Iptable   details of the system are listed below ")
                print("================================================")
                f.write(x)
                print(x)
                print("================================================")
                print('')

def routingtable():
        x = subprocess.check_output(["netstat","-r"])
        with open('/var/tmp/sap/routes', "w") as f:
                print("The routing table   details of the system are listed below ")
                print("================================================")
                f.write(x)
                print(x)
                print("================================================")
                print('')




def filesystem():
        x = subprocess.check_output(["df","-Th"])
        with open('/var/tmp/sap/filesystem', "w") as f:
                print("The filesystem   details of the system are listed below ")
                print("================================================")
                f.write(x)
                print(x)
                print("================================================")
                print('')


def devices():
        x = subprocess.check_output(["lsblk","-ap"])
        with open('/var/tmp/sap/devices', "w") as f:
                print("The devices  details of the system are listed below ")
                print("================================================")
                f.write(x)
                print(x)
                print("================================================")
                print('')



def logicalpvs():
        x = subprocess.check_output(["pvs","-a"])
        with open('/var/tmp/sap/logicalpvs', "w") as f:
                print("The Physical devices details of the system are listed below ")
                print("============================================================")
                f.write(x)
                print(x)
                print("============================================================")
                print('')


def logicalvolumes():
        x = subprocess.check_output(["lvs","-a"])
        with open('/var/tmp/sap/logicalvolumes', "w") as f:
                print("The logical volume  details of the system are listed below ")
                print("===========================================================")
                f.write(x)
                print(x)
                print("===========================================================")
                print('')



def logicalvgs():
        x = subprocess.check_output(["vgs","-a"])
        with open('/var/tmp/sap/logicalvgs', "w") as f:
                print("The logical volume group  details of the system are listed below ")
                print("=================================================================")
                f.write(x)
                print(x)
                print("=================================================================")
                print('')



oskernel()
osrelease()
systemmem()
systemcpu()
systemnuma()
filesystem()
devices()
logicalpvs()
logicalvolumes()
logicalvgs()
systemIP()
systemHostfile()
iptables()
routingtable()
print('')

os.system("tar -cvzf /var/tmp/sap.tar.gz /var/tmp/sap/")
print('')
print('==============================================')
print("The archive to be uploaded  is /var/tmp/sap.tar.gz")
print("The old archive to be uploaded is /var/tmp/sapold.tar.gz") 
