import os
import threading

import view
from file import loadPatientData, IncorrectFileFormatError, UnsupportedFileError
from predictionModel import PredictionModel
from reporter import Reporter
from window import Window


class Presenter:
    def __init__(self, _view: view.View):
        self.view = _view
        self.status = 0
        self.patient_data = None
        self.prediction_model = None
        self.result = ""
        self.window = Window()
        self.setup()

    def setup(self):
        self.prediction_model = PredictionModel()

    def loadData(self):
        file = self.view.openFileDialog(self.getCurrentDir())
        if file is not None and file != '':
            try:
                self.patient_data = loadPatientData(file)
                self.view.showData(self.patient_data)
                self.status = 1
                self.view.setStatus(self.status)
            except IncorrectFileFormatError as e:
                self.window.showWarning("File error", str(e))
            except UnsupportedFileError as e:
                self.window.showWarning("File error", str(e))

    def startAnalysis(self):
        if self.patient_data is not None:
            if self.prediction_model.isLoaded() is False:
                self.window.showWarning("Model is not loaded",
                                        "Check if file 'modelRfc.bin' is present in data directory "
                                        "and try again")
                self.setup()
            else:
                self.status = 2
                self.view.setStatus(self.status)
                t = threading.Thread(target=self.runModel)
                t.daemon = True
                t.start()

    def generateReport(self):
        reporter = Reporter(self.prediction_model.randomForest)
        report = reporter.generate(self.patient_data.toDataFrame(), self.result[0], self.result[1])
        self.window.showReport(report, self.patient_data.name)

    def onAnalysisFinish(self):
        self.view.result.setText(self.prediction_model.getResult())
        self.status = 3
        self.view.setStatus(self.status)

    def runModel(self):
        self.result = self.prediction_model.run(self.patient_data)
        self.onAnalysisFinish()

    def getCurrentDir(self) -> str:
        return os.getcwd()

    def exit(self):
        exit()

    def show(self):
        self.view.show()
