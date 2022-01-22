# TET Electricity Consumption Scraper

Script to scrape your smart electricity meter consumption data from [Mans TET](https://mans.tet.lv) website.

## Example usage

Example code is included in `main.py` file. To start using script first install necessary packages:

```
$ pip3 install -r requirements.txt
```

Then you can run following command by replacing `username` with your Mans TET portal's username, `password` with your password. Client and object IDs could be obtained from Mans TET [Patēriņa pārskats](https://mans.tet.lv/mytet/mans_tet/Elektriba/Paterina_parskats/) page by inspecting `Lejupielādēt kopsavilkumu` button URL.

```
$ python3 main.py username 'password' 2022 1 1 'clientID' 'objectID'
```

That will give you data for 2022-01-01 that will look something like this:

```
{'cols': [{'id': None, 'label': 'Date', 'pattern': None, 'type': 'date'}, {'id': None, 'label': 'kWh', 'pattern': None, 'type': 'number'}], 'rows': [{'c': [{'v': 'Date(2022, 01, 01, 01)', 'f': '01.01.2022 01:00'}, {'v': '1.08', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 02)', 'f': '01.01.2022 02:00'}, {'v': '1.03', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 03)', 'f': '01.01.2022 03:00'}, {'v': '0.99', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 04)', 'f': '01.01.2022 04:00'}, {'v': '0.84', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 05)', 'f': '01.01.2022 05:00'}, {'v': '0.89', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 06)', 'f': '01.01.2022 06:00'}, {'v': '0.83', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 07)', 'f': '01.01.2022 07:00'}, {'v': '0.90', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 08)', 'f': '01.01.2022 08:00'}, {'v': '0.91', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 09)', 'f': '01.01.2022 09:00'}, {'v': '0.94', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 10)', 'f': '01.01.2022 10:00'}, {'v': '1.15', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 11)', 'f': '01.01.2022 11:00'}, {'v': '1.06', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 12)', 'f': '01.01.2022 12:00'}, {'v': '0.99', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 13)', 'f': '01.01.2022 13:00'}, {'v': '0.92', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 14)', 'f': '01.01.2022 14:00'}, {'v': '0.95', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 15)', 'f': '01.01.2022 15:00'}, {'v': '1.12', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 16)', 'f': '01.01.2022 16:00'}, {'v': '1.27', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 17)', 'f': '01.01.2022 17:00'}, {'v': '1.30', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 18)', 'f': '01.01.2022 18:00'}, {'v': '1.35', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 19)', 'f': '01.01.2022 19:00'}, {'v': '1.34', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 20)', 'f': '01.01.2022 20:00'}, {'v': '1.42', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 21)', 'f': '01.01.2022 21:00'}, {'v': '1.48', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 22)', 'f': '01.01.2022 22:00'}, {'v': '1.43', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 01, 23)', 'f': '01.01.2022 23:00'}, {'v': '1.68', 'f': None}]}, {'c': [{'v': 'Date(2022, 01, 02, 00)', 'f': '02.01.2022 00:00'}, {'v': '1.76', 'f': None}]}]}
```
