from src.exception import CustomException
from src.logger import logging
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
import time
from src.utils import scroll_window
from src.utils import make_soup
from src.utils import save_object
from src.components.hotel_list_extraction import Hotel_List_Extraction
from src.components.data_transformation import Data_Transformation
from src.components.reviews_extraction import Reviews_Extraction
from src.components.sentiment_analysis import Sentiment_Analysis

#: creaeting webdriver


class initiate_data_ingestion:
  def __init__(self):
    print('*****************************gon********************************************DATA INGESTION INITIATED****************************************************************************')
    print('\n')
    pass
  
  def fetch_location(self):
    location=input('ENTER THE LOCATION....')
    print('Step 1- LOCATION INPUT SUCCESS')
    return location
  

  def begin_search(self,location):
      self.location=location
      #****************************************************************************************************************************************************
      #: opeing the webdriver
      driver=webdriver.Firefox()
      url='https://www.goibibo.com/hotels'
      #: fetch the url
      driver.get(url)
      
      #****************************************************************************************************************************************************
      #: wait until the content get loaded
      time.sleep(3)
      print('Step 2- URL FETCHED.....')
      #****************************************************************************************************************************************************
      #: find the input field
      try:
        # # : find the search box and enter the location
        input_container=driver.find_element(By.ID,"downshift-1-input")
        logging.info('Input container found')
        input_container.send_keys(location)
        print('Step 3- INPUT PROVIDED....')
        print('PLEASE VISIT BROWSER AND SELECT MOST FAVOURABLE ITEM FROM DROPDOWN.....')
        time.sleep(10)

        #****************************************************************************************************************************************************
        #: location added successfully
        logging.info('Data input sucess.....')
        search_button=driver.find_element(By.XPATH,"//button[@data-testid='searchHotelBtn']")
        logging.info('Search button found')
        search_button.click()
        time.sleep(5)
        print('Step 4 - SEARCH RESULT FOUND.....')

        #****************************************************************************************************************************************************
        logging.info('search button clicked...')
        scroll_window(driver,120)
        

        #****************************************************************************************************************************************************
        i=int(input('ENTER 1 TO SCROLL MORE 0 TO END SCROLLING...'))
        if i==1:
          scroll_window(driver=driver)
        else:
          logging.info('Scrolling ended....')
          print('Step 5- SCROLLING ENDED, WE ARE AT THE END OF PAGE, ALL HOTELS LIST DISPLAYED')
          pass

        #****************************************************************************************************************************************************
        #: get the page source
        page_source=driver.page_source
        soup=make_soup(page_source)


      #****************************************************************************************************************************************************
        #: save the soup inside txt file
        soup_file_name=input('ENTER THE SOUP FILE NAME...')
        soup_file_name=soup_file_name
        save_object(soup_file_name,soup)
        logging.info('Saving the soup inside txt file')
        print('Step 6- SOUP SAVED IN TXT FILE IN SOUPS FOLDER..')
        print("*"*100)
        print('\n')
        print('*********************************************************DATA INGESTION COMPLETED*******************************************************************')
        print('\n')
        return soup



      except Exception as e:
        raise CustomException(e,sys)
      

if __name__=="__main__":
  obj=initiate_data_ingestion()
  location=obj.fetch_location()
  soup=obj.begin_search(location=location)
  obj2=Hotel_List_Extraction()
  df=obj2.initiate_data_extraction(soup)
  obj3=Data_Transformation()
  df=obj3.initiate_transformation(df)
  obj4=Reviews_Extraction()
  review_df=obj4.initiate_review_extraction(df)
  obj5=Sentiment_Analysis()
  sentiment_df=obj5.sentiment_analysis()
  obj5.aggregate_review_with_dataframe(sentiment_df,df)

  