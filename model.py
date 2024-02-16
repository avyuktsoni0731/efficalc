import pickle
import joblib

class Windmill:
    filename = 'models/wind_turbine.sav'

    def __init__(self, filename = filename):
        self.model = joblib.load(open(filename, 'rb'))

    def predict(self, parameters):
        result = self.model.predict(parameters)
        return result[0]

class SolarCell:
    filename = 'models/solar_cell.sav'

    def __init__(self, filename = filename):
        self.model = joblib.load(filename)

    def predict(self, parameters):
        result = self.model.predict(parameters)
        return result[0]
