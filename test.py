import smtplib  # Импортируем библиотеку по работе с SMTP

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML

def do(name):
	msg = MIMEMultipart()
		 
	from_email='12_vt@mail.ru'
	to_email = 'kun_nursagitov@mail.ru'
	message = name
	password = '12345qwert'
	msg.attach(MIMEText(message, 'plain'))
		 
	server = smtplib.SMTP('smtp.mail.ru: 25')
	server.starttls()
	server.login(from_email, password)
	server.sendmail(from_email, to_email, msg.as_string())
	server.quit()
		
