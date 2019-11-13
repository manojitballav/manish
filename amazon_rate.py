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
    # print(pc +': '+nr)
    tmp = re.findall(r'\d+',nr)
    res = list(map(int,tmp))
    review = res[0]
    rating = res[1]
    print(str(pc)+': Reviews: '+str(review)+' Ratings: '+str(rating))

    # getting number of one_star reviews
    driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=one_star&pageNumber=1&sortBy=recent')
    # driver.implicitly_wait(3)
    oner = driver.find_element_by_xpath('//*[@id="filter-info-section"]/span[1]').text
    oner = oner.replace('-','')
    tmp1 = re.findall(r'\d+',oner)
    res1 = list(map(int,tmp1))
    oner = res1[1]

    # getting the number of two_star reviews
    driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=two_star&pageNumber=1&sortBy=recent')
    twor = driver.find_element_by_xpath('//*[@id="filter-info-section"]/span[1]').text
    twor = twor.replace('-','')
    tmp2 = re.findall(r'\d+',twor)
    res2 = list(map(int,tmp2))
    twor = res2[1]

    # getting the number of three_star reviews
    driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=three_star&pageNumber=1&sortBy=recent')
    threer = driver.find_element_by_xpath('//*[@id="filter-info-section"]/span[1]').text
    threer = threer.replace('-','')
    tmp3 = re.findall(r'\d+',threer)
    res3 = list(map(int,tmp3))
    threer = res3[1]

    # getting the number of four_star reviews
    driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=four_star&pageNumber=1&sortBy=recent')
    fourr = driver.find_element_by_xpath('//*[@id="filter-info-section"]/span[1]').text
    fourr = fourr.replace('-','')
    tmp4 = re.findall(r'\d+',fourr)
    res4 = list(map(int,tmp4))
    fourr = res4[1]

    # getting the number of five_star reviews
    driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=five_star&pageNumber=1&sortBy=recent')
    fiver = driver.find_element_by_xpath('//*[@id="filter-info-section"]/span[1]').text
    fiver = fiver.replace('-','')
    tmp5 = re.findall(r'\d+',fiver)
    res5 = list(map(int,tmp5))
    fiver = res5[1]

    # printing the breakup of reviews along ratings
    print('1 Star: '+str(oner))
    print('2 Star: '+str(twor))
    print('3 Star: '+str(threer))
    print('4 Star: '+str(fourr))
    print('5 Star: '+str(fiver))

    # closing the drivers
    driver.quit()

def read():
    # for doc in col.find({'pc':{"$in":["B07X1KT6LD"]}}):
    for doc in col.find({}):
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
