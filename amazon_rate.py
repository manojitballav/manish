from pymongo import MongoClient
from selenium import webdriver
import re,time
from selenium.common.exceptions import NoSuchElementException

# database connections
client = MongoClient('10.56.133.14',27017)
db = client['Projector']
col = db['amazon']

def five_star_scrap(pc,fiver):
    collection = db[pc]
    rating = 5
    pc = str(pc)
    driver = webdriver.Chrome()
    if(fiver < 10):
        page = int(fiver)
    elif(fiver>=10):
        page = (fiver//10)+1
    else:
        print("Brains Fried")
    for val in range(1,page+1):
        val = str(val)
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?ie=UTF8&reviewerType=all_reviews&filterByStar=five_star&pageNumber='+val+'&sortBy=recent')
        date = driver.find_elements_by_class_name('review-date')
        review = driver.find_elements_by_class_name('review-text')
        heading = driver.find_elements_by_class_name('review-title')
        for zal,kal,hal in zip(date,review,heading):
            # print('Date: '+str(zal.text))
            # print('Heading: '+str(hal.text))
            # print('Rating: '+str(5))
            # print('Review: '+str(kal.text))
            collection.update_one({"review": kal.text},{'$set':{"review":kal.text,"date":zal.text,"heading":hal.text,"rating":rating}},upsert=True)
    driver.quit()

def four_star_scrap(pc,fourr):
    collection = db[pc]
    rating = 4
    pc = str(pc)
    driver = webdriver.Chrome()
    if(fourr < 10):
        page = int(fourr)
    elif(fourr>=10):
        page = (fourr//10)+1
    else:
        print("Brains Fried")
    for val in range(1,page+1):
        val = str(val)
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?ie=UTF8&reviewerType=all_reviews&filterByStar=four_star&pageNumber='+val+'&sortBy=recent')
        date = driver.find_elements_by_class_name('review-date')
        review = driver.find_elements_by_class_name('review-text')
        heading = driver.find_elements_by_class_name('review-title')
        for zal,kal,hal in zip(date,review,heading):
            # print('Date: '+str(zal.text))
            # print('Heading: '+str(hal.text))
            # print('Rating: '+str(4))
            # print('Review: '+str(kal.text))
            collection.update_one({"review": kal.text},{'$set':{"review":kal.text,"date":zal.text,"heading":hal.text,"rating":rating}},upsert=True)
    driver.quit()

def three_star_scrap(pc,threer):
    collection = db[pc]
    rating = 3
    pc = str(pc)
    driver = webdriver.Chrome()
    if(threer < 10):
        page = int(threer)
    elif(threer>=10):
        page = (threer//10)+1
    else:
        print("Brains Fried")
    for val in range(1,page+1):
        val = str(val)
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?ie=UTF8&reviewerType=all_reviews&filterByStar=three_star&pageNumber='+val+'&sortBy=recent')
        date = driver.find_elements_by_class_name('review-date')
        review = driver.find_elements_by_class_name('review-text')
        heading = driver.find_elements_by_class_name('review-title')
        for zal,kal,hal in zip(date,review,heading):
            # print('Date: '+str(zal.text))
            # print('Heading: '+str(hal.text))
            # print('Rating: '+str(3))
            # print('Review: '+str(kal.text))
            collection.update_one({"review": kal.text},{'$set':{"review":kal.text,"date":zal.text,"heading":hal.text,"rating":rating}},upsert=True)
    driver.quit()

def two_star_scrap(pc,twor):
    collection = db[pc]
    rating = 2
    pc = str(pc)
    driver = webdriver.Chrome()
    if(twor < 10):
        page = int(twor)
    elif(twor>=10):
        page = (twor//10)+1
    else:
        print("Brains Fried")
    for val in range(1,page+1):
        val = str(val)
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?ie=UTF8&reviewerType=all_reviews&filterByStar=two_star&pageNumber='+val+'&sortBy=recent')
        date = driver.find_elements_by_class_name('review-date')
        review = driver.find_elements_by_class_name('review-text')
        heading = driver.find_elements_by_class_name('review-title')
        for zal,kal,hal in zip(date,review,heading):
            # print('Date: '+str(zal.text))
            # print('Heading: '+str(hal.text))
            # print('Rating: '+str(2))
            # print('Review: '+str(kal.text))
            collection.update_one({"review": kal.text},{'$set':{"review":kal.text,"date":zal.text,"heading":hal.text,"rating":rating}},upsert=True)
    driver.quit()

def one_star_scrap(pc,oner):
    collection = db[pc]
    rating = 1
    pc = str(pc)
    driver = webdriver.Chrome()
    if(oner < 10):
        page = int(oner)
    elif(oner>=10):
        page = (oner//10)+1
    else:
        print("Brains Fried")
    for val in range(1,page+1):
        val = str(val)
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?ie=UTF8&reviewerType=all_reviews&filterByStar=one_star&pageNumber='+val+'&sortBy=recent')
        date = driver.find_elements_by_class_name('review-date')
        review = driver.find_elements_by_class_name('review-text')
        heading = driver.find_elements_by_class_name('review-title')
        for zal,kal,hal in zip(date,review,heading):
            # print('Date: '+str(zal.text))
            # print('Heading: '+str(hal.text))
            # print('Rating: '+str(1))
            # print('Review: '+str(kal.text))
            collection.update_one({"review": kal.text},{'$set':{"review":kal.text,"date":zal.text,"heading":hal.text,"rating":rating}},upsert=True)
    driver.quit()

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
    try:
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=one_star&pageNumber=1&sortBy=recent')
        # driver.implicitly_wait(3)
        oner = driver.find_element_by_xpath('//*[@id="filter-info-section"]/span[1]').text
        oner = oner.replace('-','')
        tmp1 = re.findall(r'\d+',oner)
        res1 = list(map(int,tmp1))
        oner = int(res1[1])
        one_star_scrap(pc,oner)
    except NoSuchElementException:
        pass

    # getting the number of two_star reviews
    try:
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=two_star&pageNumber=1&sortBy=recent')
        twor = driver.find_element_by_xpath('//*[@id="filter-info-section"]/span[1]').text
        twor = twor.replace('-','')
        tmp2 = re.findall(r'\d+',twor)
        res2 = list(map(int,tmp2))
        twor = int(res2[1])
        two_star_scrap(pc,twor)
    except NoSuchElementException:
        pass

    # getting the number of three_star reviews
    try:
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=three_star&pageNumber=1&sortBy=recent')
        threer = driver.find_element_by_xpath('//*[@id="filter-info-section"]/span[1]').text
        threer = threer.replace('-','')
        tmp3 = re.findall(r'\d+',threer)
        res3 = list(map(int,tmp3))
        threer = int(res3[1])
        three_star_scrap(pc,threer)
    except NoSuchElementException:
        pass

    # getting the number of four_star reviews
    try:
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=four_star&pageNumber=1&sortBy=recent')
        fourr = driver.find_element_by_xpath('//*[@id="filter-info-section"]/span[1]').text
        fourr = fourr.replace('-','')
        tmp4 = re.findall(r'\d+',fourr)
        res4 = list(map(int,tmp4))
        fourr = int(res4[1])
        four_star_scrap(pc,fourr)
    except NoSuchElementException:
        pass

    # getting the number of five_star reviews
    try:
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&amp%3BshowViewpoints=1&filterByStar=five_star&pageNumber=1&sortBy=recent')
        fiver = driver.find_element_by_xpath('//*[@id="filter-info-section"]/span[1]').text
        fiver = fiver.replace('-','')
        tmp5 = re.findall(r'\d+',fiver)
        res5 = list(map(int,tmp5))
        fiver = int(res5[1])
        five_star_scrap(pc,fiver)
    except NoSuchElementException:
        pass

    driver.quit()

    # printing the breakup of reviews along ratings
    # print('1 Star: '+str(oner))
    # print('2 Star: '+str(twor))
    # print('3 Star: '+str(threer))
    # print('4 Star: '+str(fourr))
    # print('5 Star: '+str(fiver))

def read():
    # for doc in col.find({'pc':{"$in":["B07DJ8K2KT"]}}):
    for doc in col.find({}):
        number(doc['pc'])

if __name__ == '__main__':
    read()
