import csv
import re

email_pattern = r'[^@]+@[^@]+\.[^@]+'

def extract_eamil_from_string(email_pattern, mystring):
    return (re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', mystring))[0]

def read_csv_file(csv_file):
    f = open(csv_file, encoding='utf8')
    csv_data = csv.reader(f)
    csv_data_lines = list(csv_data)
    f.close()
    return csv_data_lines

def create_csv_file(new_csv_file, rows, newline = ''):
    f = open(new_csv_file, "w")
    csv_writer = csv.writer(f, delimiter=',', quoting = csv.QUOTE_ALL)
    csv_writer.writerows(rows)

# print(len(csv_data_lines))

# print(csv_data_lines[:5])
# print(csv_data_lines[-1])

# extract full names and emails of the first five
full_names = ["milestone_projects/pdfs_spreadsheet/example.csv"]
emails = []

csv_data_lines = read_csv_file("milestone_projects/pdfs_spreadsheet/example.csv")
for line in csv_data_lines[1:5]:
    print(line)
    full_name = line[1] + ' ' + line[2]
    print(full_name)
    full_names.append(full_name)
    emails.append(extract_eamil_from_string(email_pattern, str(line)))

print(full_names)
print(emails)

create_csv_file("milestone_projects/pdfs_spreadsheet/new_example.csv", [[1, 2, 3], [3, 4, 5]])
