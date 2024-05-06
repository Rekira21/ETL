from bs4 import BeautifulSoup
import re

html_content = '''
<div class="inarticle txtbig">
    <p style="text-align: center;"><img src="../handlers/image_news_get.ashx?id=9257C72C-59A0-4A1A-BF55-6989498E435B" alt="" width="600" height="284"></p>
    <p>La 5<sup>ème</sup> édition de la Conférence internationale "&nbsp;Financing Investment &amp; Trade in Africa&nbsp;– FITA a eu lieu le 25 et 26 mai 2022 à l'hôtel Laïco Tunis et ce, sous le haut patronage de la Présidence de la République Tunisienne et avec la présence de Madame la cheffe du Gouvernement&nbsp; qui a donné le coup d'envoi de cet &nbsp;évènement.</p>
    <p>Ce rendez-vous annuel incontournable des acteurs impliqués dans les relations économiques et commerciales Tuniso-Africaines&nbsp;à savoir&nbsp;: &nbsp;Ministres, Ambassadeurs, CEOs, Bailleurs de Fonds Internationaux et autres intervenants des quatre coins du Monde a été marqué par la présence de presque 3000 participants pour discuter des grands enjeux post COVID-19.</p>
    <p style="text-align: center;"><img src="../handlers/image_news_get.ashx?id=6275B35E-AC75-4E04-BB14-2291006C2D13" alt="" width="565" height="352"></p>
    <p>Compte tenu de son positionnement à l'égard du marché africain, la BH BANK a été fortement représentée à cette manifestation notamment par son Directeur Général M Hichem REBAI, les Directeurs Généraux des Filiales&nbsp;et le staff managérial et commercial.</p>
    <p>Cette conférence internationale a été une occasion pour le Groupe BH pour participer à des rencontres B to B et ce, dans un objectif de développer les opportunités de coopération et d'investissement et proposer des solutions &nbsp;nouvelles et créatives pour renforcer les relations&nbsp; de partenariat&nbsp; et saisir toutes les occasions pour relancer les affaires qui ont été impactées par la pandémie.</p>
    <p><strong>Communiqué</strong></p>
    <p class="dt_sign">Publié le 26/05/22 08:49</p>
</div>
'''

soup = BeautifulSoup(html_content, 'html.parser')

# Extracting title
title = soup.find('div', class_='inarticle').find('strong').text.strip()

# Extracting content
content = ' '.join([p.text.strip() for p in soup.find('div', class_='inarticle').find_all('p') if p.find('strong') is None])

# Extracting date and time
date_string = soup.find('div', class_='inarticle').find('p', class_='dt_sign').text.strip()
date_pattern = re.compile(r'Publié le (\d{2}/\d{2}/\d{2} \d{2}:\d{2})')
match = date_pattern.search(date_string)
date = match.group(1)

# Extracting author (if available)
author = None  # No author information available in the provided HTML snippet

print("Title:", title)
print("Content:", content)
print("Date:", date)
print("Author:", author)
