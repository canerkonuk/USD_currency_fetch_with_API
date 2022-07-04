

##### LIBRARIES #####
from unittest import result
import requests
import json
import pandas as pd




##### FETCHING JSON DATA WITH FIXER.IO AND API KEY#####

start_date="2021-01-01"
end_date="2021-01-10"

url = f"https://api.apilayer.com/fixer/timeseries?base=USD&start_date={start_date}&end_date={end_date}"
payload = {}
headers= {
  "apikey": "67zlWYzXxM5ziN2H1Yk7awJ2mXjbvx8x"
}

response = requests.request("GET", url, headers=headers, data = payload)
status_code = response.status_code
result = response.text

##### CHANGING JSON DATA TYPE TO DICT TYPE FOR PANDAS USAGE #####
data=json.loads(result)
print(type(data)) ###Output will be dict



##### CREATING DATAFRAME WITH PANDAS #####
DataFrame=pd.json_normalize(data["rates"]).T

#### INDEX CONTAINS DATE AND NAME DATA. SO I AM CHANGING INDEX TO COLUMNS #####
DataFrame["date_rates"]=DataFrame.index
DataFrame.reset_index(inplace=True)


#### ALSO I AM CHANGING COLUMN NAMES TO STR TYPE, BECAUSE DATAFRAME CONTAINS ONE INT TYPE COLUMN NAME #####
DataFrame.columns = DataFrame.columns.astype(str)

#### SPLITTING OLD INDEX DATA COLUMN TO DATE AND NAME COLUMNS AND REMOVING SOME COLUMNS ####
DataFrame[["date","name"]]=DataFrame["date_rates"].str.split('.', expand=True)
DataFrame["value"]=DataFrame["0"]
DataFrame.drop(["index","0","date_rates"] , axis=1, inplace=True)


#### LASTLY CREATING CSV FILE WITHOUT INDEX ####
DataFrame.to_csv("Currency.csv", index=False)


