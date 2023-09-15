from flask import Flask, make_response, request
# from flask_smorest import Api, Blueprint
# from schemas import JobSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

jobs = [
    {"company": "Apple", "title": "Recruiter", "location": "Timbuktu", "salary": 10000}, 
    {"company": "Google", "title": "Software Engineer", "location": "San Francisco", "salary": 20000},
    {"company": "Facebook", "title": "Product Manager", "location": "New York", "salary": 30000},
    {"company": "Amazon", "title": "Data Scientist", "location": "Seattle", "salary": 40000},
    {"company": "Johns Hopkins", "title": "Professor", "location": "Baltimore", "salary": 50000}
  ]

@app.get('/jobs')
def index():
  response = make_response({"result": jobs})
  response.headers['Access-Control-Allow-Origin'] = '*'
  return response

@app.post('/jobs')
def create():
  company = request.args.get('company')
  title = request.args.get('title')
  location = request.args.get('location')
  salary = request.args.get('salary')
  jobs.append({"company": company, "title": title, "location": location, "salary": salary})
  response = make_response({"result": jobs})
  response.headers['Access-Control-Allow-Origin'] = '*'
  return response