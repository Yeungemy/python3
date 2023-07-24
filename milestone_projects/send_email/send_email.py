import smtplib
from getpass import getpass

'''
Enable 2-steps verifications
Generate App passwords: app: mail, custom device: python script
'''

smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
smtp_object.ehlo()
smtp_object.starttls()
# email = "emyyeung086@gmail.com"
# pwd = "hkjjvixypyocivis"
email = getpass("Enter email: ")
pwd = getpass("Enter your passward: ")
smtp_object.login(email, pwd)
from_address = "emyyeung086@gmail.com"
to_address = "emyzheng80@gmail.com"
message = "This a test from python"
subject = "another python test"
msg = f"subject: {subject} + '\n' + message"
smtp_object.sendmail(from_address, to_address, msg)

