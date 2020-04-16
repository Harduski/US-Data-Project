import numpy as np
from scipy.signal import find_peaks, hann

"""Dieses Programm nimmt die Rohdaten von dem Ultraschall Sensor auf und erzeugt Merkmale davon. Diese Merkmale sind:
Bandbreite und Mittenfrequenz
Standardabweichung und Varianz
Maximale Amplituden der FFT
THD with noise
Schiefe und Wölbung der Normalverteilung 
Maximum der Ableitung

Eingabe:
Für das Programm werden lediglich Personen und Objekt aufnahmen in CSV mit einer Semikkolentrennung benötigt. 
Eine feste Anzahl an Datensätzen wird nicht benötigt.

Ausgabe:
Diese Merkmale werden in einem Array gespeichert und in drei CSV Files abgelegt(df_object, df_person und df_all).

Voranalyse
Für die Voranalyse sind einerseits eine FFT mit Fensterung zentriert von dem maximalwert und grundlegen statistische Signale

Bearbeitung der Merkmale:
innerhalb der For Schleife können Merkmale hinterlegt werden. Diese Merkmale werden einprogrammiert und innerhalb des 
Return Bereichs eingefügt werden. Wenn die Returnvaribalen angegeben sind, muss lediglich 
feature_per = np.zeros((size_per[0], 7)) und feature_ob = np.zeros((size_ob[0], 7)) der Zahlenwert 7 angepasst werden.

"""

#fuction
def feature_gen(df1):
    print(df1)

    # statistische Berechnung
    df_max = max(df1)
    df_max_pos, _ = find_peaks(df1, height=df_max)
    df_min = min(df1)
    df_mean = np.mean(df1)
    df_var = np.var(df1)
    df_std = np.std(df1)



    # uni_vec = np.ones(0, df_num, float)
    # print(df_max, df_min, df_mean, df_var, df_std)

    # check for bad reading
    if df_mean > bad_read_value or df_num != np.size(df1):
        print("bad reading of the value")

    # Offset substraction
    df1 = df1 - df_mean

    # praparation fft analyses

    # max value in center of fft
    df_high_peak = np.argmax(df1)
    fft_start = df_high_peak - int(num_fft / 2)
    fft_end = df_high_peak + int(num_fft / 2)

    #protection for limet of dataframe value fft_end >= df_num
    if fft_end >int(df_num):
        dif_fft=fft_end-int(df_num)
        fft_start = fft_start-dif_fft
        fft_end = fft_end-dif_fft

    if fft_start < 0:
        dif_fft=fft_end-int(df_num)
        fft_start = fft_start-dif_fft
        fft_end = fft_end-dif_fft


    x_fft = np.fft.rfftfreq(num_fft, d=del_time)
    # x_fft = x_fft[fft_start:fft_end]

    # db_fft = np.log10(fft_df/np.argmax(fft_df))
    # plot for x axis fft
    # plt.plot(x_fft)
    # plt.show()

    # FFT
    df_new = df1[fft_start:fft_end] * window
    fft_df = abs(np.fft.rfft(df_new))
    np.savetxt('sample.csv', df1[fft_start:fft_end], delimiter=",")
    fft_plot = np.copy(fft_df)

    mag = abs(20 * np.log10(fft_df))
    max_fft = max(fft_df)
    max_fft_pos = np.argmax(fft_df)
    fft_peak, _ = find_peaks(fft_df, height=max_fft)
    # fft_sample = fft_peak + fft_start
    # feature

    # distance
    distance = 18500 * del_time * (df_max_pos)

    # bandwith and center frequency
    f_center = x_fft[max_fft_pos]
    for i in range(num_fft):
        if 0.5 * max_fft > fft_df[i + max_fft_pos]:
            f_band = x_fft[i + max_fft_pos]
            f_band -= f_center
            f_band= 2*f_band
            break

    # print "f_center = %d und f_0 = %d" % (f_center, f_band)

    # THD
    total_rms = np.sqrt(np.mean(np.abs(df1[fft_start:fft_end]) ** 2))
    under_five = np.argwhere(fft_df < 2)
    for i in range(len(under_five)):
        if under_five[i] > max_fft_pos:
            uppermin = under_five[i]
            lowermin = under_five[i - 1]
            break

    fft_plot[int(lowermin):int(uppermin)] = 0.0
    noise_df = np.fft.irfft(fft_df)
    noise_rms = np.sqrt(np.mean(np.abs(noise_df) ** 2))
    THDN = noise_rms / total_rms
    print("THD+N:     %.4f%% or %.1f dB" % (THDN * 100, 20 * np.log10(THDN)))

    #

    # Num of Peaks
    num_peak, _ = find_peaks(df1, height=peak_high)
    num_peak_num = np.size(num_peak)

    for due in range(int(df_num)-1):
        deril = abs(df1[due+1])-abs(df1[due])
    max_deril = np.max(deril)



    return(THDN, f_center, f_band, max_fft, df_var, df_std, max_deril)

#variables
# define Variabels
df_num = 16384.0
sam_fre = 1900000.0
del_time = 1.0/sam_fre
    df1 = df_ob[i]
    feature_ob[i:] = feature_gen(df1)
colum_one = np.ones(size_ob[0])
data_ob=np.column_stack((feature_ob, colum_one))
#speichern df_ob
np.savetxt('df_ob.csv', data_ob, delimiter=",")

#laden df_per relativ Pfad
df_per = np.loadtxt(r'Datenquelle/Person/20170717_11_24_37_Complete.csv', delimiter=";")
size_per = df_per.shape
feature_per = np.zeros((size_per[0], 7))
for i in range(size_per[0]):
sum_df = 0.0
num_fft = 4096
peak_high = 0.05
end_x_axis = del_time*df_num
x_time = np.linspace(0.0, end_x_axis, df_num)
bad_read_value = 0.05
delay = 4000 # sampels
window = hann(num_fft)
#window = hann(int(df_num))

#laden df_ob relativ Pfad
df_ob = np.loadtxt(r'Datenquelle/Objekt/Object2.csv', delimiter=";")
size_ob = df_ob.shape
feature_ob = np.zeros((size_ob[0], 7))

for i in range(size_ob[0]):
    df1 = df_per[i]
    feature_per[i:] = feature_gen(df1)
colum_zero = np.zeros(size_per[0])
data_per = np.column_stack((feature_per, colum_zero))
#speichern df_per3
np.savetxt('df_per.csv', data_per, delimiter=",")

data_all = np.concatenate((data_ob, data_per), axis=0)
#speichern df_all
np.savetxt('df_all.csv', data_all, delimiter=",")

print(feature_per, feature_ob)

