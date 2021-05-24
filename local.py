import re
import time
from typing import Collection
from pymongo import MongoClient
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# database connections
client = MongoClient('10.56.146.102',27017)
# db = client['Manish']
db = client['manish']
col = db['asin']
pc = 'B08RSY2653'

#reading the number of reviews from Amazon Product Page
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/product-reviews/"+pc+"/")
number = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[4]/div/span').text
print(number)
# driver.quit()

number = number.replace(' global ratings','')
number  = number.replace(' global reviews','')
number  = number.replace('|','')
number = number.replace(',','')
number = list(map(int, number.split()))
print("Number of reviews are: "+str(number[1]))

# Getting the number of review of each scale and scraping them

# #1 star reviews
driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_srt?filterByStar=one_star&pageNumber=1&sortBy=recent')
number = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[4]/div[2]/span').text
print(number)
number = number.replace(' global ratings','')
number  = number.replace(' global reviews','')
number  = number.replace('|','')
number = number.replace(',','')
number = list(map(int, number.split()))
number = (number[1])
number = int(number)
print("Number of one star reviews are: "+str(number))
#scraping the reviews
#method to scrap the reviews
collection = db[pc]
rating = 1
count = 0
for val in range(1, number+1):
    val = str(val)
    driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?ie=UTF8&reviewerType=all_reviews&filterByStar=one_star&pageNumber='+val+'&sortBy=recent')    
    for mal in range(1,11):
        try:
            heading = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/div[2]/a[2]/span')
        except Exception as e:
            heading = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/div[2]/a[2]/span[1]')
            print(e)
        try:
            date = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/span').text
        except Exception as e:
            date = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/span').text
            print(e)
        date = date.replace('Reviewed in India on ','')
        try:
            review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/div[4]/span/span')
        except Exception as e:
            review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/div[4]/span/span[1]')
            print(e)
        collection.insert_one({"review":review.text,"date":date,"heading":heading.text,"rating":rating})
        count = count+1
        print(count)

# 2 star reviews
driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_srt?filterByStar=two_star&pageNumber=1&sortBy=recent')
number = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[4]/div[2]/span').text
print(number)
number = number.replace(' global ratings','')
number  = number.replace(' global reviews','')
number  = number.replace('|','')
number = number.replace(',','')
number = list(map(int, number.split()))
number = (number[1])
number = int(number)
print("Number of two star reviews are: "+str(number))
#scraping the reviews
#method to scrap the reviews
collection = db[pc]
rating = 2
count = 0
for val in range(1, number+1):
    val = str(val)
    driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?ie=UTF8&reviewerType=all_reviews&filterByStar=two_star&pageNumber='+val+'&sortBy=recent')    
    for mal in range(1,11):
        try:
            heading = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/div[2]/a[2]/span')
        except Exception as e:
            heading = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/div[2]/a[2]/span[1]')
            print(e)
        try:
            date = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/span').text
        except Exception as e:
            date = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/span').text
            print(e)
        date = date.replace('Reviewed in India on ','')
        try:
            review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/div[4]/span/span')
        except Exception as e:
            review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/div[4]/span/span[1]')
            print(e)
        collection.insert_one({"review":review.text,"date":date,"heading":heading.text,"rating":rating})
        count = count+1
        print(count)

# 3 star reviews
driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_srt?filterByStar=three_star&pageNumber=1&sortBy=recent')
number = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[4]/div[2]/span').text
print(number)
number = number.replace(' global ratings','')
number  = number.replace(' global reviews','')
number  = number.replace('|','')
number = number.replace(',','')
number = list(map(int, number.split()))
number = (number[1])
number = int(number)
print("Number of three star reviews are: "+str(number))
# scraping the reviews
# method to scrap the reviews
collection = db[pc]
rating = 3
count = 0
for val in range(1, number+1):
    val = str(val)
    driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?ie=UTF8&reviewerType=all_reviews&filterByStar=three_star&pageNumber='+val+'&sortBy=recent')    
    for mal in range(1,11):
        try:
            heading = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/div[2]/a[2]/span')
        except Exception as e:
            heading = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/div[2]/a[2]/span[1]')
            print(e)
        try:
            date = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/span').text
        except Exception as e:
            date = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/span').text
            print(e)
        date = date.replace('Reviewed in India on ','')
        try:
            review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/div[4]/span/span')
        except Exception as e:
            review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/div[4]/span/span[1]')
            print(e)
        collection.insert_one({"review":review.text,"date":date,"heading":heading.text,"rating":rating})
        count = count+1
        print(count)


# 4 star reviews
driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_srt?filterByStar=four_star&pageNumber=1&sortBy=recent')
number = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[4]/div[2]/span').text
print(number)
number = number.replace(' global ratings','')
number  = number.replace(' global reviews','')
number  = number.replace('|','')
number = number.replace(',','')
number = list(map(int, number.split()))
number = (number[1])
number = int(number)
print("Number of four star reviews are: "+str(number))
#scraping the reviews
#method to scrap the reviews
collection = db[pc]
rating = 4
count = 0
for val in range(1, number+1):
    val = str(val)
    driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?ie=UTF8&reviewerType=all_reviews&filterByStar=four_star&pageNumber='+val+'&sortBy=recent')    
    for mal in range(1,11):
        try:
            heading = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/div[2]/a[2]/span')
        except Exception as e:
            heading = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/div[2]/a[2]/span[1]')
            print(e)
        try:
            date = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/span').text
        except Exception as e:
            date = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/span').text
            print(e)
        date = date.replace('Reviewed in India on ','')
        try:
            review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/div[4]/span/span')
        except Exception as e:
            review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/div[4]/span/span[1]')
            print(e)
        collection.insert_one({"review":review.text,"date":date,"heading":heading.text,"rating":rating})
        count = count+1
        print(count)


# 5 star reviews
driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_srt?filterByStar=five_star&pageNumber=1&sortBy=recent')
number = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[4]/div[2]/span').text
print(number)
number = number.replace(' global ratings','')
number  = number.replace(' global reviews','')
number  = number.replace('|','')
number = number.replace(',','')
number = list(map(int, number.split()))
number = (number[1])
number = int(number)
print("Number of five star reviews are: "+str(number))
#scraping the reviews
#method to scrap the reviews
collection = db[pc]
rating = 5
count = 0
for val in range(1, number+1):
    val = str(val)
    driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?ie=UTF8&reviewerType=all_reviews&filterByStar=five_star&pageNumber='+val+'&sortBy=recent')    
    for mal in range(1,11):
        try:
            heading = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/div[2]/a[2]/span')
        except Exception as e:
            heading = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/div[2]/a[2]/span[1]')
            print(e)
        try:
            date = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/span').text
        except Exception as e:
            date = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/span').text
            print(e)
        date = date.replace('Reviewed in India on ','')
        try:
            review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal)+']/div/div/div[4]/span/span')
        except Exception as e:
            review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(mal+1)+']/div/div/div[4]/span/span[1]')
            print(e)
        collection.insert_one({"review":review.text,"date":date,"heading":heading.text,"rating":rating})
        count = count+1
        print(count)
driver.quit()