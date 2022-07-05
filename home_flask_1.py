import re
import random
import csv

from flask import Flask

app = Flask(__name__)

#choice page
@app.route('/')
def index():
    return '<center><h1>Hello! Make your choice: <a href = "password">password</a>, <a href = "average"> average </a>.</h1></center>'

#passwoerd
@app.route('/password')
def generate_password():
    password = ([chr(random.randrange(33, 127)) for _ in range(random.randrange(10, 21))])
    pas_check = ''.join(password)
    return f"<center><h2><u>Password lenght {len(password)} symb.</u>:  {pas_check}</h2></center>"

#  єто я так задолбался в первій раз)))
# password = []
# for _ in range(random.randrange(2, 5)):
#     password.append((string.ascii_uppercase)[random.randrange(len(string.ascii_uppercase))])
#     password.append((string.ascii_lowercase)[random.randrange(len(string.ascii_lowercase))])
# for _ in range(random.randrange(3, 5)):
#     password.append((string.digits)[random.randrange(len(string.digits))])
#     password.append((string.punctuation)[random.randrange(len(string.punctuation))])
# random.shuffle(password)
# pas = ''.join(password)
# return f"<center><h2><u>Password lenght {len(password)} symb.</u>:  {(''.join(password))}</h2></center>"

#average
@app.route('/average')
def get_average_parameters():
    # откріваем файл создаем список из строк файла CSV
    with open("hw.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=':')
        data = [(row['Index, Height(Inches), Weight(Pounds)']).split(',') for row in reader]
    height = weight = 0.0
    # перебираем список и суммируем данные
    for row in data:
        height += float(row[1])
        weight += float(row[2])
    # считаем среднее и округляем до двух знаков после запятой
    average_height = round(height/len(data), 2)
    average_weight = round(weight/len(data), 2)
    return f"<center><h2><u>average_height</u> = {average_height} inches, <u>average_weight</u> = {average_weight} pounds.</h2></center>"

if __name__ == '__main__':
    app.run(debug=True)