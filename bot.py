import requests
from bs4 import BeautifulSoup
import time
import json
url = 'https://www.otomoto.pl/osobowe/audi/?page='
headers = {'User-agent': 'Mozilla/5.0'}

# ustaw maksymalną ilość stron, które chcesz przeszukać
max_pages = int(input('Ile stron chcesz przeszukac?: '))

data = []
for page in range(1, max_pages + 1):
    print(f"Strona:{page} ")
    response = requests.get(url + str(page), headers=headers)
    if response.status_code != 200:
        print(f"Wystąpił błąd. Kod odpowiedzi: {response.status_code}")
        continue
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    prices = soup.find_all('span', {'class': 'ooa-1bmnxg7 eayvfn611'})
    
    for price in prices:
        
        price_value = float(price.text.strip().replace(' ', '').replace('PLN', '').replace('USD', '').replace('EUR', ''))

                
            
        print(price_value)
        
        
        link_to_cars = soup.find_all('article',{'class' : 'ooa-1rudse5 eayvfn60'} )
        if price_value <= 15000:
            for link in link_to_cars:
                scraped_href = link.a['href']
                
                print(scraped_href)

            
            data.append({"price:" : price_value})
            with open("prices.json", 'w') as f:
                json.dump(data, f)
            
    # zaczekaj 1 sekundę, aby nie przeciążyć serwera
    time.sleep(1)






    
    



