import zipfile  # compress single files
import shutil  # compress folder

f1 = open('file1.txt', 'w+')
f1.write('1st file')
f1.close()

f2 = open('file2.txt', 'w+')
f2.write('2nd file')
f2.close()

compress_file = zipfile.ZipFile('myfile.zip', 'w')
compress_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
compress_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
compress_file.close()

uncompress_file = zipfile.ZipFile('myfile.zip', 'r')
uncompress_file.extractall('extracted')

# But if you want to archive whole directory instead then check below

dir_to_archive = "C:\\Users\\svfarande\\onedrive\\Documents\\Study MAterial" \
                 "\\Python\\PyCharm Projects\\PyBootCamp\\Zip File\\extracted"
output_filename = 'Archived'
shutil.make_archive(output_filename, 'tar', dir_to_archive)
shutil.unpack_archive('Archived.tar', 'UnArchived', 'tar')
