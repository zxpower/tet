import sys
import requests
from lxml import html

LOGIN_URL = "https://connect.tet.lv/authorize?response_type=code&redirect_uri=https%3A%2F%2Fmans.tet.lv%2Fmytet%2Fconnect&client_id=mltc&state=L215dGV0Lw%3D%3D&scope=openid&lang=lv"

def fetch_daily_consumption(y, m, d, session, client, meter):
    fromDate = f'{y}-{m}-{d}'
    url = f"https://mans.tet.lv/myltc/api/electricity/chart?object_id={meter}&start_date={fromDate}&type=H&client_id={client}&display=kWh"

    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9,lv;q=0.8",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "referer": url,
    }
    response = session.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()
    else:
        print('Something went wrong! HTTP', response.status_code)
        return None

def get_auth_token(session):
    # Get login csrf token
    response = session.get(LOGIN_URL)
    if response.status_code == 200:
        tree = html.fromstring(response.text)
        authenticity_token = list(set(tree.xpath("//input[@name='login[_token]']/@value")))[0]
        return authenticity_token
    else:
        print('Something went wrong! HTTP', response.status_code)


def authenticate(username, password, token, session):
    # Create payload
    payload = {
        "login[username]": username,
        "login[password]": password,
        "login[facebook_id]": "",
        "login[apple_id]": "",
        "login[_token]": token
    }

    # Perform login
    response = session.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    if response.status_code == 200:
        return True
    else:
        print('Something went wrong! HTTP', response.status_code)
    

def main(username, password, year, month, day, client_id, object_id):
    session = requests.session()

    token = get_auth_token(session)
    authenticate(username, password, token, session)

    result = fetch_daily_consumption(year, month, day, session, client_id, object_id)
    print(result)

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 7:
        username = args[1]
        password = args[2]
        year = args[3]
        month = args[4]
        day = args[5]
        client_id = args[6]
        object_id = args[7]

        main(username, password, year, month, day, client_id, object_id)
    else:
        print('No input parameters specified!')
