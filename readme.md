
## Goibibo Hotel List Extractor and Review Analysis

* A end to end comprohensive data analytics project which leaverage the functionalities of Selenium, request, and BeautifulSoup to automatically extract the list of hotels of any provided location,scrape the reviews of each hotel and perform a detailed sentiment analysis on each review and automatically save the result in excel file. 

### The project consists of the following steps:
The project used modular coding techniques, oops and classes to divide different functionalities into different classes and automate the complete extraction process. It contains classes like-

* Data Ingestion: The user provides a location as input, and the program uses Selenium to automatically open a browser, search for hotels in that location, and extract the list of hotels.
* Hotel List Extraction: The program then iterates through the list of hotels and extracts necessary  details of each hotels
* Review Extraction: For each hotel URL, the program extracts the reviews for that hotel.
* Sentiment Analysis: The program then performs sentiment analysis on the extracted reviews using a hugging face pre trained model.
The project uses a modular approach, with different classes responsible for different functionalities, such as data ingestion, hotel list extraction, review extraction, and sentiment analysis.

### Prerequisites
* Python 3.x
* Selenium
* Requests
* Pandas
* Tensorflow ( for sentiment analysis)
* Keras ( for sentiment analysis)

### Installation
* Clone the repository:
```
git clone https://github.com/your-username/hotel-review-sentiment-analysis.git
```

* Fistly install the dependencies

 ``` 
 pip install -r requirements.txt
  ```

* Run Data Ingestion.py file
``` 
python data_ingestion.py 
```



If you'd like to contribute to this project, please feel free to submit a pull request or open an issue.



