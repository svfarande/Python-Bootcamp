"""Steps to send mail with Attachments from Gmail account:
For adding an attachment, you need to import:

import smtplib
from myemail.mime.multipart import MIMEMultipart
from myemail.mime.text import MIMEText
from myemail.mime.base import MIMEBase
from myemail import encoders

These are some libraries which will make our work simple.
These are the native libraries and you dont need to import any external library for this.
Firstly, create an instance of MIMEMultipart, namely “msg” to begin with.
Mention the sender’s myemail id, receiver’s myemail id and the subject
in the “From”, “To” and “Subject” key of the created instance “msg”.
In a string, write the body of the message you want to send, namely body.
Now, attach the body with the instance msg using attach function.
Open the file you wish to attach in the “rb” mode.
Then create an instance of MIMEBase with two parameters.
First one is ‘_maintype’ amd the other one is ‘_subtype’.
This is the base class for all the MIME-specific sub-classes of Message.
Note that - ‘_maintype’ is the Content-Type major type (e.g. text or image), and
‘_subtype’ is the Content-Type minor type (e.g. plain or gif or other media).
set_payload is used to change the payload the encoded form. Encode it in encode_base64.
And finally attach the file with the MIMEMultipart created instance msg.
After finishing up these steps, create a session, secure it and check the authenticity and then
after sending the mail, terminate the session."""

# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = input("Email : ")
password = input("Password : ")
toaddr = fromaddr

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders myemail address
msg['From'] = fromaddr

# storing the receivers myemail address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = input("Mail Subject : ")

# string to store the body of the mail
body = input("Mail Body : ")

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = input("Enter filename with extension - ")
path = input("Enter path of the file - ")
attachment = open(path + '\\' + filename, "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload(attachment.read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, password)

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()
