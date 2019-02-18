import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


def data(json, type):
    lst = []
    for user in json["user"]:
        lst.append(user[type])
    return lst

if __name__ == "__main__":
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    print('')
    acct = input('Enter Twitter Account:')
    # (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '200'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    type = str(input("Type the type: "))
    print(data(js, type))