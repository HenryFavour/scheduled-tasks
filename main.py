import pandas
from datetime import datetime
import random
import smtplib

my_email = "favourhenrytest@gmail.com"
password = "qprzajbrsxwsuvxh"

data = pandas.read_csv("birthdays.csv")
dt = datetime.now()
today = (dt.month, dt.day)

birthday_dict = {
    (row.month, row.day): row for index,row in data.iterrows()
}

if today in birthday_dict:

    celebrant = birthday_dict[today]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as birthday_letter:
        letter = birthday_letter.read()
        letter = letter.replace("[NAME]", celebrant["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(from_addr= my_email, to_addrs= celebrant["email"], msg=f"Subject:Happy Birthday\n\n{letter}")
