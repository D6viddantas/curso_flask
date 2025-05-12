import urllib.request 
import json

def list_filmes(tipo):
    url = ''
    if tipo == 'Populares':
        url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=57e8bbfa80f346b41ae25d2d73993d62'
    elif tipo == 'Animação':
        url = 'https://api.themoviedb.org/3/discover/movie?with_genres=16&sort_by=vote_average.desc&vote_count.gte=1000&api_key=57e8bbfa80f346b41ae25d2d73993d62'
    elif tipo == '2010':
        url = 'https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=popularity.desc&api_key=57e8bbfa80f346b41ae25d2d73993d62'
    else:
        url = 'https://api.themoviedb.org/3/discover/movie?language=de-DE&region=DE&release_date.gte=2015-11-16&release_date.lte=2016-12-02&with_release_type=2|3&api_key=57e8bbfa80f346b41ae25d2d73993d62'
    response = urllib.request.urlopen(url)

    dados = response.read()
    dados_json = json.loads(dados)['results']
    return dados_json
