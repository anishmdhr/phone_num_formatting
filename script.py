# load the phone number data in a file
# check if phone number exists
# check correct number formatting
# convert it into international formatting
# save it into new file/replace in existing file 

import pandas as pd
import numpy as np
import re

# load the data in a file

data = pd.read_csv('phone_num_formatting\\sample\\au-500.csv')

phone_data  = data[["phone1","phone2"]]

phone1Regex = re.compile(r'0\d-\d\d\d\d-\d\d\d\d')
phone2Regex = re.compile(r'0\d\d\d-\d\d\d-\d\d\d')

for phone_num in phone_data["phone1"].head():
    # Check if phone_num is in the phone1Regex format
    if phone1Regex.search(phone_num):
        print(f"Phone number: {phone_num} is in correct format")
    else:
        print(f"Phone number: {phone_num} is not in correct format")

for phone_num in phone_data["phone2"].head():
    # Check if phone_num is in the phone1Regex format
    if phone2Regex.search(phone_num):
        print(f"Phone number: {phone_num} is in correct format")
    else:
        print(f"Phone number: {phone_num} is not in correct format")

# function to convert into international formatting
def convert_to_international(num):
    if num.startswith('0'):
        return '+61-' + num[1:]
    else:
        return num
    
for phone_num in phone_data['phone1']:
    print(convert_to_international(phone_num))
    

# data[['phone1_int','phone2_int']] = data[['phone1','phone2']].replace('0','+61', regex=True)

#export dataframe to a new csv file
# data.to_csv('phone_num_formatting\\sample\\au-500_int.csv', index=False)
