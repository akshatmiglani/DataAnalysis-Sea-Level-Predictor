import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    A = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1=np.arange(df['Year'].min(),2051)
    y1=x1*A.slope + A.intercept
    plt.plot(x1,y1,'r')
    # Create second line of best fit
    df_new=df[df['Year'] >= 2000]
    B=linregress(df_new['Year'],df_new['CSIRO Adjusted Sea Level'])
    x2=np.arange(2000,2051)
    y2= x2*B.slope+B.intercept
    plt.plot(x2,y2)
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()