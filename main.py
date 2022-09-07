import datetime as dt
import pandas
import random
import smtplib

my_mail = "newmail002244@gmail.com"
my_pass = "vncdnqzamtgsrfdz"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=my_pass)
        connection.sendmail(from_addr=my_mail, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday!\n\n{contents}")
