# Python smart functions for HRM
"""
Student Name: Florian Sebastian Stanglmeier

Student Number: 11815994

Selected Topic: Big Data HRM analysis - Equality Analysis
"""

# Import the dependencies
from contextlib import nullcontext
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.graph_objs as go


# Function: [1]
# Read the CSV provided by Kaggle (https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset/version/1)


def read_data():
    data = pd.read_csv('data/hrm.csv')
    data.shape  # Prints the shape (here 1470 rows and 35 columns)
    data  # Print data to see what we're working with:
    data.describe()  # Prints information on the dataframe (count, mean,std, min...)
    return data

# Function: [2]
# Find people who work with the same manager since they started -> means that TotalWorkingYears must equal YearsWithCurrManager


def people_with_same_Manager():
    data = read_data()
    df_sameManagerSinceStart = data.loc[(
        data['TotalWorkingYears'] == data['YearsWithCurrManager'])]
    print(df_sameManagerSinceStart,
     "This is a list of employees who work under the same manager since they started working:")
    return df_sameManagerSinceStart


# [TESTED]: WORKING
people_with_same_Manager()
input("Press Enter to continue to the next function...")

# Function: [3]
# Find workers who are over and under 30 years to prevent age discrimination


def prevent_age_discrimination():
    df_sameManagerSinceStart = people_with_same_Manager()
    df_young = df_sameManagerSinceStart.loc[(
        df_sameManagerSinceStart["Age"] <= 30)]
    df_young

    df_old = df_sameManagerSinceStart.loc[(
        df_sameManagerSinceStart["Age"] > 30)]
    df_old

    # Display results from [3] in text
    len(df_old.index)
    len(df_young.index)
    print('When looking at the people who have the same managers since they started, only', len(df_old.index),
          'older people work with the same manager, while', len(df_young.index), 'young people work with the same manager.')


# [TESTED]: WORKING
prevent_age_discrimination()
input("Press Enter to continue to the next function...")


# Function: [4]
# Find people who are with the same manager since the beginning and have been in his/her role for over x=5 years


def no_new_roles():
    df_sameManagerSinceStart = people_with_same_Manager()
    df_noNewRoles = df_sameManagerSinceStart.loc[(
        df_sameManagerSinceStart['YearsInCurrentRole'] >= 5)]
    print(df_noNewRoles.head())
    print("There are", len(df_noNewRoles.index),
          "workers in this company who are with the same manager since their start and are in the same role for over 5 years")
    return df_noNewRoles


# [TESTED]: WORKING
no_new_roles()
input("Press Enter to continue to the next function...")


# Function: [5]
# Show from which departments those people are (who do their role since +5 years and have the same manager)
# Indicates the departments (especially also number of departments) which should implement a new promotion strategy
# since the people work in their role for  over 5 years with the same manager


def plot_noNewRoles():
    df_noNewRoles = no_new_roles()
    df_noNewRoles.groupby('Department')['Age'].nunique().plot(kind='bar')
    plt.title('Program will continue when you close this plot.')
    plt.show()


# [TESTED]: WORKING
plot_noNewRoles()
input("Press Enter to continue to the next function...")
# Helper function


def load_csv_as_df():
    df = pd.read_csv('data/hrm.csv')
    return df

# Function: [6]
# Divide workforce into age groups 
# Find out if the wage for a whole group is significantly larger/lower
# The median of the groups will be used
def pay_by_age():
    data = pd.read_csv("data/hrm.csv")
    # Ceate dataframe of age groups using the pandas cut method
    df = pd.cut(data['Age'], bins=[16, 25, 40, 55, np.inf])
    # Create crosstable against the mean of the Daily Rate of the specific age groups
    ax = pd.crosstab(df, data['DailyRate'].mean())
    # Create simple plot using matplotlib and save plot as pdf
    ax.plot()
    plt.savefig('data/AverageHourlyRate.pdf')
    print(ax)

# [TESTED]: Failed
pay_by_age()
input("Press Enter to continue to the next function...")

# Function: [7]
# Visualize the individually chosen user inputs in a interactive, scalable 3D model
# x denotes input 1, z denotes input 2 and y input 3, respectively
# Configure Plotly to be rendered inline in the notebook.
def scatterplot_3d():
    print("Now choose three parameters you want to 3D Plot:")
    df = pd.read_csv('data/hrm.csv')
    input1 = input("Enter your first Parameter (example: Age) => ")
    print("parameter1: ",  input1)
    input2 = input("Enter your second Parameter (example: Department)  => ")
    print("parameter2: ",  input2)
    input3 = input("Enter your third Parameter (example: DistanceFromHome ) => ")
    print("parameter3: ",  input3)

    df_clean = df[[input1, input2, input3]]
    print(df_clean)
    print("This is the data frame that only contains your specified data")
    user_pref = input("You can either save the data frame: Press s - OR - Continue without saving it as a csv: Press c (Press Enter after submission) => ")
    if user_pref == "s":
        df_clean.to_csv("data/3D_PlotData_asCSV.csv")
    elif user_pref == "c":
        print("Continuing")
    else :
        print("No specified action. Continuing without saving data to CSV.")

    # Configure the trace.
    trace = go.Scatter3d(
        x=df_clean[input1],
        z=df_clean[input2],
        y=df_clean[input3],
        mode='markers',
        marker={
            'size': 10,
            'opacity': 0.8,
        }
    )
    # Configure the layout.
    layout = go.Layout(
        margin={'l': 0, 'r': 0, 'b': 0, 't': 0}
    )
    data = [trace]
    plot_figure = go.Figure(data=data, layout=layout)
    # Render the plot.
    plotly.offline.plot(plot_figure)


# [TESTED]: WORKING
scatterplot_3d()
input("Press Enter to continue to the next function...")
# Function: [8]
# See whether the environment satisfaction is coupled to age in any way
# This function sorts a list by descending satisfaction and displays the age
# Useful to see if only younger or older workers are satisfied with their environment


def environment_satisfaction():
    df = load_csv_as_df()
    print(df[['Age', 'EnvironmentSatisfaction']].groupby(['Age'],
                                                         as_index=False).mean().sort_values(by='EnvironmentSatisfaction',
                                                                                            ascending=False),"Environment Satisfaction by Age: Descending Satisfaction")


# [TESTED]: WORKING
environment_satisfaction()
input("Press Enter to continue to the next function...")
# Function: [9]
# Locate recently promoted (User specific: Choose employees promoted in the last n years)


def recently_promoted():
    df = load_csv_as_df()
    i = int(input('Search for employees promoted in the last n years: n => '))
    d = str(input('What department do you want to filter for? (e.g. Sales )=> '))
    df_promo = df.loc[(df["YearsSinceLastPromotion"] <= i)
                      & (df['Department'] == d)]
    print(df_promo)


# [TESTED]: WORKING
recently_promoted()
input("Press Enter to continue to the next function...")

# Function: [10]
# Turnover by department analysis
# Group by departments and display average years at company for a whole department


def turnover_by_dpt():
    df = load_csv_as_df()
    print(df[['Department', 'YearsAtCompany']].groupby(['Department'],
                                                       as_index=False).mean().sort_values(by='YearsAtCompany',
                                                                                          ascending=False))


# [TESTED]: WORKING
turnover_by_dpt()

# Summary of the document in the ReadMe.md File