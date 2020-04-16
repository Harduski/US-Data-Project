import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from gui_neu import Ui_MainWindow
from QT5_function import openFileNameDialog
import os
import threading
import time
import serial
from sklearn.neural_network import MLPClassifier
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

from scipy.signal import find_peaks, hann


import numpy as np


from sklearn import svm, datasets, neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
from micromlgen import port
from sklearn_porter import Porter

from joblib import dump, load
import emlearn
from time import sleep
from pySerialTransfer import pySerialTransfer as txfer

#link = txfer.SerialTransfer('COM1')

#    link.open()
 #   sleep(2)  # allow some time for the Arduino to completely reset


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #loadUi('test.ui', self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #init Bottons

        self.ui.call_xls.clicked.connect(self.csv)
        self.ui.call_dia_train.clicked.connect(self.read_train)
        self.ui.call_dia_test.clicked.connect(self.read_test)
        self.ui.call_dia_classi.clicked.connect(self.read_classi)
        self.ui.call_dia_val.clicked.connect(self.read_val)
        self.ui.call_start_classi.clicked.connect(self.start_classi)
        self.ui.call_dialog_ob.clicked.connect(self.read_ob)
        self.ui.call_dialog_per.clicked.connect(self.read_per)
        self.ui.call_dialog_lee.clicked.connect(self.read_lee)
        self.ui.call_save_feature.clicked.connect(self.feat_extra)
        self.ui.call_vz.clicked.connect(self.choose_dir)
       # self.ui.call_com.clicked.connect(self.send_meas)
      #  self.ui.call_stop_meas.clicked.connect(self.meas)

        #todo: intialisierung von allen Tatenfunktionen (kontrolle)



    @pyqtSlot()




    #TODO: test der arduino Datensende und Datenempfang System (done)




    def csv(self):

        file = QFileDialog.getOpenFileName(self, "Choose ultra sonic data from Labview", "",
                                           "All Files (*);;XLS Files (*.xls)")
        # open the data
        file_str = open(file[0], 'r')
        file = file_str.read()

       # self.ui.ad_xls.setText(file_str)

        # replace the tabstop with a simikolon
        file_new = file.replace('\t', ';')
        file_new = file_new.replace(',', '.')
        file_new = file_new.replace('"', '')
        # file_new = file_new.replace('\r\n', ';')
        name = file_str.name
        len(name)
      #  print(file_new)

        # generate a new dataname with csv
        new = name.replace('xls', 'csv')

        # open and write new file with the replaced simikolon
        new_file = open(new, 'w+')
        new_file.write(file_new)

        # close all data
        new_file.close()
        file_str.close()

        self.ui.ad_xls.setText(new)

    def read_train(self):

        file = QFileDialog.getOpenFileName(self, "read train Data", "",
                                           "All Files (*);;CSV File (*.csv)")
        self.ui.ad_train.setText(file[0])

    def read_val(self):

        file = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                           "All Files (*);;CSV File (*.csv)")
        self.ui.ad_val.setText(file[0])

    def read_classi(self):

        file = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                           "All Files (*);;CSV File (*.csv)")
        self.ui.ad_classi.setText(file[0])

    def read_meas(self):

        file = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                           "All Files (*);;CSV File (*.csv)")
        self.ui.ad_meas.setText(file[0])

    def read_test(self):

        file = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                           "All Files (*);;CSV File (*.csv)")
        self.ui.ad_test.setText(file[0])

    def read_meas_2(self):

        file = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                           "All Files (*);;CSV File (*.csv)", )
        self.ui.ad_meas_3.setText(file[0])

    def choose_dir(self):

        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(file)

        self.ui.ad_ver.setText(file[0])

    def read_ob(self):
        file = QFileDialog.getOpenFileName(self, "Bitte Klasse Objekt einlesen", "",
                                               "All Files (*);;CSV File (*.csv)", )
        self.ui.ad_meas_ob.setText(file[0])

    def read_per(self):
        file = QFileDialog.getOpenFileName(self, "Bitte Klasse Personen einlesen", "",
                                           "All Files (*);;CSV File (*.csv)", )
        self.ui.ad_meas_per.setText(file[0])

    def read_lee(self):
        file = QFileDialog.getOpenFileName(self, "Bitte Klasse Leer einlesen", "",
                                           "All Files (*);;CSV File (*.csv)", )
        self.ui.ad_meas_lee.setText(file[0])

    #def start_com(self):

    """def send_meas(self):
        link.txBuff[0] = '1'

        link.send(1)
        response = ''
        for index in range(link.bytesRead):
            response += chr(link.rxBuff[index])



        self.ui.msg_state.setText(string))#todo: com


       #todo: implementierung der Nachrichten in python: statemaschine, messdaten und klassiergebnisse
    """
    """  def meas(self):

        link.txBuff[0] = '1'


        link.send(1)
        response = ''
        for index in range(link.bytesRead):
            response += chr(link.rxBuff[index])


        self.ui.msg_state.setText(y)
        if y == "1":
            meas_num = self.ui.ad_val_meas.text()

           # ser.writelines(bytes(meas_num,'utf8')))#todo: com
           # x = ser.readline())#todo: com
           # x = ser.readline())#todo: com

           # string = x.decode()
            #y = string.replace("\r\n", "")
            #self.ui.msg_state_ard.setText(string)
            #for i in range(int(meas_num)):
             #   meas_array = ser.readline()#todo: com

            #path_meas, _ = QFileDialog.getSaveFileName(self, "save all feature", "",
                                                            "All Files (*);;csv Files (*.csv)")
            #np.savetxt(str(path_meas), meas_array, delimiter=",")


            #todo: implementierung aller kommunikation mit dem neuen ARDUINO Protokoll


    """






    """
#todo: CLassi auf PYQT5 Frontend übertragen.
#todo: CLassi auf ucontroller
    """
    def start_classi(self):
        path_test = self.ui.ad_test.text()
        path_train = self.ui.ad_train.text()
        path_val = self.ui.ad_val.text()

        #splite of the matices
        df0 = np.loadtxt(path_test, delimiter=",")
        df1 = np.loadtxt(path_train, delimiter=",")
        df2 = np.loadtxt(path_val, delimiter=",")
        # variables
        size0 = df0.shape
        input0 = size0[1] - 1
        size1 = df1.shape
        input1 = size1[1] - 1
        size2 = df2.shape
        input2 = size2[1] - 1

        # split input and output
        X0 = df1[:, 0:input0]
        Y0 = df1[:, input0]
        X1 = df1[:, 0:input1]
        Y1 = df1[:, input1]
        X2 = df2[:, 0:input2]
        Y2 = df2[:, input2]

        if self.ui.check_train.isChecked():
            file = QFileDialog.getOpenFileName(self, "Modell einlesen", "",
                                               "All Files (*);;Joblib File (*.joblib)", )
            model = load(file[0])
        else:


            if  path_train == "" or path_val == "" or path_test == "":
                self.ui.msg_text.setText("path not complett")
            elif self.ui.check_svm.isChecked():


                #svm
                model = svm.SVC(kernel='linear', decision_function_shape='ovr', C=0.01, gamma=0.001)
                model.fit(X1, Y1)

                if self.ui.che_mue.isChecked():
                    porter = port(model)
                    file_svm = QFileDialog.getSaveFileName(self, "Save Objects", "",
                                                           "All Files (*);;Lib File (*.h)")

                    f = open(file_svm[0], 'w+')
                    f.write(porter)
                    f.close()









                # TODO: FILE save System SVM (done)

            elif self.ui.check_neighbor.isChecked():

                #Decision Tree
                model = DecisionTreeClassifier(random_state=0)
                model.fit(X1, Y1)

                if self.ui.che_mue.isChecked():
                    cmodel = emlearn.convert(model)
                    file_svm= QFileDialog.getSaveFileName(self, "Save Objects", "",
                                                             "All Files (*);;Lib File (*.h)")
                    cmodel.save(file=file_svm[0])


            elif self.ui.check_neuro.isChecked():
                # creating model
                model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10, 2), random_state=1)
                model.fit(X1, Y1)

                if self.ui.che_mue.isChecked():
                    cmodel = emlearn.convert(model)
                    file_svm = QFileDialog.getSaveFileName(self, "Save Objects", "",
                                                           "All Files (*);;Lib File (*.h)")
                    cmodel.save(file=file_svm[0])

            elif self.ui.check_bayes.isChecked():

                # bayes classifier
                model = GaussianNB()
                model.fit(X1, Y1)

                if self.ui.che_mue.isChecked():
                    cmodel = emlearn.convert(model)
                    file_svm = QFileDialog.getSaveFileName(self, "Save Objects", "",
                                                           "All Files (*);;Lib File (*.h)")
                    cmodel.save(file=file_svm[0])

            else:
                self.ui.msg_text.setText("no choice of classifier")




