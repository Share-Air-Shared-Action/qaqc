import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import pandas as pd
import csv
import numpy as np
import pylab
from pylab import xticks



df = pd.read_csv('purpleairprimary.csv', usecols = ['created_at','pm10_cf_atm_ugm3'])
df['created_at'] = pd.to_datetime(df['created_at'])

x = df['created_at']
y = df['pm10_cf_atm_ugm3']
m = round(df['pm10_cf_atm_ugm3'].mean(),3)
numzero =round(((df['pm10_cf_atm_ugm3'] == 0.000).sum()/(len(df['pm10_cf_atm_ugm3']))),5)*100
print(len(df['pm10_cf_atm_ugm3']))
n = df['pm10_cf_atm_ugm3'].count()
print (n)
st = round(df['pm10_cf_atm_ugm3'].std(),3)
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

no2_plot = df['pm10_cf_atm_ugm3'].hist(bins=50)
df['pm10_cf_atm_ugm3'] = df['pm10_cf_atm_ugm3'].replace(0, np.NaN)
print(df['pm10_cf_atm_ugm3'].mean())
mean = df['pm10_cf_atm_ugm3'].mean()
std = df['pm10_cf_atm_ugm3'].std()
nz = df['pm10_cf_atm_ugm3'].count()
print(nz)
outliers=round(((df['pm10_cf_atm_ugm3']>(mean + 4*std)).sum())/nz,5)*100
print(outliers)
no2_plot.axvline(x=mean, color='g', linestyle='solid', linewidth=2, label = 'mean')
#text(mean,1560,'Mean',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
# no2_plot.axvline(x=mean-std, color='r', linestyle='dashed', linewidth=2, label ='standard deviation')
# text(mean-std,1450,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean + std, color='r', linestyle='dashed', linewidth=2, label ='standard deviation')
#text(mean+std,1450,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
# no2_plot.axvline(x=mean+2*std, color='r', linestyle='dashed', linewidth=2)
# text(mean+2*std,1450,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
# no2_plot.axvline(x=mean + 3*std, color='r', linestyle='dashed', linewidth=2)
# text(mean+3*std,1450,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
# no2_plot.axvline(x=mean + 4*std, color='r', linestyle='dashed', linewidth=2)
# text(mean + 4 *std,1250,'Standard deviation percentage: '+ str(outliers)+'%',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.set_title("PM10 ug/m3", fontsize = 36)
no2_plot.set_xlabel("ug/m3", fontsize = 24)
no2_plot.set_ylabel("Frequency", fontsize =24)
no2_plot.text(0.96,0.96,'Total observations with zeros: '+str(n)+'\nZeros in percentage: '+str(numzero)+'%'+'\n\n\nTotal observations without zeros: '+str(nz)+'\nMean without zeros: '+ str(round(mean,3))+'\nStandard deviations without zeros: '+str(round(std,3)),
              horizontalalignment='right',verticalalignment='top',transform=no2_plot.transAxes,
              fontdict = font,bbox=dict(facecolor='white', edgecolor='black', pad=10))
plt.legend(loc ='center right')
plt.show()