# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs

soup = bs(open('./index.html'),'html.parser')

# print head_tag
# print soup.prettify()
# print soup.attrs
# print soup.title
# print soup.title.name
# print soup.title.text
# print soup.title.string
# print soup.span.string
# print soup.title.parent.name
# print soup.p      # p 속성만 가져오기
# print soup.a      # a속성만 가져오기
# print soup.find_all('a')[1]
# print soup.select ('#crawling')d
#
# print soup.findAll('a')
desc_line =  soup.findAll('div',{'class':'desc-line'})
# print type(desc_line)
# print desc_line[0]
# print
# print desc_line[1]
# print
# print desc_line[0].parent
# print
# print desc_line[0].text     # 태그 빼고 본문만 가져오기
# print
print desc_line[0].attrs    # 속성 보기
print desc_line[0].attrs['class']

