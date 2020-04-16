import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, hann

#function difenetion



# define Variabels
df_num = 16384.0
sam_fre = 1900000.0
del_time = 1.0/sam_fre
sum_df = 0.0
num_fft = 4098
peak_high = 0.05
end_x_axis = del_time*df_num
x_time = np.linspace(0.0, end_x_axis, df_num)
bad_read_value = 0.05
delay = 4000 # sampels
window = hann(num_fft)
#window = hann(int(df_num))


#read data
df1 = np.loadtxt(r'objekt.csv', delimiter=",")

#sig_ray = df1.values
print(df1)

# statistische Berechnung
df_max = max(df1)
df_min = min(df1)
df_mean = np.mean(df1)
df_var = np.var(df1)
df_std = np.std(df1)
df_max_pos, _ = find_peaks(df1, height=df_max)

# uni_vec = np.ones(0, df_num, float)
# print(df_max, df_min, df_mean, df_var, df_std)

#check for bad reading
if df_mean > bad_read_value or df_num != np.size(df1):
    print("bad reading of the value")

# Offset substraction
df1 = df1 - df_mean

#praparation fft analyses

# max value in center of fft
df_high_peak = np.argmax(df1)
fft_start = df_high_peak - int(num_fft/2)
fft_end = df_high_peak + int(num_fft/2)
x_fft = np.fft.rfftfreq(num_fft, d=del_time)
#x_fft = x_fft[fft_start:fft_end]

#db_fft = np.log10(fft_df/np.argmax(fft_df))
#plot for x axis fft
#plt.plot(x_fft)
#plt.show()



#FFT
df_new = df1[fft_start:fft_end]*window
fft_df = abs(np.fft.rfft(df_new))
fft_plot = np.copy(fft_df)

mag = abs(20*np.log10(fft_df))
max_fft = max(fft_df)
max_fft_pos = np.argmax(fft_df)
fft_peak, _ = find_peaks(fft_df, height=max_fft)
#fft_sample = fft_peak + fft_start
#feature

#distance
distance = 18500*del_time*(df_max_pos)

#bandwith and center frequency
f_center = x_fft[max_fft_pos]
for i in range(num_fft):
    if 0.5*max_fft > fft_df[i+max_fft_pos]:
        f_band = x_fft[i+max_fft_pos]
        f_band -= f_center
        break

#print "f_center = %d und f_0 = %d" % (f_center, f_band)

#THD
total_rms = np.sqrt(np.mean(np.abs(df1[fft_start:fft_end])**2))
under_five = np.argwhere(fft_df < 2)
for i in range(len(under_five)):
    if under_five[i] > max_fft_pos:
        uppermin = under_five[i]
        lowermin = under_five[i-1]
        break

fft_plot[int(lowermin):int(uppermin)] = 0.0
noise_df = np.fft.irfft(fft_df)
noise_rms = np.sqrt(np.mean(np.abs(noise_df)**2))
THDN = noise_rms/total_rms
print("THD+N:     %.4f%% or %.1f dB" % (THDN * 100, 20 * np.log10(THDN)))

#


#Num of Peaks
num_peak, _ = find_peaks(df1, height=peak_high)
num_peak_num = np.size(num_peak)



#print(num_peak, num_peak_num)

#plot Signal
#plt.plot(x_time, df1)
#plt.plot(num_peak*del_time, df1[num_peak], "x")
#plt.ylabel('Voltage')
#plt.xlabel('Sampels')
#plt.show()



#plot Signal FFT

plt.plot(x_fft, fft_df)
#plt.xscale('log')
#plt.yscale('log')
plt.ylabel('Amplitude')
plt.xlabel('Frequency')
plt.grid()
plt.show()

#plot Signal
plt.plot(df1)
plt.ylabel('Voltage')
plt.xlabel('Sampels')
plt.show()



