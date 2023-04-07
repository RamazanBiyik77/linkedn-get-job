
from flask import Flask
from flask import request
import json
from linkedin_api import Linkedin

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getJobDetail():
    api = Linkedin('<usename>', '<passwd>')
    connection = api.get_job(job_id=req_data['id'])
    req_data=request.get_json()
    return connection['description']['text']
 
if __name__ == '__main__':
    app.run()