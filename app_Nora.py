import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np
import plotly.graph_objects as go

import matplotlib.pyplot as plt
import seaborn as sns

import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objs as go

from plotly.tools import mpl_to_plotly

import math 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)




# -------------------------------------------------------------------------------------------------------------- 

#											PART 1: DESIGN PARAMETERS

# --------------------------------------------------------------------------------------------------------------
# Here we will set the colors, margins, DIV height&weight and other parameters

colors = {
		'full-background': 	'#DCDCDC',
		'block-borders': 	'black'
}

margins = {
		'block-margins': '10px 10px 10px 10px',
		'block-margins': '4px 4px 8px 4px'
}

sizes = {
		'subblock-heights': '500px'
}



# -------------------------------------------------------------------------------------------------------------- 

#											PART 2: ACTUAL LAYOUT

# --------------------------------------------------------------------------------------------------------------
# Here we will set the DIV-s and other parts of our layout
# We need too have a 2x2 grid
# I have also included 1 more grid on top of others, where we will show the title of the app



# -------------------------------------------------------------------------------------- DIV for TITLE
div_title = html.Div(children =	html.H1('Title'),
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'text-align': 'center'
							}
					)

# -------------------------------------------------------------------------------------- DIV for first raw (1.1 and 1.2)

df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")


div_1_1 = html.Div(children = dcc.Graph(id = 'fig',figure = fig),
					style = {
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width': '49%',
							'height': sizes['subblock-heights'],
					}
				)


fig_2 = px.bar(df, x="sepal_width", y="sepal_length", color="species")

div_1_2 = html.Div(children = dcc.Graph(id = 'fig_2',figure = fig_2),
					style = {
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width': '51%',
							'height': sizes['subblock-heights']
					}
				)

# Collecting DIV 1.1 and 1.2 into the DIV of first raw.
# Pay attention to the 'display' and 'flex-flaw' attributes.
# With this configuration you are able to let the DIV-s 1.1 and 1.2 be side-by-side to each other.
# If you skip them, the DIV-s 1.1 and 1.2 will be ordered as separate rows.
# Pay also attention to the 'width' attributes, which specifiy what percentage of full row will each DIV cover.
div_raw1 = html.Div(children =	[div_1_1,
								div_1_2
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'display': 'flex',
							'flex-flaw': 'row-wrap'
							})


# -------------------------------------------------------------------------------------- DIV for second raw (2.1 and 2.2)
y0 = np.random.randn(50) - 1

fig_3 = go.Figure(data = go.Box(y = y0))


div_2_1 = html.Div(children = dcc.Graph(id = 'fig_3',figure = fig_3),
					style = {
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width': '49%',
							'height': sizes['subblock-heights'],
					}
				)



x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
plt.plot(x,y)
fig4 = plt.gcf()
fig4.set_size_inches(2.5, 1.5)
plotly_fig = mpl_to_plotly(fig4)



div_2_2 = html.Div(children = dcc.Graph(id = 'matlotlib-graph',figure = plotly_fig),
					style = {
							'border': '1px {} solid'.format(colors['block-borders']), 
							'margin': margins['block-margins'],
							'width': '51%',
							'height': sizes['subblock-heights'],
					}
				)


div_raw2 = html.Div(children =	[div_2_1,
								div_2_2
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'display': 'flex',
							'flex-flaw': 'row-wrap'
							})

# -------------------------------------------------------------------------------------- Collecting all DIV-s in the final layout
# Here we collect all DIV-s into a final layout DIV

app.layout = html.Div(	[
						div_title,
						div_raw1,
						div_raw2
						],
						style = {
							'backgroundColor': colors['full-background']
						}
					)




# -------------------------------------------------------------------------------------------------------------- 

#											PART 3: RUNNING THE APP

# --------------------------------------------------------------------------------------------------------------
# >> use __ debug=True __ in order to be able to see the changes after refreshing the browser tab,
#			 don't forget to save this file before refreshing
# >> use __ port = 8081 __ or other number to be able to run several apps simultaneously
app.run_server(debug=True)