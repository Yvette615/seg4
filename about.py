# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_help(object):
    def setupUi(self, Form_help):
        Form_help.setObjectName("Form_help")
        Form_help.resize(1300, 820)
        self.frame_help = QtWidgets.QFrame(Form_help)
        self.frame_help.setGeometry(QtCore.QRect(10, 10, 1280, 800))
        self.frame_help.setStyleSheet("\n"
"#frame_help{\n"
"background-image: url(:/lognpic/素材/背景.png);\n"
"border-radius:15px;}\n"
"")
        self.frame_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_help.setObjectName("frame_help")
        self.pushButton_back = QtWidgets.QPushButton(self.frame_help)
        self.pushButton_back.setGeometry(QtCore.QRect(1150, 730, 91, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_back.setStyleSheet("border-radius: 5px; /* 边框半径 */\n"
"\n"
"background-color: rgb(230, 230, 230);\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_back.setObjectName("pushButton_back")
        self.frame_windows = QtWidgets.QFrame(self.frame_help)
        self.frame_windows.setGeometry(QtCore.QRect(360, 240, 641, 281))
        self.frame_windows.setStyleSheet("#frame_windows{\n"
"background-color: rgb(245, 245, 245,170);\n"
"border-radius:20px; \n"
"border:5px solid rgb(130, 130, 130);}")
        self.frame_windows.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_windows.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_windows.setObjectName("frame_windows")
        self.label_help = QtWidgets.QLabel(self.frame_windows)
        self.label_help.setGeometry(QtCore.QRect(260, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_help.setFont(font)
        self.label_help.setObjectName("label_help")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_windows)
        self.textBrowser.setGeometry(QtCore.QRect(40, 80, 571, 181))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("#textBrowser{\n"
"background-color: rgb(245, 245, 245,0);\n"
"border-radius:15px;}")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form_help)
        QtCore.QMetaObject.connectSlotsByName(Form_help)

    def retranslateUi(self, Form_help):
        _translate = QtCore.QCoreApplication.translate
        Form_help.setWindowTitle(_translate("Form_help", "Form"))
        self.pushButton_back.setText(_translate("Form_help", "返回"))
        self.label_help.setText(_translate("Form_help", "版本介绍"))
        self.textBrowser.setHtml(_translate("Form_help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'黑体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">欢迎使用“OCTA”医学影像分割系统，版本号v.1.0</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">联系邮箱：2374127835@qq.com</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">更新日期：2023年4月</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">如有问题请及时与我们联系，我们会在1—2个工作日之内回复您，感谢使用！</span></p></body></html>"))
import picture_rc