import pymysql
import requests
from bs4 import BeautifulSoup
import re

conn = pymysql.connect(host='127.0.0.1', user='root', password='k404', database='melon')

url = 'https://www.melon.com/chart/index.htm'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
res = requests.get(url, headers=header)
soup = BeautifulSoup(res.text, 'html.parser')

chart = soup.findAll('div', {'class': 'service_list_song'})

with conn.cursor() as cursor:
    for song in chart[:100]:
        s_rank_str = song.find('span', {'class': 'rank'}).text
        s_rank = int(re.findall('\d+', s_rank_str)[0])
        title = song.find('a', {'class': 'song_name'}).text
        artist = song.find('a', {'class': 'artist_name'}).text
        good = song.find('span', {'class': 'cnt'}).text if song.find('span', {'class': 'cnt'}) else '0'
        album = song.find('a', {'class': 'album_name'}).text
        img_url = song.find('a', {'class': 'image_typeAll'}).find('img')['src']

        print('%s위 : (%s) %s - %s' %(s_rank, album, title, artist))
        print("img_url ===== %s" %img_url)
                
        sql = "SELECT COUNT(*) FROM top100 WHERE title = %s AND artist = %s"
        cursor.execute(sql, (title, artist))
        count = cursor.fetchone()[0]
        
        if count == 0:
            sql = "INSERT INTO top100 (s_rank, album, title, artist, img_url) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (s_rank, album, title, artist, img_url))
        else:
            sql = "UPDATE top100 SET s_rank = %s, album = %s, img_url = %s WHERE title = %s AND artist = %s"
            cursor.execute(sql, (s_rank, album, img_url, title, artist))
    
    conn.commit()