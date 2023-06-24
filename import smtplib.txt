import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import csv

email_list = []

# opening the CSV file
with open("C:\\Users\\jaysh\\Downloads\\First -150.csv", mode ='r',encoding="utf-8-sig")as file:

# reading the CSV file
    csvFile = csv.reader(file)

# displaying the contents of the CSV file
    for lines in csvFile:
	    email_list.append(lines[0])

for i in email_list:

    email = 'sachin.dmvit@gmail.com'
    password = 'ijmacohuctzhgvly'
    send_to_email = email_list
    subject = "Collaboration with Dream Merchants, VIT for Stockastic'23"
    message = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <p style="font-size: 17px; font-family: Arial, Helvetica, sans-serif;">Greetings from Dream Merchants, VIT,</p>
    <p style="font-size: 17px; font-family: Arial, Helvetica, sans-serif;">This is to inform you that we would like to
        collaborate with your company as a sponsor for our flagship event <b>Stockastic'23</b>.</p>
    <p style="font-size: 17px; font-family: Arial, Helvetica, sans-serif;">Our most anticipated event, Stockastic, is a
        virtual simulation that will give the participants a real-life trading experience in a stock market, giving them
        a sense of thrill and adrenaline rush and thereby giving them a gist of the stock market.</p>
    <p style="font-size: 17px; font-family: Arial, Helvetica, sans-serif;">For this event alone, we are expecting more
        than 1,000 participants. <b>Dream Merchants is the only business management club at VIT Vellore</b>. We feel that by
        collaborating with you, we both stand to gain a lot.</p>
    <p style="font-size: 17px; font-family: Arial, Helvetica, sans-serif;">Our audience base is fairly massive, with
        approximately 40,000+ students currently pursuing their education in VIT. VIT has a strong international
        presence across the world and partnerships with over 300 foreign universities. Our patrons are definitely a
        section that can be targeted by your company to expand your reach.</p>
    <p style="font-size: 17px; font-family: Arial, Helvetica, sans-serif;">Do let us know whether you would like to
        collaborate and if there is anything else you would like to discuss in regards to the collaboration, please
        contact :</p>
    <span style="font-size: 17px; font-family: Arial, Helvetica, sans-serif;">Ishita Mehra (Chairperson) : +91
        9027625359</span>
    <br>
    <span style="font-size: 17px; font-family: Arial, Helvetica, sans-serif;">Jay Shah (Secretary) : +91
        9969138221</span>
    <p style="font-size: 17px; font-family: Arial, Helvetica, sans-serif;">Please refer to the brochure attached below
        for your ready reference.</p>
    <p style="font-size: 17px; font-family: Arial, Helvetica, sans-serif;">Thanks and Regards,</p>
    <img src="https://i.ibb.co/KsW5HkB/unnamed.png" style="height:55px; width: 150px;">
    <p style="font-size: 17px; font-family: Arial, Helvetica, sans-serif;">Connect with us on :</p>
    <a href="https://www.instagram.com/dreammerchantsvit/"><img
            src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
            style="height: 25px; width: 25px; margin-left: 4px;" /></a>
    <a href="https://www.linkedin.com/company/dream-merchants-vit/mycompany/"><img
            src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
            style="height: 25px; width: 25px; margin-left: 4px;" /></a>
    <a href="https://www.facebook.com/DreamMerchantsVIT"><img
            src="https://upload.wikimedia.org/wikipedia/commons/0/05/Facebook_Logo_%282019%29.png"
            style="height: 25px; width: 25px; margin-left: 4px;" /></a>
    <a href="https://twitter.com/DM_VIT"><img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_of_Twitter.svg/640px-Logo_of_Twitter.svg.png"
            style="height: 25px; width: 25px; margin-left: 4px;" /></a>
</body>

</html>'''

    file_location = "C:\\Users\\jaysh\\Downloads\\Stockastic Brochure.pdf"

    msg = MIMEMultipart()
    msg['From'] = email

    msg['To'] = i
    msg['Subject'] = subject
    msg['Cc'] = "dreammerchantsfinance@gmail.com"
    rcpt = [i,"dreammerchantsfinance@gmail.com"]

    msg.attach(MIMEText(message, 'html'))

    # Setup the attachment
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # Attach the attachment to the MIMEMultipart object
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, rcpt, text)
    print('sent to '+i)
    server.quit()