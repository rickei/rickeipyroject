import smtplib

sendfrom="send@send.com"
recipient="recipient@recipient.com"
password="password"


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sendfrom, password)

msg = "test MESSAGE... by python"
server.sendmail(sendfrom, recipient, msg)
server.quit()
