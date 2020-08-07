# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:54:48 2020

@author: Toshiba
"""


import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')


#Salary Parsing
df['employer provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('k','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('employer provided salary:', ''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary) / 2


#Company Name text only
df['company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)


#State Field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts


#Age of Company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)


#Parsing of Job Description(python, sql, R studio, Excel, etc.)

#Python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#R
df['R'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

#Spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#AWS
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#SQL
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() or 'SQL' in x.upper() else 0)

#Excel
df['microsoft_excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.to_csv('salary_data_cleaned.csv', index = False)

pd.read_csv('salary_data_cleaned.csv')




