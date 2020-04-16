#!/usr/bin/python

import redpitaya_scpi as scpi
import matplotlib.pyplot as plot
import time
import numpy as np

# Variables
ip_adress = '192.168.128.1'
file_path = r'Ergebnisse/Test/Test.csv'
num_of_cycle = 10
buff_array =''
buff_np = np.zeros((num_of_cycle, 16384), float)


#inizilation trigger
rp_s = scpi.scpi(host=ip_adress)

rp_s.tx_txt('ACQ:DEC 64')
rp_s.tx_txt('ACQ:TRIG:LEVEL -21')
rp_s.tx_txt('ACQ:TRIG:DLY 12192')
rp_s.tx_txt('ACQ:START')
rp_s.tx_txt('ACQ:TRIG EXT_NE')

#wait untill trigger is activated
while 1:
    rp_s.tx_txt('ACQ:TRIG:STAT?')
    if rp_s.rx_txt() == 'TD':

        break
for x in range(num_of_cycle):
    #collecting all 16xxx values and save and convert
    rp_s.tx_txt('ACQ:SOUR1:DATA?')
    buff_string = rp_s.rx_txt()
    buff_string = buff_string.strip('{}\n\r').replace("  ", "")
    #buff_array = buff_array + buff_string.strip('{}\n\r').replace(" ","") + '\n\r'
    buff = np.fromstring(buff_string, sep=',')
    buff = np.round(buff, 3)
    buff_np[x:] = buff


    #buff_string = buff_string.strip('{}\n\r').replace("  ", "").split(',')
   # buff = list(map(float, buff_string))
    #

    #plotting 16xxx vaules
    #plot.plot(buff)
    #plot.ylabel('Voltage')
    #plot.show()

np.savetxt(file_path, buff_np, delimiter=';', fmt= '%.3f')


