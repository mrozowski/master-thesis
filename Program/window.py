from os import getcwd

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QDialogButtonBox, QMessageBox, QSpacerItem, \
    QFileDialog

from file import saveReportAsPdf
from reporter import Report


class Window:
    def showReport(self, report: Report, name):
        dialog = Dialog(700, 500, "Report")

        header = QtWidgets.QLabel()
        header.setFont(getFont(12))
        header.setText(report.decision)
        header.setWordWrap(True)

        model = QtWidgets.QLabel()
        model.setFont(getFont(10))
        model.setText("Model probability: {:.1%}".format(report.probability))
        model.setWordWrap(True)

        desc = QtWidgets.QLabel()
        desc.setFont(getFont(10))
        desc.setText(report.message)
        desc.setWordWrap(True)

        list = QtWidgets.QLabel()
        list.setFont(getFont(10))
        list.setText(createBulletList(report.significantParameters))
        list.setWordWrap(True)

        tableLabel = QtWidgets.QLabel()
        tableLabel.setFont(getFont(10))
        tableLabel.setContentsMargins(0, 20, 0, 0)
        tableLabel.setText("Table showing how each parameter affects the final result")
        tableLabel.setWordWrap(True)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        dataToSave = {"decision": header.text(), "probability": model.text(), "message": report.message, "name": name,
                      "param": report.significantParameters, "table": report.reasoning,
                      "description": tableLabel.text()}
        buttonBox.accepted.connect(lambda: dialog.save(dataToSave))
        buttonBox.rejected.connect(dialog.reject)

        dialog.addWidget(header)
        dialog.addWidget(model)
        dialog.addWidget(desc)
        dialog.addWidget(list)
        dialog.addWidget(tableLabel)
        dialog.addWidget(createTable(report.reasoning))
        dialog.addWidget(buttonBox, alignment=QtCore.Qt.AlignBottom)
        dialog.showDialog()

    def showWarning(self, message, description):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)

        msg.setInformativeText(description)
        msg.setWindowTitle("Warning")

        spacer = QSpacerItem(350, 30)
        layout = msg.layout()
        layout.addItem(spacer, 1, 0, 1, 0)

        msg.exec_()


class Dialog(QDialog):
    def __init__(self, width, height, title):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(width, height)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        layoutWidget = QtWidgets.QWidget(self)
        layoutWidget.setFixedWidth(width)
        layoutWidget.setFixedHeight(height)
        self.verticalLayout = QtWidgets.QVBoxLayout(layoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

    def addWidget(self, widget: QtWidgets, alignment=None):
        if alignment is None:
            self.verticalLayout.addWidget(widget)
        else:
            self.verticalLayout.addWidget(widget, alignment=alignment)

    def save(self, data):
        file = QFileDialog.getSaveFileName(None, 'Save file', getcwd(), "Report pdf (*.pdf)")[0]
        if file is not None and file != '':
            saveReportAsPdf(file, data)

    def showDialog(self):
        self.exec_()


def createBulletList(elements):
    bulletList = "<html><ul>"
    for a in elements:
        bulletList = bulletList + "<li>{}</li>".format(a)
    bulletList = bulletList + "</ul></html>"
    return bulletList


def createTable(reasoning):
    rows = 3
    columns = 13
    redBackground = QtGui.QColor(214, 92, 92)
    greenBackground = QtGui.QColor(92, 214, 92)

    tableWidget = QTableWidget()
    tableWidget.setRowCount(rows)
    tableWidget.setFixedHeight(200)
    tableWidget.setColumnCount(columns)
    for i in range(columns):
        tableWidget.setColumnWidth(i, 80)

    columnNames = []
    index = 0
    for n in reasoning:
        columnNames.append(n.name)
        tableWidget.setItem(0, index, QTableWidgetItem("{:.3}".format(n.score)))
        tableWidget.setItem(1, index, QTableWidgetItem("{:.2%}".format(n.rate)))
        tableWidget.setItem(2, index, QTableWidgetItem("{}".format(n.patient_value)))
        if n.score > 0:
            for i in range(rows):
                tableWidget.item(i, index).setBackground(redBackground)
        elif n.score < 0:
            for i in range(rows):
                tableWidget.item(i, index).setBackground(greenBackground)

        index = index + 1

    tableWidget.setHorizontalHeaderLabels(columnNames)
    tableWidget.setVerticalHeaderLabels(["score", "rate", "patient"])
    return tableWidget


def getFont(size):
    font = QtGui.QFont()
    font.setPointSize(size)
    return font
