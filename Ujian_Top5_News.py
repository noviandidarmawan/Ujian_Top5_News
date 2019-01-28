import json
import requests
import API

def news():
    print('Selamat datang, mau tahu berita apa hari ini?')
    print('[1] Berita seputar teknologi')
    print('[2] Berita seputar bisnis')
    print('[3] Berita seputar olahraga')
    print('[4] Berita seputar kesehatan')
    print('[5] Berita seputar science')
    pilihan = input('Ketik pilihan Anda [1/2/3/4/5] : ')
    print('\n')

    
    if pilihan == '1':
        url ='https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=' + API.code
        data_teknologi = requests.get(url)
        berita1 = data_teknologi.json()['articles'][0]['title']
        berita2 = data_teknologi.json()['articles'][1]['title']
        berita3 = data_teknologi.json()['articles'][2]['title']
        berita4 = data_teknologi.json()['articles'][3]['title']
        berita5 = data_teknologi.json()['articles'][4]['title']
        print('Berikut adalah top 5 berita Indonesia bidang teknologi :')
        print('1 - '+ berita1)
        print('2 - '+ berita2)
        print('3 - '+ berita3)
        print('4 - '+ berita4)
        print('5 - '+ berita5)
    elif pilihan =='2':
        url = 'https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey=' + API.code
        data_bisnis = requests.get(url)
        berita1 = data_bisnis.json()['articles'][0]['title']
        berita2 = data_bisnis.json()['articles'][1]['title']
        berita3 = data_bisnis.json()['articles'][2]['title']
        berita4 = data_bisnis.json()['articles'][3]['title']
        berita5 = data_bisnis.json()['articles'][4]['title']
        print('Berikut adalah top 5 berita Indonesia bidang bisnis :')
        print('1 - '+ berita1)
        print('2 - '+ berita2)
        print('3 - '+ berita3)
        print('4 - '+ berita4)
        print('5 - '+ berita5)
    elif pilihan == '3':
        url = 'https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=' + API.code
        data_olahraga = requests.get(url)
        berita1 = data_olahraga.json()['articles'][0]['title']
        berita2 = data_olahraga.json()['articles'][1]['title']
        berita3 = data_olahraga.json()['articles'][2]['title']
        berita4 = data_olahraga.json()['articles'][3]['title']
        berita5 = data_olahraga.json()['articles'][4]['title']
        print('Berikut adalah top 5 berita Indonesia bidang olahraga :')
        print('1 - '+ berita1)
        print('2 - '+ berita2)
        print('3 - '+ berita3)
        print('4 - '+ berita4)
        print('5 - '+ berita5)
    elif pilihan == '4':
        url = 'https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey=' + API.code
        data_kesehatan = requests.get(url)
        berita1 = data_kesehatan.json()['articles'][0]['title']
        berita2 = data_kesehatan.json()['articles'][1]['title']
        berita3 = data_kesehatan.json()['articles'][2]['title']
        berita4 = data_kesehatan.json()['articles'][3]['title']
        berita5 = data_kesehatan.json()['articles'][4]['title']
        print('Berikut adalah top 5 berita Indonesia bidang kesehatan :')
        print('1 - '+ berita1)
        print('2 - '+ berita2)
        print('3 - '+ berita3)
        print('4 - '+ berita4)
        print('5 - '+ berita5)
    elif pilihan == '5':
        url = 'https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey=' + API.code
        data_sains = requests.get(url)
        berita1 = data_sains.json()['articles'][0]['title']
        berita2 = data_sains.json()['articles'][1]['title']
        berita3 = data_sains.json()['articles'][2]['title']
        berita4 = data_sains.json()['articles'][3]['title']
        berita5 = data_sains.json()['articles'][4]['title']
        print('Berikut adalah top 5 berita Indonesia bidang sains :')
        print('1 - '+ berita1)
        print('2 - '+ berita2)
        print('3 - '+ berita3)
        print('4 - '+ berita4)
        print('5 - '+ berita5)
    else:
        print('maaf keyword/pilihan tidak tersedia')

news()