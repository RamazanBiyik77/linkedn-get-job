
from flask import Flask, Response, abort, g, request
import json
import os, functools
from linkedin_api import Linkedin
import crypt, secrets
from threading import Thread
from threading import Lock
from requests.cookies import cookiejar_from_dict
app = Flask(__name__)
api_key = os.environ.get('api-key')
email = os.environ.get('linkedn_email')
password = os.environ.get('linkedn_password')

cookies = cookiejar_from_dict(
    {
        "liap": "true",
        "li_at": os.environ["LINKEDIN_COOKIE_LI_AT"],
        "JSESSIONID": os.environ["LINKEDIN_COOKIE_JSESSIONID"],
    }
)

def logging_decorator(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        return f(*args, **kwargs)

    return decorator

# Authentication decorator
def token_required(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'X-Access-Token' in request.headers:
            token = request.headers['X-Access-Token']
        if not token or token!=api_key: # throw error if no token provided or access key not matched
            abort(Response("You are not authorized to access this application.", 401))
        return f(*args, **kwargs)
    return decorator

@app.route('/', methods=['GET'])
@logging_decorator
@token_required
def getJobDetail():
    req_data=request.get_json()
    api = Linkedin('','', cookies=cookies)
    connection = api.get_job(job_id=req_data['id'])
    return connection['description']['text']
 
if __name__ == '__main__':
    app.run()