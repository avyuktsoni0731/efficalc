from flask import Flask,render_template,request
import numpy as np
from model import Windmill, SolarCell

app = Flask(__name__)

@app.route('/wind_turbine',methods=['GET', 'POST'])
def wind_turbine():
    parametersWindTurbine = []
    
    if request.method == 'POST':
        temperature_2m = float(request.form.get('temperature_2m'))
        relativehumidity_2m = float(request.form.get('relativehumidity_2m'))
        dewpoint_2m = float(request.form.get('dewpoint_2m'))
        windspeed_10m = float(request.form.get('windspeed_10m'))
        windspeed_100m = float(request.form.get('windspeed_100m'))
        windgusts_10m = float(request.form.get('windgusts_10m'))
        
        parametersWindTurbine.extend([temperature_2m, relativehumidity_2m, dewpoint_2m, windspeed_10m, windspeed_100m, windgusts_10m])
        parametersWindTurbine = np.array(parametersWindTurbine)
        parametersWindTurbine = parametersWindTurbine.reshape(1, 6)
        
        windTurbine = Windmill()
        returnedEfficiency = round(windTurbine.predict(parametersWindTurbine), 6)*100
        
        return render_template('wind_turbine_index.html', returnedEfficiency=returnedEfficiency)
    return render_template('wind_turbine_index.html')
    
    
@app.route('/solar_cell',methods=['GET', 'POST'])
def solar_cell():
    parametersSolarCell = []
    
    if request.method == 'POST':
        temperature_2m = float(request.form.get('temperature_2m'))
        relativehumidity_2m = float(request.form.get('relativehumidity_2m'))
        msl = float(request.form.get('msl'))
        tcc = float(request.form.get('tcc'))
        hcc = float(request.form.get('hcc'))
        mcc = float(request.form.get('mcc'))
        lcc = float(request.form.get('lcc'))
        srb = float(request.form.get('srb'))
        aoi = float(request.form.get('aoi'))
        zenith = float(request.form.get('zenith'))
        azimuth = float(request.form.get('azimuth'))
        
        parametersSolarCell.extend([temperature_2m, relativehumidity_2m, msl, tcc, hcc, mcc, lcc, srb, aoi, zenith, azimuth])
        parametersSolarCell = np.array(parametersSolarCell)
        parametersSolarCell = parametersSolarCell.reshape(1, 11)

        solarCell = SolarCell()
        returnedEfficiency = round(solarCell.predict(parametersSolarCell), 6)*100
        
        return render_template('solar_cell_index.html', returnedEfficiency=returnedEfficiency)
    return render_template('solar_cell_index.html')

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)