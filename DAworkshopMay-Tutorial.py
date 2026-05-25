# Dataset 2
# Task 1: Import necessary library
import pandas as pd
import matplotlib.pyplot as plt

# Task 2: Read & load file (show its details)
data = pd.read_excel('https://raw.githubusercontent.com/Code-Gen-Hub/Data-Analytic-Workshop-Tutorial/0fdf2909c7c8100f17d31102d5ab564d93537b37/Employee_Data_Tutorial.xlsx')
print(data)

# Task 3: Clean missing value
missing_value = data.isna().sum()
print(missing_value)

cleaned_data = data.dropna()
print(cleaned_data.info())

# ----- Extra: Clean duplicate data ----
duplicate_value = data.duplicated().sum()
print('------', duplicate_value)

cleaned_duplicate = cleaned_data.drop_duplicates()
print('***', cleaned_duplicate.info())

# Task 4: Average age grouped by department
average_age = (
    cleaned_data.groupby('Department')
    ['Age'].mean()
    .reset_index()
)
print(average_age)

# Task 5: Create bar chart
plt.bar(average_age['Department'], average_age['Age'])
