import csv

data = open('find_the_link.csv', encoding='utf-8')
data_reader = csv.reader(data)
data_lists = list(data_reader)

link = ""

'''i = 0
for line in data_lists[:]:
    link += line[i]
    i += 1'''

# enumerate adds index to each field in iterable
# >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# >>> list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# >>> list(enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
for i, line in enumerate(data_lists):
    link += line[i]

print(link)

data.close()
