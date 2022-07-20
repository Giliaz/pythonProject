import csv
from http import HTTPStatus

import requests
from flask import Flask, jsonify, Response, render_template
from webargs import validate, fields
from webargs.flaskparser import use_kwargs

from faker import Faker
faker_instance = Faker("EN")

app = Flask(__name__)


@app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
@app.errorhandler(HTTPStatus.BAD_REQUEST)
def error_handler(error):
    headers = error.data.get('headers', None)
    messages = error.data.get('messages', ["Invalid request."])
    if headers:
        return jsonify(
            {
                'errors': messages
            },
            error.code,
            headers
        )
    else:
        return jsonify(
            {
                'errors': messages
            },
            error.code,
        )


@app.route("/")
def start_page():
    return '<h3>Start page....<a href = "csv">csv (?count=..)</a>, <a href = "bitcoin"> bitcoin (?currency=..&count=..)</a>.</h3>'


@app.route('/csv')
@use_kwargs({"count": fields.Int(load_default=10, validate=[validate.Range(min=1, max=1000)]), }, location="query")
def generate_csv(count):
    person =[]
    person.append(['first_name', 'last_name', 'email', 'password', 'date_of_birth'])
    for _ in range(count):
        person.append([faker_instance.first_name(), faker_instance.last_name(), faker_instance.email(),
        faker_instance.password(),faker_instance.date_of_birth(minimum_age=20, maximum_age=70).strftime("%m.%d.%Y")])

    with open("person.csv", 'w', encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for line in person:
            writer.writerow(line)

    return (render_template("table_from_list.html", csv=person))


@app.route("/bitcoin")
@use_kwargs({"currency": fields.Str(load_default='USD'), }, location="query")
@use_kwargs({"count": fields.Int(missing=1, validate=[validate.Range(min=1, max=1000)]), }, location="query")
def get_bitcoin(currency, count):
    url = "https://bitpay.com/api/rates"
    result = requests.get(url, {})

    if result.status_code not in (HTTPStatus.OK,):
        return Response(
            "ERROR: Something went wrong",
            status=result.status_code
        )
    result = result.json()
    for entry in result:
        if entry['code'] == currency:

            url = 'https://test.bitpay.com/currencies'
            headers = {'X-Accept-Version': '2.0.0', 'Content-type': 'application/json'}
            response = requests.get(url=url, headers=headers)

            if response.status_code not in (HTTPStatus.OK,):
                return Response(
                    "ERROR: Something went wrong",
                    status=response.status_code
                )
            response = response.json()
            for dict in response['data']:
                if dict['code'] == currency:
                    return f"<h3> {count} bitcoin = {round(entry['rate'] * count, 2)} {entry['code']} {(dict['symbol'])}</h1>"
            return "<h3>This currency symbol is missing !</h3>"
    return "<h3>This currency is missing !</h3>"


if __name__ == '__main__':
    app.run(debug=True)



