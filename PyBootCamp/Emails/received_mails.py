import imaplib
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')

myemail = input("Email : ")
password = input("Password : ")
print(M.login(myemail, password))  # ('OK', [b'your@mail.com authenticated (Success)'])

print(M.list())  # Directory structure of your mail
print(M.select('inbox'))  # ('OK', [b'18283'])

typ, data = M.search(None, 'SUBJECT "PERFECT MAIL"')
print(typ)  # OK
print(data)  # [b'18280']    # if no number is returned means there was no such data and if there
# are multiple no. means there are multiple matches for your search. Also this unique number is ID
# of that mail in search result

email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')
# The Internet RFC 822 specification defines an electronic message format consisting of header
# fields and an optional message body. The header fields contain information about the message,
# such as the sender, the recipient, and the subject. If a message body is included, it is separated
# from the header fields by an empty line (\r\n).

print(email_data)
'''[(b'18281 (RFC822 {639}', 
  b'Bcc: bcc@mail.com\r\n
    Return-Path: <sender@mail.com>\r\n
	Received: from DESKTOP-NAME.www.ROUTER.com ([103.134.165.10])\r\n
	by smtp.gmail.com with ESMTPSA id z12sm14389023pjz.16.2021.02.28.07.32.59\r\n
	(version=TLS1_3 cipher=TLS_AES_256_GCM_SHA384 bits=256/256);\r\n        
	Sun, 28 Feb 2021 07:33:01 -0800 (PST)\r\n
	Message-ID: <603bb7ad.1c69fb81.543c8.0e1b@mx.google.com>\r\n
	Date: Sun, 28 Feb 2021 07:33:01 -0800 (PST)\r\n
	From: sender@mail.com\r\n
	To: to1@mail.com,to2@mail.com.com\r\n
	CC: cc1@mail.com,cc2@mail.com.com\r\n
	Subject: PERFECT MAIL\r\n
	\r\n
	This is perfect mailwith to cc and bcc. Thanks!\r\n'), 
  b')']'''

raw_email_header = email_data[0][1]  # grabbing message header
raw_email_header_str = raw_email_header.decode('utf-8')

print(raw_email_header_str)
email_message = email.message_from_string(raw_email_header_str)
print(email_message)
'''
Bcc: bcc@mail.com\r\n
Return-Path: <sender@mail.com>\r\n
Received: from DESKTOP-NAME.www.ROUTER.com ([103.134.165.10])\r\n
		by smtp.gmail.com with ESMTPSA id z12sm14389023pjz.16.2021.02.28.07.32.59\r\n
		(version=TLS1_3 cipher=TLS_AES_256_GCM_SHA384 bits=256/256);\r\n        
		Sun, 28 Feb 2021 07:33:01 -0800 (PST)\r\n
Message-ID: <603bb7ad.1c69fb81.543c8.0e1b@mx.google.com>\r\n
Date: Sun, 28 Feb 2021 07:33:01 -0800 (PST)\r\n
From: sender@mail.com\r\n
To: to1@mail.com,to2@mail.com.com\r\n
CC: cc1@mail.com,cc2@mail.com.com\r\n
Subject: PERFECT MAIL\r\n
\r\n
This is perfect mailwith to cc and bcc. Thanks!\r\n
'''

print(type(email_message))  # <class 'email.message.Message'>

# will print message body
for part in email_message.walk():
    if part.get_content_type() == 'text/plain':     # if link is in mail body then - 'text/html'
        body = part.get_payload(decode=True)
        print(body)
# b'This is perfect mailwith to cc and bcc. Thanks!\r\n'
# b indicates bytes string
