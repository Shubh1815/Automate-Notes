from bs4 import BeautifulSoup
import requests
import datetime

today = datetime.datetime.now()
limit = today + datetime.timedelta(days=2) 
current_year = today.year

TARGET_SITES = ['codeforces.com', 'codechef.com', 'codingcompetitions.withgoogle.com', 'icpc']

PATH = 'C:\\Users\\12345\\Desktop\\1\\Notes\\notes.txt'

source = requests.get('https://clist.by/').text
clist_by = BeautifulSoup(source, 'lxml')

allContests = clist_by.find('div', id='contests')
contests = allContests.select('div.row.contest.coming')

data = {}

for contest in contests:
	event_data =  contest.find('div', class_='event')

	event_name = event_data.span.text.strip().lower()
	event_site = event_data.find('div', class_='resource').a.small.text.strip()

	contest_timmings = contest.div.find('div', class_='start-time').a.text.strip()
	contest_date = contest_timmings[:2]
	contest_month = contest_timmings[3:5]

	finalized_date  = f'{contest_date} {contest_month} {current_year}'
	finalized_date = datetime.datetime.strptime(finalized_date, '%d %m %Y')


	if finalized_date <= limit:
		for sites in TARGET_SITES:
			if sites in event_site:
				data[event_name] = finalized_date.strftime('%d/%m/%Y')
				break

with open(PATH, 'r') as f:
	for line in f.readlines():
		try:
			date, event = line.split('-')
			event = event.lower().strip('\n')
			dateObj = datetime.datetime.strptime(date, '%d/%m/%Y')
			if dateObj >= today:
				data[event] = date
		except Exception:
			continue
			
with open(PATH, 'w') as f:
	for event in data:
		f.write(f'{data[event]}-{event.capitalize()}\n')


