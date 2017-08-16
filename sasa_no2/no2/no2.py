import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import pandas as pd
import scipy.stats
import csv
import numpy as np
import datetime

#put two columns of csv file into pandas
df = pd.read_csv('no2.csv', usecols = ['date','no2ppm'])
#initialize the data as datetime of pandas
df['date'] = pd.to_datetime(df['date'])
#set x axis is date
x = df['date']
#set y axis is no2ppm
y = df['no2ppm']
#get the mean of no2ppm before replaced zeros
m = round(df['no2ppm'].mean(),3)
#get the percentage of zeros by using the sum divided the total number of no2ppm
numzero =round(((df['no2ppm'] == 0.000).sum()/(len(df['no2ppm']))),5)*100
print(len(df['no2ppm']))
#count the total number of no2ppm
n = df['no2ppm'].count()
print (n)
#calculate the standard deviations before replaced zeros
st = round(df['no2ppm'].std(),3)
#defined the font format
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
#define the no2_plot is histogram
no2_plot = df['no2ppm'].hist(bins=50)
#replace all zeros to nan
df['no2ppm'] = df['no2ppm'].replace(0, np.NaN)
print(df['no2ppm'].mean())
#used pandas function to calculate the mean
mean = df['no2ppm'].mean()
#used pandas function to calculate the standard deviations
std = df['no2ppm'].std()
#calculate the count of no2ppm after replaced zeros
nz = df['no2ppm'].count()
print(nz)
#the outliers is after 5 standadard deviations percentage
outliers=round(((df['no2ppm']>(mean + 4*std)).sum())/nz,5)*100
print(outliers)
#plot the mean and five standarad deviations and label the mean
no2_plot.axvline(x=mean, color='g', linestyle='solid', linewidth=2, label = 'mean')
text(mean,1560,'Mean',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean-std, color='r', linestyle='dashed', linewidth=2, label ='standard deviation')
text(mean-std,1450,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean + std, color='r', linestyle='dashed', linewidth=2)
text(mean+std,1450,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean+2*std, color='r', linestyle='dashed', linewidth=2)
text(mean+2*std,1450,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean + 3*std, color='r', linestyle='dashed', linewidth=2)
text(mean+3*std,1450,'Standard deviation',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
no2_plot.axvline(x=mean + 4*std, color='r', linestyle='dashed', linewidth=2)
text(mean + 4 *std,1250,'Standard deviation percentage: '+ str(outliers)+'%',rotation=270,horizontalalignment='left',verticalalignment='center', fontsize = 16)
#set the title of the plot
no2_plot.set_title("NO2 PPM", fontsize = 36)
#set the x label is ppm, as well as the font size
no2_plot.set_xlabel("PPM", fontsize = 24)
#set the y axis label is ppm, as well as font size
no2_plot.set_ylabel("Frequency", fontsize =24)
#set the position of text, and put the all the things in the text, as well as set the font, bonding box, also the color.
no2_plot.text(0.96,0.96,'Total observations with zeros: '+str(n)+'\nZeros in percentage: '+str(numzero)+'%'+'\n\n\nTotal observations without zeros: '+str(nz)+'\nMean without zeros: '+ str(round(mean,3))+'\nStandard deviations without zeros: '+str(round(std,3)),
              horizontalalignment='right',verticalalignment='top',transform=no2_plot.transAxes,
              fontdict = font,bbox=dict(facecolor='white', edgecolor='black', pad=10))
plt.legend(loc ='center right')
plt.show()



