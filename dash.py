from flask import Flask, request, render_template

app = Flask(__name__)

# Updated with your hosted app links
apps = {
    "Calculator": "https://calculator-0hze.onrender.com",
    "Currency Converter": "https://curr-converter-ddrm.onrender.com",
    "Form": "https://registration-form-50r5.onrender.com",
    "Guessing Game": "https://guessing-game-ukyp.onrender.com",
    "RPS Game": "https://rock-paper-scissor-s9vc.onrender.com",
    "Historical Events": "https://historical-events-app.onrender.com",
    "Crypto Tracker": "https://crypto-price-tracker-5o9b.onrender.com"
}

@app.route("/", methods=["GET", "POST"])
def index():
    iframe_url = None
    if request.method == "POST":
        selected_app = request.form["app"]
        iframe_url = apps[selected_app]

    return render_template("dash.html", apps=apps, iframe_url=iframe_url)

if __name__ == "__main__":
    app.run(debug=False, port=5000)
