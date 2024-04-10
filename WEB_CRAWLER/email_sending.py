import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#object for MIMEMultipart
msg=MIMEMultipart() 

#path define
photo=("Enter your path here")     
  
#open and read file 
jpg=MIMEApplication(open(photo1,'rb').read())    #here rb stands for read in binary(maybe...)
jpg.add_header('content-disposition','attachment',filename=photo)
msg.attach(jpg)

#connect to server
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()    #puts the connection into TLS mode

#login server email
password = input("enter password")
server.login('pahuldeep100@gmail.com','%s'%password) 

#enter client email
text = msg.as_string()
addr_to=input('enter the gmail address :')

#sending mail
server.sendmail('pahuldeep100@gmail.com', addr_to, text)  
server.quit()

print("email send successfully")
