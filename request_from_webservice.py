import codecs
import requests
import json
from requests.exceptions import HTTPError


def main():
    with codecs.open('input.json', 'r', encoding="utf-8") as file:
        data = json.load(file)

    url = "http://localhost:5000/sample-web-service1/?epsilon=0.3&thresh=1"
    headers = {'content-type': 'application/json'}

    try:
        response = requests.post(url, data=data, headers=headers)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Error: {err}')

    response_json = response.json()
    with open('output.json', 'w') as outfile:
        json.dump(response_json, outfile)

    print('done')


if __name__ == '__main__':
    main()
