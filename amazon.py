from pymongo import MongoClient
from selenium import webdriver
import re,time

# database connections
client = MongoClient('10.56.137.20',27017)
db = client['Manish']
col = db['amazon']

def scrap(pc,pub):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    collection = db[pc]
    for val in range(1,int(pub)):
        val = str(val)
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?showViewpoints=1&sortBy=recent&pageNumber='+val+'')
        date = driver.find_elements_by_class_name('review-date')
        review = driver.find_elements_by_class_name('review-text')
        heading = driver.find_elements_by_class_name('review-title')
        for zal,kal,hal in zip(date,review,heading):
            collection.update_one({"review": kal.text},{'$set':{"review":kal.text,"date":zal.text,"heading":hal.text}},upsert=True)
            # collection.(doc)
        print('page:'+str(val))
    print('Completed: '+pc)
    driver.quit()

def number(pc):
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.in/dp/'+pc)
    time.sleep(4)
    nub = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]').text
    driver.quit()
    nub = nub.replace(' customer reviews','')
    nub = nub.replace(' customer review','')
    # reviews availabe online
    nub = nub.replace(',','')
    pub = (int(nub)//10)+2
    # reviews available locally
    dub = db[pc].count_documents({})
    if (int(nub) > pub):
        scrap(pc,pub)
    else:
        print("Panic")

def read():
    for doc in col.find():
        number(doc['pc'])

if __name__ == '__main__':
    read()
