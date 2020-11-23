### Python Forex Exchange Rate Scraper
Live URL:
[https://x-rates-exchange.herokuapp.com/latest?base=USD](https://x-rates-exchange.herokuapp.com/latest?base=USD)
<br/>
Python Forex Exchange Rate Scraper uses [x-rates.com](https://www.x-rates.com/) as it's data source.
#### Info
- Default base currency is set to ZAR (South African Rand)
- <b>The date difference should not be longer than one month (request will timeout if date difference is too large </b>

#### Routes
Check if service is running
```
/status
```
Get the latest exchange rates
```
/latest?base=ZAR
```
Get history for a specific date or between two dates
```
/history?base=ZAR&startdate=2020-11-26&enddate=2020-11-30
```
- If the `startdate` is not set, it will default to current date
- If the `enddate` is not set, it will default to `startdate`
- If the `base` is not set, it will default to `ZAR`
- Date format should be `yyyy-mm-dd`
#### Example Response
```
{
  "base": "ZAR",
  "end_at": "2020-11-23",
  "rates": {
    "2020-11-23": {
      "AED": "4.172009",
      "ARS": "0.190672",
      "AUD": "11.235278",
      "BGN": "9.311401",
      "BHD": "40.749206",
      "BND": "11.426897",
      "BRL": "2.847490",
      "BWP": "1.384033",
      "CAD": "11.741433",
      "CHF": "16.850623",
      "CLP": "0.020050",
      "CNY": "2.333320",
      "COP": "0.004217",
      "CZK": "0.691585",
      "DKK": "2.445228",
      "EUR": "18.211517",
      "GBP": "20.481810",
      "HKD": "1.976355",
      "HRK": "2.410503",
      "HUF": "0.050517",
      "IDR": "0.001083",
      "ILS": "4.585223",
      "INR": "0.206828",
      "IRR": "0.000364",
      "ISK": "0.113039",
      "KRW": "0.013773",
      "KWD": "50.112940",
      "KZT": "0.035968",
      "LKR": "0.082686",
      "LYD": "11.305613",
      "MUR": "0.382207",
      "MXN": "0.766331",
      "MYR": "3.745184",
      "NOK": "1.703658",
      "NPR": "0.128665",
      "NZD": "10.663166",
      "OMR": "39.848378",
      "PHP": "0.317877",
      "PKR": "0.095196",
      "PLN": "4.075851",
      "QAR": "4.209259",
      "RON": "3.736213",
      "RUB": "0.201748",
      "SAR": "4.085787",
      "SEK": "1.783482",
      "SGD": "11.426897",
      "THB": "0.505738",
      "TRY": "1.971227",
      "TTD": "2.258540",
      "TWD": "0.536921",
      "USD": "15.321701",
      "VEF": "1.534088",
      "YEN": "0.147744",
      "ZAR": "1.00"
    }
  },
  "start_at": "2020-11-23"
}
```
#### List of available currencies
| Name  | Code |
| ------------- | ------------- |
| Argentine Peso | ARS |
| Australian Dollar | AUD |
| Bahraini Dinar | BHD |
| Botswana Pula | BWP |
| Brazilian Real | BRL |
| Bruneian Dollar | BND |
| Bulgarian Lev | BGN |
| Canadian Dollar | CAD |
| Chilean Peso | CLP |
| Chinese Yuan Renminbi | CNY |
| Colombian Peso | COP |
| Croatian Kuna | HRK |
| Czech Koruna | CZK |
| Danish Krone | DKK |
| Euro | EUR |
| Hong Kong Dollar | HKD |
| Hungarian Forint | HUF |
| Icelandic Krona | ISK |
| Indian Rupee | INR |
| Indonesian Rupiah | IDR |
| Iranian Rial | IRR |
| Israeli Shekel | ILS |
| Japanese Yen | YEN |
| Kazakhstani Tenge | KZT |
| South Korean Won | KRW |
| Kuwaiti Dinar | KWD |
| Libyan Dinar | LYD |
| Malaysian Ringgit | MYR |
| Mauritian Rupee | MUR |
| Mexican Peso | MXN |
| Nepalese Rupee | NPR |
| New Zealand Dollar | NZD |
| Norwegian Krone | NOK |
| Omani Rial | OMR |
| Pakistani Rupee | PKR |
| Philippine Peso | PHP |
| Polish Zloty | PLN |
| Qatari Riyal | QAR |
| Romanian New Leu | RON |
| Russian Ruble | RUB |
| Saudi Arabian Riyal | SAR |
| Singapore Dollar | SGD |
| South African Rand | ZAR |
| Sri Lankan Rupee | LKR |
| Swedish Krona | SEK |
| Swiss Franc | CHF |
| Taiwan New Dollar | TWD |
| Thai Baht | THB |
| Trinidadian Dollar | TTD |
| Turkish Lira | TRY |
| Emirati Dirham | AED |
| British Pound | GBP |
| US Dollar | USD |
| Venezuelan Bolivar | VEF |
