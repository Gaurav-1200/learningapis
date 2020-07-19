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
@app.route("/detweather", methods=["POST"])
def detweather():
    city=request.form.get("city")
    city_name=city.capitalize()
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=96c644a71bf60305893f8549f63eeb9f'
    res=requests.get(url.format(city))
    data=res.json()
    weather = {
            'city' : city_name,
            'temperature' : data['main']['temp'],
            'description' : data['weather'][0]['description'].capitalize(),
            'icon' : data['weather'][0]['icon'],
            'lon' :data['coord']['lon'],
            'lat' :data['coord']['lat'],
            'country' :data['sys']['country'],'humid' :data['main']['humidity'],
            'pres':data['main']['pressure'],
            'wspeed':(data['wind']['speed']*18)/5,
            'wdir':data['wind']['deg'],
            'min':data['main']['temp_min'],
            'max':data['main']['temp_max']
        }
    return render_template("detail.html",weather=weather)



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
            'description' : data['weather'][0]['main'],
            'icon' : data['weather'][0]['icon'],
            'lon' :data['coord']['lon'],
            'lat' :data['coord']['lat']
        }
        weather_data.append(weather)
    
    return render_template("weather.html",cities=cities,weather_data=weather_data,city=city)

@app.route("/covid")
def covid():
    url='https://api.covidindiatracker.com/total.json'
    res=requests.get(url)
    data=res.json()
    confirmed=data["confirmed"]
    active=data["active"]
    recovered=data["recovered"]
    deaths=data["deaths"]
    cactive=data["aChanges"]
    cconfirmed=data["cChanges"]
    crecovered=data["rChanges"]
    cdeaths=data["dChanges"]

    securl='https://api.covid19api.com/summary'
    sres=requests.get(securl)
    sdata=sres.json()
    wconfirmed=sdata["Global"]["TotalConfirmed"]
    wrecovered=sdata["Global"]["TotalRecovered"]
    wdeaths=sdata["Global"]["TotalDeaths"]
    wactive=wconfirmed-(wrecovered+wdeaths)
    wcconfirmed=sdata["Global"]["NewConfirmed"]
    wcrecovered=sdata["Global"]["NewRecovered"]
    wcdeaths=sdata["Global"]["NewDeaths"]
    wcactive=wcconfirmed-(wcrecovered+wcdeaths)
    


    return render_template("covid.html",confirmed=confirmed,active=active,deaths=deaths,recovered=recovered,cactive=cactive,cconfirmed=cconfirmed,cdeaths=cdeaths,crecovered=crecovered,wconfirmed=wconfirmed,wactive=wactive,wdeaths=wdeaths,wrecovered=wrecovered,wcactive=wcactive,wcconfirmed=wcconfirmed,wcdeaths=wcdeaths,wcrecovered=wcrecovered)



if __name__=="__main__":
    app.run(debug=True)