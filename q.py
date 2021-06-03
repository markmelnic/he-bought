from time import sleep
from requests import get
from playsound import playsound

previous = 0
while True:
    volume = get("https://horizon.stellar.org/accounts/GDLB4PPVRRLG3K7GK3JOSYQNJHWKF6KLDMEU3L6PDQRKLR43CDNTV4P3").json()
    for c in volume["balances"]:
        if c["asset_code"] == "PIPO":
            volume = float(c["balance"])
            break

    if previous != volume:
        playsound('he_bought.mp3')
        previous = volume

    sleep(120)
