from flask import Flask, render_template, jsonify, request
import requests
app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():

        if request.method=="GET":
            currency = "TRY"
            res = requests.get(f"https://api.exchangeratesapi.io/latest?base={currency}")
            ress = requests.get("https://api.exchangeratesapi.io/latest?base=EUR&symbols=TRY")
            resss = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=TRY")
            ressss = requests.get("https://api.exchangeratesapi.io/latest?base=GBP&symbols=TRY")

            data = res.json()
            datas = ress.json()
            datass = resss.json()
            datasss = ressss.json()

            return render_template("index.html", data=data, currency=currency, datas=datas, datass=datass,
                                   datasss=datasss)
        else:
            currency =request.form.get("currency")
            res = requests.get(f"https://api.exchangeratesapi.io/latest?base={currency}")
            ress = requests.get("https://api.exchangeratesapi.io/latest?base=EUR&symbols=TRY")
            resss = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=TRY")
            ressss = requests.get("https://api.exchangeratesapi.io/latest?base=GBP&symbols=TRY")

            data = res.json()
            datas = ress.json()
            datass = resss.json()
            datasss = ressss.json()

            return render_template("index.html", data=data, currency=currency, datas=datas, datass=datass,
                                   datasss=datasss)







@app.route("/convert", methods=["POST","GET"])
def convert():
        if request.method=="GET":
            ress = requests.get("https://api.exchangeratesapi.io/latest?base=EUR&symbols=TRY")
            resss = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=TRY")
            ressss = requests.get("https://api.exchangeratesapi.io/latest?base=GBP&symbols=TRY")
            datas = ress.json()
            datass = resss.json()
            datasss = ressss.json()
            year = 2020
            month = 1
            day = 1
            baz = "TRY"
            convert = "USD"
            date = "2020-01-01"
            history = requests.get(f"https://api.exchangeratesapi.io/{year}-{month}-{day}?base={baz}&symbols={convert}")
            historyy = requests.get(f"https://api.exchangeratesapi.io/latest?base={baz}&symbols={convert}")
            data_history = history.json()
            data_historyy = historyy.json()
            return render_template("convert.html", baz=baz, day=day, year=year, month=month, convert=convert,date=date,datas=datas, datass=datass,
                                   datasss=datasss)

        else:
            ress = requests.get("https://api.exchangeratesapi.io/latest?base=EUR&symbols=TRY")
            resss = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=TRY")
            ressss = requests.get("https://api.exchangeratesapi.io/latest?base=GBP&symbols=TRY")
            datas = ress.json()
            datass = resss.json()
            datasss = ressss.json()
            baz = request.form.get("baz")
            convert = request.form.get("convert")
            year = request.form.get("year")
            month = request.form.get("month")
            day = request.form.get("day")

            history = requests.get(f"https://api.exchangeratesapi.io/{year}-{month}-{day}?base={baz}&symbols={convert}")
            historyy = requests.get(f"https://api.exchangeratesapi.io/latest?base={baz}&symbols={convert}")
            data_history = history.json()
            data_historyy = historyy.json()
            date=data_history["date"]
            sonuç=data_history["rates"][convert]
            sonuç1=data_historyy["rates"][convert]
            deff = " "
            if sonuç1>sonuç:
                percent = (data_historyy["rates"][convert]) / (data_history["rates"][convert]) * 100
                deff = "-"
            else:
                percent = (data_history["rates"][convert]) / (data_historyy["rates"][convert]) * 100
                deff = "+"

            return render_template("convert.html", baz=baz, day=day, year=year, month=month, convert=convert,date=date,sonuç=sonuç,percent=percent,datas=datas,datass=datass,
                                   datasss=datasss,deff=deff)




""" @app.route("/flights/<int:flight_id>")
def flight(flight_id):
  

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")

    # Get all passengers.
    passengers = flight.passengers
    return render_template("flight.html", flight=flight, passengers=passengers)"""



