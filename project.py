# KRÜPTOVALUUTADE HINNAD EI VASTA HETKE TURU HINDADELE!!!!!!!!
btc = 16300
btcU = 17000
eth = 1228
ethU = 1282
bnb = 285
bnbU = 299
ltc = 73
ltcU = 77
kogusumma = 0

algus = print("Tere tulemast krüptovaluuta hinna kontrollimis programmi! Hinna teada saamiseks täida järgnevad väljad")
liik = str(input("Mis krüptovaluutat soovid osta?(Kasuta lühendeid) "))
kogus = float(input("Kui palju soovid krüptovaluutat osta? "))
valuuta = str(input("Mis valuutat soovid ostmisel kasutada? "))
if liik == "btc":
   if valuuta == "usd":
        kogusumma = btcU * kogus
        print("Ostuhind oleks hetkel " + str(kogusumma))
   elif valuuta == "eur":
       kogusumma = btc * kogus
       print("Ostuhind oleks hetkel " + str(kogusumma))
   else:
       print("Selles valuutas me hetkel krüptovaluuta hinda ei kontrolli, proovi uuesti kasutades EUR või USD")

elif liik == "eth":
   if valuuta == "usd":
        kogusumma = ethU * kogus
        print("Ostuhind oleks hetkel " + str(kogusumma))
   elif valuuta == "eur":
       kogusumma = eth * kogus
       print("Ostuhind oleks hetkel " + str(kogusumma))
   else:
        print("Selles valuutas me hetkel krüptovaluuta hinda ei kontrolli, proovi uuesti kasutades EUR või USD")
elif liik == "ltc":
    if valuuta == "usd":
        kogusumma = ltcU * kogus
        print("Ostuhind oleks hetkel " + str(kogusumma))
    elif valuuta == "eur":
        kogusumma = ltc * kogus
        print("Ostuhind oleks hetkel " + str(kogusumma))
    else:
        print("Selles valuutas me hetkel krüptovaluuta hinda ei kontrolli, proovi uuesti kasutades EUR või USD")
elif liik == "bnb":
    if valuuta == "usd":
        kogusumma = bnbU * kogus
        print("Ostuhind oleks hetkel " + str(kogusumma))
    elif valuuta == "eur":
        kogusumma = bnb * kogus
        print("Ostuhind oleks hetkel " + str(kogusumma))
    else:
        print("Selles valuutas me hetkel krüptovaluuta hinda ei kontrolli, proovi uuesti kasutades EUR või USD")
else:
    print("Selle krüptovaluuta hinda hetkel jälgida ei saa, proovi uuesti kasutades btc, eth, ltc või bnb ja vaata üle kas sisestasid mida soovid kontrollida")




