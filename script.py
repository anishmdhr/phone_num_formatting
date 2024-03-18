# load the phone number data in a file
# check if phone number exists
# check correct number formatting
# convert it into international formatting
# save it into new file/replace in existing file 

import pandas as pd
import os
import re
import csv

# Set current working directory from current directory to phone_num_formatting
os.chdir('phone_num_formatting')

# load the data in a file

data = pd.read_csv('sample\\au-500.csv')

phone_data  = data[["phone1","phone2"]]

# Regular expressions for checking phone number formats
phone1Regex = re.compile(r'0\d{1}-\d{4}-\d{4}')  
phone2Regex = re.compile(r'0\d{3}-\d{3}-\d{3}')


def check_format_and_convert(num):
    if re.match(phone1Regex, num):  # Using re.match instead of re.search
        return "+61-" + num[1:]  # Convert to international format
    elif re.match(phone2Regex, num):
        return "+61-" + num[1:]  # Convert to international format
    else:
        return None  # Invalid format, return None

# take each phone number and convert it to international format
data['phone1_intl'] = phone_data['phone1'].apply(check_format_and_convert)
data['phone2_intl'] = phone_data['phone2'].apply(check_format_and_convert)

# Drop rows with invalid phone numbers
data = data.dropna(subset=['phone1_intl', 'phone2_intl'])

print(data.head())


# save the modified data to a new CSV file

data.to_csv('sample\\formatted_phone_numbers.csv', index=False)
# Error: phone numbers being calculated as formula in excel file

data.to_excel('sample\\au-500-intl.xlsx', index=False)

# export dataframe to a new csv file
data.to_csv('sample\\au-500-intl.csv', index=False, quoting=csv.QUOTE_ALL)




