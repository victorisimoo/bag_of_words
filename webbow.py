
from cgitb import html
import bs4 as bs
from matplotlib.pyplot import text
import nltk
import re
import urllib.request

url = 'https://es.wikipedia.org/wiki/Universidad_Rafael_Land%C3%ADvar'

# obtengo el html original
html_original = urllib.request.urlopen(url).read()

# limpiar la información
html_articulos = bs.BeautifulSoup(html_original, 'lxml')
parrafos_html = html_articulos.find_all('p')

# obtención de texto en lenguaje natural
texto_articulo = ""
for para in parrafos_html:
    texto_articulo += para.text
    
# corpus = texto a analizar
corpus = nltk.sent_tokenize(texto_articulo, "spanish")

for i in range(len(corpus)):
    corpus[i] = corpus[i].lower()
    corpus[i] = re.sub(r'\W', ' ', corpus[i])
    corpus[i] = re.sub(r'\s+', ' ', corpus[i])
    
# creación de tabla de frecuencias
frecuencias_bow = {}

for oracion in corpus:
    tokens = nltk.word_tokenize(oracion, "spanish")    
    for token in tokens:
        if token not in frecuencias_bow.keys():
            frecuencias_bow[token] = 1
        else:
            frecuencias_bow[token] += 1

sorted(frecuencias_bow.items(), key=lambda x: x[1], reverse=True)
print(frecuencias_bow)