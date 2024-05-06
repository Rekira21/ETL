from bs4 import BeautifulSoup
import time
from selenium import webdriver

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Replace with your preferred browser

# Load the webpage
url = "https://www.ilboursa.com/marches/news_valeur?p=3&s=BH"
driver.get(url)

# Wait for JavaScript rendering (5 seconds)
time.sleep(5)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract the articles...
articles = []
for article in soup.find_all( 'div', class_='home_content mt15 lh25' ):
    title = None
    date = None
    text = None

    h2_tags = article.find_all('h2')
    if len(h2_tags) > 0:
        title = h2_tags[0].text.strip()
    else:
        print(f"Skipping article with no <h2> tag: {article.text}")

    time_tags = article.find_all('time')
    if len(time_tags) > 0:
        date = time_tags[0].text.strip()
    else:
        print(f"Skipping article with no <time> tag: {article.text}")

    p_tags = article.find_all('p')
    if len(p_tags) > 0:
        text = p_tags[0].text.strip()
    else:
        print(f"Skipping article with no <p>^[[A tag: {article.text}")

    articles.append({ 'title': title, 'date': date, 'text': text })


# Load the transformed data into a CSV file
with open('ilboursa_news.csv', 'w', newline='') as csvfile:
    fieldnames = [  'title',  'date',  'text' ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for article in articles:
        writer.writerow({  'title': article.get(  'title'),  'date': article.get('date'),  'text': article.get('text') })