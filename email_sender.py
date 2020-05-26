import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Paweł Pikus'
email['to'] = 'dev.********@gmail.com'
email['subject'] = 'You won 10000 rubles!'

email.set_content(html.substitute({'name': 'Paweł'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dev.*********@gmail.com', '*************')
    smtp.send_message(email)
    print('Done!')
