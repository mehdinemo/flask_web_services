#!flask/bin/python
from sample_clase import SampleClass

import traceback
from flask import Flask, request, jsonify
import codecs
import json

app = Flask(__name__, static_url_path='')

with codecs.open('app.config.json', 'r', encoding="utf-8") as file:
    config = json.load(file)

core_numbers = config["core_numbers"]
clm = SampleClass("this is a test", core_numbers)


@app.route('/sample-web-service1/', methods=['POST'])
def sample_web_service1():
    # دریافت پارامترها از body
    data = request.get_json()
    if data is None:
        return jsonify('No data is provided!')

    # دریافت پارامترها از uri
    # معادل با
    # [FromUri]Input_structure input در C#
    epsilon = request.args.get('epsilon')
    if epsilon is None:
        epsilon = 0.9
    else:
        epsilon = float(epsilon)

    thresh = request.args.get('thresh')
    if thresh is None:
        thresh = 2
    else:
        thresh = int(thresh)

    try:
        result = clm.method1(data["nodes"], data["edges"], epsilon)
        return jsonify(result)
    except Exception as ex:
        error = {}
        error["message"] = str(ex)
        error["traceback"] = traceback.format_exc()
        return jsonify(error)


@app.route('/', methods=['POST'])
def index():
    return clm.print_test("Hello, World!")


if __name__ == '__main__':
    app.run(debug=True)
