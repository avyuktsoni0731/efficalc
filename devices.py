import pickle


class Windmill:
    filename = 'windmill.sav'

    def __init__(self, input):
        self.model = pickle.load(open(self.filename, 'rb'))
        result = self.model.precit(input)


class SolarCell:
    filename = 'solarcell.sav'

    def __init__(self):
        self.model = pickle.load(open(self.filename, 'rb'))



