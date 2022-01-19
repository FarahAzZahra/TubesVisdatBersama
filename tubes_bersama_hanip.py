# -*- coding: utf-8 -*-
"""tubes bersama hanip.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13nfENL484gQdaF91mitDhhyLAbpsSg-R

FINAL PROJECT - Visualisasi Data

Kelas : IF - 42 - GAB06

Kelompok :

Farah Az Zahra (1301190312)

Dika Fajar Ramadan (1301190260)

# Import data
"""

import pandas as pd
import numpy as np

from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show, curdoc
from bokeh.models import ColumnDataSource, HoverTool, GroupFilter,CDSView, DateRangeSlider, CustomJS,Dropdown
from bokeh.layouts import row, column, gridplot, layout
from bokeh.models.widgets import Tabs, Panel, Slider, Select
from bokeh.resources import INLINE

from datetime import date

# Download dataset
!gdown --id 1LQUiVGxRW6wdXlUgx2SH3cSEyYfNZU0C

temp = pd.read_csv("indexProcessed.csv", parse_dates=['Date'])
temp

temp.info()

pd.unique(temp["Index"])

hsi = temp[temp.Index == 'HSI']
nya = temp[temp.Index == 'NYA']
nsei = temp[temp.Index == 'NSEI']

source_hsi = ColumnDataSource(data=hsi)
source_nya = ColumnDataSource(data=nya)
source_nsei = ColumnDataSource(data=nsei)

hsi.info()

# Menampilkan ke plot HTML
output_file('Level 1.html', title='Level 1')

# Membuat Figure untuk menampilkan adj close
fig1 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Adj. Close',
    title='Adj. Close',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot adj close dari Hangseng
a = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_hsi,
    color='blue',
    legend_label='HSI'
)

# Untuk menampilkan line plot adj close dari Nasdaq
b = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_nya,
    color='red',
    legend_label='NYA'
)

# Untuk menampilkan line plot adj close dari Nikkei
c = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_nsei,
    color='yellow',
    legend_label='NSEI'
)

# Bokeh Library
tooltips = [
            ('Index','@Name'),
            ('Adj. Close', '$@{Adj Close}{0.2f}')
]

# Menambahkan HoverTool untuk membuat fig
fig1.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Membuat Figure untuk menampilkan volume
fig2 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Volume',
    title='Volume',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot Volume dari Hangseng
a = fig2.line(
    x='Date',
    y='Volume',
    source=source_hsi,
    color='blue',
    legend_label='HSI'
)

# Untuk menampilkan line plot volume dari Hangseng
b = fig2.line(
    x='Date',
    y='Volume',
    source=source_nya,
    color='red',
    legend_label='NYA'
)

# Untuk menampilkan line plot volume dari Hangseng
c = fig2.line(
    x='Date',
    y='Volume',
    source=source_nsei,
    color='yellow',
    legend_label='NSEI'
)

# Bokeh Library
tooltips = [
            ('Index','@Name'),
            ('Volume', '@Volume')
]

# Menambahkan HoverTool untuk membuat fig
fig2.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Membuat Figure untuk menampilkan volume
fig3 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Close USD',
    title='Close USD',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot Volume dari Hangseng
a = fig3.line(
    x='Date',
    y='CloseUSD',
    source=source_hsi,
    color='blue',
    legend_label='HSI'
)

# Untuk menampilkan line plot volume dari Hangseng
b = fig3.line(
    x='Date',
    y='CloseUSD',
    source=source_nya,
    color='red',
    legend_label='NYA'
)

# Untuk menampilkan line plot volume dari Hangseng
c = fig3.line(
    x='Date',
    y='CloseUSD',
    source=source_nsei,
    color='yellow',
    legend_label='NSEI'
)

# Bokeh Library
tooltips = [
            ('Index','@Name'),
            ('Close USD', '@CloseUSD')
]

# Menambahkan HoverTool untuk membuat fig
fig3.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Menampilkan ke plot HTML
output_file('Level 3.html', title='Level 3')

fig1.legend.click_policy = 'hide'
fig2.legend.click_policy = 'hide'
fig3.legend.click_policy = 'hide'

# Membuat tiga panel yaitu Adj Close,Volume,Day Perc Change
Adj_Close = Panel(
    child=fig1,
    title='Adj Close'
)
Volume = Panel(
    child=fig2,
    title='Volume'
)
CloseUSD = Panel(
    child=fig3,
    title='Close USD'
)

tabs = Tabs(tabs=[
                  Adj_Close, Volume, CloseUSD
                ])

show(tabs)