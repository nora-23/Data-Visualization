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
c.execute("DROP TABLE IF EXISTS main_data")
c.execute("DROP TABLE IF EXISTS means")
c.execute("DROP TABLE IF EXISTS shap_p_values_text")

c.execute("Create TABLE main_data (Id int, main_value int)")
c.execute("Create TABLE means (Id int, means float)")
c.execute("Create TABLE shap_p_values_text (Id int, p_value float)")


i = 0
a = []
b = []
d = []

while True:
    x = np.random.randint(1,7)
    a.append(x)
    b.append(np.mean(a))
    b_mean = b[i]
    if len(b) >= 3:
        y = stats.shapiro(b)[1]
        d.append(y)
        c.execute("INSERT INTO shap_p_values_text values ({},{})".format(i, y))    
    c.execute("INSERT INTO main_data values ({},{})".format(i + 1, x))
    c.execute("INSERT INTO means values ({},{})".format(i + 1, b_mean))
    connection.commit()
    i += 1
    time.sleep(0.5)