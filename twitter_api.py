import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


def data_search(json, type):

    lst = []
    for user in json["users"]:
        lst.append([user["name"], user[type]])
    return lst


def data_name(name):
    
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': name, 'count': '200'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    return js


if __name__ == "__main__":
    print('')
    acct = input('Enter Twitter Account:')
    type = input("Type that you want to see from the users info : ")
    js = data_name(acct)
    print(data_search(js, type))
