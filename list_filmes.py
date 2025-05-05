import urllib.request 
import json

url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=57e8bbfa80f346b41ae25d2d73993d62'

response = urllib.request.urlopen(url)

dados = response.read()
dados_json = json.loads(dados)['results']
