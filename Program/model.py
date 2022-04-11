from pandas import DataFrame


class PatientData:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = 0
        self.cp = 1
        self.trestbps = 0
        self.chol = 0
        self.fbs = 0
        self.restecg = 0
        self.thalach = 0
        self.exang = 0
        self.oldpeak = 0
        self.slope = 0
        self.ca = 0
        self.thal = 0

    def getFbsValue(self):
        if self.fbs == 0:
            return "below 120mg/dl"
        else:
            return "above 120mg/dl"

    def getThalValue(self):
        if self.thal == 1:
            return "Normal"
        elif self.thal == 2:
            return "Fixed defect"
        else:
            return "Reversable defect"

    def getExangValue(self):
        if self.exang == 1:
            return "Yes"
        else:
            return "No"

    def getSlopeValue(self):
        if self.slope == 1:
            return "Upsloping"
        elif self.slope == 2:
            return "Flat"
        else:
            return "Downsloping"

    def getCpValue(self):
        if self.cp == 0:
            return "Typical angina"
        elif self.cp == 1:
            return "Atypical angina"
        elif self.cp == 2:
            return "Non-anginal pain"
        elif self.cp == 3:
            return "Asymptomatic"
        else:
            return "Not recognized"

    def getGenderValue(self):
        if self.gender == 1:
            return "Male"
        else:
            return "Female"

    def toDataFrame(self):
        data = [{'age': self.age, 'sex': self.gender, 'cp': self.cp,
                 'trestbps': self.trestbps, 'chol': self.chol, 'fbs': self.fbs,
                 'restecg': self.restecg, 'thalach': self.thalach, 'exang': self.exang,
                 'oldpeak': self.oldpeak, 'slope': self.slope, 'ca': self.ca, 'thal': self.thal}]

        return DataFrame(data)
