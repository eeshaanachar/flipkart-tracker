import smtplib
import sqlite3
import requests
from bs4 import BeautifulSoup
from secrets import Credentials


def send_mail(mail_id, prod_url, cur_price):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as session:
        session.login(Credentials.email_id, Credentials.password)
        message = f'Subject: Price Drop\n\n{prod_url} is now selling for {cur_price}'
        session.sendmail(Credentials.email_id, mail_id, message)

connection = sqlite3.connect('database.sqlite')
cursor = connection.cursor()

cursor.execute('delete from Entry where date < datetime("now", "-90 day")')
connection.commit()

for id_, url, wanted_price, mail_id, _ in cursor.execute('select * from Entry').fetchall():
    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        cur_price = int(soup.find(class_="_1vC4OE _3qQ9m1").text.replace(',','')[1:])
        if cur_price <= wanted_price:
            send_mail(mail_id, url, cur_price)
            cursor.execute('delete from Entry where id_=?', (id_,))
            connection.commit()
    except:
        continue
