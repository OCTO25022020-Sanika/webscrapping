from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
driver = webdriver.Chrome("C:\\Users\\Sanika\\Desktop\\chromedriver_win32 final\\chromedriver.exe")
products=[] #List to store name of the product
prices=[] #List to store price of the product
driver.get("https://www.amazon.in/s?k=goggles&ref=nb_sb_noss_1")
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('a',href=True, attrs={'class':'a-link-normal a-text-normal'}):
    name=a.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
    products.append(name.text)
for a1 in soup.findAll('a',href=True, attrs={'class':'a-size-base a-link-normal s-no-hover a-text-normal'}):
    name1=a1.find('span', attrs={'class':'a-price-whole'})
    prices.append(name1.text)
df = pd.DataFrame()
df['products']=products
df
df.to_csv("products.csv")
df1 = pd.DataFrame()
df1['prices']=prices
df1
df1.to_csv("prices.csv")
