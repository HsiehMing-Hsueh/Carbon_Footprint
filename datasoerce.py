import requests
import csv
from io import StringIO


class CarbonFootPrint():
    
    
    @classmethod
    def download_aqi(cls) ->list:
        response = requests.get('https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv')
        
        if response.ok:
            file = StringIO(response.text,newline="")
            csvReader = csv.reader(file)
            next(csvReader)
            
            for item in csvReader:
                print(item[0],item[1],item[3],item[7],item[19],item[37],item[47],item[70])
        else:
            raise Exception("下載失敗")
