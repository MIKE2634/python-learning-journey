import smtplib

sender = "mikaelmika263@gmail.com"
receiver = "mikiiiomosh@gmail.com"


message = """Subject: Python Test

Hello,

This email was sent from Python.
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender)

server.sendmail(sender, receiver, message)

server.quit()

print("Email sent")