from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Project 5 - Docker + ECS Flask Application is running!"

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "Project 5 Docker ECS Flask"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)