from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from GUI import Ui_Dialog
import sys
from math import sqrt

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.setFixedSize(239, 351)
Dialog.show()



class ex():
    def __init__(self, value, act, curr_dig):
        self.value = value
        self.act = act
        self.curr_dig = curr_dig
        self.sqrt_flag = 0
        self.evaluted_flag = 0



    def add_dig(self, dig):
        if dig == ".":
            for i in self.curr_dig:
                if i == ".":
                    return

            if len(self.curr_dig) == 0 : return

        if self.evaluted_flag == 1:
            self.curr_dig = ""
            self.evaluted_flag = 0

        self.curr_dig += dig
        ui.label.setText(self.curr_dig)




    def change_sign(self):
        if len(self.curr_dig) == 0: return

        if self.curr_dig[0] != "-":
            self.curr_dig = "-" + self.curr_dig

        else:
            self.curr_dig = self.curr_dig[1:]

        ui.label.setText(self.curr_dig)




    def step_back(self):
        if self.evaluted_flag == 1 or self.sqrt_flag == 1: return

        elif len(self.curr_dig) == 2 and self.curr_dig[0] == "-":
            self.curr_dig = ""

        else:
            self.curr_dig = self.curr_dig[:-1]

        ui.label.setText(self.curr_dig)




    def to_sqrt(self):
        if len(self.curr_dig) == 0 or self.curr_dig[0] == "-":
            return

        else:
            self.curr_dig = str(sqrt(float(self.curr_dig)))

        self.sqrt_flag = 1
        ui.label.setText(self.curr_dig)




    def change_value(self):
        if self.act == "+":
            self.value += float(self.curr_dig)
        elif self.act == "-":
            self.value -= float(self.curr_dig)
        elif self.act == "x":
            self.value *= float(self.curr_dig)
        elif self.act == "/":
            self.value /= float(self.curr_dig)

        self.curr_dig = str(self.value)
        self.evaluted_flag = 1
        self.sqrt_flag = 0

        ui.label.setText(self.curr_dig)




    def to_sum(self):
        if self.act == "":
            self.act = "+"
            self.value = float(self.curr_dig)
            self.sqrt_flag = 0
            self.evaluted_flag = 1

        else:
            self.change_value()
            self.act = "+"




    def to_minus(self):
        if self.act == "":
            self.act = "-"
            self.value = float(self.curr_dig)
            self.evaluted_flag = 1

        else:
            self.change_value()
            self.act = "-"




    def to_multiple(self):
        if self.act == "":
            self.act = "x"
            self.value = float(self.curr_dig)
            self.evaluted_flag = 1

        else:
            self.change_value()
            self.act = "x"




    def to_division(self):
        if self.act == "":
            self.act = "/"
            self.value = float(self.curr_dig)
            self.evaluted_flag = 1

        else:
            self.change_value()
            self.act = "/"
            ui.label.setText(self.curr_dig)




    def to_equal(self):
        self.change_value()
        self.value = 0
        self.act = ""
        self.sqrt_flag = 0




    def clean(self):
        self.value = 0
        self.act = ""
        self.curr_dig = ""
        self.sqrt_flag = 0
        self.evaluted_flag = 0
        ui.label.setText(self.curr_dig)




a = ex(0, "", "")
ui.pushButton.clicked.connect(partial(a.add_dig, "1"))
ui.pushButton_2.clicked.connect(partial(a.add_dig, "2"))
ui.pushButton_3.clicked.connect(partial(a.add_dig, "3"))
ui.pushButton_4.clicked.connect(partial(a.add_dig, "4"))
ui.pushButton_5.clicked.connect(partial(a.add_dig, "5"))
ui.pushButton_6.clicked.connect(partial(a.add_dig, "6"))
ui.pushButton_7.clicked.connect(partial(a.add_dig, "7"))
ui.pushButton_8.clicked.connect(partial(a.add_dig, "8"))
ui.pushButton_9.clicked.connect(partial(a.add_dig, "9"))
ui.pushButton_17.clicked.connect(partial(a.add_dig, "0"))
ui.pushButton_18.clicked.connect(partial(a.add_dig, "."))

ui.pushButton_20.clicked.connect(a.change_sign) #+/-
ui.pushButton_11.clicked.connect(a.step_back)   #<=
ui.pushButton_12.clicked.connect(a.to_sqrt)     #sqrt

ui.pushButton_16.clicked.connect(a.to_sum)      #+
ui.pushButton_14.clicked.connect(a.to_minus)    #-
ui.pushButton_15.clicked.connect(a.to_multiple) #x
ui.pushButton_13.clicked.connect(a.to_division) #/
ui.pushButton_19.clicked.connect(a.to_equal)    #=

ui.pushButton_10.clicked.connect(a.clean)       #C


sys.exit(app.exec_())