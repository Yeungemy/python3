from zipfile import ZipFile
import shutil

def createFile(file_name, content):
    file = open(file_name, 'w+')
    file.write(content)
    file.close()

def zip_files(zipped_container, zipped_files):
    zip_comp = ZipFile(zipped_container, 'w')
    
    for file_name in zipped_files:
        zip_comp.write(file_name)

    zip_comp.close()

def unzip_files(zipped_container):
    test_zip_file = ZipFile(zipped_container, 'r')
    test_zip_file.extractall()
    test_zip_file.close()


file_one = 'file_one.txt'
file_one_content = "Test file one"

file_two = 'file_two.txt'
file_two_content = "Test file two"

createFile(file_one, file_one_content)
createFile(file_two, file_two_content)

zip_files('zip_comp.zip', [file_one, file_two])
unzip_files('zip_comp.zip')

zip_dir_path = "milestone_projects\\puzzle\\zip_files\\assets"
unzip_dir_path = "milestone_projects\\puzzle\\zip_files\\example.zip"

shutil.make_archive('example', 'zip', zip_dir_path)
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')