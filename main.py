import yagmail
import pandas
from news import NewsFeed
import datetime
import time


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today)
    email = yagmail.SMTP(user="aartisrinivasan83@gmail.com", password="saatvik2012")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}, this is an automated email sending app I created. I'm sending you "
                        f"news about {row['interest']}. Hope you'd find it interesting!\n\n{news_feed.get()}\nAarti", )


while True:
    if datetime.datetime.now().hour == 17 and datetime.now().mean == 43:

        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)