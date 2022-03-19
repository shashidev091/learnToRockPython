import datetime as dt
import random
import smtplib

MY_EMAIL = 'shashibhushanbhagat@yahoo.com'
MY_APP_PASSWORD = 'eqiaeujqwxhsdlyd'

now = dt.datetime.now()
print(now.year)
year = now.year

if year == 2022:
    print("Still wear mask")

if now.weekday() == 5:
    with open('quotes.txt', 'r') as data_file:
        data = data_file.readlines()
        print(data)

        with smtplib.SMTP(host="smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_APP_PASSWORD)
            connection.sendmail(to_addrs="skujur873@gmail.com", from_addr=MY_EMAIL,
                                msg=f"Subject:Monday Motivation\n\n {random.choice(data)}")

print(now.weekday())
print(now.day)
