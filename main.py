# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:57:33 2022

@author: hasan
"""

#-------------------KÜTÜPHANE---------------------
#-------------------------------------------------
import sys, os
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *#QtWidgets.QApplications gibi tanımlamalara gerek kalmaz.
from anaSayfa import *





#-------------------UYGULAMA----------------------
#-------------------------------------------------
uygulama = QApplication(sys.argv)
anaPencere = QMainWindow()
anaPencere.show()
ui = Ui_MainWindow()#Erişimleri buradan yapacağız. Örneğin lbl. gibi
ui.setupUi(anaPencere)#Tasarımdaki form ile pencere birleştirme




#-------------------FONKSİYONLAR------------------
#-------------------------------------------------
def HESAPLA():
    if(ui.cmbFormul.currentText() == "Harris Benedict"):
        HARRISBENEDICT()
    if(ui.cmbFormul.currentText() == "Schoffield"):
        SCHOFFIELD()

def HARRISBENEDICT():
    _boy = int(ui.lneBoy.text())
    _kilo = int(ui.lneKilo.text())
    _yas = int(ui.lneYas.text())
    
    if(ui.cmbCinsiyet.currentText()=="Kadın"):
        deger = 655 + (9.6*_kilo) + (1.8*_boy) - (4.7*_yas)
        ui.lneBMH.setText(str(deger))
        
    if(ui.cmbCinsiyet.currentText()=="Erkek"):
        deger = 66.5 + (13.7*_kilo) + (5*_boy) - (6.7*_yas)
        ui.lneBMH.setText(str(deger))




def SCHOFFIELD():
    _boy = int(ui.lneBoy.text())
    _kilo = int(ui.lneKilo.text())
    _yas = int(ui.lneYas.text())

    if(ui.cmbCinsiyet.currentText()=="Kadın"):
        if(_yas>=18 and _yas<=29):
            deger = (14.8*_kilo) + 486
            ui.lneBMH.setText(str(deger))
        
        if(_yas>=30 and _yas<=59):
            deger = (8.1*_kilo) + 846
            ui.lneBMH.setText(str(deger))
        
        if(_yas>=60):
            deger = (9*_kilo) + 658
            ui.lneBMH.setText(str(deger))


    if(ui.cmbCinsiyet.currentText()=="Erkek"):
        if(_yas>=18 and _yas<=29):
            deger = (15*_kilo) + 692
            ui.lneBMH.setText(str(deger))
        
        if(_yas>=30 and _yas<=59):
            deger = (11.4*_kilo) + 873
            ui.lneBMH.setText(str(deger))
        
        if(_yas>=60):
            deger = (11.7*_kilo) + 587
            ui.lneBMH.setText(str(deger))





ui.btnHesapla.clicked.connect(HESAPLA)










sys.exit(uygulama.exec_())