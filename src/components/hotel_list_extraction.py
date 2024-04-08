from src.exception import CustomException
from src.logger import logging
from src.utils import save_dataframe,make_dataframe_from_records
import sys
from tqdm import tqdm



class Hotel_List_Extraction:
  def __init__(self):
    print('\n')
    print('***********************************************************************INITIATING HOTEL LIST SCRAPING*******************************************************************************')
    logging.info(
        "Initiating extraction of hotels list")
    pass

  def initiate_data_extraction(self,soup):
    #****************************************************************************************************************************************************
    try:
        #" finding the container which stored each div of hotel list"
        
        container=soup.find('div',class_='infinite-scroll-component')
        _divs=container.find_all('div',recursive=False)   #: div which contain hotel info


        #****************************************************************************************************************************************************
        #: filtering the div as it container some black divs
        filtered_div=[]
        for div in _divs:
            id=div.get('id')
            if id is not None and id.startswith('htl_id_seo'):
                filtered_div.append(div)
        print("Step 1- TOTAL NUMBER OF HOTELS: ....",len(filtered_div))

        #****************************************************************************************************************************************************
        #: extracting the data from each div
        



        #****************************************************************************************************************************************************
        hotel_data=[]
        logging.info(
            'Number of hotels displayed'   
    )
        for div in tqdm(filtered_div,desc='Scraping In Process'):
          data={}

          hid=div.get('id')
          each=div.find('div',{
              'class':'HotelCardstyles__WrapperSectionMetaDiv-sc-1s80tyk-5 lnusVe'
          })
          data['hid']=hid
          
          try:
              name=each.find('div',{'class':'HotelCardstyles__HotelNameWrapperDiv-sc-1s80tyk-17 djDlfm'}).text
              data['name'] = name
          except:
              data['name'] = None  
          
          
          try:
              city=each.find('div',{'class':'PersuasionHoverTextstyles__TextWrapperSpan-sc-1c06rw1-15 hpnrYJ'}).text
              data['city'] = city
          except:
              data['city'] = None 
          

          try:
              distance_from_center=each.find('span',{'class':'HotelCardstyles__PersuationLocText-sc-1s80tyk-3 dfMOaa'}).text
              data['distance_from_center'] = distance_from_center
          except:
              data['distance_from_center'] = None
          

          try:
              price=each.find('p',{'itemprop':'priceRange'}).text
              data['price'] = price
          except:
              data['price'] = None
          

          try:
              tax=each.find('span',{'class':'HotelCardstyles__TaxPriceTextWrapper-sc-1s80tyk-34 JrHEe'}).text
              data['tax'] = tax
          except:
              data['tax'] = None
          
          try:
              hotel_type=each.find('span',{'class':'HotelCardstyles__HotelTypeTag-sc-1s80tyk-16 gvxJbv'}).text
              data['hotel_type'] = hotel_type
          except:
              data['hotel_type'] = None
          
          try:
              rating_value=each.find('span',{'itemprop':'ratingValue'}).text
              data['rating_value'] = rating_value
          except:
              data['rating_value'] = None

          try:
              image_urls = []
              img_div=each.find('div',{'class':'HotelCardstyles__ImageGalleryWrapperDiv-sc-1s80tyk-1 hYnRpm'})
              images=img_div.find_all('img')
              for img in images:
                  image_urls.append(img.get('src'))
              data['image_urls'] = image_urls
          except:
              pass
        
          #****************************************************************************************************************************************************
          hotel_data.append(data)
        logging.info(
            'hotels list extraction completed...'   
    )
        df=make_dataframe_from_records(hotel_data)
        _name=input('ENTER THE NAME FOR UPDATED DATAFRAME.....')
        print('Step 3- CREATING THE DATAFRAME......')
        full_path=r'C:\Users\ankit\Desktop\HotelList\artifacts\data\{0}'.format(_name)
        save_dataframe(full_path,df)
        print('CSV FILES SAVED IN DATA FOLDER ')
        print('\n')
        print('Step 2 ***************************************************************HOTEL LIST EXTRACTION COMPLETED************************************************************************************......')
        print('\n')
        logging.info(
     'hotels list saved in csv file in data folder'   
    )
        return df
    #****************************************************************************************************************************************************
    
    except Exception as e:
        raise CustomException(e,sys)

  
      