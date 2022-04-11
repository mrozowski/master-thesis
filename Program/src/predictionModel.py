import file
from config import message
from sklearn.ensemble import RandomForestClassifier


class PredictionModel:
    def __init__(self):
        self.result = ""
        self.ready = False
        self.randomForest: RandomForestClassifier = file.loadModel()
        self.prediction = 0
        self.probability = 0.0
        self.setup()

    def setup(self):
        if self.randomForest is not None:
            self.ready = True

    def run(self, data):
        if self.ready:
            matrix = createMatrix(data)
            prediction = self.randomForest.predict(matrix)
            probability = self.randomForest.predict_proba(matrix)
            self.result = generateResult(prediction, probability[0][1])
            return prediction, probability[0][1]

    def getResult(self):
        return self.result

    def isLoaded(self) -> bool:
        return self.randomForest is not None


def createMatrix(data):
    matrix = [[data.age, data.gender, data.cp, data.trestbps,
               data.chol, data.fbs, data.restecg, data.thalach,
               data.exang, data.oldpeak, data.slope, data.ca, data.thal]]
    return matrix


def generateResult(prediction, probability):
    if 0.45 < probability < 0.55:
        return message['INCONCLUSIVE']
    if prediction == 0:
        return message['HEALTHY']
    else:
        return message['SICK']
