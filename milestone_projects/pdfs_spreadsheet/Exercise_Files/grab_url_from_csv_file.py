import re
import csv

'''
Learned enumerate to grab URL from a csv puzzle
'''


def read_csv(csv_file):
    f = open(csv_file, encoding ='utf-8')
    csv_data = csv.reader(f)
    data_lines = list(csv_data)

    f.close()
    return data_lines

url_pattern = r'(https?://[^\s]+)'
result = ""

data_lines = read_csv("milestone_projects/pdfs_spreadsheet/Exercise_Files/find_the_link.csv")

print('\n' * 100)

for row_num, data_line in enumerate(data_lines):
    print(f"'\n{data_line}") 
    result += data_line[row_num]

print('\n' * 2)

print((re.match(url_pattern, result))[0])

print(result)  