import smtplib

email = input("Email : ")
password = input("Password : ")
from_email = email
to_email = email
subject = input("Mail Subject : ")
message = input("Mail Body : ")
mail = "Subject: " + subject + '\n' + message

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print(server.login(email, password))
print(server.sendmail(from_email, to_email, mail))
print(server.quit())
