from flask import Flask,render_template,request
import pandas as pd
from graphWT import plot_graph_WT
from graphSC import plot_graph_SC
###

app = Flask(__name__)

# wind turbine inputs
input_data_wt = pd.read_csv("./data/input_wt.csv")
w_speed=pd.read_csv('./data/input_wt.csv', usecols=['Wind speed m/s'])
p_out=pd.read_csv('./data/input_wt.csv', usecols=['output(kW)'])

# solar cell inputs
input_data_sc = pd.read_csv('./data/input_sc.csv')
sdx = pd.read_csv('./data/input_sc.csv', usecols=['Voltage']).sort_values(by='Voltage', ascending=True)
sdy = pd.read_csv('./data/input_sc.csv', usecols=['Current'])
input_data_sc['Power'] = input_data_sc['Voltage'] * input_data_sc['Current']
input_data_sc.to_csv('./data/input_sc.csv', index=False)

## app.routes and functions for devices
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
        
        # def calculate_efficiency(power_out):
        #     efficiency = round((power_out / power_input) * 100, 2)
        #     eff_data.append(efficiency)

        # eff_data = []
        # k=len(input_data_wt)
        
        # for i in range(0,k):
        #     wind_speed = w_speed.loc[i].item()
        #     power_out = p_out.loc[i].item()
        #     if wind_speed<3 or wind_speed>20:
        #         eff_data.append(0)
        #     else:
        #         power_input = 0.5*3.14*1.204*rotor_radius*wind_speed
        #         calculate_efficiency(power_out)
        
        dict = {'Efficiency': eff_data}
        df = pd.DataFrame(dict)
        df.to_csv('./data/output_wt.csv')

        plot_graph_WT()
        
    data = pd.read_csv('./data/output_wt.csv')
    data.reset_index()
    data.drop(columns="Unnamed: 0", inplace=True)
    data.index = data.index + 1
        
    return render_template('wind_turbine_index.html', tables=[data.to_html()], titles=[''])

@app.route('/solar_cell',methods=['GET', 'POST'])
def solar_cell():
    if request.method == 'POST':
        P_in = float(request.form.get('p_in'))

        k=len(input_data_sc)
        for i in range(0,k):
            if sdx.loc[i].item()==0.0:
                ssc=sdy.loc[i].item()
                break
        for i in range(0,k):
            if sdy.loc[i].item()==0.0:
                ocv = sdx.loc[i].item()
                break
        
        fill_factor = round((input_data_sc['Power'].max()/(ssc * ocv)), 2)
        efficiency_sc = round(((ssc * ocv * fill_factor) / P_in) * 100, 2)
        
        output_sc = []
        output_sc.append(efficiency_sc)
        
        dict = {'Efficiency': output_sc}
        df = pd.DataFrame(dict)
        df.to_csv('./data/output_sc.csv')
        
        plot_graph_SC()

    data = pd.read_csv('./data/output_sc.csv')
    data.reset_index()
    data.drop(columns='Unnamed: 0', inplace=True)
    data.index = data.index + 1
    
    return render_template('solar_cell.html', tables=[data.to_html()], titles=[''])

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)