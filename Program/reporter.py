from shap import TreeExplainer
from pandas import DataFrame
from utils import ReasoningUtils


class Reporter:
    def __init__(self, model):
        self.model = model

    def generate(self, patient_data: DataFrame, prediction, probability):
        explainer = TreeExplainer(self.model)
        shap_values = explainer.shap_values(patient_data)
        reasoning = DataFrame(shap_values[1], columns=patient_data.columns.values)
        utils = ReasoningUtils(reasoning, patient_data)
        message = self._createMessage(prediction, probability, utils)

        return Report(message[0], message[1], message[2], utils.reasoning, probability)

    def _createMessage(self, prediction, probability, utils):
        decision = self._createDecisionString(probability)
        if prediction == 1:
            positive = utils.getPositive()
            parameters = []
            i = 0
            for reason in positive[:3]:
                parameters.append("{} {:.1%} ".format(reason.name, reason.rate))

            body = "The most significant parameters that determine a positive result are:"
        else:
            negative = utils.getNegative()
            parameters = []
            for reason in negative[:3]:
                parameters.append("{} {:.1%} ".format(reason.name, reason.rate))
            body = "The most significant parameters that determine a negative result are:"

        return decision, body, parameters

    def _createDecisionString(self, probability) -> str:
        if probability <= 0.15:
            decision = "Patient has very low risk of heart disease."
        elif 0.15 < probability <= 0.45:
            decision = "Patient has low risk of heart disease."
        elif 0.45 < probability <= 0.55:
            decision = "Patient needs further tests to rule out the heart disease"
        elif 0.55 < probability <= 0.70:
            decision = "Patient has high risk of heart disease."
        else:
            decision = "Patient has very high risk of heart disease."
        return decision


class Report:
    def __init__(self, decision, message, params, reasoning, probability):
        self.decision = decision
        self.message = message
        self.significantParameters = params
        self.reasoning = reasoning
        self.probability = probability
