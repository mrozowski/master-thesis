import csv
import pickle

import pandas as pd
from fpdf import FPDF

from config import PARAMETERS
from config import MODEL as modelPath
from model import PatientData


def loadModel():
    return openFile(modelPath)


def openFile(fileName):
    try:
        with open(fileName, "rb") as file:
            return pickle.load(file)
    except IOError:
        return None


def openCsv(fileName):
    data = []
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
        return data


def openTxt(fileName):
    data = []
    with open(fileName, 'r') as file:
        for row in file.readlines():
            temp = []
            for word in row.split(','):
                temp.append(word.strip())
            data.append(temp)
        return data


def loadPatientData(fileName) -> PatientData:
    if fileName.endswith('.csv'):
        csv_content = openCsv(fileName)
        return parseData(csv_content)
    elif fileName.endswith('.txt'):
        txt_content = openTxt(fileName)
        return parseData(txt_content)
    else:
        raise UnsupportedFileError(fileName)


def parseData(content) -> PatientData:
    if set(PARAMETERS).issubset(set(content[0])) is False:
        raise IncorrectFileFormatError("Some parameters are missing")

    data = toDataFrame(content)
    try:
        patientData = PatientData()
        patientData.name = str(data["name"][0])
        patientData.age = int(data["age"][0])
        patientData.gender = int(data["sex"][0])
        patientData.cp = int(data["cp"][0])
        patientData.trestbps = int(data["trestbps"][0])
        patientData.chol = int(data["chol"][0])
        patientData.fbs = str(data["fbs"][0])
        patientData.restecg = int(data["restecg"][0])
        patientData.thalach = int(data["thalach"][0])
        patientData.exang = int(data["exang"][0])
        patientData.oldpeak = float(data["oldpeak"][0])
        patientData.slope = int(data["slope"][0])
        patientData.ca = int(data["ca"][0])
        patientData.thal = int(data["thal"][0])
        return patientData
    except ValueError as e:
        raise IncorrectFileFormatError(str(e))


def toDataFrame(data):
    names = data[0]
    values = data[1]
    df = pd.DataFrame(columns=names)
    series = pd.Series(values, index=df.columns)
    df = df.append(series, ignore_index=True)
    return df


def saveReportAsPdf(fileName, data):
    pdf = PDF()
    pdf.add_page()
    pdf.titles("Heart disease report")
    pdf.texts(data["name"], "Patient name: ")
    pdf.ln(5)
    pdf.texts(data["decision"], "Result: ")
    pdf.texts(data["probability"])

    pdf.description(data["message"], data["param"])
    pdf.table(data["table"], data["description"])
    pdf.output(fileName, 'F')


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.epw = self.w - 2 * self.l_margin

    def titles(self, title):
        self.set_xy(0.0, 0.0)
        self.set_font('Arial', 'B', 16)
        self.cell(w=210.0, h=40.0, align='C', txt=title, border=0)
        self.ln(40)

    def texts(self, text, start=""):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, start + text)

    def description(self, text, params):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, text)
        self.bulletList(params)
        self.ln(10)

    def bulletList(self, params):
        for a in params:
            self.set_x(12)
            self.multi_cell(0, 6, chr(127) + " " + a)

    def table(self, data, desc):
        self.multi_cell(0, 10, desc)
        self.set_font('Arial', 'B', 10)
        for row in data:
            self.cell(self.epw / 13, 10, str("{}".format(row.name)), align='C', border=1)
        self.set_font('Arial', '', 8)
        self.ln(10)
        for row in data:
            self.cell(self.epw / 13, 10, str("{:.3}".format(row.score)), align='C', border=1)
        self.ln(10)
        for row in data:
            self.cell(self.epw / 13, 10, str("{:.2%}".format(row.rate)), align='C', border=1)
        self.ln(10)
        for row in data:
            self.cell(self.epw / 13, 10, str("{}".format(row.patient_value)), align='C', border=1)


class IncorrectFileFormatError(Exception):
    pass


class UnsupportedFileError(Exception):
    def __init__(self, message):
        super(UnsupportedFileError, self) \
            .__init__("Unsupported file extension: " + message)
