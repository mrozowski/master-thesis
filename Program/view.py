import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from bulb import Bulb
from button import *
from config import *
from model import PatientData


class View(object):
    def __init__(self):
        self.MainWindow = None
        self.presenter = None
        self.bulb_one = None
        self.bulb_two = None
        self.bulb_three = None
        self.status = None
        self.result = None
        self.data = []

    def set_presenter(self, _presenter):
        self.presenter = _presenter

    def showData(self, patient_data: PatientData):
        self.data[0].setText(patient_data.name)
        self.data[1].setText(str(patient_data.age))
        self.data[2].setText(patient_data.getGenderValue())
        self.data[3].setText(patient_data.getCpValue())
        self.data[4].setText(str(patient_data.trestbps))
        self.data[5].setText(str(patient_data.chol))
        self.data[6].setText(patient_data.getFbsValue())
        self.data[7].setText(str(patient_data.restecg))
        self.data[8].setText(str(patient_data.thalach))
        self.data[9].setText(patient_data.getExangValue())
        self.data[10].setText(str(patient_data.oldpeak))
        self.data[11].setText(patient_data.getSlopeValue())
        self.data[12].setText(str(patient_data.ca))
        self.data[13].setText(patient_data.getThalValue())

    def setupUi(self, ):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1000, 655)
        self.MainWindow.setStyleSheet("background-color: " + DARK_BLUE + ";")

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setStyleSheet("QLabel{color: " + TEXT_COLOR_LIGHT + "; }")
        self.centralwidget.setObjectName("centralwidget")

        self.menu = QtWidgets.QLabel(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(130, 45, 90, 20))
        self.menu.setFont(getFont(12))
        self.menu.setAlignment(QtCore.Qt.AlignCenter)
        self.menu.setObjectName("menu")

        self.dane = QtWidgets.QLabel(self.centralwidget)
        self.dane.setGeometry(QtCore.QRect(640, 45, 90, 20))

        self.dane.setFont(getFont(12))
        self.dane.setAlignment(QtCore.Qt.AlignCenter)
        self.dane.setObjectName("dane")

        menu_border = QtWidgets.QLabel(self.centralwidget)
        menu_border.setGeometry(QtCore.QRect(35, 47, 280, 16))
        menu_border.setStyleSheet(BORDER)

        dane_border = QtWidgets.QLabel(self.centralwidget)
        dane_border.setGeometry(QtCore.QRect(410, 47, 545, 16))
        dane_border.setStyleSheet(BORDER)

        self.menu_put_data = MenuButton("Load data", self.centralwidget)
        self.menu_put_data.setGeometry(QtCore.QRect(85, 120, 180, 60))
        self.menu_put_data.setObjectName("put_data")
        self.menu_put_data.clicked.connect(lambda: self.presenter.loadData())

        self.menu_check = MenuButton("Analyse", self.centralwidget)
        self.menu_check.setGeometry(QtCore.QRect(85, 210, 180, 60))
        self.menu_check.setObjectName("check")
        self.menu_check.clicked.connect(lambda: self.presenter.startAnalysis())
        self.menu_check.setDisabled(True)

        self.menu_report = MenuButton("Generate report", self.centralwidget)
        self.menu_report.setGeometry(QtCore.QRect(85, 300, 180, 60))
        self.menu_report.setObjectName("generate_report")
        self.menu_report.clicked.connect(lambda: self.presenter.generateReport())
        self.menu_report.setDisabled(True)

        self.menu_exit = MenuButton("Exit", self.centralwidget)
        self.menu_exit.setGeometry(QtCore.QRect(85, 390, 180, 60))
        self.menu_exit.setObjectName("exit")
        self.menu_exit.clicked.connect(lambda: self.presenter.exit())

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 590, 1000, 60))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.frame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.bulb_one = Bulb(self.frame, 20, 5)

        self.bulb_two = Bulb(self.frame, 80, 5)

        self.bulb_three = Bulb(self.frame, 140, 5)

        self.horizontalLayout.addWidget(self.frame)

        self.status = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.status.setText(STATUS_IDLE)
        self.status.setFont(getFont(10))
        self.status.setObjectName("status")

        self.horizontalLayout.addWidget(self.status)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(430, 108, 540, 350))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.data_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.data_grid.setContentsMargins(0, 0, 0, 0)
        self.data_grid.setHorizontalSpacing(7)
        self.data_grid.setVerticalSpacing(1)
        self.data_grid.setObjectName("data_grid")

        """ Name """
        self.label_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_name.setObjectName("label_3")
        self.data_grid.addWidget(self.label_name, 0, 0, 1, 1)

        self.name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name.setObjectName("label_17")
        self.data_grid.addWidget(self.name, 0, 1, 1, 1)

        """ Age """
        self.label_age = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_age.setObjectName("label_4")
        self.data_grid.addWidget(self.label_age, 1, 0, 1, 1)

        self.age = QtWidgets.QLabel(self.gridLayoutWidget)
        self.age.setObjectName("label_18")
        self.data_grid.addWidget(self.age, 1, 1, 1, 1)

        """ Gender """
        self.label_gender = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_gender.setObjectName("label_5")
        self.data_grid.addWidget(self.label_gender, 2, 0, 1, 1)

        self.gender = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gender.setObjectName("label_19")
        self.data_grid.addWidget(self.gender, 2, 1, 1, 1)

        """ Chest pain """
        self.label_cp = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_cp.setObjectName("label_6")
        self.data_grid.addWidget(self.label_cp, 3, 0, 1, 1)

        self.cp = QtWidgets.QLabel(self.gridLayoutWidget)
        self.cp.setObjectName("label_20")
        self.data_grid.addWidget(self.cp, 3, 1, 1, 1)

        """ Old_peak """
        self.label_oldpeak = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_oldpeak.setObjectName("label_9")
        self.data_grid.addWidget(self.label_oldpeak, 3, 2, 1, 1)

        self.oldpeak = QtWidgets.QLabel(self.gridLayoutWidget)
        self.oldpeak.setObjectName("label_27")
        self.data_grid.addWidget(self.oldpeak, 3, 3, 1, 1)

        """ Slope """
        self.label_slope = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_slope.setObjectName("label_13")
        self.data_grid.addWidget(self.label_slope, 4, 2, 1, 1)

        self.slope = QtWidgets.QLabel(self.gridLayoutWidget)
        self.slope.setObjectName("label_28")
        self.data_grid.addWidget(self.slope, 4, 3, 1, 1)

        """ CA """
        self.label_ca = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ca.setObjectName("label_14")
        self.data_grid.addWidget(self.label_ca, 5, 2, 1, 1)

        self.ca = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ca.setObjectName("label_55")
        self.data_grid.addWidget(self.ca, 5, 3, 1, 1)

        """ Thal """
        self.label_thal = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_thal.setObjectName("label_16")
        self.data_grid.addWidget(self.label_thal, 6, 2, 1, 1)

        self.thal = QtWidgets.QLabel(self.gridLayoutWidget)
        self.thal.setObjectName("label_56")
        self.data_grid.addWidget(self.thal, 6, 3, 1, 1)

        """ Exang """
        self.label_exang = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_exang.setObjectName("label_10")
        self.data_grid.addWidget(self.label_exang, 2, 2, 1, 1)

        self.exang = QtWidgets.QLabel(self.gridLayoutWidget)
        self.exang.setObjectName("label_24")
        self.data_grid.addWidget(self.exang, 2, 3, 1, 1)

        """ Fbs """
        self.label_fbs = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_fbs.setObjectName("label_15")
        self.data_grid.addWidget(self.label_fbs, 6, 0, 1, 1)

        self.fbs = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fbs.setObjectName("label_23")
        self.data_grid.addWidget(self.fbs, 6, 1, 1, 1)

        """ Thalah """
        self.label_thalach = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_thalach.setObjectName("label_11")
        self.data_grid.addWidget(self.label_thalach, 1, 2, 1, 1)

        self.thalah = QtWidgets.QLabel(self.gridLayoutWidget)
        self.thalah.setObjectName("label_25")
        self.data_grid.addWidget(self.thalah, 1, 3, 1, 1)

        """ Restecg """
        self.label_restecg = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_restecg.setObjectName("label_12")
        self.data_grid.addWidget(self.label_restecg, 0, 2, 1, 1)

        self.restecg = QtWidgets.QLabel(self.gridLayoutWidget)
        self.restecg.setObjectName("label_26")
        self.data_grid.addWidget(self.restecg, 0, 3, 1, 1)

        """ Chol """
        self.chol = QtWidgets.QLabel(self.gridLayoutWidget)
        self.chol.setObjectName("label_22")
        self.data_grid.addWidget(self.chol, 5, 1, 1, 1)

        self.label_chol = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_chol.setObjectName("label_8")
        self.data_grid.addWidget(self.label_chol, 5, 0, 1, 1)

        """ Trestbps """
        self.trestbps = QtWidgets.QLabel(self.gridLayoutWidget)
        self.trestbps.setObjectName("label_21")
        self.data_grid.addWidget(self.trestbps, 4, 1, 1, 1)

        self.label_trestbps = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_trestbps.setObjectName("label_7")
        self.data_grid.addWidget(self.label_trestbps, 4, 0, 1, 1)

        self.data_grid.setColumnStretch(0, 1)
        self.data_grid.setColumnStretch(1, 2)
        self.data_grid.setColumnStretch(2, 1)
        self.data_grid.setColumnStretch(3, 2)

        self.data.append(self.name)  # 0: name
        self.data.append(self.age)  # 1: age
        self.data.append(self.gender)  # 2: gender
        self.data.append(self.cp)  # 3: cp
        self.data.append(self.trestbps)  # 4: trestbps
        self.data.append(self.chol)  # 5: chol
        self.data.append(self.fbs)  # 6: fbs

        self.data.append(self.restecg)  # 7: restecg
        self.data.append(self.thalah)  # 8: thalah
        self.data.append(self.exang)  # 9: exang
        self.data.append(self.oldpeak)  # 10: oldpeak
        self.data.append(self.slope)  # 11: slope
        self.data.append(self.ca)  # 12: ca
        self.data.append(self.thal)  # 13: thal

        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(430, 520, 90, 20))
        self.label_result.setFont(getFont(12))

        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(520, 520, 350, 50))
        self.result.setFont(getFont(10))
        self.result.setWordWrap(True)
        self.result.setAlignment(Qt.AlignTop)
        self.result.setObjectName("result")

        self.dane.raise_()
        self.menu.raise_()
        self.menu_put_data.raise_()
        self.menu_check.raise_()
        self.menu_exit.raise_()
        self.horizontalLayoutWidget.raise_()
        self.gridLayoutWidget.raise_()
        self.label_result.raise_()
        self.result.raise_()
        self.menu_report.raise_()
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Master Thesis Software"))
        self.menu.setText(_translate("MainWindow", "Menu"))
        self.dane.setText(_translate("MainWindow", "Data"))

        self.label_oldpeak.setText(_translate("MainWindow", "Oldpeak"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.gender.setText(_translate("MainWindow", "..."))
        self.label_thal.setText(_translate("MainWindow", "Thal"))
        self.label_cp.setText(_translate("MainWindow", "Chest pain"))
        self.slope.setText(_translate("MainWindow", "..."))
        self.ca.setText(_translate("MainWindow", "..."))
        self.label_ca.setText(_translate("MainWindow", "Ca"))
        self.age.setText(_translate("MainWindow", "..."))
        self.exang.setText(_translate("MainWindow", "..."))
        self.cp.setText(_translate("MainWindow", "..."))
        self.thal.setText(_translate("MainWindow", "..."))
        self.label_fbs.setText(_translate("MainWindow", "Sugar lvl"))
        self.label_gender.setText(_translate("MainWindow", "Gender"))
        self.name.setText(_translate("MainWindow", "..."))
        self.label_thalach.setText(_translate("MainWindow", "Thalach"))
        self.label_restecg.setText(_translate("MainWindow", "Restecg"))
        self.label_slope.setText(_translate("MainWindow", "Slope"))
        self.chol.setText(_translate("MainWindow", "..."))
        self.label_exang.setText(_translate("MainWindow", "Exang"))
        self.trestbps.setText(_translate("MainWindow", "..."))
        self.fbs.setText(_translate("MainWindow", "..."))
        self.label_chol.setText(_translate("MainWindow", "Chol"))
        self.label_trestbps.setText(_translate("MainWindow", "Trestbps"))
        self.label_age.setText(_translate("MainWindow", "Age"))
        self.thalah.setText(_translate("MainWindow", "..."))
        self.restecg.setText(_translate("MainWindow", "..."))
        self.oldpeak.setText(_translate("MainWindow", "..."))
        self.label_result.setText(_translate("MainWindow", "Result:"))
        self.result.setText(_translate("MainWindow", ""))

    def changeStatusMessage(self, status):
        self.status.setText(status)

    def turnOffBulbs(self):
        self.bulb_one.setOff()
        self.bulb_two.setOff()
        self.bulb_three.setOff()

    def setStatus(self, status):
        if status == 0:
            self.changeStatusMessage(STATUS_IDLE)
            self.menu_check.setDisabled(True)
            self.menu_report.setDisabled(True)
            self.turnOffBulbs()
        elif status == 1:
            self.changeStatusMessage(STATUS_READY)
            self.menu_check.setDisabled(False)
            self.menu_report.setDisabled(True)
            self.result.setText("")
            self.turnOffBulbs()
            self.bulb_one.setOn()
        elif status == 2:
            self.changeStatusMessage(STATUS_PROCESSING)
            self.bulb_two.setOn()
        else:
            self.changeStatusMessage(STATUS_DONE)
            self.menu_report.setDisabled(False)
            self.bulb_three.setOn()

    def openFileDialog(self, currentDir) -> str:
        file_name = QFileDialog.getOpenFileName(None, 'Open file', currentDir, "Excel file (*.csv);; Text file (*.txt)")
        return file_name[0]

    def show(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setWindowIcon(QtGui.QIcon('graphic/icon.ico'))
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi()
        self.MainWindow.show()
        sys.exit(app.exec_())


def getFont(size):
    font = QtGui.QFont()
    font.setPointSize(size)
    return font
