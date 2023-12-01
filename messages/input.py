from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def send_user_input():
    source = request.form.get('source')
    message = request.form.get('message')

    db_service_url = f'http://192.168.1.152:5000/user'

    user_input = {
        'source': source,
        'message': message
    }

    response = requests.post(db_service_url, data=user_input)

    return render_template('input.html', message=response)


@app.route('/send_user_input')
def index():
    return render_template('input.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
