import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
# if port no. 587 doesn't work you can try 465, if that also doesn't work don't pass any port no.
# if you are using port 587 which means you are using TLS (Transport Layer Security) encryption
# if you are using port 465 which means you are using SSL (Secure Sockets Layer) encryption

# now lets greet server & establish connection using ehlo() which will tell if connection is
# successful or not. This method call needs to be done directly after creating smtplib object,
# calling it after some methods can lead to error
print(smtp_obj.ehlo())  # (250, b'smtp.gmail.com at your service, [103.134.165.10]
#  \nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
# a successful connection is indicated by o/p starting with 250 like above

print(smtp_obj.starttls())   # (220, b'2.0.0 Ready to start TLS')
# if using 465 skip this as you will be using SSL

# Use gmail App Passwords for security - https://support.google.com/accounts/answer/185833?hl=en/
# Click on 2-Step Verification link - https://support.google.com/accounts/answer/185839
# Then follow "Turn on 2-Step Verification" steps and get it turned on get back to 185833 (1st link)
# and then "Create & use App Passwords"

email = input("Email : ")
password = input("Password : ")
print(smtp_obj.login(email, password))  # (235, b'2.7.0 Accepted')

from_email = email
to_email = email
subject = input("Mail Subject : ")
message = input("Mail Body : ")
mail = 'Subject: ' + subject + '\n' + message

print(smtp_obj.sendmail(from_email, to_email, mail))    # {}
# empty {} dictionary indicates its successful

print(smtp_obj.quit())  # (221, b'2.0.0 closing connection ml17sm15836132pjb.18 - gsmtp')
