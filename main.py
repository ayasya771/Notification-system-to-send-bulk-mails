import smtplib
from email.mime.text import MIMEText
import datetime
import schedule
import time

# Create a list to store the email addresses of recipients
recipients = []

# Create a dictionary to store the messages and their priorities
messages = {}

# Create a function to send an email
def send_email(to, message, priority):
    msg = MIMEText(message)
    msg['Subject'] = "Notification - Priority: " + str(priority)
    msg['From'] = "notifications@example.com"
    msg['To'] = to

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.example.com')
    server.starttls()
    server.login("notifications@example.com", "password")

    # Send the email
    server.sendmail("notifications@example.com", to, msg.as_string())
    server.quit()

# Create a function to schedule and send emails
def send_emails():
    for to in recipients:
        for message in messages:
            send_email(to, message['text'], message['priority'])

# Schedule the email sending function to run every day at 9 AM
schedule.every().day.at("09:00").do(send_emails)

while True:
    schedule.run_pending()
    time.sleep(1)
