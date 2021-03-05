import zipfile
import os
import re

unzip = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
unzip.extractall('puzzle unzipped')
unzip.close()

instructions = open(os.getcwd() + "\\puzzle unzipped\\extracted_content\\Instructions.txt", 'r')
print(f"\n{instructions.read()}")
instructions.close()

for root, folders, files in os.walk(os.getcwd() + "\\puzzle unzipped\\extracted_content"):
    # print(f"------------------------\nCurrently looking in '{root}' directory - ")

    # print(f"\nThe folders are - ")
    # for i_folder in folders:
    #    print(f"\t{i_folder}")

    # print(f"\nThe files are - ")
    for i_file in files:
        # print(f"\t{i_file}")
        myfile = open(root + "\\" + i_file, 'r')
        contents = myfile.read()
        myfile.close()
        match = re.search(r'\d{3}-\d{3}-\d{4}', contents)
        if match:
            print(f"\nTelephone number - {match.group()} found in '{i_file}' file which is in "
                  f"\n'{root}' directory")
            print(f"At index starting from {match.start()} to {match.end()}")

    # print("\n")

# OUTPUT -

'''
Good work on unzipping the file!
You should now see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-#### 
Use the Python os module and regular expressions to iterate through each file, open it, and search 
for a telephone number. Good luck!

Telephone number - 719-266-2837 found in 'EMTGPSXQEJX.txt' file which is in 
'C:\\Users\\A711929\\OneDrive - Atos\\Documents\\Study MAterial\\Python\\PyCharm Projects
\\PyBootCamp\\Advance Modules Puzzle\\puzzle unzipped\\extracted_content\\Four' directory
At index starting from 1062 to 1074
'''
