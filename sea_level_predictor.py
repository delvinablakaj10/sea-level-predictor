import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    #Extract the data
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    #Generate new line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    #Create data from min year to 2050 for our line of best fit
    x_new = np.arange(x.min(), 2051)

    #Calculate the corresponding y values for our new x values using y=mx+c
    y_new = slope * x_new + intercept

    #Instantiate a Figure and Axes
    fig, ax = plt.subplots()

    #Plot the 'Year' and 'CSIRO Adjusted Sea Level' data
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    #Plot the new linear regression line
    ax.plot(x_new, y_new, color='red')

    print(f"The projected sea level rise in 2050 is: {y_new[-1]} units")

    plt.show()


    # Create first line of best fit
    


    # Create second line of best fit
    #Extract the data
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    #Generate new line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    #Create data from min year to 2050 for our line of best fit
    x_new = np.arange(x.min(), 2051)

    #Calculate the corresponding y values for our new x values using y=mx+c
    y_new = slope * x_new + intercept

    #Creating a new line from 2000 onward
    df_2000 = df[df['Year'] >= 2000]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']

    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(x_2000, y_2000)
    x_new_2000 = np.arange(x_2000.min(), 2051)
    y_new_2000 = slope_2000 * x_new_2000 + intercept_2000

    #Instantiate a Figure and Axes
    fig, ax = plt.subplots()

    #Plot the 'Year' and 'CSIRO Adjusted Sea Level' data
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])



    #Plot the new linear regression line
    ax.plot(x_new, y_new, color='red')

    #Plot the new linear regression line from 2000 onward
    ax.plot(x_new_2000, y_new_2000, color='green')

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    plt.show()


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()