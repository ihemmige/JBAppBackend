from flask import Flask

app = Flask(__name__)

jobs = [
    {"company": "Apple", "title": "Recruiter", "location": "Timbuktu", "salary": 10000}, 
    {"company": "Google", "title": "Software Engineer", "location": "San Francisco", "salary": 20000},
    {"company": "Facebook", "title": "Product Manager", "location": "New York", "salary": 30000},
    {"company": "Amazon", "title": "Data Scientist", "location": "Seattle", "salary": 40000},
    {"company": "Johns Hopkins", "title": "Professor", "location": "Baltimore", "salary": 50000}
  ]

@app.get('/')
def index():
    return {"result":jobs}