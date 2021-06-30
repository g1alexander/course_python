import json

country = []
countries_count = []
visa_count = []
countries = []

with open("SalesJan2009.csv", "r") as excel:
    for row in excel:
        if "Visa" in row:
            country.append(row.split(",")[7])

for n in range(len(country)):
    if country[n] not in countries_count:
        countries_count.append(country[n])
        visa_count.append(country.count(country[n]))
   

for c in range(len(visa_count)):
    countries.append({"country": countries_count[c], "cards": visa_count[c]})

#  print(countries) #ejercicio profe

# pruebas ------

Json =  json.dumps(countries)

print(Json)