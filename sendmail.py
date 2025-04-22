import smtplib
from email.mime.text import MIMEText

def send_mail(subject, message, recipient):
    sender = "dancing.data.mail@gmail.com"
    from_password = ""

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ",".join(recipient)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, from_password)
        server.send_message(msg)
        server.quit() 
