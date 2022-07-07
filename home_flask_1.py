import random
import csv
import string

from flask import Flask

app = Flask(__name__)

#choice page
@app.route('/')
def index():
    return '<center><h1>Hello! Make your choice: <a href = "password">password</a>, <a href = "average"> average </a>.</h1></center>'

#passwoerd
@app.route('/password')
def generate_password():
    # this line creates a list of ASCII codes from 33 to 126 (characters, letters, numbers) for 10 to 20 characters
     password = [chr(random.randrange(33, 127)) for _ in range(random.randrange(10, 21))]
     paswwod_check = ''.join(password)
     return f"<center><h2><u>Password lenght {len(password)} symb.</u>:  {paswwod_check}</h2></center>"

#def generate_password():
    #num = random.randrange(10, 21)
    #password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=num))
    #return f"<center><h2><u>Password lenght {len(password)} symb.</u>:  {password}</h2></center>"

#def generate_password():
#   password = []
#   for _ in range(random.randrange(2, 5)):
#       password.append((string.ascii_uppercase)[random.randrange(len(string.ascii_uppercase))])
#       password.append((string.ascii_lowercase)[random.randrange(len(string.ascii_lowercase))])
#   for _ in range(random.randrange(3, 5)):
#       password.append((string.digits)[random.randrange(len(string.digits))])
#       password.append((string.punctuation)[random.randrange(len(string.punctuation))])
#   random.shuffle(password)
#   pas = ''.join(password)
#   return f"<center><h2><u>Password lenght {len(password)} symb.</u>:  {(''.join(password))}</h2></center>"

#average
@app.route('/average')
def get_average_parameters():
   with open("hw.csv", newline='') as file:
       reader = csv.DictReader(file, delimiter=':')
       data = [(row['Index, Height(Inches), Weight(Pounds)']).split(',') for row in reader]
   height = weight = 0.0
   for row in data:
       height += float(row[1])
       weight += float(row[2])
   average_height = round(height/len(data), 2)
   average_weight = round(weight/len(data), 2)
   return f"<center><h2><u>average_height</u> = {average_height} inches, <u>average_weight</u> = {average_weight} pounds.</h2></center>"

#def get_average_parameters():
# with open("hw.csv", newline='') as file:
#     reader = csv.DictReader(file, delimiter=',')
#     count = 0
#     height = weight = 0.0
#     for row in reader:
#         height += float(row[' Height(Inches)'])
#         weight += float(row[' Weight(Pounds)'])
#         count += 1
#     average_height: float = round((height/count), 2)
#     average_weight = round((weight/count), 2)
#     return f"<center><h2><u>average_height</u> = {average_height} inches, <u>average_weight</u> = {average_weight} pounds.</h2></center>"

if __name__ == '__main__':
    app.run(debug=True)
