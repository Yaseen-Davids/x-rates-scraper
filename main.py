import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
from flask_cors import CORS

currencyNames = {
  'Argentine Peso': { 'code': 'ARS' },
  'Australian Dollar': {'code': 'AUD'},
  'Bahraini Dinar': { 'code': 'BHD' },
  'Botswana Pula': { 'code': 'BWP' },
  'Brazilian Real': { 'code': 'BRL' },
  'Bruneian Dollar': { 'code': 'BND' },
  'Bulgarian Lev': { 'code': 'BGN' },
  'Canadian Dollar': { 'code': 'CAD' },
  'Chilean Peso': { 'code': 'CLP' },
  'Chinese Yuan Renminbi': { 'code': 'CNY' },
  'Colombian Peso': { 'code': 'COP' },
  'Croatian Kuna': { 'code': 'HRK' },
  'Czech Koruna': { 'code': 'CZK' },
  'Danish Krone': { 'code': 'DKK' },
  'Euro': { 'code': 'EUR' },
  'Hong Kong Dollar': { 'code': 'HKD' },
  'Hungarian Forint': { 'code': 'HUF' },
  'Icelandic Krona': { 'code': 'ISK' },
  'Indian Rupee': { 'code': 'INR' },
  'Indonesian Rupiah': { 'code': 'IDR' },
  'Iranian Rial': { 'code': 'IRR' },
  'Israeli Shekel': { 'code': 'ILS' },
  'Japanese Yen': { 'code': 'YEN' },
  'Kazakhstani Tenge': { 'code': 'KZT' },
  'South Korean Won': { 'code': 'KRW' },
  'Kuwaiti Dinar': { 'code': 'KWD' },
  'Libyan Dinar': { 'code': 'LYD' },
  'Malaysian Ringgit': { 'code': 'MYR' },
  'Mauritian Rupee': { 'code': 'MUR' },
  'Mexican Peso': { 'code': 'MXN' },
  'Nepalese Rupee': { 'code': 'NPR' },
  'New Zealand Dollar': { 'code': 'NZD' },
  'Norwegian Krone': { 'code': 'NOK' },
  'Omani Rial': { 'code': 'OMR' },
  'Pakistani Rupee': { 'code': 'PKR' },
  'Philippine Peso': { 'code': 'PHP' },
  'Polish Zloty': { 'code': 'PLN' },
  'Qatari Riyal': { 'code': 'QAR' },
  'Romanian New Leu': { 'code': 'RON' },
  'Russian Ruble': { 'code': 'RUB' },
  'Saudi Arabian Riyal': { 'code': 'SAR' },
  'Singapore Dollar': { 'code': 'SGD' },
  'South African Rand': { 'code': 'ZAR' },
  'Sri Lankan Rupee': { 'code': 'LKR' },
  'Swedish Krona': { 'code': 'SEK' },
  'Swiss Franc': { 'code': 'CHF' },
  'Taiwan New Dollar': { 'code': 'TWD' },
  'Thai Baht': { 'code': 'THB' },
  'Trinidadian Dollar': { 'code': 'TTD' },
  'Turkish Lira': { 'code': 'TRY' },
  'Emirati Dirham': { 'code': 'AED' },
  'British Pound': { 'code': 'GBP' },
  'US Dollar': { 'code': 'USD' },
  'Venezuelan Bolivar': { 'code': 'VEF' }
}

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def status():
  return jsonify(status="API IS RUNNING")


@app.route("/history")
def history():
  base = request.args.get("base")
  startDate = request.args.get("startdate")
  endDate = request.args.get("enddate")

  if base == None:
    base = "ZAR"
  
  if startDate == None:
    startDate = datetime.today().strftime("%Y-%m-%d")

  if endDate == None:
    endDate = startDate

  formatStartDate = datetime.strptime(startDate, "%Y-%m-%d")
  formatEndDate = datetime.strptime(endDate, "%Y-%m-%d")

  obj = {}
  rates = {}

  while formatStartDate <= formatEndDate:
    URL = "https://www.x-rates.com/historical/?from=" + base + "&amount=1&date=" + formatStartDate.strftime("%Y-%m-%d")

    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")

    table = soup.find("table", attrs={"class":"tablesorter ratesTable"})
    table_body = table.find("tbody")

    vals = {}

    rows = table_body.find_all("tr")
    for row in rows:
      cols = row.find_all("td")
      cols = [ele.text.strip() for ele in cols]
      vals[currencyNames[cols[0]]['code']] = cols[2]

    vals["ZAR"] = "1.00"

    rates[formatStartDate.strftime("%Y-%m-%d")] = vals

    formatStartDate = formatStartDate + timedelta(days=1)

  obj['base'] = base
  obj['start_at'] = startDate
  obj['end_at'] = endDate
  obj['rates'] = rates

  return jsonify(obj)


@app.route("/latest")
def latestrates():
  base = request.args.get("base")
  date = datetime.today().strftime("%Y-%m-%d")

  if base == None:
    base = "ZAR"  

  URL = "https://www.x-rates.com/historical/?from=" + base + "&amount=1&date=" + date

  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")

  obj = {}
  rates = {}
  table = soup.find("table", attrs={"class":"tablesorter ratesTable"})
  table_body = table.find("tbody")

  rows = table_body.find_all("tr")
  for row in rows:
      cols = row.find_all("td")
      cols = [ele.text.strip() for ele in cols]
      rates[currencyNames[cols[0]]['code']] = cols[2]

  # insert ZAR
  rates["ZAR"] = "1.00"
  
  obj['base'] = base
  obj['date'] = date
  obj['rates'] = rates

  return jsonify(obj)


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(debug=True, host="0.0.0.0", port=port)
