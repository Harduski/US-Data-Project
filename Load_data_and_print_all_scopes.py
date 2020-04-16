
import tkinter as tk
from tkinter import filedialog
import time
import numpy as np
import matplotlib.pyplot as plt

#variable
count = 0

#timestring generation
timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
#print(timestr)

#search for data in a browser
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes = (("csv files","*.csv"),("all files","*.*")))

#load data from browser choice
matrix = np.loadtxt(file_path, delimiter=";")
size_data = matrix.shape


for i in range(size_data[0]):

    ploty = matrix[i]
    #filter
    ran_val = max(ploty) - min(ploty)
 #   for c in range(ploty.size):
  #      if abs(ploty[c]) >= 0.7:
   #         ploty[c] = np.median(ploty)
    #ploty = ploty - np.median(ploty)



    plt.plot(ploty)
    plt.xlabel('time')
    plt.ylabel('voltage')
    #save plot as image
    if ran_val < 0:
        count = count + 1
    elif file_path.find('Person') != -1:
        plt.savefig('Ergebnisse\Person\Person_' + timestr + '_' + str(i))
    elif file_path.find('Leer') != -1:
        plt.savefig('Ergebnisse\Leer\Leer_' + timestr + '_' + str(i))
    elif file_path.find('Objekt') != -1:
        plt.savefig('Ergebnisse\Objekt\objekt_' + timestr + '_' + str(i))
    else:
        print('error')
    plt.close()
print(count)
