# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
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
        self.frame_windows.setGeometry(QtCore.QRect(40, 40, 1071, 721))
        self.frame_windows.setStyleSheet("#frame_windows{\n"
"background-color: rgb(245, 245, 245,170);\n"
"border-radius:20px; \n"
"border:5px solid rgb(170, 200, 220);}")
        self.frame_windows.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_windows.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_windows.setObjectName("frame_windows")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_windows)
        self.textBrowser.setGeometry(QtCore.QRect(30, 90, 1021, 611))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("#textBrowser{\n"
"background-color: rgb(245, 245, 245,0);\n"
"border-radius:15px;}")
        self.textBrowser.setObjectName("textBrowser")
        self.label_help = QtWidgets.QLabel(self.frame_windows)
        self.label_help.setGeometry(QtCore.QRect(470, 30, 151, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_help.setFont(font)
        self.label_help.setObjectName("label_help")

        self.retranslateUi(Form_help)
        QtCore.QMetaObject.connectSlotsByName(Form_help)

    def retranslateUi(self, Form_help):
        _translate = QtCore.QCoreApplication.translate
        Form_help.setWindowTitle(_translate("Form_help", "Form"))
        self.pushButton_back.setText(_translate("Form_help", "返回"))
        self.textBrowser.setHtml(_translate("Form_help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'黑体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">        OCTA</span><span style=\" font-family:\'宋体\'; font-size:14pt;\">医学影像分割系统 是一个全自动的病灶位置自动识别系统，用于识别医疗影像中的病灶位置并在影像上标注出病灶位置以辅助诊疗。OCTA医学影像分割系统可以一次识别多张医疗影像并同时给出分割结果，用户可以在系统内浏览病灶分割结果，进行文字批注解和自动生成诊断报告。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/新前缀/素材/图片1.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">    ①“预测图像”图框：导入特定路径下的待预测图像后，待预测图像将显示在“预测图像”图框内。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">    ②“分割结果”图框：在系统完成预测后，分割结果将会一一对应待预测图像显示在“分割结果”图框内。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">    ③预测。点击“预测”按钮，系统开始运行，预测已导入的图像分割结果。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">    ④清除。清除系统已导入的待预测图像和分割结果。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">    ⑤左右切换。点击左右切换按钮可以同时切换“预测图像”和“分割结果”图框内的内容，浏览全部图像分割结果。</span></p></body></html>"))
        self.label_help.setText(_translate("Form_help", "帮助手册"))
import picture_rc
