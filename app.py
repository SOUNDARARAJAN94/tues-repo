from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Jenkins + Docker + Python CI/CD"

@app.route("/health")
def health():
    return "Application is Running Successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
