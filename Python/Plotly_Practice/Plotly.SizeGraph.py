import numpy as np
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import cufflinks as cf
import pandas as pd
import numpy as np


plotly.tools.set_credentials_file(username='', api_key='')

# Create random data with numpy
import numpy as np


DEL = pd.read_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Plots/Feb232017/del_Size.csv')
INS = pd.read_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Plots/Feb232017/ins_Size.csv')

X = pd.DataFrame()
XI = pd.DataFrame()
X = DEL['log_size']
print X.head(5)
XI = INS['log_size']
print XI.head(5)


# Create traces
trace0 = go.Scatter(
    x = X,
    # y = X,
    mode = 'lines',
    name = 'DEL',
    xaxis="Variant Size (log10)"
)
trace1 = go.Scatter(
    x = XI,
    # y = XI,
    mode = 'lines+markers',
    name = 'INS',
    xaxis="Variant Size (log10)"
)
# trace2 = go.Scatter(
#     x = random_x,
#     y = random_y2,
#     mode = 'markers',
#     name = 'markers'
# )
data = [trace0,trace1]

py.iplot(data, filename='line2')


# Double Histogram Plot
cf.set_config_file(offline=False, world_readable=True, theme='pearl')

df = pd.DataFrame({'DEL_size': DEL['log_size'],
                   'INS_size': INS['log_size']})
                   
df.head(2)

df.iplot(kind='histogram', subplots=True, shape=(2, 1), filename='hist-plot4')

# source: https://plot.ly/pandas/histograms/