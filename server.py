from flask import Flask, render_template, request
from quote import get_quote
from waitress import serve

app = Flask(__name__)
@app.route("/")
@app.route("/index")

def index():
    return render_template('index.html')

@app.route("/quote")
def new_quote():
    category = request.args.get("category")

    if not bool(category.strip()):
        city = "happiness"

    quote_data = get_quote(category)

    if not quote_data["cod"] == 200:
        return render_template("city-not-found.html")
    
    return render_template(
        "weather.html",
        quote = quote_data[0]["quote"],
        author = quote_data[0]["author"],
    )

if __name__ == "__main__":
   serve(app, host="0.0.0.0", port=7000)
