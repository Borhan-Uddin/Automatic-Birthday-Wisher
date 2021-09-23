
import pandas as pd
import datetime
import smtplib
import os

os.chdir(r"D:\Javascript code\Python-api")

data = pd.read_excel("data.xlsx")
day_now = datetime.datetime.now().strftime("%d-%m")
year_now = datetime.datetime.now().strftime("%Y")
time_now = datetime.datetime.now().strftime("%H:%M:%S")

print(time_now)

MAIL_ID = "" #your email address
PSWD = "" # email's password

def send_wish(to,sub,msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(MAIL_ID, PSWD)
    s.sendmail(MAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()



for index, item in data.iterrows():

    bday = item["Birthday"].strftime("%d-%m")
    if bday == day_now : #and time_now == wish_time
        send_wish(item["Email"],"Birthday wish",item["Message"])
    