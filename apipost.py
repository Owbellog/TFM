import requests
import json
from json import JSONEncoder
import numpy as np


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

age = 51
job = 6
marital = 1 
education = 5
default = 2
housing = 2
loan = 2
contact = 1
month = 0
day_of_week = 0
duration = 0
campaign = 0
pdays = 0
previous = 0
poutcome = 2
empvarrate = 0
conspriceidx = 0
consconfidx = 0
euribor3m = 0
nremployed = 0
id = 36940

payload = f'age={age}'
payload = payload + f'&job={job}'
payload = payload + f'&marital={marital}'
payload = payload + f'&education={education}'
payload = payload + f'&default={default}'
payload = payload + f'&housing={housing}'
payload = payload + f'&loan={loan}'
payload = payload + f'&contact={contact}'
payload = payload + f'&month={month}'
payload = payload + f'&day_of_week={day_of_week}'
payload = payload + f'&duration={duration}'
payload = payload + f'&campaign={campaign}'
payload = payload + f'&pdays={pdays}'
payload = payload + f'&previous={previous}'
payload = payload + f'&poutcome={poutcome}'
payload = payload + f'&empvarrate={empvarrate}'
payload = payload + f'&conspriceidx={conspriceidx}'
payload = payload + f'&consconfidx={consconfidx}'
payload = payload + f'&euribor3m={euribor3m}'
payload = payload + f'&nremployed={nremployed}'
payload = payload + f'&id={id}'


#print(payload)
url = 'http://127.0.0.1:5001/query-example'

# response = requests.request("POST", url, data = payload)
response = requests.get(url, params = payload)
rget = str(response.text.encode('utf8')).replace('"','').replace("'","")[1:100]

print(rget)

# f =json.loads(rget)
# print(f)

decodedArrays = json.loads(rget)
finalNumpyArray = np.asarray(decodedArrays)
print(finalNumpyArray[0])
