class ReasoningUtils:
    def __init__(self, dataframe, patient):
        self.dataFrame = dataframe
        self.reasoning = []
        self.sumValue = 0.0
        self.setup(patient)

    def setup(self, patient):
        patient_values = patient.values.flatten().tolist()
        list = self.dataFrame.values.flatten().tolist()
        names = self.dataFrame.columns.values
        self.sumValue = sum([abs(a) for a in list])

        for i in range(len(list)):
            value = list[i]
            p_value = patient_values[i]
            self.reasoning.append(Reason(value, p_value, names[i], abs(value) / self.sumValue))

    def maxValue(self):
        return max(self.reasoning)

    def getOrderedList(self):
        self.reasoning.sort(reverse=True)
        return self.reasoning

    def getPositive(self):
        positive = []
        for a in self.reasoning:
            if a.score > 0:
                positive.append(a)
        positive.sort(reverse=True)
        return positive

    def getNegative(self):
        negative = []
        for a in self.reasoning:
            if a.score < 0:
                negative.append(a)
        negative.sort()
        return negative


class Reason:
    def __init__(self, value, p_value, name, rate):
        self.score = value
        self.patient_value = p_value
        self.name = name
        self.rate = rate

    def __gt__(self, other):
        if not isinstance(other, Reason):
            return NotImplemented
        return self.score > other.score

    def __eq__(self, other):
        if not isinstance(other, Reason):
            return NotImplemented
        return self.score == other.score

    def __str__(self):
        return "( {}, {}, {:.1%} )".format(self.score, self.name, self.rate)
