import re

'''
Character Identifier

Character	Description         Pattern Code	Example Match
\d	        A digit	            file_\d\d	    file_25
\w	        Alphanumeric	    \w-\w\w\w	    A-b_1
\s	        White space	        a\sb\sc	        a b c
\D	        A non digit	        \D\D\D	        ABC
\W	        Non-alphanumeric	\W\W\W\W\W	    *-+=)
\S	        Non-whitespace	    \S\S\S\S	    Yoyo
'''

text = "I have mobile. My 1st mobile number is 123-456-7898. My 2nd mobile number is 321-654-8987"
# phones = re.finditer(r'\d{3}-\d{3}-\d{4}', text)
phones = re.finditer(r'\d\d\d-\d\d\d-\d\d\d\d', text)
for i in phones:
    print(f"{i} '{i.group()}' -> {i.span()} from index {i.start()} to {i.end()}")

'''
Quantifier

Character	Description	                Pattern Code	Example Match
+	        Occurs one or more times	Version \w-\w+	Version A-b1_1
{3}	        Occurs exactly 3 times	    \D{3}	        abc
{2,4}	    Occurs 2 to 4 times	        \d{2,4}	        123
{3,}	    Occurs 3 or more	        \w{3,}	        anycharacters
\*	        Occurs zero or more times	A\*B\*C*	    AAACC
?	        Once or none	            plurals?	    plural
'''

