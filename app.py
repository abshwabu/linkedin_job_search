import requests
from bs4 import BeautifulSoup

# Define the LinkedIn job search URL (example for Laravel jobs)
url = "https://www.linkedin.com/jobs/search?keywords=Laravel&location=Worldwide"

# Send a GET request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Example: Extract job titles and links
    jobs = soup.find_all('a', {'class': 'result-card__full-card-link'})
    for job in jobs:
        title = job.text.strip()
        link = job['href']
        print(f"Job Title: {title}\nLink: {link}\n")
        print('success')
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
