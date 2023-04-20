import requests
from bs4 import BeautifulSoup

url = 'https://www.nike.com/kr/w/men-shoes-nik1zy7ok'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
res = requests.get(url, headers=header)
soup = BeautifulSoup(res.text, 'html.parser')

chart = soup.select('.product-grid > main > div')

for i, song in enumerate(chart):
    # rank = song.select_one('.rank').text
    # title = song.select_one('.ellipsis.rank01 > span > a').text
    # artist = song.select_one('.ellipsis.rank02 > a').text
    # good = song.select_one('.button_etc > button.like > span.cnt').text if song.select_one('.button_etc > button.like > span.cnt') else '0'
    # album = song.select_one('.ellipsis.rank03 > a').text
    # img_url = song.select_one('.image_typeAll > img')
    # if img_url :
    #     img_url = img_url['src']
    # else:
    #     img_url = '이미지 없음'

    # print('%d위 : (%s) %s - %s' %(i+1, album, title, artist))
    print(song)


chart = soup.findAll('div',{'class':'service_list_song'})

for tag in chart :
    imgUrl1 = tag.find('a',{'class':'image_typeAll'})
    imgUrl2 = imgUrl1.find('img')['src'] 
    print(imgUrl1)
    print(imgUrl2)