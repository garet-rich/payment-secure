from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  
  return render_template('index.html')

@app.route('/create_card', methods=['POST'])
def create_card():

  card_num = request.form["card_num"]
  exp_date = request.form["exp_date"]
  cvv = request.form["cvv"]

  return render_template('create.html', card_num=card_num, exp_date=exp_date, cvv=cvv)

@app.route('/store_card', methods=['POST'])
def store_card():
  card_num = request.form["card_num"]
  exp_date = request.form["exp_date"]
  cvv = request.form["cvv"]

  os.environ['HTTPS_PROXY'] = 'https://tntivucxwfw.sandbox.verygoodproxy.com'
  res = requests.post('https://echo.apps.verygood.systems/post',
                         json = {'card_num':card_num, 'exp_date':exp_date, 'cvv':cvv},
                         verify='path/to/sandbox.pem')
  
  res = res.json()

  return render_template('store.html', response=res)

if __name__ == '__main__':
  app.run()