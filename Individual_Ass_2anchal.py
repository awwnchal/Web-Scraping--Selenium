#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 23:45:49 2023

@author: anchalchaudhary
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo
import json
import random

def main():


    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()
    q9()


def q2():
 
    S = Service("/Applications/chromedriver")
    O = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=S, options=O)
    driver.implicitly_wait(20)
    driver.set_script_timeout(120)
    driver.set_page_load_timeout(10)
    
    
    driver.get("https://opensea.io/collection/boredapeyachtclub?search[sortAscending]=false&search[stringTraits][0][name]=Fur&search[stringTraits][0][values][0]=Solid%20Gold")
    time.sleep(2)
        
    
    #wait = WebDriverWait(driver, 20)  # Wait up to 60 seconds for element to appear
    #element = wait.until(EC.presence_of_element_located((By.ID, 'my_element_id')))
    
    
    dod = driver.find_elements(By.XPATH,"//a[@class='sc-1f719d57-0 fKAlPV Asset--anchor']")
    
    links=[]
    len(dod)
    
    links = [element.get_attribute('href') for element in dod[:8]]
    #print(links)
    
    
    # =============================================================================
    # for i, link in enumerate(links):
    #     print(link)
    #     driver.get(link)
    #     info = driver.page_source
    #     filename = f"bayc_{i+1}.htm"
    #     with open(filename,"w",encoding="utf-8") as w:
    #         w.write(info)
    # =============================================================================
    for i in range(len(links)):
        
       
        # print(links[i])
         driver.get(links[i])
         info = driver.page_source
         filename = f"bayc_{i+1}.htm"
         with open(filename,"w",encoding="utf-8") as w:
             w.write(info)
    
    driver.quit()
    

def q3():
    try:
         client = pymongo.MongoClient()
    except Exception:
         print("Error: " + Exception) 
     

    db = client["bayc"] #database
    collection = db["bayc"]   
        
    for i in range(8):    
        filename = f"bayc_{i+1}.htm"
        with open(filename, 'r') as file:
           soup = BeautifulSoup(file, 'html.parser')
           names = soup.select("h1.sc-29427738-0.hKCSVX.item--title") #list of 1 element
           DICTNAME = {"name": (names[0].text)}
          # print(DICTNAME)
           attributes = soup.select("div.Property--type") 
           values = soup.select("div.Property--value") #list of attributes for eac fi;e
           #print(attributes)
           
           for at, v in zip(attributes, values):
               DICTNAME[at.text] = v.text
               
           #print(DICTNAME)   
           collection.insert_one(DICTNAME)
           
        
def q4():
    r = requests.get("https://www.yellowpages.com/search?search_terms=Pizzeria&geo_location_terms=San+Francisco%2C+CA")
    filename = f"sf_pizzeria_search_page.htm"
    with open(filename,"w",encoding="utf-8") as w:
        w.write(r.content.decode('utf-8'))


# =============================================================================
# #TripAdvisor rating IIE, 
# #number of TA reviews IIE,
# =============================================================================
     
def q5():
    
