import PyPDF2
import re

file = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(file)

for num in range(pdf_reader.numPages):
    match = re.search(r'\d{3}\D\d{3}\D\d{4}', pdf_reader.getPage(num).extractText())
    if match:
        print(f"Phone number {match.group()} was present on page no. {num + 1} of PDF document\n"
              f"It was located on index starting from {match.start()} to {match.end()} "
              f"of page no. {num + 1} of PDF document")
        # Phone number 505.503.4455 was present on page no. 14 of PDF document
        # It was located on index starting from 1727 to 1739 of page no. 14 of PDF document

''' SOLUTION GIVEN in lecture
pattern = r'\d{3}'
allPDFtext = ''
for num in range(pdf_reader.numPages):
    allPDFtext += ' ' + pdf_reader.getPage(num).extractText()
# findall will not work as it will give only list of matching patterns
print(re.findall(pattern, allPDFtext))  # ['000', '000', '000', '505', '503', '445']
for each_iter in re.finditer(pattern, allPDFtext):
    print(each_iter)
# <re.Match object; span=(655, 658), match='000'>
# <re.Match object; span=(17805, 17808), match='000'>
# <re.Match object; span=(35059, 35062), match='000'>
# <re.Match object; span=(41808, 41811), match='505'>
# <re.Match object; span=(41812, 41815), match='503'>
# <re.Match object; span=(41816, 41819), match='445'>
print(allPDFtext[41808: 41808 + 20])  # 505.503.4455. So hor  # now redefine pattern using this o/p
pattern = r'\d{3}.\d{3}.\d{4}'
print(re.search(pattern, allPDFtext))
# <re.Match object; span=(41808, 41820), match='505.503.4455'>'''

file.close()
