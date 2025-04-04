MODULE END PROJECT

import pandas as pd
import numpy as np

df = pd.read_csv('Documents/Companydata.csv')
df['height'] = np.random.randint(150, 181, size=len(df))

print(df.info())
print(df.head())

# 1. Employee Distribution by Team

team_distribution = df['Team'].value_counts()
team_percentage = (team_distribution / len(df)) * 100

print(pd.DataFrame({
    'Employee Count': team_distribution,
    'Percentage': team_percentage.round(3)
}))

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.countplot(x='Team', data=df, order=team_distribution.index)
plt.title('Employee Distribution by Team')
plt.xticks(rotation=45)
plt.ylabel('Number of Employees')
plt.tight_layout()
plt.show()

# 2. Segregate Employees by Position

position_counts = df['Position'].value_counts()
print(position_counts)

plt.figure(figsize=(10, 6))
sns.countplot(y='Position', data=df, order=position_counts.index)
plt.title('Employee Distribution by Position')
plt.xticks(rotation=45)
plt.xlabel('Count' )
plt.tight_layout()
plt.show()

# 3. Predominant Age Group

bins = [20, 30, 40, 50, 60, 70]
labels = ['20-29', '30-39', '40-49', '50-59', '60-69']
df['age_group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

age_group_counts = df['age_group'].value_counts().sort_index()
print(age_group_counts)

plt.figure(figsize=(8, 5))
sns.barplot(x=age_group_counts.index, y=age_group_counts.values)
plt.title('Employee Age Group Distribution')
plt.ylabel('Number of Employees')
plt.xlabel('Age Group')
plt.tight_layout()
plt.show()

# 4. Highest Salary Expenditure by Team and Position

team_salary = df.groupby('Team')['Salary'].sum().sort_values(ascending=False)
print("Top Team by Salary Expenditure:", team_salary.head(1))

plt.figure(figsize=(10, 6))
sns.barplot(x=team_salary.index, y=team_salary.values)
plt.title('Salary Expenditure by Team')
plt.xlabel('Team')
plt.ylabel('Total Salary Expenditure')
plt.xticks(rotation=45)
plt.show()

# 5. Correlation Between Age and Salary

correlation = df['Age'].corr(df['Salary'])
print(f"Correlation between Age and Salary: {correlation:.2f}")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Age', y='Salary', alpha=0.7)
sns.regplot(data=df, x='Age', y='Salary', scatter=False, color='red')
plt.title('Age vs. Salary')
plt.tight_layout()
plt.show()


avg_salary_by_age = df.groupby('Age')['Salary'].mean()
plt.figure(figsize=(8, 5))
avg_salary_by_age.plot(kind='line', marker='o')
plt.title('Average Salary by Age')
plt.xlabel('Age')
plt.ylabel('Average Salary')
plt.grid(True)
plt.tight_layout()
plt.show()

Data Story
Team New Orleans Pelicans having the highest number of Employees.
Teams Orlando Magic and Minnesota Timberwolves having the least number of employees.
Position SG had the highest representation, suggesting it plays a central role in the company’s operations.
The most predominant age group was 20-29 years, followed by the 30-39 range.
The team with the highest salary expenditure was Team Cleveland Cavaliers.