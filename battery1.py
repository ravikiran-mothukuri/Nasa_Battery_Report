import pandas as pd
import plotly.express as px

data = pd.read_csv('00001.csv')

print(data.columns)
print(data.head())

fig_voltage = px.line(data, 
                      x='Time', 
                      y='Voltage', 
                      title='Voltage Measured Over Time')
                      
fig_voltage.show()


fig_current = px.line(data, 
                      x='Time',  
                      y='Current',  
                      title='Current Measured Over Time')
                      
fig_current.show()


fig_temperature = px.line(data, 
                          x='Time',  
                          y='Temperature',  
                          title='Temperature Measured Over Time')
                          
fig_temperature.show()


fig_voltage_load = px.line(data, 
                           x='Time',  
                           y='Voltage_load',  
                           title='Voltage under Load Over Time')
                           
fig_voltage_load.show()


fig_current_load = px.line(data, 
                           x='Time',  
                           y='Current_load',  
                           title='Current under Load Over Time')
                           
fig_current_load.show()
