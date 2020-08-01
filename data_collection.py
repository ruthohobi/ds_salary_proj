# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:36:53 2020

@author: Toshiba
"""


import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Toshiba/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
