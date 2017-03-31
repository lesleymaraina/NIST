import plotly
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

plotly.tools.set_credentials_file(username='', api_key='')

DEL = pd.read_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Plots/Feb232017/del_Size.csv')
INS = pd.read_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Plots/Feb232017/ins_Size.csv')
X = pd.DataFrame()
XI = pd.DataFrame()
X = DEL['log_size']
XI = INS['log_size']



# x0 = np.random.randn(500)
# x1 = np.random.randn(500)+1

trace1 = go.Histogram(
    x=X,
    histnorm='count',
    name='Deletions',
    autobinx=False,
    xbins=dict(
        start=-3.2,
        end=2.8,
        size=0.2
    ),
    marker=dict(
        color='fuchsia',
        line=dict(
            color='grey',
            width=0
        )
    ),
    opacity=0.75
)
trace2 = go.Histogram(
    x=XI,
    name='Insertions',
    autobinx=False,
    xbins=dict(
        start=-1.8,
        end=4.2,
        size=0.2
    ),
    marker=dict(
        color='rgb(255, 217, 102)'
    ),
    opacity=0.75
)
data = [trace1, trace2]
layout = go.Layout(
    title='Variant Sizes',
    xaxis=dict(
        title='SV Size (log10)'
    ),
    yaxis=dict(
        title='Count'
    ),
    barmode='overlay',
    bargap=0.25,
    bargroupgap=0.3
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='line3')

# N = 500
# x = np.linspace(0, 1, N)
# y = np.random.randn(N)
# df = pd.DataFrame({'x': x, 'y': y})
# df.head()


# Single Histogram - Deletions
trace1 = go.Histogram(
    x=X,
    histnorm='count',
    name='Deletions',
    autobinx=False,
    xbins=dict(
        start=-3.2,
        end=10,
        size=0.2
    ),
    marker=dict(
        color='rgba(82,128,201, .9)',
        line=dict(
            color='grey',
            width=0
        )
    ),
    opacity=0.75
)

data = [trace1]
layout = go.Layout(
    title='Variant Sizes[Insertions]',
    xaxis=dict(
        title='SV Size (log10)'
    ),
    yaxis=dict(
        title='Count'
    ),
    barmode='overlay',
    bargap=0.25,
    bargroupgap=0.3
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='lineINS')

# Single Histogram - Deletions
trace1 = go.Histogram(
    x=X,
    histnorm='count',
    name='Deletions',
    autobinx=False,
    xbins=dict(
        start=-3.2,
        end=10,
        size=0.2
    ),
    marker=dict(
        color='rgba(242,127,19, .9)',
        line=dict(
            color='grey',
            width=0
        )
    ),
    opacity=0.75
)

data = [trace1]
layout = go.Layout(
    title='Variant Sizes[Deletions]',
    xaxis=dict(
        title='SV Size (log10)'
    ),
    yaxis=dict(
        title='Count'
    ),
    barmode='overlay',
    bargap=0.25,
    bargroupgap=0.3
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='lineDEL')