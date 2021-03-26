import sqlite3
import time
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.gridspec import GridSpec
import statsmodels.api as sm
from scipy import stats
from matplotlib.animation import FuncAnimation

connection = sqlite3.connect('data_d.db')

c = connection.cursor()

fig = plt.figure(figsize=(10, 4))
gs = GridSpec(nrows=2, ncols=3)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[1, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax4 = fig.add_subplot(gs[:,2])
ax3 = fig.add_subplot(gs[1, 1])


def animate(i):
    ax0.cla()
    ax1.cla()
    ax2.cla()
    ax4.cla()
    query = ('SELECT * FROM means')
    data = pd.read_sql_query(query, connection)
    x_random_mean= data.means
    ax0.hist(x_random_mean,bins = 6)
        
 
    query2 = ('SELECT * FROM shap_p_values_text')
    data2 = pd.read_sql_query(query2, connection)
    x2 = data2.p_value.values
    ax1.text(0.01, 0.5,f"P values is: {x2[-1]}")
    ax1.axes.get_yaxis().set_visible(False)
    ax1.axis('off')
    
    sm.ProbPlot(x_random_mean).qqplot(line='s', ax=ax2)

    ax3.plot(data2.Id, x2)
        
    query4 = ('SELECT * FROM main_data')
    data4 = pd.read_sql_query(query4, connection)
    data41 = data4.main_value.values
    ax4.hist(data41, bins= 6)

animation = FuncAnimation(plt.gcf(), animate, interval=500)

plt.show()