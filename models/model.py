import pickle


class Windmill:
    filename = 'wind_turbine.sav'

    def __init__(self, filename = filename):
        self.model = pickle.load(open(filename, 'rb'))

    def predict(self, parameters):
        # self.model = pickle.load(open(self.filename, 'rb'))
        result = self.model.predict(parameters)
        return result


class SolarCell:
    filename = 'solar_cell.sav'

    def __init__(self, filename = filename):
        self.model = pickle.load(open(filename, 'rb'))

    def predict(self, parameters):
        # self.model = pickle.load(open(self.filename, 'rb'))
        result = self.model.predict(parameters)
        return result
