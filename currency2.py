import requests

def main():
    other=input("EUR to be Converted to ")
    res = requests.get("http://data.fixer.io/api/latest?access_key=a3b3fc9004011722073fb44f2423df62")
    if res.status_code!=200:
        raise Exception("ERROR IN CONNECTION WITH API")
    data=res.json()
    rate=data["rates"][other]
    print(f"1 EUR  is equal to{rate} {other}")

if __name__=="__main__":
    main()