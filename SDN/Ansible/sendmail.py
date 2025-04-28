import smtplib
from email.mime.text import MIMEText

def send_mail(subject, message, to_email):
    from_mail = "dancing.data.mail@gmail.com"
    from_password = ""

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['From'] = from_mail
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_mail, from_password)
        server.send_message(msg)
        server.quit() 
