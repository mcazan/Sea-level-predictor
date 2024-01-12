import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y)

    # Create first line of best fit
    x_p=np.arange(1880,2051,1)
    r=linregress(x,y)
    y_p=r.slope*x_p+r.intercept
    plt.plot(x_p,y_p, 'r')

    # Create second line of best fit
    df_new=df.loc[df['Year']>=2000]
    x2=df_new['Year']
    y2=df_new['CSIRO Adjusted Sea Level']
    x_p2=np.arange(2000,2051,1)
    r2=linregress(x2,y2)
    y_p2=r2.slope*x_p2+r2.intercept

    plt.plot(x_p2, y_p2,'y') 
  
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
  
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()