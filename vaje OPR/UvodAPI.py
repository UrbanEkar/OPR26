# slovarji (dictionary)

slovar = {"ključ" : "vrednost",
          "ključ2" : "vrednost2"}
#print(slovar)

#dostop
#print(slovar["ključ"])

#raznoliki slovar

razno = {"stevilo" : 6,
         "ime" : "Urban",
         "seznam" : [1,2,3,4],
         "slovar" : {"firma" : "mercedes", "moč" : "200kw"}}

"""
print(razno["stevilo"] + 10)
print(max(razno["seznam"]))
print(razno["slovar"])
print(razno["slovar"]["firma"])
print(razno["slovar"]["moč"])
"""


# Open Meteo API

import requests
base_url = "https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&daily=rain_sum&timezone=Europe%2FLondon&forecast_days=1"

call = requests.get(base_url).json() #200 - 300 je okej druge stevilke niso spletna stran dotcom-monitor

#print(call)
#print(call["daily"]["rain_sum"][0])

#naloge

#Izpiši trenutno temperaturo.

base_url = "https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&hourly=temperature_2m&current=temperature_2m&timezone=Europe%2FLondon&forecast_days=1"
call = requests.get(base_url).json()

#print(call["current"]["temperature_2m"])


#Izpiši temperature za naslednjih 7 dni.
base_url = "https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&daily=weather_code,temperature_2m_max,temperature_2m_min&hourly=temperature_2m&timezone=Europe%2FLondon"

call = requests.get(base_url).json() #200 - 300 je okej druge stevilke niso spletna stran dotcom-monitor

#print(call["daily"]["time"][0])
#print(call["daily"]["temperature_2m_max"][0])

index = 0

temp = call["daily"]["temperature_2m_max"]

sez = call["daily"]["time"]

print(temp)

index = 0

"""
for s in sez:
    print(f"Dan1: {s}, temperatura: {temp[{index}]}")
    index+= 1

"""

#Ugotovi, kateri dan bo najtoplejši oz. najhladnejši, in izpiši datum ter temperaturo.



#Ugotovi, kateri dan ima največjo razliko med dnevno in nočno temperaturo.





#Med 10 največjimi slovenskimi mesti poišči tisto;
#ki bo danes najtoplejše oz. najhladnejše,
#ki bo imelo najmanj oz. največ dežja,
#ki bo imelo najmanj oz. največ vetra.