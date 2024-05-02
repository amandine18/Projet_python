import json 
import matplotlib.pyplot as plt

class DataVisuaLizer:
    def __init__(self, data):
        self.data = data
    
    def create_bar_chart_hor_Noshow(self, x_data, y_data, title, xlabel, ylabel, chemin):
        plt.barh(y_data, x_data)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
        # plt.savefig('P:/1-EPSI/Projet python/Cinématographie/graphiques/'+ chemin + '.png')

    def create_bar_chart_ver_Noshow(self, x_data, y_data, title, xlabel, ylabel, chemin):
        plt.bar(x_data, y_data)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        # plt.text(x_data, y_data, y_data)
        plt.show()
        # plt.savefig('P:/1-EPSI/Projet python/Cinématographie/graphiques/'+ chemin + '.png')

    def create_point_chart_Noshow(self, mini, x_data, title, xlabel, ylabel, chemin):
        plt.scatter(x_data, mini)
        # plt.scatter(x_data, maxi)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
        # plt.savefig('P:/1-EPSI/Projet python/Cinématographie/graphiques/'+ chemin + '.png')

with open('films.json', 'r') as f:
    data = json.load(f)
    minim = []
    maxim = []
    duree_moyenne = []
    note_moyenne = []
    genres = []
    vote_moyenne = []
    for item in data:
        durees = []
        notes = []
        dates = []
        votes = []
        for i in item:
            date = i['annee']
            dates.append(date)
            high = max(dates)
            little = min(dates)
            duree = i['duree']
            durees.append(duree)
            moyenne = sum(durees)/len(durees)
            note = i['note']
            notes.append(note)
            note_moy = sum(notes)/len(notes)
            vote = i['nb_vote']
            votes.append(vote)
            vote_moy = sum(votes)
            genre = i['genre'][0:4]

        duree_moyenne.append(round(moyenne, 2))
        note_moyenne.append(round(note_moy, 2))
        minim.append(little)
        maxim.append(high)
        genres.append(genre)
        vote_moyenne.append(round(vote_moy, 2))

        year = DataVisuaLizer(data = [little, high, genre])
        star = DataVisuaLizer(data = [note_moy, genre])
        time = DataVisuaLizer(data = [moyenne, genre])
        nb = DataVisuaLizer(data = [vote_moy, genre])
        
    # year.create_point_chart_Noshow(minim, maxim, genres, "années de sorties les plus anciennes/recentes par genre", "genres", "années de sortie", "dates_min_max")
    # star.create_bar_chart_hor_Noshow(note_moyenne, genres, "note moyenne par genre", "notes moyennes", "genres", "notes_moy")
    # time.create_bar_chart_ver_Noshow(genres, duree_moyenne, "durées moyennes par genre", "genres", "durées moyennes", "durees_moy")
    # nb.create_bar_chart_hor_Noshow(vote_moyenne, genres, "nombre de vote par genre", "nombre de votes", "genres", "votes_moy")

with open('durees_DR_merged_classique.json', 'r') as f:
    data = json.load(f)
    genres = []
    durees_min = []
    durees_max = []
    dates = []
    for i in data:
        date = i['date_min']
        dates.append(date)
        duree_min = i['duree_min']
        durees_min.append(duree_min)
        duree_max = i['duree_max']
        durees_max.append(duree_max)
        genre = i['genre'][0:4]
        genres.append(genre)
    
        year = DataVisuaLizer(data = [date, genre])
        time_min = DataVisuaLizer(data = [duree_min, genre])
        time_max = DataVisuaLizer(data = [duree_max, genre])

    # year.create_point_chart_Noshow(dates, genres, "les plus anciennes sorties par genre", "années de sortie", "genres", "anees_sorties")
    # time_min.create_bar_chart_ver_Noshow(genres, durees_min, "films les plus courts par genre", "genre", "durée", "durees_min")
    time_max.create_bar_chart_ver_Noshow(genres, durees_max, "films les plus long par genre", "genres", "durées", "durees_max")
