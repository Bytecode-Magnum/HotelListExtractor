from src.utils import save_dataframe
import pandas as pd
from src.logger import logging
from src.exception import CustomException
import sys


class Data_Transformation:
  def __init__(self) -> None:
    print('\n')
    print('**********************************************************************DATA TRANSFORMATION INITIATED*******************************************************************************')
    print('\n')
    logging.info(
        'Initiating data transformation'
    )
    pass


  def initiate_transformation(self,df):
    try:
        df['id']=None
        df['id']=df['hid'].apply(lambda x: x.split("seo_")[-1])
        for i, id in df['id'].items():
          url= f"https://www.goibibo.com/hotels/odin-hostels-hotel-in-jibhi-{id}/?hquery={{%22ci%22:%2220240410%22,%22co%22:%2220240411%22,%22r%22:%221-2-0%22,%22ibp%22:%22%22}}&cc=IN&vcid=4926068515457680357&locusId=CTJIBH&locusType=city&cityCode=CTJIBH"
          df.loc[i, 'hotel_link'] = url
        print('DATA TRANSFORMATION ENDED, PROVIDE A NEW FILENAME FOR SAVING UPDATED DATAFRAME\n')
        _name=input('DATAFRAME HAS BEEN CLEANED ENTER THE NEW  NAME FOR UPDATED DATAFRAME.....')
        full_path=r'C:\Users\ankit\Desktop\HotelList\artifacts\data\{0}'.format(_name)
        save_dataframe(full_path,df)
        print('**************************************************DATA TRANSFORMATION ENDED ****************************************************************************************************')
        print('\n')
        logging.info(
          'data transformation ended....'
        )
        return df
    
    except Exception as e:
      raise CustomException(e,sys)
  

      
