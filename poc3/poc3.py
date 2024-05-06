import requests
from bs4 import BeautifulSoup
import json

def extract_content_from_link(link):
    # Fetch HTML content from the link
    response = requests.get(link)
    html_content = response.content
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract title from the top of the HTML document
    title_tag = soup.find('title')
    title = title_tag.text.strip() if title_tag else ''
    
    # Extract content
    content_tags = soup.find('div', class_='inarticle').find_all('p')
    content = '\n'.join([tag.text.strip() for tag in content_tags if tag.text.strip()])
    
    # Extract date
    date_tag = soup.find('p', class_='dt_sign')
    date = date_tag.text.strip() if date_tag else ''
    
    # Extract author from JSON-LD script
    author = ''
    script_tags = soup.find_all('script', type='application/ld+json')
    for script in script_tags:
        json_data = json.loads(script.string)
        if 'author' in json_data:
            author = json_data['author']['name']
            break
    
    return {
        'title': title,
        'content': content,
        'date': date,
        'author': author
    }

# Example usage
link = 'https://www.ilboursa.com/marches/la-bh-bank-lance-son-centre-de-developpement-des-competences-bh-academy-_24300'
content_data = extract_content_from_link(link)
print(content_data)
