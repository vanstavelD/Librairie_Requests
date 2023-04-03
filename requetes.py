import requests
import pandas as pd
from datetime import datetime

# API endpoint et clé d'API OpenWeather
url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "5d4b0fea341a107ff8647f85d7981506" 

# Liste des villes françaises
cities = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille",
          "Rennes", "Reims", "Le Havre", "Saint-Etienne", "Toulon", "Grenoble", "Dijon", "Nîmes", "Angers", "Dunkerque"]

# Dictionnaire pour stocker les données de chaque ville
data_dict = {
    "Ville": [],
    "Température actuelle": [],
    "Température ressentie": [],
    "Température minimale": [],
    "Température maximale": [],
    "Pression": [],
    "Humidité": [],
    "Vitesse du vent": [],
    "Direction du vent": [],
    "Lever du soleil": [],
    "Coucher du soleil": []
}

# Boucle sur chaque ville pour récupérer les données
for city in cities:
    # Paramètres de la requête
    params = {"q": city + ",FR", "units": "metric", "appid": api_key}

    # Envoie de la requête à l'API OpenWeather
    response = requests.get(url, params=params)

    # Traitement des données de la réponse si la requête a réussi
    if response.status_code == 200:
        data = response.json()
        # Ajout des données à notre dictionnaire
        data_dict["Ville"].append(city)
        data_dict["Température actuelle"].append(data["main"]["temp"])
        data_dict["Température ressentie"].append(data["main"]["feels_like"])
        data_dict["Température minimale"].append(data["main"]["temp_min"])
        data_dict["Température maximale"].append(data["main"]["temp_max"])
        data_dict["Pression"].append(data["main"]["pressure"])
        data_dict["Humidité"].append(data["main"]["humidity"])
        data_dict["Vitesse du vent"].append(data["wind"]["speed"])
        data_dict["Direction du vent"].append(data["wind"]["deg"])
        print(data_dict)
        # Conversion de l'heure du lever/coucher du soleil en une chaîne lisible pour l'homme
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%Y-%m-%d %H:%M:%S')
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%Y-%m-%d %H:%M:%S')
        data_dict["Lever du soleil"].append(sunrise)
        data_dict["Coucher du soleil"].append(sunset)
    else:
        print("erreur")
# Création du DataFrame pandas à partir du dictionnaire
df = pd.DataFrame(data_dict)

# Exportation du DataFrame dans un fichier CSV
df.to_csv("weather_data.csv", index=False)

# Affichage des données
print(df)

