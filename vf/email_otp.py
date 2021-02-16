import smtplib , random 

otp = random.randrange(900,10000)


sender_email = 'naiyf00234@gmail.com'
rec_email = input('enter your email : ')
password = 'naiyf123'
message = 'this is your otp number '+str(otp)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print('login :)')

server.sendmail(sender_email, rec_email , message)
print('email send to ', rec_email)


user = ''

while user != otp:
	print('enter otp :  ')
	user = int(input())
	
print('otp is correct')
