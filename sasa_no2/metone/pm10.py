import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import pandas as pd
import csv
import numpy as np
import datetime
import matplotlib.dates as mdates


df = pd.read_csv('pm10.csv', usecols = ['time','value'])
df['time'] = pd.to_datetime(df['time'])

x = df['time']
y = df['value']

m = round(df['value'].mean(),3)
numzero =round(((df['value'] == 0.000).sum()/(len(df['value']))),5)*100
print(len(df['value']))
n = df['value'].count()
print (n)
st = round(df['value'].std(),3)
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
no2_plot = df['value'].hist(bins=50)
df['value'] = df['value'].replace(0, np.NaN)
print(df['value'].mean())
mean = df['value'].mean()
std = df['value'].std()
nz = df['value'].count()
print(nz)
outliers=round(((df['value']>(mean + 4*std)).sum())/nz,5)*100
print(outliers)
no2_plot.axvline(x=mean, color='g', linestyle='solid', linewidth=2, label = 'mean')
text(mean,240,'Mean',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean-std, color='r', linestyle='dashed', linewidth=2, label ='standard deviation')
text(mean-std,220,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean + std, color='r', linestyle='dashed', linewidth=2)
text(mean+std,220,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean+2*std, color='r', linestyle='dashed', linewidth=2)
text(mean+2*std,220,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean + 3*std, color='r', linestyle='dashed', linewidth=2)
text(mean+3*std,220,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean + 4*std, color='r', linestyle='dashed', linewidth=2)
text(mean + 4 *std,190,'Standard deviation percentage: '+ str(outliers)+'%',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.set_title("PM10 PPM", fontsize = 36)
no2_plot.set_xlabel("ug/m3", fontsize = 24)
no2_plot.set_ylabel("Frequency", fontsize =24)
no2_plot.text(0.96,0.96,'Total observations with zeros: '+str(n)+'\nZeros in percentage: '+str(numzero)+'%'+'\n\n\nTotal observations without zeros: '+str(nz)+'\nMean without zeros: '+ str(round(mean,3))+'\nStandard deviations without zeros: '+str(round(std,3)),
              horizontalalignment='right',verticalalignment='top',transform=no2_plot.transAxes,
              fontdict = font,bbox=dict(facecolor='white', edgecolor='black', pad=10))
plt.legend(loc = 'center right')
plt.show()