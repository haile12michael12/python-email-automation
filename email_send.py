import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

to=input("please enter the email of receiver:-")
message=input("write your massega:-")
def send_email():
        # set up the smtp server
        server = smtplib.SMTP(smt.gmail.com, 587)
        server.starttls() # secure the connection
        server.login('senderemail', 'password')
        server.sendmail('senderemail',to,message)
        server.close()

        sendEmail(to,message)

        

        