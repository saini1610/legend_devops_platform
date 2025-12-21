from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    os.makedirs("/data", exist_ok=True)
    with open("/data/hits.txt", "a") as f:
        f.write("hit\n")
    return "Legend DevOps App Running"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

