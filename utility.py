from flask import Flask, render_template,redirect,url_for,request,flash
import os
import requests


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/currency")
def fixer():
    return render_template("results.html")

@app.route("/convert", methods=["GET","POST"])
def convert():
    if request.method == "GET":
        return redirect (url_for('fixer'))
    else:
        amount=float(request.form.get("amount"))
        source=request.form.get("first")
        other=request.form.get("second")
        res= requests.get("http://data.fixer.io/api/latest?access_key=a3b3fc9004011722073fb44f2423df62")
        if res.status_code!=200:
            raise Exception("ERROR IN CONNECTION WITH API")
        data=res.json()
        rate1=float(data["rates"][source])
        rate2=float(data["rates"][other])
        date=data["date"]
        return render_template("results.html", source=source, other=other, rate1=rate1, rate2=rate2, date=date, amount=amount)


@app.route("/weather")
def weather():
    weather_data=[]
    cities=["Delhi","London", "Tokoyo","Faridabad","Sydney","Hyderabad","Munger","Dhanbad"]
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=96c644a71bf60305893f8549f63eeb9f'
    for city in cities:
        surl=url.format(city)
        res=requests.get(surl)
        data=res.json()
        weather = {
            'city' : city,
            'temperature' : data['main']['temp'],
            'description' : data['weather'][0]['description'],
            'icon' : data['weather'][0]['icon'],
            'lon' :data['coord']['lon'],
            'lat' :data['coord']['lat']
        }
        weather_data.append(weather)
    
    return render_template("weather.html",cities=cities,weather_data=weather_data)

@app.route("/Translate")
def translate():
    return render_template("translate.html")



if __name__=="__main__":
    app.run(debug=True)