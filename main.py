import requests
from bs4 import BeautifulSoup
import csv

# Webページを取得して解析する
url = 'https://www.python.org/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Upcoming Eventsの情報を取得する
event_widget = soup.find('div', class_='medium-widget event-widget last')
event_list = event_widget.find_all('li')

# CSVファイルに書き込む
with open('events.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'event_name', 'date'])

    for event in event_list:
        date = event.find('time').text.strip()
        name = event.find('a').text.strip()
        writer.writerow(['Upcoming Events', name, date])
