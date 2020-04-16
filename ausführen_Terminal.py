import os
path = open('path.txt', 'r')
path = path.read()
#path = 'C:\Users\dennis\Documents\red_pitaya\plink.exe root@192.168.128.1 -ssh -pw root -m "config.txt"'
print(path)
os.system(path)
