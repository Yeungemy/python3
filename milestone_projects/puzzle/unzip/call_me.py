from zipfile import ZipFile
import os
import re

def upzip_file(zipped_file):
    f = ZipFile(zipped_file, 'r')
    f.extractall()
    f.close()

def read_file(file_path, need_close = True):
    f = open(file_path, 'r')
    content = (f.read())
    print(content)

    if need_close:
        f.close()
    return content

def search_in_directory(dir_path, pattern):
    results = []
    for folder, subfolder, files in os.walk(dir_path):
        for f in files:
            file_path = folder + '//' + f
            result = re.findall(pattern,  folder + '//' + read_file(file_path))
            if result:
                results.append(result)
    return results

folder_path = os.getcwd() + "/milestone_projects/puzzle/unzip/extracted_content"
instruction_file_path = folder_path + "/Instructions.txt"

# phone pattern
phone_pattern = r'\d{3}-\d{3}-\d{4}'
results = []
results.extend(search_in_directory(folder_path, phone_pattern) )          
print(results)
        
