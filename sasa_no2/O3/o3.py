import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import pandas as pd
import csv
import numpy as np
import datetime


df = pd.read_csv('o3.csv', usecols = ['date','o3ppm'])


df['date'] = pd.to_datetime(df['date'])

x = df['date']
y = df['o3ppm']
m = round(df['o3ppm'].mean(),3)
numzero =round(((df['o3ppm'] == 0.000).sum()/(len(df['o3ppm']))),5)*100
print(len(df['o3ppm']))
n = df['o3ppm'].count()
print (n)
st = round(df['o3ppm'].std(),3)
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
no2_plot = df['o3ppm'].hist(bins=50)
df['o3ppm'] = df['o3ppm'].replace(0, np.NaN)
print(df['o3ppm'].mean())
mean = df['o3ppm'].mean()
std = df['o3ppm'].std()
nz = df['o3ppm'].count()
print(nz)
outliers=round(((df['o3ppm']>(mean + 2*std)).sum())/nz,5)*100
print(outliers)
no2_plot.axvline(x=mean, color='g', linestyle='solid', linewidth=2, label = 'mean')
text(mean,1920,'Mean',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean-std, color='r', linestyle='dashed', linewidth=2, label ='standard deviation')
text(mean-std,1750,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean + std, color='r', linestyle='dashed', linewidth=2)
text(mean+std,1750,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean+2*std, color='r', linestyle='dashed', linewidth=2)
text(mean+2*std,1650,'Standard deviation: '+ str(outliers)+'%',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean + 3*std, color='r', linestyle='dashed', linewidth=2)
text(mean+3*std,1750,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean + 4*std, color='r', linestyle='dashed', linewidth=2)
text(mean + 4 *std,1750,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.set_title("O3 PPM", fontsize = 36)
no2_plot.set_xlabel("PPM", fontsize = 24)
no2_plot.set_ylabel("Frequency", fontsize =24)
no2_plot.text(0.96,0.96,'Total observations with zeros: '+str(n)+'\nZeros in percentage: '+str(numzero)+'%'+'\n\n\nTotal observations without zeros: '+str(nz)+'\nMean without zeros: '+ str(round(mean,3))+'\nStandard deviations without zeros: '+str(round(std,3)),
              horizontalalignment='right',verticalalignment='top',transform=no2_plot.transAxes,
              fontdict = font,bbox=dict(facecolor='white', edgecolor='black', pad=10))
plt.legend(loc ='center right')
plt.show()