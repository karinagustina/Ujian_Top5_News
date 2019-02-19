#Ujian_Top5_News

import requests
print('Selamat datang, mau tahu berita apa hari ini?')
print('[1] Berita seputar teknologi')
print('[2] Berita seputar bisnis')
print('[3] Berita seputar olahraga')
print('[4] Berita seputar kesehatan')
print('[5] Berita seputar science')
kategori = input('Ketik pilihan Anda [1/2/3/4/5] : ')
if kategori == '1':
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=84b85859b12744358ca6eba326fe65ff'
    data = requests.get(url)
    output = data.json()
    print('Berikut adalah top 5 berita Indonesia bidang technology :')
    print('1 - ', data.json()['articles'][1]['title'])
    print('2 - ',data.json()['articles'][2]['title'])
    print('3 - ',data.json()['articles'][3]['title'])
    print('4 - ',data.json()['articles'][4]['title'])
    print('5 - ',data.json()['articles'][5]['title'])
elif kategori == '2':
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey=84b85859b12744358ca6eba326fe65ff'
    data = requests.get(url)
    output = data.json()
    print('Berikut adalah top 5 berita Indonesia bidang business :')
    print('1 - ', data.json()['articles'][1]['title'])
    print('2 - ',data.json()['articles'][2]['title'])
    print('3 - ',data.json()['articles'][3]['title'])
    print('4 - ',data.json()['articles'][4]['title'])
    print('5 - ',data.json()['articles'][5]['title'])
elif kategori == '3':
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=84b85859b12744358ca6eba326fe65ff'
    data = requests.get(url)
    output = data.json()
    print('Berikut adalah top 5 berita Indonesia bidang sports :')
    print('1 - ', data.json()['articles'][1]['title'])
    print('2 - ',data.json()['articles'][2]['title'])
    print('3 - ',data.json()['articles'][3]['title'])
    print('4 - ',data.json()['articles'][4]['title'])
    print('5 - ',data.json()['articles'][5]['title'])
elif kategori == '4':
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey=84b85859b12744358ca6eba326fe65ff'
    data = requests.get(url)
    output = data.json()
    print('Berikut adalah top 5 berita Indonesia bidang health :')
    print('1 - ', data.json()['articles'][1]['title'])
    print('2 - ',data.json()['articles'][2]['title'])
    print('3 - ',data.json()['articles'][3]['title'])
    print('4 - ',data.json()['articles'][4]['title'])
    print('5 - ',data.json()['articles'][5]['title'])
else:
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey=84b85859b12744358ca6eba326fe65ff'
    data = requests.get(url)
    output = data.json()
    print('Berikut adalah top 5 berita Indonesia bidang science :')
    print('1 - ', data.json()['articles'][1]['title'])
    print('2 - ',data.json()['articles'][2]['title'])
    print('3 - ',data.json()['articles'][3]['title'])
    print('4 - ',data.json()['articles'][4]['title'])
    print('5 - ',data.json()['articles'][5]['title'])
