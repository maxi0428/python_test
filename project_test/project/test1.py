import pymysql
import requests
from bs4 import BeautifulSoup
import time

conn = pymysql.connect(host='127.0.0.1', user='root', password='k404', database='melon')

url = 'https://www.melon.com/chart/index.htm'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
res = requests.get(url, headers=header)
soup = BeautifulSoup(res.text, 'html.parser')

chart = soup.select('.service_list_song > table > tbody > tr')

with conn.cursor() as cursor:
    for song in chart[:100]:
        s_rank = song.select_one('.rank').text
        title = song.select_one('.ellipsis.rank01 > span > a').text
        artist = song.select_one('.ellipsis.rank02 > a').text
        good = song.select_one('.button_etc > button.like > span.cnt').text if song.select_one('.button_etc > button.like > span.cnt') else '0'
        album = song.select_one('.ellipsis.rank03 > a').text
        img_url = song.select_one('.image_typeAll > img')['src']
      
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
    time.sleep(3600)