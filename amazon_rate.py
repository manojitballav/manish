from pymongo import MongoClient
from selenium import webdriver
import re,time

# database connections
client = MongoClient('10.56.133.14',27017)
db = client['Manish']
col = db['amazon']


def number(pc):
    driver = webdriver.Chrome()
    # get total number of reviews
    driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=acr_dpproductdetail_text?ie=UTF8&amp;showViewpoints=1')
    # number of reviews
    nr = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div[11]/div').text
    nr = nr.replace(',','')
    print(pc +': '+nr)
    tmp = re.findall(r'\d+',nr)
    res = list(map(int,tmp))
    review = res[0]
    print(review)
    rating = res[1]
    print(rating)
    print(str(pc)+': Reviews: '+str(review)+' Ratings: '+str(rating))
    driver.quit()


def read():
    for doc in col.find({'pc':{"$in":["B07X1KT6LD"]}}):
    # for doc in col.find({}):
        number(doc['pc'])

if __name__ == '__main__':
    read()

# Xpath repo
# Fetching the star rating
# /html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div[1]/div/div/div[2]/a[1]/i/span
# /html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div['+tal+']/div/div/div[2]/a[1]/i/span

# Fetching reviewer name
# /html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/a/div[2]/span
# /html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div[10]/div/div/div[1]/a/div[2]/span

# Fetching review title
# /html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div[1]/div/div/div[2]/a[2]/span
# /html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div[10]/div/div/div[2]/a[2]/span

# Fetching review body
# /html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div[1]/div/div/div[4]/span/span
# /html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div[10]/div/div/div[4]/span/span

# Fetching review date
# /html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div[1]/div/div/span
# /html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div[10]/div/div/span

# Number of reviews
# https://www.amazon.in/product-reviews/B07X2KLKRZ/ref=acr_dpproductdetail_text?ie=UTF8&amp;showViewpoints=1
# /html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div[11]/div



# one star
# https://www.amazon.in/product-reviews/B07X2KLKRZ/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&amp%3BshowViewpoints=1&sortBy=recent&pageNumber=2&filterByStar=one_star
