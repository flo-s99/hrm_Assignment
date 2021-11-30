# -*- coding: utf-8 -*-
# Python smart functions for HRM
"""
Student Name: Florian Sebastian Stanglmeier

Student Number: 11815994

Selected Topic: Big Data HRM analysis - Equality Analysis
"""

# Import the dependencies
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
    data = pd.read_csv('hrm.csv')
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
    print("This is a list of employees who work under the same manager since they started working:",
          df_sameManagerSinceStart)
    return df_sameManagerSinceStart


# [TESTED]: WORKING
# people_with_same_Manager()

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
# prevent_age_discrimination()

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
# no_new_roles()

# Function: [5]
# Show from which departments those people are (who do their role since +5 years and have the same manager)
# Indicates the departments (especially also number of departments) which should implement a new promotion strategy
# since the people work in their role for  over 5 years with the same manager


def plot_noNewRoles():
    df_noNewRoles = no_new_roles()
    df_noNewRoles.groupby('Department')['Age'].nunique().plot(kind='bar')
    plt.show()


# [TESTED]: WORKING
# plot_noNewRoles()

# Helper function


def load_csv_as_df():
    df = pd.read_csv('hrm.csv')
    return df

# Function: [6]
# 3 dimensional analysis with individual user input for flexibility
# Generates new DataFrame with just the specified parameters


def data_plot_3d():
    df = pd.read_csv('hrm.csv')
    input1 = input("Enter your first Parameter (example: Age)")
    print("parameter1: ",  input1)
    input2 = input("Enter your second Parameter (example: Department)")
    print("parameter2: ",  input2)
    input3 = input("Enter your third Parameter (example: DistanceFromHome )")
    print("parameter3: ",  input3)

    df_clean = df[[input1, input2, input3]]
    print(df_clean)
    return df_clean, input1, input2, input3


# [TESTED]: WORKING
# data_plot_3d()


# Function: [7]
# Visualize the individually chosen user inputs in a interactive, scalable 3D model
# x denotes input 1, z denotes input 2 and y input 3, respectively
# Configure Plotly to be rendered inline in the notebook.
def scatterplot_3d():
    df_clean, input1, input2, input3 = data_plot_3d()
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
# scatterplot_3d()

# Function: [8]
# See whether the environment satisfaction is coupled to age in any way
# This function sorts a list by descending satisfaction and displays the age
# Useful to see if only younger or older workers are satisfied with their environment


def environment_satisfaction():
    df = load_csv_as_df()
    print(df[['Age', 'EnvironmentSatisfaction']].groupby(['Age'],
                                                         as_index=False).mean().sort_values(by='EnvironmentSatisfaction',
                                                                                            ascending=False))


# [TESTED]: WORKING
# environment_satisfaction()

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
# recently_promoted()

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

# Summary of the document (Also in ReadMe.md file):
"""
1. The functions are primariy focused to perform big data employee analysis and is optimized as of right now for visualizing fairness analysis

2. Each function is indexed[1-10] and explained in the # section. I will still give further explanation here:

[1] Open the CSV file in the directory and transform it into a pandas dataframe. Then we(a) see what shape our data has(how many rows of data entries and how many columns/features). Next, (b) we display the data to get an inuition how our data looks, what features there are and whether there are missing values. After that, we(c) display some general information for the whole dataframe: Median values, max/min values, std and so on.

[2] Find people who work with the same manager since they started working: This indicates that either these people aren't working for many years or that their manager doesn't promote them. Analyzing this is a great indicator to find bad relationships or / and managers within the company.

[3] This function let's us explore, whether the group from before, who didn't get promoted and are with the same manager, is discriminated regarding age: When nearly all people are younger than 30 this would indicate the company doesn't promote young talent.

[4] Since a lower age could also mean that they don't have as much experience, we check how many people of the above mentioned group are in their current role for over 5-years, which means, they are pretty surely discriminated, as they do their job for quite a while. So, we find people who are with the same manager since the beginning and have been in his/her role for over x = 5 years.

[5] Show from which departments those people are(who do their role since + 5 years and have the same manager. Indicates the departments(especially also number of departments) which should implement a new promotion strategy since the people work in their role for over 5 years with the same manager.

[6] This function let's the user choose any three features he/she likes(numerically). Then, after choosing the desired features, the researcher will be automatically provided with a cleaned dataset containing only the desired features. This is done by a data query of the original dataframe with regards to the specific user input.

[7] In this section we leverage the cleaned dataset by the researcher. One can perform three dimensional analysis, especially in form of 3D-scatterplots, which are interactive: This means the user is able to spin and zoom the rendered model. This can be really helpful in combination with clustering or just to see outliers in a three-dimensional space with regards to the chosen feature set.

[8] To hold on to the principle of equality analysis, we want to check with regards to the feature "Environment Satisfaction", whether satisfaction is dependent on age. To analyze this all ages are grouped and then compared in descending order with their satisfaction.

[9] This function is to perform further in depth equality analysis: This section is, again, completely customizable by the user. We let the researcher query a list, in which there are only employees which:
- Were promoted in the last n years
- And belong to the department d

This is really helpful to find inequalities across departments.

[10] The last function is of great general importance: We calculate employee-turnover by department. Monitoring in which department the people stay the longest is a significant indicator for great working conditions, while less years at the company in department d denote lower employee satisfaction in this very department.


3. This smartsheet can be used for a broad spectrum of big data employee analysis. Concrete other functions include:

- Checking whether employees from one department get more training than others

- Visualizing three dimensional triplets to see whether wanted or unwanted patterns are forming, for example find out if WorkLifeBalance has a connection with Department and YearsAtCompany

- Check whether people who travel frequently are more satisfied overall than those who don't

- Find paygaps based on patterns(Lower age -> Lower pay? and so on..)
"""
