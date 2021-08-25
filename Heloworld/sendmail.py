import smtplib
from email.mime.text import MIMEText

#def send_mail(DonorName,Bloodgroup,MobileContact,City,Diabetic,Comments):
def send_mail(DonorName,Bloodgroup,MobileContact,City,Comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'e8167cd99e4af9'
    password = '07ef76797bd787'
    message = f"<h3>New Feedback Submission</h3><ul><li>DonorName: {DonorName}</li><li>Bloodgroup: {Bloodgroup}</li><li>MobileContact: {MobileContact}</li><li>City: {City}</li><li>Comments: {Comments}</li></ul>"
    sender_email = 'smtp.mailtrap@mailtrap.io'
    receiver_email = 'smtp.mailtrap@mailtrap.io'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Notificaton on Blood Donation  project blooddonation '
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
#send_mail('customer','dealer','ratings','comments')
print("Mail Sent ")