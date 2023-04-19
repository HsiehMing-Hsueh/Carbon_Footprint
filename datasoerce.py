import requests
import csv
from io import StringIO


class CarbonFootPrint():
    
    API_KEY = "e8dd42e6-9b8b-43f8-991e-b3dee723a52d"
    @classmethod
    def download_aqi(cls) ->list:
        response = requests.get(f'https://data.epa.gov.tw/api/v2/cfp_p_02?api_key={cls.API_KEY}&limit=1000&sort=ImportDate desc&format=CSV')
        
        if response.ok:
            file = StringIO(response.text,newline="")
            csvReader = csv.reader(file)
            next(csvReader)
            for item in csvReader:
                print(item[0])
        else:
            raise Exception("下載失敗")
