# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wind.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from  PyQt5.QtWidgets import QDialog,QMainWindow,QApplication
import os
import datetime
if not os.path.exists("WindNote"):
    os.mkdir("WindNote")
    fp=open('WindNote/type.txt','w')
    fp.write("默认\n")
    fp.close()
    fs=open('WindNote/默认.txt','w')
    fs.write("笔记本名称：默认"+"\n"+"笔记本创建时间："+datetime.datetime.now().strftime('%Y-%m-%d')+"\n\n\n\n")
class Ui_MainWindow(object):
    def search(self):
        self.plainTextEdit.setPlainText('')
        fp=open('WindNote/'+self.comboBox.currentText()+".txt",'r')
        obj=fp.read()
        objs=obj.split('\n\n')
        for i in objs:
            if self.lineEdit.text() in i:
                self.plainTextEdit.appendPlainText(i+"\n") 
        fp.close()      
    def save(self):
        note=self.comboBox.currentText()
        title=self.lineEdit.text()
        essay=self.plainTextEdit.toPlainText()
        timenow=datetime.datetime.now().strftime('%Y-%m-%d')
        fp=open('WindNote/'+note+".txt",'a')
        fp.write('时间：'+timenow+"\n"+'主题：'+title+"\n"+'内容：'+essay+"\n\n")
        fp.close()
        self.lineEdit.setText('')
        self.plainTextEdit.setPlainText('')
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 301)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 33))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(50, 10, 81, 33))
        self.comboBox.setObjectName("comboBox")
        fp=open('WindNote/type.txt','r')
        items=fp.read()
        self.comboBox.addItems(items.split('\n')[0:-1])
        fp.close()
        self.plainTextEdit = QtWidgets.QPlainTextEdit(MainWindow)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 40, 471, 261))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(140, 10, 31, 33))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(180, 10, 111, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(410, 10, 51, 33))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 10, 51, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 10, 41, 33))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.search)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Dialog", "风语"))
        self.label.setText(_translate("Dialog", "本本"))
        self.label_3.setText(_translate("Dialog", "主题"))
        self.pushButton.setText(_translate("Dialog", "保存"))
        self.pushButton_2.setText(_translate("Dialog", "新建"))
        self.pushButton_3.setText(_translate("Dialog", "搜索"))


class Ui_Dialog(object):
    import os
    def makeDir(self):
        if not os.path.exists('WindNote/'+self.lineEdit.text()+".txt"):
            fp=open("WindNote/"+self.lineEdit.text()+".txt",'w')
            fp.write("笔记本名称："+self.lineEdit.text()+"\n"+"笔记本创建时间："+datetime.datetime.now().strftime('%Y-%m-%d')+"\n\n\n\n")
            fp.close()
            fs=open('WindNote/type.txt','a')
            fs.write(self.lineEdit.text()+"\n")
            fs.close()
            self.lineEdit.setText("创建成功，重启后生效")
        else:
            self.lineEdit.setText("这个本子已经存在")
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(212, 98)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 10, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 81, 29))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 60, 81, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.makeDir)
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "名字"))
        self.pushButton.setText(_translate("Dialog", "返回"))
        self.pushButton_2.setText(_translate("Dialog", "创建"))

class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        
class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog()
        self.child.setupUi(self)


if __name__=='__main__':

    app=QApplication(sys.argv)
    window=parentWindow()
    child=childWindow()
    btn=window.main_ui.pushButton_2
    btn.clicked.connect(child.show)
    btn2=child.child.pushButton
    btn2.clicked.connect(child.close)
    window.show()
    sys.exit(app.exec_())
