from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_azure():
    return "<h1>Hello, Azure!</h1><p>Welcome to my Azure Web App!</p>"

if __name__ == '__main__':
    app.run(debug=True)
