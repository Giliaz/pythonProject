import csv

from flask import Flask, request, jsonify, Response, render_template
from webargs import validate, fields
from webargs.flaskparser import use_kwargs

from faker import Faker
faker_instance = Faker("EN")

app = Flask(__name__)


@app.route("/")
def start_page():
    return "<p>Start page....</p>"

@app.route('/csv')
@use_kwargs({"row": fields.Int(missing=10, validate=[validate.Range(min=1, max=1000)]), }, location="query")
def generate_password(row):
    with open("person.csv", 'w', encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(['first_name', 'last_name', 'email', 'password', 'date_of_birth'])
        for _ in range(row):
            person = []
            person.append(faker_instance.first_name())
            person.append(faker_instance.last_name())
            person.append(faker_instance.email())
            person.append(faker_instance.password())
            person.append(faker_instance.date_of_birth(minimum_age=20, maximum_age=70).strftime("%m.%d.%Y"))
            writer.writerow(person)
    with open("person.csv", encoding='utf8', newline='') as csvfile:
          return render_template("s3_csv_table.html", csv=csvfile)


if __name__ == '__main__':
    app.run(debug=True)
