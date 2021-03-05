import smtplib

print('Login - ')
sender_mail = input('Email : ')
password = input('Password : ')

n = input('\nEnter no. of "To"s in your mail : ')
To = []
for i in range(int(n)):
    To.append(input(f'"To"({i+1}) : '))

n = input('\nEnter no. of "CC"s in your mail : ')
CC = []
for i in range(int(n)):
    CC.append(input(f'"CC"({i+1}) : '))

n = input('\nEnter no. of "BCC"s in your mail : ')
BCC = []
for i in range(int(n)):
    BCC.append(input(f'"BCC"({i+1}) : '))

subject = input('\nSubject : ')
body = input('Body : ')

mail = f"From: {sender_mail}\nTo: {','.join(To)}\nCC: {','.join(CC)}\nSubject: {subject}\n\n{body}"

To = To + CC + BCC

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_obj.ehlo())
print(smtp_obj.starttls())
print(smtp_obj.login(sender_mail, password))
print(smtp_obj.sendmail(sender_mail, To, mail))
print(smtp_obj.quit())
