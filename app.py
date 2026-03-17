from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Vidya Kaarthika A"
    roll = "2023bcs0093"

    return render_template("index.html", name=name, roll=roll)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)