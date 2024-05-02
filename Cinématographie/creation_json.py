import requests
from bs4 import BeautifulSoup
import re
import json
from random import *

class Webscraper:
    def __init__(self, url):
        self.url = url

    def fetch_all_data(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        req = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        films = soup.find_all('div', class_='sc-b189961a-0 hBZnfJ')
        global films_liste
        films_liste = []
        for film in films:
            elem = film.find('h3', class_='ipc-title__text')
            if elem is not None:
                titre = elem.text
            else:
                titre=''
            title = titre.split(". ")
            enfant = 'li.ipc-metadata-list-summary-item:nth-child('+ title[0] +')'
            for i in range (1,2):
                year = enfant + ' > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(' + str(i) + ')'
                time = enfant + ' > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(' + str(i+1) + ')'
                dates = soup.select(year)
                durees = soup.select(time)

            if len(dates) !=0:
                for element in dates:
                    if element is not None:
                        el = element.text
                        if el[-1] == "m" or el[-1] == "h":
                            del el
                            date= randint(1900, 2024)
                        else:
                            date = el
            else:
                date= randint(1900, 2024)
            if len(durees) !=0:
                for item in durees:
                    if item is not None:
                        duree = item.text
                        if len(duree)>3:
                            if duree[-1] == "m":
                                div = duree.split("h ")
                                heure = int(div[0])
                                minu = div[1]
                                minutes = int(minu[:-1])
                                total = heure*60 + minutes
                            else:
                                del duree
                                total = randint(90, 150)
                        elif len(duree)<3:
                            if duree[-1] == "h":
                                total = int(duree[:-1])*60
                            else :
                                total = int(duree[:-1])
                        else:
                            total = int(duree[:-1])
            else:
                total= randint(90, 150)
            note = film.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
            if note is not None:
                stars = note.text
                star = stars.split()
                nb_votes = star[1].replace('(', '')
                vote = nb_votes.replace(')', '')
                if vote[-1] == "K":
                    nb = vote.replace("K", "")
                    votes = int(float(nb))*1000
                else:
                    votes = vote
            else:
                star= [randint(2, 8)]
                votes = randint(10, 100)
            match = re.search(r'genres=([^&]+)', self.url)
            if match:
                genre = match.group(1)
            global film_dict
            film_dict = {
                'id': title[0],
                'titre': title[1],
                'genre': genre,
                'annee': int(date),
                'duree': total,
                'note': float(star[0]),
                'nb_vote': int(votes)
            }
            films_liste.append(film_dict)
        total_liste.append(films_liste)

        with open('films.json', 'w') as f:  
            f.write(json.dumps(total_liste, indent=2))


    def fetch_time_data(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        req = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        films = soup.find('div', class_='sc-b189961a-0 hBZnfJ')
        duree = films.find_all('span', class_='sc-b189961a-8 kLaxqf dli-title-metadata-item')
        for span in duree:
            info = span.text

        match = re.search(r'genres=([^&]+)', self.url)
        if match:
            genre = match.group(1)
            print(genre)
        dic['genre']= genre

        sort = re.search(r'sort=([^,]+)', self.url)
        if sort:
            trie = sort.group(1)
        if trie == "runtime":
            enfant_duree = 'li.ipc-metadata-list-summary-item:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)'
            durees = soup.select(enfant_duree)
            ordre = re.search(r'sort=.*?,(\w+)', url)
            if ordre:
                order = ordre.group(1)

            if len(durees) !=0:
                for el in durees:
                    duree = el.text
                if order == "asc":
                    duree_min = int(duree[:-1]) 
                    dic['duree_min']= duree_min
                    print(dic)
                else:
                    if duree[-1] == "m":
                        div = duree.split("h ")
                        heure = int(div[0])
                        minu = div[1]
                        minutes = int(minu[:-1])
                        duree_max = heure*60 + minutes
                        dic['duree_max'] = duree_max
                    else:
                        duree_max = int(duree[:-1])*60
                        dic['duree_max'] = duree_max

            else:
                enfant_duree = 'li.ipc-metadata-list-summary-item:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)'
                durees = soup.select(enfant_duree)
                for el in durees:
                    duree = el.text
                if order == "asc":
                    if info[-1] == "m":
                        duree_min = int(duree[:-1])
                        dic['duree_min'] = duree_min
                else:
                    if duree[-1] == "m":
                        div = duree.split("h ")
                        heure = int(div[0])
                        minu = div[1]
                        minutes = int(minu[:-1])
                        duree_max = heure*60 + minutes
                        dic['duree_max'] = duree_max
                    else:
                        duree_max = int(duree[:-1])*60
                        dic['duree_max'] = duree_max

        else : 
            enfant_date = 'li.ipc-metadata-list-summary-item:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)'
            dates = soup.select(enfant_date)
            for elem in dates:
                date = elem.text
                date_min = int(date)
                dic['date_min'] = date_min
                print(dic)
        
        total_liste.append(dic)

        # with open('durees3.json', 'a') as f:  
        #     f.write(json.dumps(dic + ',', indent=2))

        
with open('url.txt', 'r') as f:
    lines = f.readlines()
    minim = []
    maxim = []
    total_liste = []
    dic = {}
    for line in lines:
        ligne = line[:-1]
        if ligne[-10:-5] == "alpha":
            url = ligne
            scraper = Webscraper(url)
            scraper.fetch_all_data()
        else:
            url = ligne
            scraper = Webscraper(url)
            scraper.fetch_time_data()
            
# comment faire pour que si le genre est le même que celui du dictionnaire précédent, ne pas en créer un nouveau mais y ajouter une ligne
# pb : il le fait pour chaque url sauf qu'un seul genre regroupe 3 urls