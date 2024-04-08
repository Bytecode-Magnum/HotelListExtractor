from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd



def scroll_window(driver,timeout=120):
    #: Infinite Scroll ----> Scrolling till the end of the pages
    try:
        def scroll_windows():
            # Scroll to a few inches above the bottom of the page
            target_height = driver.execute_script("return document.body.scrollHeight") * 0.9
            driver.execute_script("window.scrollTo(0, arguments[0]);", target_height)
        start_time=time.time()
        while True:
            if time.time() - start_time > timeout:
                print("Timeout reached. Exiting scrolling loop.")
                break
            old_height = driver.execute_script('return document.body.scrollHeight')
            scroll_windows()
            time.sleep(3)
            new_height = driver.execute_script('return document.body.scrollHeight')
            if new_height == old_height:
                    break
    except Exception as e:
        raise CustomException(e,sys)


def make_soup(page_source):
    try:
        soup=BeautifulSoup(page_source,'html.parser')
        return soup
    except Exception   as e:
        raise CustomException(e,sys)



import logging

def save_object(file_name, data):
    try:
        file_path = f"C:\\Users\\ankit\\Desktop\\HotelList\\artifacts\\soups\\{file_name}.txt"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(data))
    except Exception as e:
        logging.error('Error occurred in save_object: %s', e)
        raise CustomException(e, sys)


    

def load_object(object_path):
    
    try:
        with open(object_path,'r') as f:
            content=f.read()
            return content
    except Exception as e:
        raise CustomException(e,sys)    



def make_dataframe_from_records(record):
    try:
        df=pd.DataFrame.from_records(record)
        return df
    except Exception as e:
        raise CustomException(e,sys)

def save_dataframe(file_name,df):
    try:
        df.to_csv(file_name,index=False)
    except Exception as e:
        raise CustomException(e,sys)

    