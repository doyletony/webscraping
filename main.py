import requests
from bs4 import BeautifulSoup

# This is the part to comment when code is concluded
# html_texts = open('home.html')



print("What job do you want to search for?")
search_job = input('> ')
address = 'https://www.timesjobs.com/candidate/job-search.html?searchType=p' \
          f'ersonalizedSearch&from=submit&txtKeywords={search_job}&txtLocation='

print("Loading page")
print(address)

html_texts = requests.get(address).text

soup = BeautifulSoup(html_texts, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text.strip()

    published_date = job.find('span', class_='sim-posted').text.strip()
    # skips job post if it is outdated
    if 'few days ago' in published_date:
        continue

    skills = job.find('span', class_='srp-skills').text.strip()
    skills_list = skills.split(",")
    skills = ', '.join(skill.strip() for skill in skills_list)

    link = job.header.h2.a['href']

    print('\n')
    print(f"Company Name: {company_name}")
    print(f"Skills Required: {skills}")
    print(f"Published Date: {published_date}")
    print(f"Link: {link}")

# TODO: Add a code that asks user to select a job and then prints the description
