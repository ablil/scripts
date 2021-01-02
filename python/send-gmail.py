#!/usr/bin/python
# Author: ablil
# Description: Send Gmail with attachements
# Gmail email and password are read from the following env variable
# $EMAIL and $PASSWORD

import sys
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class GmailSender:

    def __init__(self, email, password):
        self.email = email
        self.password = password

        self.conn = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.conn.ehlo()
        self.conn.login(self.email, self.password)


    def send(self, receiver, subject, body='', attachments=[]):
        # setup msg
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # attach files
        for f in attachments:
            with open(f, 'rb') as fil:
                buff = fil.read()
                name = os.path.basename(f)
                part = MIMEApplication(buff, name)
            part['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(f))
            msg.attach(part)

        # send
        print(f"Sending email to {receiver} with {len(attachments)} attachments")
        self.conn.sendmail(self.email, receiver, msg.as_string())
        self.conn.quit()
        print("Email sent successfully")

def check_files(files):
    for filename in files:
        if not os.path.exists(filename):
            print(f"File {filename} NOT found or you do NOT have permission")
            exit(2)

def main():

    if len(sys.argv[1:]) < 2:
        print(f"Usage: py {sys.argv[0]} receiver@addr subject file1 ...")
        exit(1)

    receiver = sys.argv[1]
    subject = sys.argv[2]
    files = sys.argv[3:]; check_files(files)

    body = input('Type email body: ')

    sender = GmailSender(os.environ['EMAIL'], os.environ['PASSWORD'])
    sender.send(receiver, subject, body, files)

if __name__=='__main__':
    main()
