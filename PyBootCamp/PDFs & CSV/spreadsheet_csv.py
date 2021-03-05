# CSV - Comma Separated Values

import csv

# Wrong Way to open file - Common Error - UnicodeDecodeError
# data = open('example.csv')
# Mention encoding to identify special characters in file like below -
data = open('example.csv', encoding='utf-8')
data_csv = csv.reader(data)
data_lines = list(data_csv)     # convert data in list[list[]] form

# print(data_lines[0])    # column header

# lets print 1st 5 data
for line in data_lines[:6]:
    print(line)
'''
['id', 'first_name', 'last_name', 'myemail', 'gender', 'ip_address', 'city']
['1', 'Joseph', 'Zaniolini', 'jzaniolini0@simplemachines.org', 'Male', '163.168.68.132', 
'Pedro Leopoldo']
['2', 'Freida', 'Drillingcourt', 'fdrillingcourt1@umich.edu', 'Female', '97.212.102.79', 'Buri']
['3', 'Nanni', 'Herity', 'nherity2@statcounter.com', 'Female', '145.151.178.98', 'Claver']
['4', 'Orazio', 'Frayling', 'ofrayling3@economist.com', 'Male', '25.199.143.143', 'Kungur']
['5', 'Julianne', 'Murrison', 'jmurrison4@cbslocal.com', 'Female', '10.186.243.144', 
'Sainte-Luce-sur-Loire']
'''

# lets get emails from 2nd to 5th line
for line in data_lines[2:6]:
    print(line[3])
'''
fdrillingcourt1@umich.edu
nherity2@statcounter.com
ofrayling3@economist.com
jmurrison4@cbslocal.com
'''

# lets get full name from 3rd to 5th line
for line in data_lines[2:6]:
    print(line[1] + ' ' + line[2])
'''
Freida Drillingcourt
Nanni Herity
Orazio Frayling
Julianne Murrison
'''

# writing data to CSV file
out_to_csv = open('my.csv', mode='w', newline='')   # note mode is write
csv_writer = csv.writer(out_to_csv, delimiter=',')  # csv reader and writer are sister
# as its CSV delimeter is ',' also it can be '\t' (tab) or ';' (semi colon)

print(csv_writer.writerow(['a', 'b', 'c']))    # 7 # return no. characters written
# 7 = 3 (abc) + 2 (,) + 2 CRLF ('\r\n') Carriage Return & Line Feed
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])       # return's nothing
out_to_csv.close()      # remember to close the file once finished writing

# appending data to CSV
out_to_csv = open('my.csv', mode='a', newline='')   # note mode is append
csv_writer = csv.writer(out_to_csv, delimiter=',')

csv_writer.writerow(['10', '11', '12'])
csv_writer.writerows([['13', '14', '15'], ['16', '17', '18']])
out_to_csv.close()
