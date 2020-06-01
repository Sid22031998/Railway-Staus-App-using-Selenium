from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print('\n*****Railway Status System*****\n')
print('1. Train Status')
print('2. PNR Status')
print('3. Book Tickets')
print('\nEnter your choice: ')
a=int(input())

if a==1:
	print('\nEnter Train Number : ')
	n=int(input())
	driver = webdriver.Chrome("chromedriver.exe")
	driver.get('https://www.railyatri.in/live-train-status')
	search_bar = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/form/div[1]/input')
	search_bar.send_keys(n)
	search_bar.send_keys(Keys.ENTER)

elif a==2:
	print('\nEnter PNR Number:')
	n=int(input())
	driver = webdriver.Chrome("chromedriver.exe")
	driver.get('https://www.trainspnrstatus.com/')
	search_bar = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/form/input')
	search_bar.send_keys(n)
	search_bar.send_keys(Keys.ENTER)
elif a==3:
	driver = webdriver.Chrome("chromedriver.exe")
	driver.get('https://www.irctc.co.in/')
else:
	print('\nInvalid Input')