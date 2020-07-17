import requests

def main():
    url ='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=96c644a71bf60305893f8549f63eeb9f'
    city=input("shehar ")
    url=url.format(city)
    res=requests.get(url)
    data=res.json()
    #print(data)
    print(data["sys"]["country"])


if __name__=="__main__":
    main()