#




        if self.ui.check_train_3.isChecked():
                #file creation
                    path_classi, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                    "All Files (*);;joblib Files (*.joblib)")
                    dump(model, path_classi)

        predicted = model.predict(X0)

        score = model.score(X2, Y2)

        #todo: Testen der joblib file Funktion(done)




        #todo: Testen der learnem Funktion. nach dem neustart installieren(done)

    def feat_extra(self):
        def feature_gen(df1):
            print(df1)

            # statistische Berechnung
            df_max = max(df1)
            df_min = min(df1)
            df_peak = df_max-df_min
            df_mean = np.mean(df1)
            df_var = np.var(df1)
            df_std = np.std(df1)
            df_max_pos, _ = find_peaks(df1, height=df_max)

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

            # protection for limet of dataframe value fft_end >= df_num
            if fft_end > int(df_num):
                dif_fft = fft_end - int(df_num)
                fft_start = fft_start - dif_fft
                fft_end = fft_end - dif_fft

            if fft_start < 0:
                dif_fft = fft_end - int(df_num)
                fft_start = fft_start - dif_fft
                fft_end = fft_end - dif_fft

            x_fft = np.fft.rfftfreq(num_fft, d=del_time)
            # x_fft = x_fft[fft_start:fft_end]

            # db_fft = np.log10(fft_df/np.argmax(fft_df))
            # plot for x axis fft
            # plt.plot(x_fft)
            # plt.show()

            # FFT
            df_new = df1[fft_start:fft_end] * window
            fft_df = abs(np.fft.rfft(df_new))
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
                    f_band = 2 * f_band
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
            """
            fft_plot[int(lowermin):int(uppermin)] = 0.0
            noise_df = np.fft.irfft(fft_df)
            noise_rms = np.sqrt(np.mean(np.abs(noise_df) ** 2))
            THDN = noise_rms / total_rms
            print("THD+N:     %.4f%% or %.1f dB" % (THDN * 100, 20 * np.log10(THDN)))
            """
            skew = 0.0
            woeb = 0.0
            fund_wv = np.copy(fft_df[lowermin:uppermin])
            std_wv = np.std(fund_wv)
            mean_wv = np.mean(fund_wv)
            for i in range(len(fund_wv)):
                skew = skew + (fund_wv[i]-mean_wv)*(fund_wv[i]-mean_wv)*(fund_wv[i]-mean_wv)/std_wv
                woeb = woeb + (fund_wv[i]-mean_wv)*(fund_wv[i]-mean_wv)*(fund_wv[i]-mean_wv)*(fund_wv[i]-mean_wv)/std_wv
                n = i
            skew = skew /n
            woeb = woeb / n








            return (f_center, f_band, skew, woeb)
        # define Variabels
        df_num = 16384.0
        sam_fre = 1900000.0
        del_time = 1.0 / sam_fre
        sum_df = 0.0
        num_fft = 4098
        peak_high = 0.05
        end_x_axis = del_time * df_num
        x_time = np.linspace(0.0, end_x_axis, df_num)
        bad_read_value = 0.05
        delay = 4000  # sampels
        window = hann(num_fft)
        # window = hann(int(df_num))

        path = self.ui.ad_meas.text()

        df_ob = np.loadtxt(path, delimiter=";")
        size_ob = df_ob.shape
        feature_ob = np.zeros((size_ob[0], 7))

        for i in range(size_ob[0]):
            df1 = df_ob[i]
            feature_ob[i:] = feature_gen(df1)
        colum_one = np.ones(size_ob[0])
        data_ob = np.column_stack((feature_ob, colum_one))

        fileName, _ = QFileDialog.getSaveFileName(self, "Save Objects", "",
                                                      "All Files (*);;csv Files (*.csv)")
        np.savetxt(str(fileName), data_ob, delimiter=";")


        path_per = self.ui.ad_meas_3.text()


        df_per = np.loadtxt(path_per, delimiter=";")

        size_per = df_per.shape
        feature_per = np.zeros((size_per[0], 7))
        for i in range(size_per[0]):
            df1 = df_per[i]
            feature_per[i:] = feature_gen(df1)
        colum_zero = np.zeros(size_per[0])
        data_per = np.column_stack((feature_per, colum_zero))

        fileName_2, _ = QFileDialog.getSaveFileName(self, "save Person", "",
                                                  "All Files (*);;csv Files (*.csv)")
        np.savetxt(str(fileName_2), data_per, delimiter=";")

        if not self.ui.ad_meas_lee.isempty():
            path_lee = self.ui.ad_meas_lee.text()

            df_lee = np.loadtxt(path_lee, delimiter=";")

            size_lee = df_lee.shape
            feature_lee = np.zeros((size_per[0], 7))
            for i in range(size_lee[0]):
                df1 = df_lee[i]
                feature_lee[i:] = feature_gen(df1)
            colum_zero = np.zeros(size_per[0])
            data_lee = np.column_stack((feature_lee, colum_zero))

            fileName_3, _ = QFileDialog.getSaveFileName(self, "save Person", "",
                                                        "All Files (*);;csv Files (*.csv)")
            np.savetxt(str(fileName_3), data_per, delimiter=";")
            data_all = np.concatenate((data_ob, data_per, data_lee), axis=0)
        else:
            data_all = np.concatenate((data_ob, data_per), axis=0)



        fileName_4, _ = QFileDialog.getSaveFileName(self, "save all feature", "",
                                                    "All Files (*);;csv Files (*.csv)")
        np.savetxt(str(fileName_4), data_all, delimiter=";")


        print(feature_per, feature_ob, feature_lee)





app = QApplication(sys.argv)
w = AppWindow()

w.show()
sys.exit(app.exec_())