# =============================================================================
#     try:
#          client = pymongo.MongoClient()
#     except Exception:
#          print("Error: " + Exception) 
#      
# 
#     db = client["sf_pizzerias"] #database
#     collection = db["sf_pizzerias"]   
# 
# =============================================================================
    filename = f"sf_pizzeria_search_page.htm"
    with open(filename, 'r') as file:
       soup = BeautifulSoup(file, 'html.parser')
       
       results = soup.select("div.result")
       results = results[1:]
      # print(result)
       
       names = soup.select("a.business-name")    
       names = names[1:-2] 
       
       for i in range(len(results)):
    
           
           dict = {"businessname": (names[i].text)}  #dictionary create 
           dict["url"] =  ("https://www.yellowpages.com" + names[i]['href'])
           dict["rank" ]= i+1
        
           try:
               r = results[i].find('div', {'class': 'ratings'}).find('div')
               dict["star ratings"] = r['class'][1]              
               dict["No of reviews"]= results[i].find('div',{'class': 'ratings',}).find('span',{'class':'count'}).text


           except:    
               dict["star ratings"]= None
               dict["No of reviews"]= None
                          
           try:
             
               a = results[i].find('div', {'class': 'amenities-info'})
               s = a.find_all('span')              
               amenities_list = [span.text for span in s]           
               dict["Amenities"]= amenities_list
                                       
           except:    
                  dict["Amenities"]= None                  
           try:
              dict["dollar_signs"] = results[i].find('div', {'class': 'price-range'}).text
               
           except:    
                  dict["dollar_signs"] = None                    
           try:
               dict["Review"] = results[i].find('p',{'class': 'body'}).text
                                                  
           except:    
               dict["Review"] = None                     
           try:
               dict["Years in business"] = results[i].find('div',{'class':'number'}).text
                                                        
           except:    
               dict["Years in business"] = None 
           try:
               
               y = results[i].find('div',{'class':'ratings','data-tripadvisor': True})
               k = json.loads(y['data-tripadvisor'])
               dict["TA rating"] = k['rating']
               dict["count"] = k['count']
                
               
                                                        
           except:    
               dict["TA rating"] = None      
               dict["count"] = None
               
               #<div class="ratings" data-tripadvisor="{&quot;rating&quot;:&quot;4.5&quot;,&quot;count&quot;:&quot;2662&quot;}" data-israteable="true" data-foursquare="9.03"><a class="rating hasExtraRating" href="/san-francisco-ca/mip/tonys-pizza-napoletana-17514197#yp-rating" data-analytics="{&quot;click_id&quot;:22,&quot;listing_features&quot;:&quot;ratings&quot;}" data-impressed="1"><div class="result-rating five  "></div><span class="count">(1)</span></a><a class="ta-rating-wrapper" href="/san-francisco-ca/mip/tonys-pizza-napoletana-17514197#ta-rating" data-analytics="{&quot;click_id&quot;:2396}" data-impressed="1"><div class="ta-rating extra-rating ta-4-5"></div><span class="ta-count">(2662)</span></a><span class="fs-rating-wrapper"><span class="fs-rating"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 17" width="15" height="20"><use xlink:href="#foursquare"></use></svg></span><span class="count">9.0</span></span></div>
                              
                  
           #print(dict)
# =============================================================================
#            collection.insert_one(dict)
# =============================================================================
def q6():
    try:
         client = pymongo.MongoClient()
    except Exception:
         print("Error: " + Exception) 
     

    db = client["sf_pizzerias"] #database
    collection = db["sf_pizzerias"]   

    filename = f"sf_pizzeria_search_page.htm"
    with open(filename, 'r') as file:
       soup = BeautifulSoup(file, 'html.parser')
       
       results = soup.select("div.result")
       results = results[1:]
      # print(result)
       
       names = soup.select("a.business-name")    
       names = names[1:-2] 
       
       for i in range(len(results)):
    
           
           dict = {"businessname": (names[i].text)}  #dictionary create 
           dict["url"] =  ("https://www.yellowpages.com" + names[i]['href'])
           dict["rank" ]= i+1
        
           try:
               r = results[i].find('div', {'class': 'ratings'}).find('div')
               dict["star ratings"] = r['class'][1]              
               dict["No of reviews"]= results[i].find('div',{'class': 'ratings',}).find('span',{'class':'count'}).text


           except:    
               dict["star ratings"]= None
               dict["No of reviews"]= None
                          
           try:
             
               a = results[i].find('div', {'class': 'amenities-info'})
               s = a.find_all('span')              
               amenities_list = [span.text for span in s]           
               dict["Amenities"]= amenities_list
                                       
           except:    
                  dict["Amenities"]= None                  
           try:
              dict["dollar_signs"] = results[i].find('div', {'class': 'price-range'}).text
               
           except:    
                  dict["dollar_signs"] = None                    
           try:
               dict["Review"] = results[i].find('p',{'class': 'body'}).text
                                                  
           except:    
               dict["Review"] = None                     
           try:
               dict["Years in business"] = results[i].find('div',{'class':'number'}).text
                                                        
           except:    
               dict["Years in business"] = None 
           try:
               
               y = results[i].find('div',{'class':'ratings','data-tripadvisor': True})
               k = json.loads(y['data-tripadvisor'])
               dict["TA rating"] = k['rating']
               dict["count"] = k['count']
                
               
                                                        
           except:    
               dict["TA rating"] = None      
               dict["count"] = None
               
               #<div class="ratings" data-tripadvisor="{&quot;rating&quot;:&quot;4.5&quot;,&quot;count&quot;:&quot;2662&quot;}" data-israteable="true" data-foursquare="9.03"><a class="rating hasExtraRating" href="/san-francisco-ca/mip/tonys-pizza-napoletana-17514197#yp-rating" data-analytics="{&quot;click_id&quot;:22,&quot;listing_features&quot;:&quot;ratings&quot;}" data-impressed="1"><div class="result-rating five  "></div><span class="count">(1)</span></a><a class="ta-rating-wrapper" href="/san-francisco-ca/mip/tonys-pizza-napoletana-17514197#ta-rating" data-analytics="{&quot;click_id&quot;:2396}" data-impressed="1"><div class="ta-rating extra-rating ta-4-5"></div><span class="ta-count">(2662)</span></a><span class="fs-rating-wrapper"><span class="fs-rating"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 17" width="15" height="20"><use xlink:href="#foursquare"></use></svg></span><span class="count">9.0</span></span></div>
                              
                  
           #print(dict)
           collection.insert_one(dict)    
    
          
           
           
