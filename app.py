from flask import Flask, request
import requests

app = Flask(__name__)


def get_weather():
    params = {"access_key": "86a3fe972756lk34a6a042bll348b1e3", "query": "Moscow"}
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return f"Сейчас в Москве {api_response['current']['temperature']} градусов"


def send_message(chat_id, text):
    method = "sendMessage"
    token = "840446984:AAFuVTW-FYP5tJVu8mqhc9y4E0j1fr2lCD0"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
        chat_id = request.json["message"]["chat"]["id"]
        weather = get_weather()
        send_message(chat_id, weather)
    return {"ok": True}


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1', debug=True)
