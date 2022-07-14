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
    return '<h1>Start page....<a href = "csv">csv (?count=..)</a>, <a href = "bitcoin"> bitcoin (?currency=..) </a>, <a href = "bit_symbol"> bit_symbol (?currency=..)</a></h1>'


@app.route('/csv')
@use_kwargs({"count": fields.Int(missing=10, validate=[validate.Range(min=1, max=1000)]), }, location="query")
def generate_password(count):

    with open("person.csv", 'w', encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(['first_name', 'last_name', 'email', 'password', 'date_of_birth'])
        for _ in range(count):
            person = []
            person.append(faker_instance.first_name())
            person.append(faker_instance.last_name())
            person.append(faker_instance.email())
            person.append(faker_instance.password())
            person.append(faker_instance.date_of_birth(minimum_age=20, maximum_age=70).strftime("%m.%d.%Y"))
            writer.writerow(person)

    with open("person.csv", encoding='utf8', newline='') as csvfile:
          return render_template("s3_csv_table.html", csv=csvfile)


@app.route("/bitcoin")
@use_kwargs({"currency": fields.Str(missing='USD'), }, location="query")
def get_bitcoin(currency):
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
            return f"<h1> 1 bitcoin = {entry['rate']} {entry['code']} </h1>"
    return "<h1>This currency is missing !</h1>"


@app.route("/bit_symbol")
@use_kwargs({"currency": fields.Str(missing='USD'), }, location="query")
def bit_symbol(currency):
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
            return f"<h1>{(dict['symbol'])}<h1>"
    return "<h1>This currency symbol is missing !</h1>"


if __name__ == '__main__':
    app.run(debug=True)
