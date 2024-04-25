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
    print(request.args)
    quote_data = get_quote(category)
    if category == "" and len(quote_data) != 0:
        return render_template("index.html")

    if len(quote_data) == 0:
        return render_template("quote-not-found.html")
    
    return render_template(
        "quote.html",
        keyword = quote_data[0]["category"].capitalize(),
        quote = quote_data[0]["quote"],
        author = quote_data[0]["author"]
    )

if __name__ == "__main__":
   serve(app, host="0.0.0.0", port=7000)
