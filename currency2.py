import requests

def main():
    amount=int(input("Amount "))
    source =input("Currency to be converted ")
    other=input("EUR to be Converted to ")
    res = requests.get("http://data.fixer.io/api/latest?access_key=a3b3fc9004011722073fb44f2423df62")
    if res.status_code!=200:
        raise Exception("ERROR IN CONNECTION WITH API")
    data=res.json()
    rate1=data["rates"][source]
    rate2=data["rates"][other]
    print(f"{amount} {source}  is equal to  {rate2*amount/rate1} {other}")

if __name__=="__main__": 
    main()