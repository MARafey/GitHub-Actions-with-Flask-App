from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello,My name is Muhammad Abdur Rafey and this is my test for the Github Actions"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
