import smtplib

my_email = 'shashibhushanbhagat@yahoo.com'
my_password = "eqiaeujqwxhsdlyd"
with smtplib.SMTP(host="smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="skujur873@gmail.com", msg=f"Subject:Hello\n\nHello Shashi \nThis is an test.")
    connection.close()

