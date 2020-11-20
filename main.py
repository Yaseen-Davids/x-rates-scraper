import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def status():
  return jsonify(status='API IS RUNNING')

@app.route('/rates')
def rates():
  base = request.args.get('base')
  date = request.args.get('date')

  if base == None:
    base = 'ZAR'
  
  if date == None:
    date = datetime.today().strftime('%Y-%m-%d')

  URL = "https://www.x-rates.com/historical/?from=" + base + "&amount=1&date=" + date

  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")

  obj = {}
  table = soup.find("table", attrs={"class":"tablesorter ratesTable"})
  table_body = table.find("tbody")

  rows = table_body.find_all("tr")
  for row in rows:
      cols = row.find_all("td")
      cols = [ele.text.strip() for ele in cols]
      obj[cols[0]] = { "rate": cols[1], "inverse": cols[2] }
  
  return jsonify(obj)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
