import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
import os
import pandas as pd
from pathlib import Path
import regex as re
df = pd.DataFrame(columns=['Title','Company','Ratings','Reviews','URL'])
# url="https://www.naukri.com/python-jobs"
# page_len=(len(url))
url="https://www.naukri.com/python-jobs"
# page_len=(len(url))
# page = requests.get(url)
# page.otext

options=Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(r"C:\Users\MSI\.wdm\drivers\chromedriver\win32\91.0.4472.101\chromedriver.exe",options= options)
driver.get(url)
time.sleep(10)
soup = BeautifulSoup(driver.page_source,"html5lib")
def norm(fetch_data)
for  param in range(1,40):
    #data=os.Path.join(r"C:\Users\MSI\.wdm\drivers\chromedriver\win32\91.0.4472.101\chromedriver.exe")
    url="https://www.naukri.com/"+s
    # page_len=(len(url))
    # page = requests.get(url)
    # page.otext
    options=Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(r"C:\Users\MSI\.wdm\drivers\chromedriver\win32\91.0.4472.101\chromedriver.exe",options= options)
    driver.get(url)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source,"html5lib")
    
    #print(soup.prettify())
    driver.close()
    results = soup.find(class_='list')
    #print(results)
    job_elems = results.find_all('article',class_='jobTuple bgWhite br4 mb-8')
    
    for job_elem in job_elems:
        urla=job_elem.find('a',class_='title fw500 ellipsis')
        url=urla.get('href')
        ##Pring title
        Title=job_elem.find('a',class_='title fw500 ellipsis').text.upper()
        title= re.sub(r'[^\w\s]',' ', Title)
        Com=job_elem.find('a',class_='subTitle ellipsis fleft')
        
        ##Ratiing
        rating_spam=job_elem.find('span',class_='starRating fleft dot')
        if rating_spam is None:
            continue
        else:
            Rating=rating_spam.text
        ##Review
        Review_span=job_elem.find('a',class_='reviewsCount ml-5 fleft blue-text')
        if Review_span is None:
            continue
        else:
            Reviews=Review_span.text
    #Appending the data
        'Title','Company','Ratings','Reviews','URL'
        df=df.append({'URL' : url,'Title' : title,"Company": Com.text.upper() ,'Ratings' : Rating,'Reviews' : Reviews},ignore_index=True)
df.head()

def norm(x):##This function to normalize teh title.
    y=x.split(" ")
    if("DATA" in y )and ("ANALYST" in y):
    
        return("DATA ANALYST")
    elif("SENIOR" in y )and ("PYTHON" in y):
        return("SENIOR PYTHON ENGINEER")
    elif("DATA" in y )and ("ENGINEER" in y):
        return("DATA ENGINEER")
    elif("PERMOFORMANCE" in y )and ("TEST" in y):
        return("PERFORMANCE TEST ENGINEER")
    elif("BIG" in y )and ("BIG" in y):
        return("BIG DATA ENGINEER")
    elif("SENIOR" in y ) or ('SR' in y)and ("ANALYST" in y):
        return("SENIOR DATA ANALYST")
    elif("PYTHON" in y) and ("DESIGNER" in y):
        return("PYTHON DESIGNER")
    else:
        return(x)
    
    
for i in range(df.shape[0]):
    
    df["Title"][i]=norm(df["Title"][i])
df.to_csv("Naukri1.csv",index=False)

def norm(x):##This function to normalize teh title.
    y=x.split(" ")
    if("DATA" in y )and ("ANALYST" in y):
    
        return("DATA ANALYST")
    if("SENIOR" in y )and ("PYTHON" in y):
        return("SENIOR PYTHON ENGINEER")
    if("DATA" in y )and ("ENGINEER" in y):
        return("DATA ENGINEER")
    if("PERMOFORMANCE" in y )and ("TEST" in y):
        return("PERFORMANCE TEST ENGINEER")
    if("BIG" in y )and ("BIG" in y):
        return("BIG DATA ENGINEER")
    if("SENIOR" in y ) or ('SR' in y)and ("ANALYST" in y):
        return("SENIOR DATA ANALYST")
    if("PYTHON" in y) and ("DESIGNER" in y):
        return("PYTHON DESIGNER")
    
    
for i in range(df.shape[0]):
    df["Title"][i]=norm(df["Title"][i])
    


