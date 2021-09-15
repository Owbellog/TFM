import db
import numpy as np
from flask import Flask
from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle
from json import JSONEncoder
from pandas import json_normalize
import json
import os



class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

app = Flask(__name__)


@app.route('/query-example')
def query_example():

    
   
    age = request.args.get('age')
    job = request.args.get('job')
    marital = request.args.get('marital')
    education = request.args.get('education')
    default = request.args.get('default')
    housing = request.args.get('housing')
    loan = request.args.get('loan')
    contact = request.args.get('contact')
    month = request.args.get('month')
    day_of_week = request.args.get('day_of_week')
    duration = request.args.get('duration')
    campaign = request.args.get('campaign')
    pdays = request.args.get('pdays')
    previous = request.args.get('previous')
    poutcome = request.args.get('poutcome')
    empvarrate = request.args.get('empvarrate')
    conspriceidx = request.args.get('conspriceidx')
    consconfidx = request.args.get('consconfidx')
    euribor3m = request.args.get('euribor3m')
    nremployed = request.args.get('nremployed')
    id = request.args.get('id')


    payload = '{'
    payload = payload + f'"age":{age}'
    payload = payload + f',"job":{job}'
    payload = payload + f',"marital":{marital}'
    payload = payload + f',"education":{education}'
    payload = payload + f',"default":{default}'
    payload = payload + f',"housing":{housing}'
    payload = payload + f',"loan":{loan}'
    payload = payload + f',"contact":{contact}'
    payload = payload + f',"month":{month}'
    payload = payload + f',"day_of_week":{day_of_week}'
    payload = payload + f',"duration":{duration}'
    payload = payload + f',"campaign":{campaign}'
    payload = payload + f',"pdays":{pdays}'
    payload = payload + f',"previous":{previous}'
    payload = payload + f',"poutcome":{poutcome}'
    payload = payload + f',"empvarrate":{empvarrate}'
    payload = payload + f',"conspriceidx":{conspriceidx}'
    payload = payload + f',"consconfidx":{consconfidx}'
    payload = payload + f',"euribor3m":{euribor3m}'
    payload = payload + f',"nremployed":{nremployed}'
    payload = payload + '}'
    
    path = os.path.dirname(os.path.abspath(__file__)) 
    filename = f'{path}\\model2.pickel'
    loaded_model = pickle.load(open(filename, 'rb'))
    info = json.loads(payload)
    
    df = json_normalize(info)
    pl = loaded_model.predict(df)
    pk = np.append(pl,id)
    l =  json.dumps(pk, cls=NumpyArrayEncoder)
    return l


if __name__ == '__main__':
    app.run(debug=True, port=5001)