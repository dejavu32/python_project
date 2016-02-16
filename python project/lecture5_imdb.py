# -*- coding: utf-8 -*-

movie_total = []

import requests
from bs4 import BeautifulSoup as bs

def crawl_movie_info(src):
    res = requests.get(src)

    if res.status_code == 200:
        soup = bs(res.text, "html.parser")

        # titles를 가져오는 방법은 아래 두가지 방법으로 가능하나 첫번째의 경우 select 내에서 하나씩 소거해가며 찾아야됨.
        # title의 selector , :nth-child(1)는 제거해야 에러가 안남
        # titles = soup.select('#main > div > div > div > table > tbody > tr > td > h4 > a')
        titles = soup.findAll('h4', {'itemprop':'name'})
        for title in titles:
            print title.text


        # score = movie.findAll('h4', {'itemprop':'name'})
        print title
        #main > div > div.list.detail > div:nth-child(2)


crawl_movie_info("http://www.imdb.com/movies-coming-soon/2015-01/")

target_url = 'http://www.imdb.com/movies-coming-soon/{0}'

# for i in range (1,13):
#     date = "2015-"+ str(i).zfill(2)
#     # print "2015-"+ str(i).zfill(2) + " crawling..."
#     print target_url.format(date) + " crawling..."
#     crawl_movie_info(target_url.format(date))
#     print target_url.format(date) + " done."
# title의 selector ; #main > div > div.list.detail > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.overview-top > h4 > a
