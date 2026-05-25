# 1. library must be import to use
# 2. read_excel() -> load data to display
# 3. .info() allow us to view the details of data
# 4. isna() help us to detect invalid / missing value
# 5. dropna() help us to remove missing value / data

# import python library to use
import pandas as pd # pandas for data analysis, manage, cleaning
import matplotlib.pyplot as plt # for visualize purpose

# 1. Data Collection - read & load data out from files
data = pd.read_excel('https://github.com/Code-Gen-Hub/Data_Analytic_Workshop/raw/main/Employee%20Sample%20Data.xlsx')
print(data.info())

# 2. Data Cleaning - check for missing value
missing_value = data.isna().sum()
print(missing_value)

# remove missing value .dropna()
cleaned_data = data.dropna()
print(cleaned_data.info())

# 3. Data Mining
# Average annual salary grouped by department
average_salary = (
    cleaned_data.groupby('Department') # group each department
    ['Annual Salary'].mean() # calculate average annual salary (each dept)
    .reset_index() # set index number
)

average_salary.index = average_salary.index + 1

print(average_salary)

# 4. Data Visualization
# bar chart - bar(x, y)
plt.bar(average_salary['Department'], average_salary['Annual Salary'])
