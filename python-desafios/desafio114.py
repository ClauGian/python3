import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.cursoemvideo.com')
except urllib.error.URLError:
    print('O site Curso em Vídeo não está acessível no momento.')
else:
    print('Consegui acessar o site Curso em Vídeo com sucesso.')
    print(site.read())

