from src.exception import CustomException
from tqdm import tqdm
from src.utils import make_dataframe_from_records,save_dataframe
import pandas as pd
import sys
import requests
from src.logger import logging

class Reviews_Extraction:
  def __init__(self) -> None:
    print('*********************************************************************REVIEWS EXTRACTION PROCESS INITIATED********************************************************************')
    pass


  def fetch_response(self,id,i):
        cookies = {
            'tvc_sess_alive': '1',
            'tvc_setShoppers': '0|0|0|0',
            'tvc_sm_lpc': 'not_set%20/%20not_set%20/%20(not%20set)',
            'ls_sm_lpc24': 'not_set%20/%20not_set%20/%20(not%20set)',
            'ls_sm_lpc7': 'not_set%20/%20not_set%20/%20(not%20set)',
            'AMCVS_289D7D6662CD510D0A495FC9%40AdobeOrg': '1',
            'bm_sv': 'D25CBA683523773B8F48688697485D28~YAAQrHUsMR8RZ4eOAQAA8tsgshd2jx9jykfVv1O193I+twzOcfo6eYlFjMbFAOw3Grmlp3uUCfko8UjWbdC9wz+Ue3Go7ELm/JKMD9uUX+DwtstRTQ+GBr5qPFZLJufKwSi9lqazLw5dOtKFNooySuumWIt2DDVuv/fF0XabvLfQaURZrNnl8+UVFwyKc+A76zx0WtEO30FnmExygoDgg6TU78knhybERGENRnUQQOVlF9rC3hGPu/NMqGbzAuGmjQ==~1',
            '_gcl_au': '1.1.1418592023.1712385478',
            '_ga': 'GA1.1.11489579.1712385479',
            'AMCV_289D7D6662CD510D0A495FC9%40AdobeOrg': '179643557%7CMCIDTS%7C19820%7CMCMID%7C37860774192521647163799034986260202835%7CMCAAMLH-1712990277%7C12%7CMCAAMB-1712990277%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1712392677s%7CNONE%7CMCSYNCSOP%7C411-19827%7CvVersion%7C5.5.0',
            'ak_bmsc': '1C94E0D0F067D84B7A0832368374A342~000000000000000000000000000000~YAAQlHUsMf/HYJqOAQAA0uAgshdsGgEIen6h4ZsOSbBsS36JdI0OrjXrveL4pPpz3JR4/7nhG0gZJZx7D0iovAHGzgntJLjvDfilODP9Rb215fuoait1HbE1vPSbddyiiZ8aaiZEcNCpaXluHjqDJG4ahbXiaAjKf293P7NWewqkd9ZHrhQRTWFHkvVKYmuZ6dNMVidexRiM7A9TdUSg1MjWkN25NoeUw4nA07hmhU0M1K0n9jnXto2qbDtzrR8BCdHAAm4J7JEBYRIZSxBT/IhC9gSSI62CM4O+c7CoO+MWm74zyy7RcIJvOhlo8knUBBiwZY2l+ZuPnJptG6a3x4vuKQAOeCC0oC2fj0QfoXzRPhz5/fvs+lW8qDlg3zlPh0sQcu6Ljl0tEUExe/MHmRnsjZwPNoz8DPC20VGvSltuBKgSCFrvRGFAEz8NUZw7SwZ83r1xj6h/qOR8JtylqxmDMVspvuojabp4qbbI2l8N/i1VUSoTwswHcVbqeP+DXTlySipTodQB0LfpundRVvL3QvN0NachdQ==',
            '_fbp': 'fb.1.1712385480170.854765330',
            'gpv_pn': 'funnel%3Adomestic%20hotels%3Adetails',
            's_cc': 'true',
            'session-id': '773a23d9-8fc5-4bd3-8f12-a407c8980e9e',
            's_ips': '8263.60009765625',
            'bm_sz': 'A4A1D689BE9DF913BD3B5FE4BD02598A~YAAQFNjIF98oFrKOAQAAU1w+shfdTM7elJlUsDUZQ3wORaGO/hmU9Xl9tLa5xvvqRXTj104aesNX9J68sYYyIVp93Yq03hML+DzuMHZo5AVdfCZJhrVn0gRc20v9P0TQEvuq7wB7PafeWxkDZblKuWkgPCNGJ8c5qv0nazGTh7xYk1z+qCnVYuGPpBt9vEvTdgI9rsWrm8Vx+AAYRH4wlsPaD56qQaQwZpubW+BBjvD6fLeemf3Yskm6a69vnj2D9jnZIE8Hn4nrZt3nXdbD2ps+AxroLEJ+WCg7J+WeqUf9Kh7YY4vC+yJhz7hKryOXKuq+WDtIfVJBFr0dhrNq55QU+SIZPvH880hrYU+vH9E2nqW4InGTKPn2n2zVV6+pn1HLQi+le+9mE+V0aq7W/JfU/z3sXnHNlGC0AZoUyjhXNSPYUSn+GP7Jei4EO4JrdYaUV0e7HfaISoUkaNUwFi8gg2nH3ttcUJH/Jc/CHAw=~3294516~3224628',
            'tvc_sess': '%7B%22sm%22:%22(direct)%20/%20(none)%20/%20(not%20set)%22,%22t%22:1712387412525%7D',
            '_uetsid': '36349890f3e011ee8b48b7cc3cff47ce',
            '_uetvid': '3634d580f3e011eea8ae696e1ccfc141',
            '_ga_W4B122MQXT': 'GS1.1.1712385478.1.1.1712387412.34.0.0',
            's_plt': '1.41',
            's_pltp': 'funnel%3Adomestic%20hotels%3Adetails',
            '_abck': 'D9ACE159C51F195A1ECF29F92D199FC3~-1~YAAQFNjIFx4pFrKOAQAAwWQ+sguqNmyn4MfnNJbfr5ObOSyhrI/FlkIQE9rC8pO+6YPJR6d9UChFP2zdTrcFwx8Qu9YYTzhOMzaE2uWvA+Nm/DBDI+ROP4BYznNkuIKZ/32kT+qXlqzmuraWTEGbuBgfeMMn2fs+Mp003bvhaF9RFGaDN9kFzkA6jfDQ54MnFe0iyoCzn3baKHWZH17aakCHd/MkbUB4V7YqyTeVzbYZxA8LsfIo1+b0ILJlH238diGUZztySTFPY57GyMCj25AenS0mZtzpyevi+UvI7rY3B+1LBnrORzLATspHX46wZMzXABft42VOscypraN+AxPQJN7aNSNfB9voB/SGVkmL4eK0T7IlriakJWWYn8TAXO6C8y8Ud9nugf4=~-1~-1~-1',
            's_tp': '8459',
            's_ppv': 'funnel%253Adomestic%2520hotels%253Adetails%2C98%2C98%2C8263%2C10%2C12',
            's_nr30': '1712387463667-New',
            's_sq': 'ibibowebsiteprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dfunnel%25253Adomestic%252520hotels%25253Adetails%2526link%253D2%2526region%253Dguest-reviews%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dfunnel%25253Adomestic%252520hotels%25253Adetails%2526pidt%253D1%2526oid%253DfunctionUr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DLI',
        }
        
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'tvc_sess_alive=1; tvc_setShoppers=0|0|0|0; tvc_sm_lpc=not_set%20/%20not_set%20/%20(not%20set); ls_sm_lpc24=not_set%20/%20not_set%20/%20(not%20set); ls_sm_lpc7=not_set%20/%20not_set%20/%20(not%20set); AMCVS_289D7D6662CD510D0A495FC9%40AdobeOrg=1; bm_sv=D25CBA683523773B8F48688697485D28~YAAQrHUsMR8RZ4eOAQAA8tsgshd2jx9jykfVv1O193I+twzOcfo6eYlFjMbFAOw3Grmlp3uUCfko8UjWbdC9wz+Ue3Go7ELm/JKMD9uUX+DwtstRTQ+GBr5qPFZLJufKwSi9lqazLw5dOtKFNooySuumWIt2DDVuv/fF0XabvLfQaURZrNnl8+UVFwyKc+A76zx0WtEO30FnmExygoDgg6TU78knhybERGENRnUQQOVlF9rC3hGPu/NMqGbzAuGmjQ==~1; _gcl_au=1.1.1418592023.1712385478; _ga=GA1.1.11489579.1712385479; AMCV_289D7D6662CD510D0A495FC9%40AdobeOrg=179643557%7CMCIDTS%7C19820%7CMCMID%7C37860774192521647163799034986260202835%7CMCAAMLH-1712990277%7C12%7CMCAAMB-1712990277%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1712392677s%7CNONE%7CMCSYNCSOP%7C411-19827%7CvVersion%7C5.5.0; ak_bmsc=1C94E0D0F067D84B7A0832368374A342~000000000000000000000000000000~YAAQlHUsMf/HYJqOAQAA0uAgshdsGgEIen6h4ZsOSbBsS36JdI0OrjXrveL4pPpz3JR4/7nhG0gZJZx7D0iovAHGzgntJLjvDfilODP9Rb215fuoait1HbE1vPSbddyiiZ8aaiZEcNCpaXluHjqDJG4ahbXiaAjKf293P7NWewqkd9ZHrhQRTWFHkvVKYmuZ6dNMVidexRiM7A9TdUSg1MjWkN25NoeUw4nA07hmhU0M1K0n9jnXto2qbDtzrR8BCdHAAm4J7JEBYRIZSxBT/IhC9gSSI62CM4O+c7CoO+MWm74zyy7RcIJvOhlo8knUBBiwZY2l+ZuPnJptG6a3x4vuKQAOeCC0oC2fj0QfoXzRPhz5/fvs+lW8qDlg3zlPh0sQcu6Ljl0tEUExe/MHmRnsjZwPNoz8DPC20VGvSltuBKgSCFrvRGFAEz8NUZw7SwZ83r1xj6h/qOR8JtylqxmDMVspvuojabp4qbbI2l8N/i1VUSoTwswHcVbqeP+DXTlySipTodQB0LfpundRVvL3QvN0NachdQ==; _fbp=fb.1.1712385480170.854765330; gpv_pn=funnel%3Adomestic%20hotels%3Adetails; s_cc=true; session-id=773a23d9-8fc5-4bd3-8f12-a407c8980e9e; s_ips=8263.60009765625; bm_sz=A4A1D689BE9DF913BD3B5FE4BD02598A~YAAQFNjIF98oFrKOAQAAU1w+shfdTM7elJlUsDUZQ3wORaGO/hmU9Xl9tLa5xvvqRXTj104aesNX9J68sYYyIVp93Yq03hML+DzuMHZo5AVdfCZJhrVn0gRc20v9P0TQEvuq7wB7PafeWxkDZblKuWkgPCNGJ8c5qv0nazGTh7xYk1z+qCnVYuGPpBt9vEvTdgI9rsWrm8Vx+AAYRH4wlsPaD56qQaQwZpubW+BBjvD6fLeemf3Yskm6a69vnj2D9jnZIE8Hn4nrZt3nXdbD2ps+AxroLEJ+WCg7J+WeqUf9Kh7YY4vC+yJhz7hKryOXKuq+WDtIfVJBFr0dhrNq55QU+SIZPvH880hrYU+vH9E2nqW4InGTKPn2n2zVV6+pn1HLQi+le+9mE+V0aq7W/JfU/z3sXnHNlGC0AZoUyjhXNSPYUSn+GP7Jei4EO4JrdYaUV0e7HfaISoUkaNUwFi8gg2nH3ttcUJH/Jc/CHAw=~3294516~3224628; tvc_sess=%7B%22sm%22:%22(direct)%20/%20(none)%20/%20(not%20set)%22,%22t%22:1712387412525%7D; _uetsid=36349890f3e011ee8b48b7cc3cff47ce; _uetvid=3634d580f3e011eea8ae696e1ccfc141; _ga_W4B122MQXT=GS1.1.1712385478.1.1.1712387412.34.0.0; s_plt=1.41; s_pltp=funnel%3Adomestic%20hotels%3Adetails; _abck=D9ACE159C51F195A1ECF29F92D199FC3~-1~YAAQFNjIFx4pFrKOAQAAwWQ+sguqNmyn4MfnNJbfr5ObOSyhrI/FlkIQE9rC8pO+6YPJR6d9UChFP2zdTrcFwx8Qu9YYTzhOMzaE2uWvA+Nm/DBDI+ROP4BYznNkuIKZ/32kT+qXlqzmuraWTEGbuBgfeMMn2fs+Mp003bvhaF9RFGaDN9kFzkA6jfDQ54MnFe0iyoCzn3baKHWZH17aakCHd/MkbUB4V7YqyTeVzbYZxA8LsfIo1+b0ILJlH238diGUZztySTFPY57GyMCj25AenS0mZtzpyevi+UvI7rY3B+1LBnrORzLATspHX46wZMzXABft42VOscypraN+AxPQJN7aNSNfB9voB/SGVkmL4eK0T7IlriakJWWYn8TAXO6C8y8Ud9nugf4=~-1~-1~-1; s_tp=8459; s_ppv=funnel%253Adomestic%2520hotels%253Adetails%2C98%2C98%2C8263%2C10%2C12; s_nr30=1712387463667-New; s_sq=ibibowebsiteprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dfunnel%25253Adomestic%252520hotels%25253Adetails%2526link%253D2%2526region%253Dguest-reviews%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dfunnel%25253Adomestic%252520hotels%25253Adetails%2526pidt%253D1%2526oid%253DfunctionUr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DLI',
            'origin': 'https://www.goibibo.com',
            'referer': 'https://www.goibibo.com/',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        }
        
        params = {
            'offset': f'{5*i}',
            'limit': '5',
            'sortBy': 'help',
            'webp': 'true',
            'flavour': 'dWeb',
        }
        response = requests.get(
            f'https://ugcx.goibibo.com/api/HotelReviews/forMobileV4/{id}',
            params=params,
            cookies=cookies,
            headers=headers,
        )
        return response
  


  def initiate_review_extraction(self,df):
      try:
      #: USING ID AS PRIMARY KEY TO JOIN WITH OTHER DATAFRAMES
        hotel_reviews=[]
        data={}
        for i,j in tqdm(df.iterrows()):
            print("*"*100)
            print(f'REVIEWS OF DATAFRAME AT INDEX {i} IN PROGRESS..........\n\n')
            id=j['id']
            data={}
            data['id']=id
            data['reviews']=[]
            collected_review=[]
            initial_fetch=self.fetch_response(id,i)
            data_fetch=initial_fetch.json()
            nor=data_fetch['reviewsCount']
            print('tTOTAL REVIEW IN ', id, ":",nor)
            if nor!=0:
                last=round(int(nor)/5)
                for i in tqdm(range(last),desc='Scraping reviews'):
                    response=self.fetch_response(id,i) # type: ignore
                    json_data=response.json()
                    for i in range(5):
                        try:
                            review=json_data['reviews'][i]['reviewContent']
                            collected_review.append(review+"****")
                        except Exception as e:
                            if isinstance(e, IndexError):
                                print("NO MORE ITEM AVAILABLE.")
                                print(f'ALL REVIEWS  {id} SCRAPED...\n')
                                print("\n\n")
                                pass
                            else:
                                print(type(e))
                                print(e)
                                pass
                            
                data['reviews']=(collected_review)
                hotel_reviews.append(data)
                data={}
            else:
                print('sorry 0 reviews found')
                hotel_reviews.append(data)
                data={}

        review_df=make_dataframe_from_records(hotel_reviews)
        _name=input('Enter the name for the Review dataframe csv...')
        full_path=r'C:\Users\ankit\Desktop\HotelList\artifacts\data\{0}'.format(_name)
        save_dataframe(full_path,review_df)
        logging.info(
            'Review extraction completed..........'
        )
        print('***************************************************************REVIEWS EXTRACTION COMPLETED****************************************************')
        print('***************************************************************CONGRATULATION******************************************************************')

      except Exception as e:
          raise CustomException(e,sys)


if __name__=="__main__":
    obj4=Reviews_Extraction()
    obj4.initiate_review_extraction()