def q7():
    try:
         client = pymongo.MongoClient()
    except Exception:
         print("Error: " + Exception) 
    db = client["sf_pizzerias"]
    collection = db["sf_pizzerias"]
    cursor = list(collection.find({},{"url":1}))
    for i in range(30):
        
       
        r =  requests.get(cursor[i]['url'])
        filename = f"sf_pizzerias_{i+1}.htm"
        with open(filename,"w",encoding="utf-8") as w:
           w.write(r.content.decode('utf-8'))    
def q8():
    ad=[]
    for i in range(30):    
        filename = f"sf_pizzerias_{i+1}.htm"
        with open(filename, 'r') as file:
            
             soup = BeautifulSoup(file, 'html.parser')                      
             address_span = soup.find('span', class_='address')
             address = address_span.text.strip()
             address = address.replace("San", ", San").replace("san", ", San")
             dict = {"Address" : address}
             ad.append(address)
             phone = soup.find('a', class_='phone dockable')
             phone = phone.text.strip()
             dict["Phone number"] = phone
             #print(dict)
             try:
                 
                 
                website = soup.find("a", {"class": "website-link dockable"})
              
                website = website["href"]
                dict["Website "] = website
             except:
                 dict["Website "] = None
                 
   # print(ad)       
                 
def q9():
    try:
         client = pymongo.MongoClient()
    except Exception:
         print("Error: " + Exception) 
    db = client["sf_pizzerias"]
    collection = db["sf_pizzerias"]    


    ad=[]
    for i in range(30):    
        filename = f"sf_pizzerias_{i+1}.htm"
        with open(filename, 'r') as file:
            
             soup = BeautifulSoup(file, 'html.parser')                      
             address_span = soup.find('span', class_='address')
             address = address_span.text.strip()
             address = address.replace("San", ", San").replace("san", ", San")
             dict = {"Address" : address}
             ad.append(address)
             phone = soup.find('a', class_='phone dockable')
             phone = phone.text.strip()
             dict["Phone number"] = phone
             #print(dict)
             try:
                 
                 
                website = soup.find("a", {"class": "website-link dockable"})
              
                website = website["href"]
                dict["Website "] = website
             except:
                 dict["Website "] = None
                 
                 
                
        db.sf_pizzerias.update_many({"rank": i+1}, {"$set": dict})
                            
                 
    #print(len(ad))       
       
    for a in ad: #runs 30 times
        
        link = f"http://api.positionstack.com/v1/forward?access_key=2ef2c398625533adc9423fc4425f76c7&query={a}"
        response = requests.get(link)
        contributors = response.json()
        
        try:
            
            lat = contributors['data'][0]['latitude']
            long = contributors['data'][0]['longitude']
            dict = {"latitude" : lat} #create
            dict["longitude "] = long
          #  print(dict)
            db.sf_pizzerias.update_many({"Address": a}, {"$set": dict})
        except:
            
            lat = random.uniform(-92,+92)
            long = random.uniform(-92,+92)
            dict = {"latitude" : lat} 
            dict["longitude "] = long
           # print(dict)
            db.sf_pizzerias.update_many({"Address": a}, {"$set": dict})
            

          

if __name__ == '__main__':
	main()