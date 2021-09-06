from flask import *
from flask_mail import Mail, Message
import csv
import os
from roaming import mail,app

# Send confirmation email
def send_confirmation_email(email, message):
    msg = Message("Thanks for reaching out", sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = message
    mail.send(msg)

#Write to csv
def append_to_csv(filename,headers,detail):
    with open(filename,"a",encoding="utf-8",newline='') as fp:
        writer = csv.DictWriter(fp, headers)
        if is_empty(filename=filename):
            writer.writeheader()
        writer.writerows(detail)

#Check if file is empty or not
def is_empty(filename):
    return os.stat(filename).st_size == 0


