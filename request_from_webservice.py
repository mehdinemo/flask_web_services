import requests
import json
from requests.exceptions import HTTPError
from config import config


def main():
    with open('input.json', 'r', encoding="utf-8") as file:
        data = json.load(file)

    epsilon = config['epsilon']
    thresh = config['thresh']
    url = config['url']
    url = url.format(epsilon, thresh)
    headers = {'content-type': 'application/json'}

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Error: {err}')

    response_json = response.json()
    with open('output.json', 'w') as outfile:
        json.dump(response_json, outfile)

    for k, v in response_json.items():
        print(k, ":", v)


if __name__ == '__main__':
    main()
