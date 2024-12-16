import pandas as pd
import plotly.express as px

data = pd.read_csv('metadata_nasa_battery.csv')
data['Cycle_count'] = range(1, len(data) + 1)

data_req = data.dropna(subset=['Re', 'Rct'])
print(data.columns)
print(data.head())

# With RE
fig_re = px.line(data_req, 
                 x='Cycle_count', 
                 y='Re', 
                 title='Electrolyte Resistance with Cycle count')
                 
fig_re.show()

# with  (Rct)
fig_rct = px.line(data_req, 
                  x='Cycle_count', 
                  y='Rct', 
                  title='Charge Transfer Resistance (Rct) over Cycles') 
                  
fig_rct.show()
