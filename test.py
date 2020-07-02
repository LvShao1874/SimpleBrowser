# -*- coding: utf-8 -*-
from selenium import webdriver
from SimpleBrowser import SimpleBrowser
import time


def test():
    driver = None
    try:
        driver = webdriver.Chrome()
        driver = SimpleBrowser(driver)
        driver.get("http://www.baidu.com")
        
        search_input = driver.find_one("//*[@id='kw']")
        driver.wait_and_input(search_input, "hello selenium")
        
        time.sleep(3)
        search_button = driver.find_one("//*[@id='su']")
        driver.wait_and_click(search_button)

        time.sleep(3)
        search_input = driver.find_one("//*[@id='kw']")
        driver.wait_and_input(search_input, " hello selenium", is_clear=False)

        time.sleep(3)
        search_button = driver.find_one("//*[@id='su']")
        driver.wait_and_click(search_button)
        
        time.sleep(10)
    
    finally:
        driver.quit() if driver else None


if __name__ == '__main__':
    test()
