# danawa.py

'''
    윈도우키 + R --> 실행창
    cmd 엔터키
        > pip install requests
        > pip install beautifulsoup4

'''

import requests as r
from bs4 import BeautifulSoup

url = "http://www.danawa.com"
h = {"User-agent" : "Mozilla/5.0"}

response = r.get(url, headers=h) # 해당 페이지 읽어오기

soup = BeautifulSoup(response.content, "html.parser") # 객체생성
#print(soup)

# 전체 HTML 코드에서 <div class="cm_pick_content"> 태그 내용만 가져오기
# find("태그명") --> 해당 태그와 이름이 같은게 모두 찾아짐
# find("태그명", {"속성명" : "속성의 값"}) --> 해당 태그, 속성 값 일치해야 찾음
cmpick = soup.find("div", {"class" : "cm_pick_content"})
#print(cmpick)

data = []
index = 0

# 존재하는 7개의 ul 태그를 찾는데, find_all()은 같은 이름의 태그가 여러 개일 때
# 리스트 형태로 반환해준다.

for ul in cmpick.find_all("ul"): # 7회 반복
    for li in ul.find_all("li"): # 6회 반복
        product = li.find("p").text.replace("\n", "") # <p>태그의 일반텍스트를 문자열로 반환
        price_data = li.find("div")
        price = price_data.find("span", {"class" : "price_type2"}).text
        print(product)
        print(price)
        index += 1
        if price_data.find("span", {"class":"percent_type1"}):
            percent = price_data.find("span").text
            data.append([index, product, percent, price])

        else:
            data.append([index, product, price])

print(data)

with open("danawa.csv", "w") as file:
    for d in data:
        if len(d) == 3:
            file.write("{},{},{},{}\n".format(d[0], d[1].replace(",", ""), "0%", d[2].replace(",", "")))
        else:
            file.write("{},{},{},{}\n".format(d[0], d[1].replace, d[2], d[3].replace(",", "")))


































































