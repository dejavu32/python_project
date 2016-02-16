# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs

result = requests.get('https://pixabay.com/en/')

# print dir(result)
print result.status_code        # 200
# print result.text
re_soup = bs(result.text,'html.parser')
re_soup_list= re_soup.findAll('div',{'class':'item'})
# print len(re_soup.select ('#gallery > div.flex_grid.credits > div > a > img'))      # 32

print re_soup.select ('#gallery > div.flex_grid.credits > div:nth-of-type(1) > a > img')
# print re_soup.select ('#gallery > div.flex_grid.credits > div > a > img')[0].attrs
# print re_soup.select ('#gallery > div.flex_grid.credits > div > a > img')[0].attrs['src']
# print re_soup_list[1].select ('#gallery > div.flex_grid.credits > div > a > img')


img_srcs = "https://pixabay.com"+ re_soup.select ('#gallery > div.flex_grid.credits > div > a > img')[0].attrs['src']
print img_srcs

import urllib
def download_image(img_src, filename):
    res = urllib.urlretrieve(img_src, filename)
    return res

images = re_soup.select ('#gallery > div.flex_grid.credits > div > a > img')

for i in images:
    imgage_src = "https://pixabay.com"+i.attrs['src']
    print imgage_src.split('/')[-1]+' downloading..'
    download_image(imgage_src, imgage_src.split('/')[-1])       # 폴더 위치까지 적으면 특정 폴더로 저장.
    



