# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = False
from bs4 import BeautifulSoup
import pandas


from datetime import datetime
import os


def login(driver):
    flag=False
    try:
        driver.get('https://www.linkedin.com/uas/login')
        
        time.sleep(4)

        print("enter  Username")
        email=driver.find_element_by_id('username')
        email.send_keys('futuresea713@gmail.com')
        
        print("enter  password")
        passwd=driver.find_element_by_id('password')
        passwd.send_keys('Future95713!')
        
        
        print("Click  on Signin")
        driver.find_element_by_xpath('//button[@aria-label="Sign in"]').click()
        
        time.sleep(2)

        
        flag=True
        pass
    except:
        pass
    
    return flag

def search_name_get_url(driver,url):
    try:
        driver.get(url)
        time.sleep(5)
        list = driver.find_element_by_css_selector("ul.search-results__list.list-style-none")
        mans = list.find_elements_by_tag_name('button')
        for man in mans:
            driver.execute_script("arguments[0].click();", man)
            time.sleep(1)
        
            try:
                butt = driver.find_element_by_css_selector("button.mr1.artdeco-button.artdeco-button--muted.artdeco-button--3.artdeco-button--secondary.ember-view")
                butt.click()
                message = driver.find_element_by_id("custom-message")
                message.send_keys("https://www.linkedin.com/pulse/credit-my-motto-hongbo-kim")
                time.sleep(1)
                div = driver.find_element_by_css_selector("div.artdeco-modal.artdeco-modal--layer-default.send-invite")
                butts = div.find_elements_by_tag_name("button")
                for idx, butt in enumerate(butts):
                    if idx == 2:
                        driver.execute_script("arguments[0].click();", butt)
                        time.sleep(1)
            except:
                pass
    except Exception as e:
        print(e)
        pass

def main():
    driver=''
    try:

        driver=webdriver.Chrome('chromedriver',options=options)
        
        print("Login Process started")
        if login(driver):
            i = 25
            while i < 100:
                url = "https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22us%3A0%22%5D&origin=FACETED_SEARCH&page=" + str(i)
                search_name_get_url(driver,url)
                i += 1
        else:
            print("Not able to login  try again")
        
    except Exception as e:
        print(e)
        pass
    driver.close()
    



main()