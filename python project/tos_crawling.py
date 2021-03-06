# -*- coding: utf-8 -*-
import requests, os
from bs4 import BeautifulSoup as bs

f = open('./board.txt', 'w')

#################################### 건의 게시판 본문 가져오기 테스트
# result = requests.get('http://tos.nexon.com/community/suggest/view.aspx?n4ArticleSN=27')     # 건의게시판
# result = requests.get('http://tos.nexon.com/community/free/view.aspx?n4ArticleSN=106501')     # 자유게시판
# print result.text
# re_soup = bs(result.text,'html.parser')
# print result.status_code

# words = re_soup.findAll('div',{'class':'viewContents'})[0].text.split()
# word = re_soup.findAll('div',{'class':'viewContents'})[0].text


#################################### 건의 게시판 본문 가져오기

def get_url_text(url):
    result = requests.get(url)
    re_soup = bs(result.text,'html.parser')
    try:
        if result.status_code == 200:

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

            # lines = [str(n)+'\t', title.encode('utf-8').strip()+ '\t', date[0].text.encode('utf-8').strip() + '\t', word.encode('utf-8').strip() + '\n']
            lines = [title.encode('utf-8').strip()+ '\t', date[0].text.encode('utf-8').strip() + '\t', word.encode('utf-8').strip() + '\n']
            # print lines
            # f.writelines(lines)
            board_main = word.encode('utf-8').strip()        # 게시판 본문 내용
            # print board_main
            return board_main

    except IndexError:
        # print n , '글없음'
        return '글없음'

f.close()

# 샘플로 여러라인 출력하기
# num = range(1, 100)
# for n in num:
#     url = 'http://tos.nexon.com/community/suggest/view.aspx?n4ArticleSN='+ str(n)
#     # print url             # 테스트용 url 출력
#     result = requests.get(url)

from collections import Counter
import urllib
import random
from lxml import html
# import pytagcloud
import sys




# from konlpy.tag import Hannanum    # 한국어 형태소 분석 모듈

from konlpy.tag import Kkma

def get_tags(text, ntags=50, multiplier=30):           # 폰트 크기 조절은 multiplier값을 조정해서
    # h = Hannanum()
    r = lambda: random.randint(0,255)
    color = lambda: (r(), r(), r())
    h = Kkma()
    text = unicode(text, 'utf-8')
    nouns = h.nouns(text)
    count = Counter(nouns)
    return [{ 'color': color(), 'tag': n, 'size': c*multiplier }\
                for n, c in count.most_common(ntags)]


import webbrowser
import pytagcloud           # word cloud 그리기

def draw_cloud(tags, filename,
               fontname='NotoSansCJKkr-Bold', size=(1200, 800)):          # fontname='Noto Sans CJK' 한글,
                # NotoSansCJKkr-Medium, NotoSansCJKkr-Bold, NotoSansCJKkr-Regular_0, NotoSansCJKkr-Light
    pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
    webbrowser.open(filename)

# 결과 출력 테스트
# 여러글 한번에 출력
text = ''
for i in range(19400,19430):        #   for i in range(19340,19430): 2/25일 하루치

    url = 'http://tos.nexon.com/community/suggest/view.aspx?n4ArticleSN='+ str(i)
    text += get_url_text(url)+ ''

print text
taglist = get_tags(text)          # 입렵받은 url의 본문 내용을 tags로 나누어주는
# print(taglist)

draw_cloud(taglist, 'e:\cloud_tos_test.jpg')










# 한 글씩 출력
# url = 'http://tos.nexon.com/community/suggest/view.aspx?n4ArticleSN='+ str(100)
# print url                           # 테스트용 url 출력
# board_main = get_url_text(url)
# print board_main                    # 게시판의 본문 내용 테스트 출력



# tags = get_tags(board_main)          # 입렵받은 url의 본문 내용을 tags로 나누어주는
# print(tags)                         # tag의 결과는 딕셔너리 리스트 형태
#
# draw_cloud(tags, 'wordcloud.png')   # 워드 클라우딩된 이미지 출력
#

















# 파일로 만든 결과를 워드 클라우딩 하기
# text = ''
# for i in range(19380,19430):        #   for i in range(19340,19430): 2/25일 하루치
#
#     url = 'http://tos.nexon.com/community/suggest/view.aspx?n4ArticleSN='+ str(i)
#     text += get_url_text(url)+ ''

# import os
# f = open('tos_crawling_result_sample.txt', 'w')
# f.write(text)
# f = open('tos_crawling_result_sample.txt','r')
# s= f.read()
# tags = get_tags(s)          # 입렵받은 url의 본문 내용을 tags로 나누어주기. 데이터가 클 경우 메모리 오류 발생. 수정요망.
# draw_cloud(tags, 'e:\\file_test.png')
# f.close()
#



