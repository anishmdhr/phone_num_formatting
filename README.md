Sample data from: https://www.briandunning.com/sample-data/

This script takes all phone numbers (various formats of phone number in Australia) in a file and changes them into international format.

The script tskes these steps to achieve the said outcome:

1. Loads the sample data into a data frame using pandas
2. Extracts the columns containing phone numbers
3. Compares the phone numbers to regular experessions to determine if they are phone numbers in required format
4. Converts the phone numbers that are valid into international format
5. Create new dataframe containing only specific columns
6. Export the new dataframe to both a csv and xlsx file

P.S. There is a problem of the international format phone numbers being converted into formula when opened in Excel. The csv file itsef is correct and the problem doesnot persist when exporting the dataframe as an Excel file.
