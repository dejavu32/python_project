# -*- coding: utf-8 -*-
import requests, os
from bs4 import BeautifulSoup as bs

f = open('./board.txt', 'w')

#################################### 건의 게시판 본문 가져오기 테스트
result = requests.get('http://tos.nexon.com/community/suggest/view.aspx?n4ArticleSN=27')     # 건의게시판
# result = requests.get('http://tos.nexon.com/community/free/view.aspx?n4ArticleSN=106501')     # 자유게시판
re_soup = bs(result.text,'html.parser')

words = re_soup.findAll('div',{'class':'viewContents'})[0].text.split()
word = re_soup.findAll('div',{'class':'viewContents'})[0].text


#################################### 건의 게시판 본문 가져오기
num = range(1, 100)
for n in num:
    url = 'http://tos.nexon.com/community/suggest/view.aspx?n4ArticleSN='+ str(n)
    print url
    result = requests.get(url)

    try:
        if result.status_code == 200:
            re_soup = bs(result.text,'html.parser')

            title = re_soup.findAll('h2',{'class':'tit'})[0].text
            word = re_soup.findAll('div',{'class':'viewContents'})[0].text
            date = re_soup.findAll('span',{'class':'date'})

            # print '글번호 : ' + str(n)
            # print '제목 : ' + title.encode('utf-8').strip()
            # print '본문 : ' + word.encode('utf-8').strip()
            # print date[0].text
            # lines = ['글번호 : ' + str(n)+'\n', '제목 : ' + title.encode('utf-8').strip()+ '\n',\
            #          '날짜 : '+ date[0].text.encode('utf-8').strip() + '\n', \
            #          '본문 : ' + word.encode('utf-8').strip() + '\n\n']

            lines = [str(n)+'\t', title.encode('utf-8').strip()+ '\t', date[0].text.encode('utf-8').strip() + '\t', word.encode('utf-8').strip() + '\n']

            print lines
            f.writelines(lines)

    except IndexError:
        print n , '글없음'



f.close()


