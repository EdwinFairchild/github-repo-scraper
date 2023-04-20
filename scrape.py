import requests
from bs4 import BeautifulSoup

# Repository URL
repo_main_url = "https://github.com/Analog-Devices-MSDK/msdk"
# Repository URL for Pull Requests
repo_pr_url = "https://github.com/Analog-Devices-MSDK/msdk/pulls"


response = requests.get(repo_main_url)
soup = BeautifulSoup(response.text, 'html.parser')
try:
    num_commits = soup.find_all('span', class_="d-none d-sm-inline")[1].find('strong').text
except IndexError:
    num_commits = 0 # if there are no commits, the span is not present  
#print(f"msdk repo contains {num_commits} commits") 

last_commit_user = soup.find("a", class_="commit-author user-mention").text
#print(last_commit_user)

commit_message = soup.find("a",class_="Link--primary markdown-title")['title'].replace("\n"," ")
#print(commit_message)

commit_time = soup.find("relative-time",class_="no-wrap")['datetime'][:-1]

commit_date = soup.find("relative-time",class_="no-wrap").text

#print(f"{commit_date} {commit_time}")

issues_count = soup.find("span", id="issues-repo-tab-count").text
#print(f"Issues Count: {issues_count}")

pr_count = soup.find("span", id="pull-requests-repo-tab-count").text
#print(f"Pull Requests: {pr_count}")

fork_count = soup.find("span", id="repo-network-counter").text
#print(f"Fork Count: {fork_count}")

star_count = soup.find("span", id="repo-stars-counter-star").text
#print(f"Star Count: {star_count}")


# PUTTING IT ALL TOGETHER

#DICTIONARY
repo_info = {
    "last_user":last_commit_user,
    "date": commit_date,
    "time": commit_time,
    "message": commit_message,
    "commits": num_commits,
    "issues": issues_count,
    "pull_requests": pr_count,
    "forks": fork_count,
    "stars": star_count,
    
}

# PRINTING OUT EACH KEY AND VALUE FROM DICTIONARY
for key, value in repo_info.items():
    print(f"{key:<20}{value}")

print("--------------------------------")

# find all elements with the specified class
response = requests.get(repo_pr_url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
opened_by_elements = soup.find_all('span', {'class': 'opened-by'})
title_tags = soup.find_all('a', class_='Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title')
commit_build_statuses = soup.find_all('div', {'class': 'commit-build-statuses'})

for element, title_tag, commit_build_status in zip(opened_by_elements, title_tags, commit_build_statuses):
    author = element.select_one('a.Link--muted').text
    time = element.find('relative-time').get('datetime')
    title_text = title_tag.text
    check_status = 'OK' if commit_build_status.find('svg', {'class': 'octicon-check'}) else 'X'
    label_tag = title_tag.find_next_sibling('span', {'class': 'lh-default d-block d-md-inline'})
    label_text = ', '.join([label.text.strip() for label in label_tag.find_all('a', {'id': lambda x: x and x.startswith('label-')})]) if label_tag else 'N/A'
    print(f'Title: {title_text}')
    print(f'Author: {author}')
    print(f'Time: {time}')
    print(f'Check Status: {check_status}')
    print(f'Label: {label_text}')
    print('--------------------------------')