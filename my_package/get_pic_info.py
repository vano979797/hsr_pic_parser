from bs4 import BeautifulSoup
import requests
from cut_url import cut_url


def get_pic(url, type_pic):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        pictures = soup.find_all('img')
        for picture in pictures:
            if picture['alt'] == type_pic:
                pic = picture['src'] 
                pic = cut_url(pic)
                soup = BeautifulSoup(html_content, 'html.parser')
                name = soup.find('h1').get_text()
                return(pic, name)
    elif response.status_code == 500:
        print('Error loading the page:', response.status_code)
