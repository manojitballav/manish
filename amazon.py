from pymongo import MongoClient
from selenium import webdriver
import re,time

# database connections
client = MongoClient('10.56.133.14',27017)
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
def scrap_xpath(pc,pub):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    collection = db[pc]
    for val in range(1, int(pub)):
        val = str(val)
        driver.get('https://www.amazon.in/product-reviews/'+pc+'/ref=cm_cr_getr_d_paging_btm_next_'+val+'?showViewpoints=1&sortBy=recent&pageNumber='+val+'')
        for tal in range(1,10):
            tal = str(tal)
            rating = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div['+tal+']/div/div/div[2]/a[1]')
            print(rating)
            # author = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div['+tal+']/div/div/div[1]/a/div[2]/span')
            # title = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div['+tal+']/div/div/div[2]/a[2]/span')
            # review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div['+tal+']/div/div/div[4]/span/span')
            # date = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div[3]/div['+tal+']/div/div/span')
            # collection.update_one({"review":review.text,"rating":rating.text},{'$set':{"rating":rating.text,"author":author.text,"title":title.text,"review":review.text,"date":date.text}},upsert = True)
        print('page:'+str(val))
    print('Completed: '+pc)
    driver.quit()

def number(pc):
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.in/dp/'+pc)
    time.sleep(4)
    # nub = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]').text
    driver.quit()
    # nub = nub.replace(' customer reviews','')
    # nub = nub.replace(' customer review','')
    # reviews availabe online
    # nub = nub.replace(',','')
    # pub = (int(nub)//10)+2
    pub = int(43)
    # reviews available locally
    # dub = db[pc].count_documents({})
    # if (int(nub) > pub):
        # scrap(pc,pub)
    scrap(pc,pub)
    # else:
    #     print("Panic")

def read():
    for doc in col.find({'pc':{"$in":["B07X1KT6LD"]}}):
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
