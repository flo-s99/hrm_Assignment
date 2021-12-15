[SETUP]

1. Activate a virtual environment. Here I used .venv and it can be activated by typing in the command line:
   source .venv/bin/activate
2. The dependencies are locked in the requirements.txt file generated with a pip freeze in a virtual environment. To install the requirements type:
   pip install -r requirements.txt

[EXPLANATIONS]

1. The functions are primariy focused to perform big data employee analysis and is optimized as of right now for visualizing fairness within a firms' HR management

2. Each function is indexed [1-10] and explained in the # section. I will still give further explanation here:

[1] Open the CSV file in the directory and transform it into a pandas dataframe. Then we(a) see what shape our data has(how many rows of data entries and how many columns/features). Next, (b) we display the data to get an inuition how our data looks, what features there are and whether there are missing values. After that, we(c) display some general information for the whole dataframe: Median values, max/min values, std and so on.

[2] Find people who work with the same manager since they started working: This indicates that either these people aren't working for many years or that their manager doesn't promote them. Analyzing this is a great indicator to find bad relationships or / and managers within the company.

[3] This function let's us explore, whether the group from before, who didn't get promoted and are with the same manager, is discriminated regarding age: When nearly all people are younger than 30 this would indicate the company doesn't promote young talent.

[4] Since a lower age could also mean that they don't have as much experience, we check how many people of the above mentioned group are in their current role for over 5-years, which means, they are pretty surely discriminated, as they do their job for quite a while. So, we find people who are with the same manager since the beginning and have been in his/her role for over x = 5 years.

[5] Show from which departments those people are(who do their role since + 5 years and have the same manager. Indicates the departments(especially also number of departments) which should implement a new promotion strategy since the people work in their role for over 5 years with the same manager.

[6] This function tries to analyze whether certain age groups are significantly paid different than others. For that, we group the workers into 4 groups: Youngest (16-25 years), Young (26-40 years), Medium (40-55) and Old (56-infinity). We should observe linear or really subtle exponential grwoth, because over the years, workers shold get wage raises. The file is stored as a PDF file for convenience (in data folder), but the console also logs the raw data output.

[7] This function let's the user choose any three features he/she likes (numerical features). Then, after choosing the desired features, the researcher will be automatically provided with a cleaned dataset containing only the desired features. This is done by a data query of the original dataframe with regards to the specific user input. The user can either decide to save and export the data as CSV or just continue. We use the input data of the viewerto then construct a 3D Plot. One can perform three dimensional analysis, especially in form of 3D-scatterplots, which are interactive: This means the user is able to spin and zoom the rendered model. This can be really helpful in combination with clustering or just to see outliers in a three-dimensional space with regards to the chosen feature set. Model is also saved as a .html file.

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
