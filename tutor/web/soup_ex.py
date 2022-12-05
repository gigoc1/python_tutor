import requests 

from bs4 import BeautifulSoup
def get_soup(url):      

      res = requests.get(url)       
      if res.status_code == 200:            
            return BeautifulSoup(res.text, 'html.parser')

def selectEx(s):  
      print("자식태그  (>) : ",s.select("._lnb_text_3f3tB>.blind "))  
      # print("#자손 태그 (띄어쓰기) : ", s.select("div.section_cell strong")[0].text)  
      # print("#아이디 태그 조합", s.select("#t134953 div.tit_area strong")[0].text) 
      # print("=======================")      
      # print(s.select("#t134953 div.list_type a")[0])
      # print("=======================")
      # print(s.select("#t134953 div.list_type a span.txt")[0].text)      
      # print(s.select("#t134953 div.list_type a")[0]['href'])      
      # print("=======================")
      # print()
      # print(s.select("#t134953 div.list_type a img"))      
      # print(s.select("#t134953 div.list_type a img")[0]['src'])
      # print("=======================")      
      # print(s.select("#t134953 div.list_type a>span.txt")[0].text)            
      # print("=======================")      
      # for tags in s.select("#t134953 div.list_type ul>li"):
      #       print(tags)
      #       print("img link :", tags.select_one('img')['src'])
      #       print("a txt : ", tags.select_one('a span.txt').text)
      #       print("a link :", tags.select_one('a')['href'])
      #       print("a txt :", tags.select_one('a>span.txt').text)
      #       print("price :", tags.select_one('span.price>em').text)
      #       print(tags.select('span.list_tag span'))            
      #       print("hot deal : ", "".join([v.text for v in tags.select('span.list_tag span')]))            
      #       print("#####################################") 
      # print("@@@@@@@@@@ select() 와 select_one()")
      # print(s.select_one("div.section_cell div li a").text) #select_one와 select의 차이(여러개가 있지만 하나만 가져온다.)
      # print(    s.select("div.section_cell div li a")[0].text) 
      # print(    s.select("div.section_cell div li a")[1].text) 

if __name__ == '__main__':
    s = get_soup('https://shopping.naver.com/')
    selectEx(s)