from email.mime.text import MIMEText
import smtplib

def send_email(email, height, weight,average_height,average_weight,count):
    from_email="jtb.moonie@gmail.com"
    from_password="esoqfifdbsgufvuk"
    to_email=email

    subject="Average Height and Weight data"
    message="Hey there, <br>Your height is <strong>%s cm</strong>.<br> Average height of all is <strong>%s cm</strong> and that is calculated out of <strong>%s</strong> people.<br> Your weight is <strong>%s kg</strong><br> Average weight of all is <strong>%s kg</strong> and that is calculated out of <strong>%s</strong> people.<br> Thanks!" % (height,average_height,count,weight,average_weight,count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
