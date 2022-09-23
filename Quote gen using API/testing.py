import requests
a = -2.976074
b = 104.775429

dic = {
    'lat':a,
    'lng':b,
}
s = requests.get(url = 'https://api.sunrise-sunset.org/json', params = dic)
s.raise_for_status()
