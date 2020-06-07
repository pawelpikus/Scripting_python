import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Paweł Pikus'
email['to'] = 'dev.tester1982@gmail.com'
email['subject'] = 'You won 10000 rubles!'

email.set_content(html.substitute({'name': 'Paweł'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    login = 'xxx'
    passwd = 'xxx'
    smtp.ehlo()
    smtp.starttls()
    smtp.login(login, passwd)
    smtp.send_message(email)
    print('Done!')
