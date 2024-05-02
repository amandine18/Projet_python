genres = ['action', 'adventure', 'animation', 'biography', 'comedy', 'crime', 'documentary', 'drama', 'family', 'fantasy', 'film-noir', 'game-show', 'history', 'horror', 'music', 'musical', 'mystery', 'news', 'reality-tv', 'romance', 'sci-fi', 'sport','talk-show', 'thriller', 'war', 'western']
trie = ['alpha', 'runtime', 'year']
ordre = ['asc', 'desc']

for genre in genres:
    url1 = 'https://www.imdb.com/search/title/?title_type=feature&genres=' + genre
    for tri in trie:
        if tri == 'runtime':
            url2 = url1 + '&sort=' + tri
            for order in ordre:
                url3 = url2 + ',' + order
                with open('url.txt', 'a') as f:
                    f.write(url3 + '\n')
                url3 = url1 + '&sort=' + tri
        elif tri == 'alpha':
            url2 = url1 + '&sort=' + tri + ',desc'
            with open('url.txt', 'a') as f:
                f.write(url2 + '\n')
        elif tri =='year':
            url2 = url1 + '&sort=' + tri + ',asc'
            with open('url.txt', 'a') as f:
                f.write(url2 + '\n')
        url1 = 'https://www.imdb.com/search/title/?title_type=feature&genres=' + genre

