import pickle

class Windmill:
    filename = './models/wind_turbine.sav'

    def __init__(self, filename = filename):
        self.model = pickle.load(open(filename, 'rb'))

    def predict(self, parameters):
        result = self.model.predict(parameters)
        return result[0]

class SolarCell:
    filename = './models/solar_cell.sav'

    def __init__(self, filename = filename):
        self.model = pickle.load(open(filename, 'rb'))

    def predict(self, parameters):
        result = self.model.predict(parameters)
        return result[0]
