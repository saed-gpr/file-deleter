import subprocess
import os 
from colorama import Fore # it is just for fun :))

cmd = subprocess.check_output('F: && dir /S /B *.psd', shell= True).decode().split('\n')

# for running this tool you should clear the line 10-16 from hashes (#) !!


#for i in cmd:
#
#    if i != '':
#        i = i[:-1]
#
#        os.remove(i)
#        print(Fore.RED + i + 'is deleted now :))!!')