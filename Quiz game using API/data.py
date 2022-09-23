import requests

parameters = {
    'amount' : 10, 
    'tyoe' : 'boolean'
}
req = requests.get(url = 'https://opentdb.com/api.php?amount=10&type=boolean', params = parameters)
data = req.json()
question_data = data['results']

