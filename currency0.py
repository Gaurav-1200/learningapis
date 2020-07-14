import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=a3b3fc9004011722073fb44f2423df62")
    if res.status_code!=200:
        raise Exception("ERROR IN CONNECTION WITH API")
    data=res.json()
    print (data)

if __name__=="__main__":
    main()