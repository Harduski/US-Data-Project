import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


sam_fre = 1900000.0
del_time = 1.0/sam_fre


df = np.loadtxt('Datenquelle/Objekt/Object2.csv', delimiter=';')
df_1 = df[6,:]
df_max = np.max(df_1)
df_max_pos, _ = find_peaks(df_1, height=df_max)
x = df_1[int(df_max_pos)-2048:int(df_max_pos)+2048]



np.savetxt('sample.csv', x,newline=',', delimiter='', fmt='%1.3f')

fft_df = abs(np.fft.rfft(x))
np.savetxt('sample_fft.csv', fft_df,newline=',', delimiter='', fmt='%1.3f')
x_fft = np.fft.rfftfreq(4096, d=del_time)
np.savetxt('sample_fft_x.csv', x_fft/1000,newline=',', delimiter='', fmt='%1.3f')
plt.plot((fft_df))
plt.xlabel('Hz')
plt.ylabel('1')
plt.show()

