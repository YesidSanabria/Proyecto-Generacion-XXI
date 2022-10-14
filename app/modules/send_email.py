import smtplib
from email.message import EmailMessage

message = EmailMessage()

email_subject = "Email test from Python" 
sender_email_address = "sspg.xxi@gmail.com" 
receiver_email_address = "receiver_email@address.com" 

# Configure email headers 
message['Subject'] = email_subject 
message['From'] = sender_email_address 
message['To'] = receiver_email_address