# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_neu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1011, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.CSV = QtWidgets.QWidget()
        self.CSV.setObjectName("CSV")
        self.label = QtWidgets.QLabel(self.CSV)
        self.label.setGeometry(QtCore.QRect(60, 30, 501, 16))
        self.label.setObjectName("label")
        self.ad_xls = QtWidgets.QLineEdit(self.CSV)
        self.ad_xls.setGeometry(QtCore.QRect(40, 60, 431, 20))
        self.ad_xls.setObjectName("ad_xls")
        self.call_xls = QtWidgets.QToolButton(self.CSV)
        self.call_xls.setGeometry(QtCore.QRect(500, 60, 81, 19))
        self.call_xls.setObjectName("call_xls")
        self.tabWidget.addTab(self.CSV, "")
        self.Messdaten = QtWidgets.QWidget()
        self.Messdaten.setObjectName("Messdaten")
        self.label_5 = QtWidgets.QLabel(self.Messdaten)
        self.label_5.setGeometry(QtCore.QRect(40, 10, 471, 16))
        self.label_5.setObjectName("label_5")
        self.call_start_meas = QtWidgets.QToolButton(self.Messdaten)
        self.call_start_meas.setGeometry(QtCore.QRect(50, 280, 61, 19))
        self.call_start_meas.setObjectName("call_start_meas")
        self.call_stop_meas = QtWidgets.QToolButton(self.Messdaten)
        self.call_stop_meas.setGeometry(QtCore.QRect(160, 280, 61, 19))
        self.call_stop_meas.setObjectName("call_stop_meas")
        self.ad_name_meas = QtWidgets.QLineEdit(self.Messdaten)
        self.ad_name_meas.setGeometry(QtCore.QRect(620, 210, 121, 20))
        self.ad_name_meas.setObjectName("ad_name_meas")
        self.ad_ver = QtWidgets.QLineEdit(self.Messdaten)
        self.ad_ver.setGeometry(QtCore.QRect(40, 210, 441, 20))
        self.ad_ver.setObjectName("ad_ver")
        self.label_13 = QtWidgets.QLabel(self.Messdaten)
        self.label_13.setGeometry(QtCore.QRect(40, 50, 221, 16))
        self.label_13.setObjectName("label_13")
        self.label_11 = QtWidgets.QLabel(self.Messdaten)
        self.label_11.setGeometry(QtCore.QRect(640, 190, 111, 16))
        self.label_11.setObjectName("label_11")
        self.call_vz = QtWidgets.QToolButton(self.Messdaten)
        self.call_vz.setGeometry(QtCore.QRect(500, 210, 81, 19))
        self.call_vz.setObjectName("call_vz")
        self.call_com = QtWidgets.QToolButton(self.Messdaten)
        self.call_com.setGeometry(QtCore.QRect(40, 100, 81, 19))
        self.call_com.setObjectName("call_com")
        self.label_10 = QtWidgets.QLabel(self.Messdaten)
        self.label_10.setGeometry(QtCore.QRect(200, 170, 71, 16))
        self.label_10.setObjectName("label_10")
        self.ad_val_meas = QtWidgets.QLineEdit(self.Messdaten)
        self.ad_val_meas.setGeometry(QtCore.QRect(460, 280, 113, 20))
        self.ad_val_meas.setObjectName("ad_val_meas")
        self.label_2 = QtWidgets.QLabel(self.Messdaten)
        self.label_2.setGeometry(QtCore.QRect(460, 260, 101, 16))
        self.label_2.setObjectName("label_2")
        self.che_sens = QtWidgets.QRadioButton(self.Messdaten)
        self.che_sens.setGeometry(QtCore.QRect(400, 60, 51, 17))
        self.che_sens.setObjectName("che_sens")
        self.che_classi = QtWidgets.QRadioButton(self.Messdaten)
        self.che_classi.setGeometry(QtCore.QRect(460, 60, 82, 17))
        self.che_classi.setObjectName("che_classi")
        self.che_read = QtWidgets.QRadioButton(self.Messdaten)
        self.che_read.setGeometry(QtCore.QRect(550, 60, 82, 17))
        self.che_read.setObjectName("che_read")
        self.msg_classi = QtWidgets.QLabel(self.Messdaten)
        self.msg_classi.setGeometry(QtCore.QRect(70, 350, 111, 41))
        self.msg_classi.setObjectName("msg_classi")
        self.msg_state = QtWidgets.QLabel(self.Messdaten)
        self.msg_state.setGeometry(QtCore.QRect(290, 350, 111, 41))
        self.msg_state.setObjectName("msg_state")
        self.msg_state_ard = QtWidgets.QLabel(self.Messdaten)
        self.msg_state_ard.setGeometry(QtCore.QRect(480, 350, 111, 41))
        self.msg_state_ard.setObjectName("msg_state_ard")
        self.tabWidget.addTab(self.Messdaten, "")
        self.Klassifikation = QtWidgets.QWidget()
        self.Klassifikation.setObjectName("Klassifikation")
        self.check_neuro = QtWidgets.QRadioButton(self.Klassifikation)
        self.check_neuro.setGeometry(QtCore.QRect(60, 80, 161, 17))
        self.check_neuro.setObjectName("check_neuro")
        self.call_dia_classi = QtWidgets.QToolButton(self.Klassifikation)
        self.call_dia_classi.setGeometry(QtCore.QRect(480, 140, 81, 19))
        self.call_dia_classi.setObjectName("call_dia_classi")
        self.check_bayes = QtWidgets.QRadioButton(self.Klassifikation)
        self.check_bayes.setGeometry(QtCore.QRect(290, 80, 82, 17))
        self.check_bayes.setObjectName("check_bayes")
        self.check_svm = QtWidgets.QRadioButton(self.Klassifikation)
        self.check_svm.setGeometry(QtCore.QRect(390, 80, 82, 17))
        self.check_svm.setObjectName("check_svm")
        self.label_3 = QtWidgets.QLabel(self.Klassifikation)
        self.label_3.setGeometry(QtCore.QRect(60, 50, 521, 16))
        self.label_3.setObjectName("label_3")
        self.ad_classi = QtWidgets.QLineEdit(self.Klassifikation)
        self.ad_classi.setGeometry(QtCore.QRect(40, 140, 421, 20))
        self.ad_classi.setObjectName("ad_classi")
        self.check_train = QtWidgets.QCheckBox(self.Klassifikation)
        self.check_train.setGeometry(QtCore.QRect(470, 80, 101, 17))
        self.check_train.setObjectName("check_train")
        self.label_4 = QtWidgets.QLabel(self.Klassifikation)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 501, 16))
        self.label_4.setObjectName("label_4")
        self.call_dia_train = QtWidgets.QToolButton(self.Klassifikation)
        self.call_dia_train.setGeometry(QtCore.QRect(480, 210, 81, 19))
        self.call_dia_train.setObjectName("call_dia_train")
        self.ad_train = QtWidgets.QLineEdit(self.Klassifikation)
        self.ad_train.setGeometry(QtCore.QRect(40, 210, 421, 20))
        self.ad_train.setObjectName("ad_train")
        self.label_39 = QtWidgets.QLabel(self.Klassifikation)
        self.label_39.setGeometry(QtCore.QRect(40, 180, 221, 16))
        self.label_39.setObjectName("label_39")
        self.label_59 = QtWidgets.QLabel(self.Klassifikation)
        self.label_59.setGeometry(QtCore.QRect(40, 310, 161, 16))
        self.label_59.setObjectName("label_59")
        self.call_dia_val = QtWidgets.QToolButton(self.Klassifikation)
        self.call_dia_val.setGeometry(QtCore.QRect(480, 340, 81, 19))
        self.call_dia_val.setObjectName("call_dia_val")
        self.ad_val = QtWidgets.QLineEdit(self.Klassifikation)
        self.ad_val.setGeometry(QtCore.QRect(40, 340, 421, 20))
        self.ad_val.setObjectName("ad_val")
        self.call_stop_classi = QtWidgets.QToolButton(self.Klassifikation)
        self.call_stop_classi.setGeometry(QtCore.QRect(170, 390, 61, 19))
        self.call_stop_classi.setObjectName("call_stop_classi")
        self.call_start_classi = QtWidgets.QToolButton(self.Klassifikation)
        self.call_start_classi.setGeometry(QtCore.QRect(60, 390, 61, 19))
        self.call_start_classi.setObjectName("call_start_classi")
        self.call_dia_test = QtWidgets.QToolButton(self.Klassifikation)
        self.call_dia_test.setGeometry(QtCore.QRect(480, 280, 81, 19))
        self.call_dia_test.setObjectName("call_dia_test")
        self.label_60 = QtWidgets.QLabel(self.Klassifikation)
        self.label_60.setGeometry(QtCore.QRect(40, 250, 221, 16))
        self.label_60.setObjectName("label_60")
        self.ad_test = QtWidgets.QLineEdit(self.Klassifikation)
        self.ad_test.setGeometry(QtCore.QRect(40, 280, 421, 20))
        self.ad_test.setObjectName("ad_test")
        self.check_train_3 = QtWidgets.QCheckBox(self.Klassifikation)
        self.check_train_3.setGeometry(QtCore.QRect(600, 80, 101, 17))
        self.check_train_3.setObjectName("check_train_3")
        self.che_mue = QtWidgets.QCheckBox(self.Klassifikation)
        self.che_mue.setGeometry(QtCore.QRect(340, 390, 291, 17))
        self.che_mue.setObjectName("che_mue")
        self.check_neighbor = QtWidgets.QRadioButton(self.Klassifikation)
        self.check_neighbor.setGeometry(QtCore.QRect(180, 80, 111, 17))
        self.check_neighbor.setObjectName("check_neighbor")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.Klassifikation)
        self.tabWidget_2.setGeometry(QtCore.QRect(570, 110, 221, 351))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.ad_layer = QtWidgets.QLineEdit(self.tab)
        self.ad_layer.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.ad_layer.setObjectName("ad_layer")
        self.ad_alpha = QtWidgets.QLineEdit(self.tab)
        self.ad_alpha.setGeometry(QtCore.QRect(30, 80, 113, 20))
        self.ad_alpha.setObjectName("ad_alpha")
        self.com_act = QtWidgets.QComboBox(self.tab)
        self.com_act.setGeometry(QtCore.QRect(20, 180, 141, 22))
        self.com_act.setObjectName("com_act")
        self.com_act.addItem("")
        self.com_act.addItem("")
        self.com_act.addItem("")
        self.com_act.addItem("")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(40, 10, 91, 16))
        self.label_21.setObjectName("label_21")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(40, 160, 91, 16))
        self.label_31.setObjectName("label_31")
        self.com_solv = QtWidgets.QComboBox(self.tab)
        self.com_solv.setGeometry(QtCore.QRect(20, 240, 141, 22))
        self.com_solv.setObjectName("com_solv")
        self.com_solv.addItem("")
        self.com_solv.addItem("")
        self.com_solv.addItem("")
        self.label_32 = QtWidgets.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(40, 220, 91, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab)
        self.label_33.setGeometry(QtCore.QRect(30, 60, 91, 16))
        self.label_33.setObjectName("label_33")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.ad_maxdepth = QtWidgets.QLineEdit(self.tab_3)
        self.ad_maxdepth.setGeometry(QtCore.QRect(40, 30, 113, 20))
        self.ad_maxdepth.setObjectName("ad_maxdepth")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(60, 10, 91, 16))
        self.label_15.setObjectName("label_15")
        self.ad_mls = QtWidgets.QLineEdit(self.tab_3)
        self.ad_mls.setGeometry(QtCore.QRect(40, 80, 113, 20))
        self.ad_mls.setObjectName("ad_mls")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(50, 60, 101, 16))
        self.label_20.setObjectName("label_20")
        self.che_bal_2 = QtWidgets.QCheckBox(self.tab_3)
        self.che_bal_2.setGeometry(QtCore.QRect(10, 120, 291, 17))
        self.che_bal_2.setObjectName("che_bal_2")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.com_kernel = QtWidgets.QComboBox(self.tab_2)
        self.com_kernel.setGeometry(QtCore.QRect(30, 20, 141, 22))
        self.com_kernel.setObjectName("com_kernel")
        self.com_kernel.addItem("")
        self.com_kernel.addItem("")
        self.com_kernel.addItem("")
        self.com_kernel.addItem("")
        self.com = QtWidgets.QComboBox(self.tab_2)
        self.com.setGeometry(QtCore.QRect(30, 80, 141, 22))
        self.com.setObjectName("com")
        self.com.addItem("")
        self.com.addItem("")
        self.ad_gam = QtWidgets.QLineEdit(self.tab_2)
        self.ad_gam.setGeometry(QtCore.QRect(40, 140, 113, 20))
        self.ad_gam.setObjectName("ad_gam")
        self.ad_C = QtWidgets.QLineEdit(self.tab_2)
        self.ad_C.setGeometry(QtCore.QRect(40, 180, 113, 20))
        self.ad_C.setObjectName("ad_C")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(60, 0, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(70, 60, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(70, 120, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(70, 160, 47, 13))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(60, 210, 81, 16))
        self.label_14.setObjectName("label_14")
        self.ad_degree = QtWidgets.QLineEdit(self.tab_2)
        self.ad_degree.setGeometry(QtCore.QRect(40, 230, 113, 20))
        self.ad_degree.setObjectName("ad_degree")
        self.che_bal = QtWidgets.QCheckBox(self.tab_2)
        self.che_bal.setGeometry(QtCore.QRect(10, 280, 291, 17))
        self.che_bal.setObjectName("che_bal")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(322, 302, 47, 13))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tabWidget.addTab(self.Klassifikation, "")
        self.Feature = QtWidgets.QWidget()
        self.Feature.setObjectName("Feature")
        self.call_save_feature = QtWidgets.QToolButton(self.Feature)
        self.call_save_feature.setGeometry(QtCore.QRect(60, 130, 81, 19))
        self.call_save_feature.setObjectName("call_save_feature")
        self.call_dialog_ob = QtWidgets.QToolButton(self.Feature)
        self.call_dialog_ob.setGeometry(QtCore.QRect(290, 60, 81, 19))
        self.call_dialog_ob.setObjectName("call_dialog_ob")
        self.ad_meas_ob = QtWidgets.QLineEdit(self.Feature)
        self.ad_meas_ob.setGeometry(QtCore.QRect(50, 60, 201, 20))
        self.ad_meas_ob.setObjectName("ad_meas_ob")
        self.label_9 = QtWidgets.QLabel(self.Feature)
        self.label_9.setGeometry(QtCore.QRect(60, 20, 521, 16))
        self.label_9.setObjectName("label_9")
        self.call_dialog_per = QtWidgets.QToolButton(self.Feature)
        self.call_dialog_per.setGeometry(QtCore.QRect(670, 60, 81, 19))
        self.call_dialog_per.setObjectName("call_dialog_per")
        self.ad_meas_per = QtWidgets.QLineEdit(self.Feature)
        self.ad_meas_per.setGeometry(QtCore.QRect(430, 60, 201, 20))
        self.ad_meas_per.setObjectName("ad_meas_per")
        self.label_17 = QtWidgets.QLabel(self.Feature)
        self.label_17.setGeometry(QtCore.QRect(80, 40, 47, 13))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Feature)
        self.label_18.setGeometry(QtCore.QRect(440, 40, 47, 13))
        self.label_18.setObjectName("label_18")
        self.che_midfre = QtWidgets.QCheckBox(self.Feature)
        self.che_midfre.setGeometry(QtCore.QRect(60, 170, 141, 17))
        self.che_midfre.setObjectName("che_midfre")
        self.che_band = QtWidgets.QCheckBox(self.Feature)
        self.che_band.setGeometry(QtCore.QRect(60, 200, 111, 17))
        self.che_band.setObjectName("che_band")
        self.che_woe = QtWidgets.QCheckBox(self.Feature)
        self.che_woe.setGeometry(QtCore.QRect(60, 230, 101, 17))
        self.che_woe.setObjectName("che_woe")
        self.che_schie = QtWidgets.QCheckBox(self.Feature)
        self.che_schie.setGeometry(QtCore.QRect(60, 260, 70, 17))
        self.che_schie.setObjectName("che_schie")
        self.call_dialog_lee = QtWidgets.QToolButton(self.Feature)
        self.call_dialog_lee.setGeometry(QtCore.QRect(670, 130, 81, 19))
        self.call_dialog_lee.setObjectName("call_dialog_lee")
        self.label_19 = QtWidgets.QLabel(self.Feature)
        self.label_19.setGeometry(QtCore.QRect(440, 110, 47, 13))
        self.label_19.setObjectName("label_19")
        self.ad_meas_lee = QtWidgets.QLineEdit(self.Feature)
        self.ad_meas_lee.setGeometry(QtCore.QRect(430, 130, 201, 20))
        self.ad_meas_lee.setObjectName("ad_meas_lee")
        self.tabWidget.addTab(self.Feature, "")
        self.msg_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.msg_text.setGeometry(QtCore.QRect(80, 491, 256, 161))
        self.msg_text.setObjectName("msg_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ad_xls, self.call_xls)
        MainWindow.setTabOrder(self.call_xls, self.ad_ver)
        MainWindow.setTabOrder(self.ad_ver, self.ad_name_meas)
        MainWindow.setTabOrder(self.ad_name_meas, self.call_start_meas)
        MainWindow.setTabOrder(self.call_start_meas, self.call_stop_meas)
        MainWindow.setTabOrder(self.call_stop_meas, self.call_vz)
        MainWindow.setTabOrder(self.call_vz, self.ad_val_meas)
        MainWindow.setTabOrder(self.ad_val_meas, self.call_com)
        MainWindow.setTabOrder(self.call_com, self.ad_classi)
        MainWindow.setTabOrder(self.ad_classi, self.check_train)
        MainWindow.setTabOrder(self.check_train, self.check_train_3)
        MainWindow.setTabOrder(self.check_train_3, self.check_neuro)
        MainWindow.setTabOrder(self.check_neuro, self.check_bayes)
        MainWindow.setTabOrder(self.check_bayes, self.check_svm)
        MainWindow.setTabOrder(self.check_svm, self.call_dia_classi)
        MainWindow.setTabOrder(self.call_dia_classi, self.ad_train)
        MainWindow.setTabOrder(self.ad_train, self.call_dia_train)
        MainWindow.setTabOrder(self.call_dia_train, self.ad_test)
        MainWindow.setTabOrder(self.ad_test, self.call_dia_test)
        MainWindow.setTabOrder(self.call_dia_test, self.ad_val)
        MainWindow.setTabOrder(self.ad_val, self.call_dia_val)
        MainWindow.setTabOrder(self.call_dia_val, self.call_start_classi)
        MainWindow.setTabOrder(self.call_start_classi, self.call_stop_classi)
        MainWindow.setTabOrder(self.call_stop_classi, self.che_mue)
        MainWindow.setTabOrder(self.che_mue, self.ad_meas_ob)
        MainWindow.setTabOrder(self.ad_meas_ob, self.call_dialog_ob)
        MainWindow.setTabOrder(self.call_dialog_ob, self.ad_meas_per)
        MainWindow.setTabOrder(self.ad_meas_per, self.call_dialog_per)
        MainWindow.setTabOrder(self.call_dialog_per, self.call_save_feature)
        MainWindow.setTabOrder(self.call_save_feature, self.che_midfre)
        MainWindow.setTabOrder(self.che_midfre, self.che_band)
        MainWindow.setTabOrder(self.che_band, self.che_woe)
        MainWindow.setTabOrder(self.che_woe, self.che_schie)
        MainWindow.setTabOrder(self.che_schie, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.msg_text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "XLS in CSV"))
        self.call_xls.setText(_translate("MainWindow", "in CSV"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CSV), _translate("MainWindow", "XLS in CSV"))
        self.label_5.setText(_translate("MainWindow", "Messdatenaufnahme"))
        self.call_start_meas.setText(_translate("MainWindow", "start"))
        self.call_stop_meas.setText(_translate("MainWindow", "stop"))
        self.label_13.setText(_translate("MainWindow", "Start der Kommunikation"))
        self.label_11.setText(_translate("MainWindow", "Name Messdatei"))
        self.call_vz.setText(_translate("MainWindow", "Load"))
        self.call_com.setText(_translate("MainWindow", "Start Kom. "))
        self.label_10.setText(_translate("MainWindow", "verzeichnis"))
        self.label_2.setText(_translate("MainWindow", "Anzahl der Messdaten"))
        self.che_sens.setText(_translate("MainWindow", "Sensor"))
        self.che_classi.setText(_translate("MainWindow", "Klassifikation"))
        self.che_read.setText(_translate("MainWindow", "Messen"))
        self.msg_classi.setText(_translate("MainWindow", "TextLabel"))
        self.msg_state.setText(_translate("MainWindow", "TextLabel"))
        self.msg_state_ard.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Messdaten), _translate("MainWindow", "Messdaten"))
        self.check_neuro.setText(_translate("MainWindow", "Neuronale Netze"))
        self.call_dia_classi.setText(_translate("MainWindow", "Load"))
        self.check_bayes.setText(_translate("MainWindow", "Bayes"))
        self.check_svm.setText(_translate("MainWindow", "SVM"))
        self.label_3.setText(_translate("MainWindow", "Klassifikator"))
        self.check_train.setText(_translate("MainWindow", "Load Train Data"))
        self.label_4.setText(_translate("MainWindow", "Lade Klassifikationsdaten"))
        self.call_dia_train.setText(_translate("MainWindow", "Load"))
        self.label_39.setText(_translate("MainWindow", "Trainingsdaten Objekt"))
        self.label_59.setText(_translate("MainWindow", "Validierungsdaten Objekt"))
        self.call_dia_val.setText(_translate("MainWindow", "Load"))
        self.call_stop_classi.setText(_translate("MainWindow", "stop"))
        self.call_start_classi.setText(_translate("MainWindow", "start"))
        self.call_dia_test.setText(_translate("MainWindow", "Load"))
        self.label_60.setText(_translate("MainWindow", "Testdaten"))
        self.check_train_3.setText(_translate("MainWindow", "save Train Data"))
        self.che_mue.setText(_translate("MainWindow", "Klassifikator für Mikrocontroller"))
        self.check_neighbor.setText(_translate("MainWindow", "Decision tree"))
        self.com_act.setItemText(0, _translate("MainWindow", "relu"))
        self.com_act.setItemText(1, _translate("MainWindow", "identity"))
        self.com_act.setItemText(2, _translate("MainWindow", "logistic"))
        self.com_act.setItemText(3, _translate("MainWindow", "tanh"))
        self.label_21.setText(_translate("MainWindow", "Hidden Layer Size"))
        self.label_31.setText(_translate("MainWindow", "Activation"))
        self.com_solv.setItemText(0, _translate("MainWindow", "adam"))
        self.com_solv.setItemText(1, _translate("MainWindow", "lbfgs"))
        self.com_solv.setItemText(2, _translate("MainWindow", "sgd"))
        self.label_32.setText(_translate("MainWindow", "Solver"))
        self.label_33.setText(_translate("MainWindow", "alpha"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "neuro"))
        self.label_15.setText(_translate("MainWindow", "Maximale Tiefe"))
        self.label_20.setText(_translate("MainWindow", "mindest blatt größe"))
        self.che_bal_2.setText(_translate("MainWindow", "unausgeglichener Datensatz"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "tree"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Bayes"))
        self.com_kernel.setItemText(0, _translate("MainWindow", "rbf"))
        self.com_kernel.setItemText(1, _translate("MainWindow", "linear"))
        self.com_kernel.setItemText(2, _translate("MainWindow", "poly"))
        self.com_kernel.setItemText(3, _translate("MainWindow", "sigmoid"))
        self.com.setItemText(0, _translate("MainWindow", "ovr"))
        self.com.setItemText(1, _translate("MainWindow", "ovo"))
        self.label_6.setText(_translate("MainWindow", "Kernel"))
        self.label_7.setText(_translate("MainWindow", "Decision Funktion"))
        self.label_8.setText(_translate("MainWindow", "Gamma"))
        self.label_12.setText(_translate("MainWindow", "C"))
        self.label_14.setText(_translate("MainWindow", "Freiheitsgrad"))
        self.che_bal.setText(_translate("MainWindow", "unausgeglichener Datensatz"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "SVM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Klassifikation), _translate("MainWindow", "Klassifikator"))
        self.call_save_feature.setText(_translate("MainWindow", "Save Feature"))
        self.call_dialog_ob.setText(_translate("MainWindow", "Load"))
        self.label_9.setText(_translate("MainWindow", "Load Data and save feature"))
        self.call_dialog_per.setText(_translate("MainWindow", "Load"))
        self.label_17.setText(_translate("MainWindow", "Object"))
        self.label_18.setText(_translate("MainWindow", "Person"))
        self.che_midfre.setText(_translate("MainWindow", "Mittenfrequenz"))
        self.che_band.setText(_translate("MainWindow", "Bandbreite"))
        self.che_woe.setText(_translate("MainWindow", "Wölbung"))
        self.che_schie.setText(_translate("MainWindow", "Schiefe"))
        self.call_dialog_lee.setText(_translate("MainWindow", "Load"))
        self.label_19.setText(_translate("MainWindow", "leer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Feature), _translate("MainWindow", "Feature"))