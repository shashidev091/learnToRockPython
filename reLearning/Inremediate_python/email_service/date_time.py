import datetime as dt
import random
import smtplib
from pandas import read_csv

MY_EMAIL = 'shashibhushanbhagat@yahoo.com'
MY_APP_PASSWORD = 'eqiaeujqwxhsdlyd'
SMTP_HOST = 'smtp.mail.yahoo.com'
SMTP_PORT = 587

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

today = (now.month, now.day)

birthdays_data = read_csv('birthdays.csv')

birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in birthdays_data.iterrows()}

# with open('birthdays.csv') as data_file:
#     print(data_file.readlines()[2])
print(birthday_dict)

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_template/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        print(birthday_person["name"])
        final_letter = content.replace("[NAME]", birthday_person["name"])
        print(final_letter)

    with smtplib.SMTP(host="smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_APP_PASSWORD)
        connection.sendmail(
            to_addrs=birthday_person["email"],
            from_addr=MY_EMAIL,
            msg=f"Subject:Happy Birthday!\n\n {final_letter}"
        )

"""
    - You can deploy this app for free in PythonAnywhere so that it runs automatically daily
"""