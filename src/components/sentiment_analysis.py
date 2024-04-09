import pandas as pd
from transformers import pipeline
from src.utils import save_dataframe
from tqdm import tqdm
from src.exception import CustomException
from src.logger import logging
import sys

class Sentiment_Analysis:
    def __init__(self):
        try:
            logging.info(
                'Importing the data for sentiment analysis and model from hugging face'
            )
            print('***********************************************SENTIMENT ANALYSIS INITITATED****************************************************************')
            
        except Exception as e:
            raise CustomException(e,sys)

    def sentiment_analysis(self):
        df=pd.read_csv(r"C:\Users\ankit\Desktop\HotelList\artifacts\data\sfdsfd.csv")
        logging.info(
            'initiating the sentiment analysis'
        )
        sanm = pipeline(
                model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", 
                return_all_scores=True
            )
        try:
            print('*****************************************************ITERATING THE RECORDS FROM THE DATAFRAME*********************************************************')
            for i, j in tqdm(df.iterrows()):
                pos = []
                neu = []
                neg = []
                
                reviews = j['reviews']
                reviews = [item.replace("****", "").replace("\'", "").replace(",", "").replace("\"", "").strip() for item in reviews]
                total_reviews = len(reviews) - 1
                if total_reviews != 0:
                    for each in reviews:
                        result = sanm(each)
                        pos.append(result[0][0]['score'])
                        neu.append(result[0][1]['score'])
                        neg.append(result[0][2]['score'])
                    positive = sum(pos) / len(pos)
                    neutral = sum(neu) / len(neu)
                    negative = sum(neg) / len(neg)
                    df.loc[i, 'Positive'] = positive
                    df.loc[i, 'Neutral'] = neutral
                    df.loc[i, 'Negative'] = negative
                    df.loc[i, 'Total Reviews'] = total_reviews
                else:
                    df.loc[i, 'Positive'] = 0
                    df.loc[i, 'Neutral'] = 0
                    df.loc[i, 'Negative'] = 0
                    df.loc[i, 'Total Reviews'] = total_reviews
            logging.info(
                'sentiment analysis completed'
            )
            print("**************************************************************************SENTIMENT ANALYSIS COMPLETED****************************************************************")
            return df
        except Exception as e:
            raise CustomException(e, sys)

    def aggregate_review_with_dataframe(self,review_df,df2):
        logging.info(
            'merging the dataframe initiated'
        )
        print("*******************************************************************AGGREGATING THE HOTEL LIST DATAFRAME AND SENTIMENT ANALYSIS******************************************************")
        df3 = pd.merge(review_df, df2, how='inner', on='id')
        print('WE HAVE SUCCESSFULLY MERGED THE SENTIMENT ANALYSIS AND LIST OF HOTELS')
        file_name = input('ENTER THE NAME FOR THIS DATAFRAME FOLLOWED BY .CSV: ')
        full_path=r'C:\Users\ankit\Desktop\HotelList\artifacts\data\{0}'.format(file_name)
        save_dataframe(full_path, df3)
        logging.info('Task of extarcting hotel list, review of each, and sentiment analysis completed')
        print('***************************************************************CONGRATULATION ALL THE TASK COMPLETED******************************************************************')
