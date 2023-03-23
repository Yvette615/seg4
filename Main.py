import sys, time
import os
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainframe import *
from logn import *
from choose import *
from report import *
from help import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import CT.predict as predict
import Convid19.paddleSeg.infer as infer
import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF


class MyWindow_report(QMainWindow, Ui_Form_report):
    def __init__(self, parent=None):
        super(MyWindow_report, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.pushButton_back.clicked.connect(lambda: self.close())
        self.pushButton_out.clicked.connect(lambda: self.topdf())  # 转化成pdf

    def topdf(self):
        pdf = FPDF(format='letter', unit='cm')
        pdf.add_page()
        pdf.set_top_margin(2.54)
        pdf.set_left_margin(2.18)
        for i in range(len(MyWin.choicepiclist)):
            pdf.image(MyWin.choicepiclist[i])
        text = self.textEdit_imfo.toPlainText()
        # pdf.add_font('youyuan','','youyuan.ttf',True)
        # pdf.set_font("youyuan", size=12)
        # pdf.cell(0, 0, u"诊断说明", align="C")
        # pdf.cell(0, 0, text, align='L')
        pdf.output("unicode2.pdf", 'F')  # 写好的
        msg_box = QMessageBox.information(self, '导出成功', '已成功导出PDF报告')


class MyWindow_choose(QMainWindow, Ui_Form_choose):
    def __init__(self, parent=None):
        super(MyWindow_choose, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.pushButton_confirm.clicked.connect(self.choice)

    def choice(self):
        global leixing  # 全局变量
        if self.radioButton_shipan.isChecked() == True:
            print("shipan")
            leixing = "shipan"
        MyWin.choice_pre()


# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 00:03:15 2021

@author: Wkx0530
"""
class MyWindow(QMainWindow, Ui_Form_main):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        MyWin_choose = MyWindow_choose()
        self.pushButton_close.clicked.connect(lambda: {MyWin_choose.show()})
        self.imgName = ""
        self.mixnum = 0
        self.listnum = 0
        self.listfile = []
        self.listpic = []
        self.listbtn = []

        self.pushButton_right.clicked.connect(self.nextpic)  # 下一张
        self.pushButton_indir.clicked.connect(self.choosedir)  # 选择路径
        self.pushButton_pre.clicked.connect(self.predict)  # 预测
        self.pushButton_left.clicked.connect(self.backpic)  # 上一张
        self.pushButton_delete.clicked.connect(self.delete)  # 清空
        self.pushButton_back.clicked.connect(lambda: self.close())  # 返回首页
        self.pushButton_export.clicked.connect(lambda: self.MyWin_report_show())  # 导出报告

        self.number = 0
        self.topFiller = self.frame_show1
        self.scroll = QScrollArea()
        self.scroll.setGeometry(0, 0, 975, 135)
        self.scroll.setWidget(self.topFiller)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox.addSpacing(0)
        self.vbox.addWidget(self.scroll)
        self.frame_show2.setLayout(self.vbox)
        self.frame_show1.setLayout(self.hbox)

        self.choicepiclist = []

    def MyWin_report_show(self):
        global leixing
        m = 0
        for i in range(len(self.listbtn)):
            if self.listbtn[i].isChecked():
                if m <= 4:
                    print(i, "ischecked")
                    m = m + 1
                    if m == 1:
                        if leixing == "shipan":
                            for root, dirs, files in os.walk("CT/results/added_prediction/"):
                                files
                            png = QtGui.QPixmap("CT/results/added_prediction/" + files[i]).scaled(
                                MyWin_report.label_upleft.width(), MyWin_report.label_upleft.height())
                            MyWin_report.label_upleft.setPixmap(png)
                            self.choicepiclist.append("CT/results/added_prediction/" + files[i])

                    if m == 2:
                        if leixing == "shipan":
                            for root, dirs, files in os.walk("CT/results/added_prediction/"):
                                files
                            png = QtGui.QPixmap("CT/results/added_prediction/" + files[i]).scaled(
                                MyWin_report.label_upleft.width(), MyWin_report.label_upleft.height())
                            MyWin_report.label_upright.setPixmap(png)
                            self.choicepiclist.append("CT/results/added_prediction/" + files[i])

                    if m == 3:
                        if leixing == "shipan":
                            for root, dirs, files in os.walk("CT/results/added_prediction/"):
                                files
                            png = QtGui.QPixmap("CT/results/added_prediction/" + files[i]).scaled(
                                MyWin_report.label_upleft.width(), MyWin_report.label_upleft.height())
                            MyWin_report.label_downleft.setPixmap(png)
                            self.choicepiclist.append("CT/results/added_prediction/" + files[i])

                    if m == 4:
                        if leixing == "shipan":
                            for root, dirs, files in os.walk("CT/results/added_prediction/"):
                                files
                            png = QtGui.QPixmap("CT/results/added_prediction/" + files[i]).scaled(
                                MyWin_report.label_upleft.width(), MyWin_report.label_upleft.height())
                            MyWin_report.label_downright.setPixmap(png)
                            self.choicepiclist.append("CT/results/added_prediction/" + files[i])

        MyWin_report.show()

    def choosedir(self):  # 点击后选择导入的图像路径
        # imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", ".", "*.jpg;;*.png;;All Files(*)")
        root = tk.Tk()
        root.withdraw()
        _translate = QtCore.QCoreApplication.translate
        global leixing
        if leixing == "shipan":
            self.imgName = filedialog.askdirectory(initialdir=r'D:/pycharm/pythonProject/Seg4U/CT/')
        abs_dir = os.path.abspath('.')
        abs_dir = abs_dir + '/'
        self.imgName = self.imgName[len(abs_dir):]
        self.imgName = self.imgName + '/'
        print(self.imgName)
        self.imgName = r"D:\pycharm\pythonProject\Seg4U\CT\dataset\test"
        for root, dirs, files in os.walk(self.imgName):
            print(files)  # 当前路径下所有非目录子文件
        self.listfile = files
        jpg = QtGui.QPixmap(self.imgName + files[self.listnum]).scaled(self.label_pre_img.width(), self.label_pre_img.height())
        self.label_pre_img.setPixmap(jpg)
        self.maxnum = len(files)
        self.label_indir.setText(_translate("Form", "输入路径：" + self.imgName + self.listfile[self.listnum]))


    def choice_pre(self):
        global leixing
        _translate = QtCore.QCoreApplication.translate
        self.label_leixing.setText(_translate("Form", "影像类型：" + leixing))

    def nextpic(self):  # 切换查看下一张图片
        _translate = QtCore.QCoreApplication.translate
        if self.listnum != self.maxnum:
            self.listnum = self.listnum + 1
        if self.listnum == self.maxnum:
            self.listnum = self.maxnum - 1
            self.label_next.setText(_translate("Form", "已经是最后一张"))
            app.processEvents()
            time.sleep(1)
            self.label_next.setText(_translate("Form", ""))
        j = QtGui.QPixmap(self.imgName + self.listfile[self.listnum]).scaled(self.label_pre_img.width(),
                                                                             self.label_pre_img.height())
        self.label_pre_img.setPixmap(j)
        global leixing
        if leixing == "shipan":
            for root, dirs, files in os.walk("CT/results/added_prediction/"):
                files
            png = QtGui.QPixmap("CT/results/added_prediction/" + files[self.listnum]).scaled(self.label_div_img.width(),
                                                                                             self.label_div_img.height())
            self.label_div_img.setPixmap(png)
            for root, dirs, files in os.walk("CT/results/added/"):
                files
            png = QtGui.QPixmap("CT/results/added/" + files[self.listnum]).scaled(self.label_pre_img.width(),
                                                                                             self.label_pre_img.height())
            self.label_pre_img.setPixmap(png)
            self.label_indir.setText(_translate("Form", "输入路径：" + self.imgName + self.listfile[self.listnum]))
            self.label_outdir.setText(_translate("Form", "输出路径：" + "CT/results/added_prediction/" + files[self.listnum]))

    def backpic(self):  # 切换查看上一张图片
        _translate = QtCore.QCoreApplication.translate
        if self.listnum != -1:
            self.listnum = self.listnum - 1
        if self.listnum == -1:
            self.listnum = 0
            self.label_next.setText(_translate("Form", "已经是第一张"))
            app.processEvents()
            time.sleep(1)
            self.label_next.setText(_translate("Form", ""))
        j = QtGui.QPixmap(self.imgName + self.listfile[self.listnum]).scaled(self.label_pre_img.width(),
                                                                             self.label_pre_img.height())
        self.label_pre_img.setPixmap(j)
        global leixing
        if leixing == "shipan":
            for root, dirs, files in os.walk("CT/results/added_prediction/"):
                files
            png = QtGui.QPixmap("CT/results/added_prediction/" + files[self.listnum]).scaled(self.label_div_img.width(),
                                                                                             self.label_div_img.height())
            self.label_div_img.setPixmap(png)
            for root, dirs, files in os.walk("CT/results/added/"):
                files
            png = QtGui.QPixmap("CT/results/added/" + files[self.listnum]).scaled(self.label_pre_img.width(),
                                                                                             self.label_pre_img.height())
            self.label_pre_img.setPixmap(png)
            self.label_indir.setText(_translate("Form", "输入路径：" + self.imgName + self.listfile[self.listnum]))
            self.label_outdir.setText(_translate("Form", "输出路径：" + "CT/results/added_prediction/" + files[self.listnum]))
    def predict(self):  # 点击后运行，并显示预测结果
        global leixing
        _translate = QtCore.QCoreApplication.translate
        # event = threading.Event()
        # self.movie = QMovie("D:/PycharmProjects/医学分割系统/素材/加载.gif")
        # self.label_div_img.setMovie(self.movie)
        # self.movie.start()
        # event.wait()

        self.listpic = []
        self.listbtn = []

        if leixing == "shipan":  ###
            predict.main(self.imgName, "CT/results/")
            for root, dirs, files in os.walk("CT/results/added_prediction/"):
                files
            png = QtGui.QPixmap("CT/results/added_prediction/" + files[self.listnum]).scaled(self.label_div_img.width(),
                                                                                             self.label_div_img.height())
            self.label_div_img.setPixmap(png)

            self.label_outdir.setText(_translate("Form", "输出路径：" + self.imgName + files[self.listnum]))

            self.frame_show1.resize(150 * self.maxnum, 85)

            QApplication.processEvents()
            for filename in range(self.maxnum):
                self.MapButton = QPushButton(self.topFiller)
                self.MapButton.setMinimumSize(70, 70)
                self.MapButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                btn_icon = "CT/results/added_prediction/" + files[filename]
                self.MapButton.setIcon(QtGui.QIcon(btn_icon))
                self.MapButton.setIconSize(QtCore.QSize(70, 70))
                self.listpic.append(self.MapButton)
                self.hbox.addWidget(self.MapButton)
                self.cbtn = QCheckBox(self.topFiller)
                self.listbtn.append(self.cbtn)
                self.hbox.addWidget(self.cbtn)
        if len(self.listpic) >= 1:
            self.listpic[0].clicked.connect(lambda: self.tiaozhuan(0))
        if len(self.listpic) >= 2:
            self.listpic[1].clicked.connect(lambda: self.tiaozhuan(1))
        if len(self.listpic) >= 3:
            self.listpic[2].clicked.connect(lambda: self.tiaozhuan(2))
        if len(self.listpic) >= 4:
            self.listpic[3].clicked.connect(lambda: self.tiaozhuan(3))
        if len(self.listpic) >= 5:
            self.listpic[4].clicked.connect(lambda: self.tiaozhuan(4))
        if len(self.listpic) >= 6:
            self.listpic[5].clicked.connect(lambda: self.tiaozhuan(5))
        if len(self.listpic) >= 7:
            self.listpic[6].clicked.connect(lambda: self.tiaozhuan(6))
        if len(self.listpic) >= 8:
            self.listpic[7].clicked.connect(lambda: self.tiaozhuan(7))
        if len(self.listpic) >= 9:
            self.listpic[8].clicked.connect(lambda: self.tiaozhuan(8))
        if len(self.listpic) >= 10:
            self.listpic[9].clicked.connect(lambda: self.tiaozhuan(9))
        if len(self.listpic) >= 11:
            self.listpic[10].clicked.connect(lambda: self.tiaozhuan(10))
        if len(self.listpic) >= 12:
            self.listpic[11].clicked.connect(lambda: self.tiaozhuan(11))




    def tiaozhuan(self, filename):
        _translate = QtCore.QCoreApplication.translate
        self.listnum = filename
        j = QtGui.QPixmap(self.imgName + self.listfile[self.listnum]).scaled(self.label_pre_img.width(),
                                                                             self.label_pre_img.height())
        self.label_pre_img.setPixmap(j)
        global leixing
        if leixing == "shipan":
            for root, dirs, files in os.walk("CT/results/added_prediction/"):
                files
            png = QtGui.QPixmap("CT/results/added_prediction/" + files[self.listnum]).scaled(self.label_div_img.width(),
                                                                                             self.label_div_img.height())
            self.label_div_img.setPixmap(png)
            self.label_indir.setText(_translate("Form", "输入路径：" + self.imgName + self.listfile[self.listnum]))
            self.label_outdir.setText(_translate("Form", "输出路径：" + "CT/results/added_prediction/" + files[self.listnum]))

    def delete(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_indir.setText(_translate("Form", "输入路径："))
        self.label_outdir.setText(_translate("Form", "输出路径："))
        self.label_leixing.setText(_translate("Form", "影像类型："))
        jpg = QtGui.QPixmap("")
        self.label_pre_img.setPixmap(jpg)
        self.label_div_img.setPixmap(jpg)
        for i in range(self.hbox.count()):
            self.hbox.removeItem(self.hbox.itemAt(i))
        for i in range(len(self.listbtn)):
            self.listbtn[i].deleteLater()
            self.listpic[i].deleteLater()



class MyWindow_help(QMainWindow, Ui_Form_help):
    def __init__(self, parent=None):
        super(MyWindow_help, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.pushButton_back.clicked.connect(lambda: self.close())


class MyWindow_logn(QMainWindow, Ui_Form_logn):
    def __init__(self, parent=None):
        super(MyWindow_logn, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.pushButton_help.clicked.connect(lambda: MyWin_help.show())   #这里少一个about    信号和槽
        self.pushButton_logn.clicked.connect(lambda: self.logn_in())
        self.pushButton_exit.clicked.connect(lambda: self.close())

    def logn_in(self):
        yonghuming = self.lineEdit_user.text()
        mima = self.lineEdit_password.text()

        if yonghuming == "1" and mima == "1":
            # MyWin_logn.close()
            MyWin.show()
        else:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '用户名或密码错误')
            msg_box.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWin_help = MyWindow_help()
    MyWin_logn = MyWindow_logn()
    MyWin_report = MyWindow_report()

    MyWin_logn.show()
    MyWin = MyWindow()
    sys.exit(app.exec_())