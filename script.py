import pandas as pd
import os
import re
import csv

# Set current working directory from current directory to phone_num_formatting
os.chdir('phone_num_formatting')

# load the data in a file
data = pd.read_csv('sample\\au-500.csv')

# Extract the phone number columns
phone_data  = data[["phone1","phone2"]]

# Regular expressions for checking phone number formats
phone1Regex = re.compile(r'0\d{1}-\d{4}-\d{4}')  # landline format
phone2Regex = re.compile(r'0\d{3}-\d{3}-\d{3}')  # Mobile format   


def check_format_and_convert(num):
    if re.match(phone1Regex, num) or re.match(phone2Regex, num):  # Using re.match instead of re.search
        return "+61-" + num[1:]  # Convert to international format
    else:
        return None  # Invalid format, return None

# take each phone number and convert it to international format
data['phone1_intl'] = phone_data['phone1'].apply(check_format_and_convert)
data['phone2_intl'] = phone_data['phone2'].apply(check_format_and_convert)

# Drop rows only when both 'phone1_intl' and 'phone2_intl' are invalid
data = data.dropna(subset=['phone1_intl', 'phone2_intl'], how='all')

# print(data.head())

data.to_excel('sample\\au-500-intl.xlsx', index=False)

# export dataframe to a new csv file
# Error: phone numbers being calculated as formula in excel file
data.to_csv('sample\\au-500-intl.csv', index=False)

