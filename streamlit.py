import streamlit as st
import requests
import datetime
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static



# Définir la fonction qui effectuera la requête API en direct en fonction de la ville 
def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5d4b0fea341a107ff8647f85d7981506".format(city)
    response = requests.get(url)
    data = response.json()
    return data


def main():
    st.title("Application météo en direct")
    city = st.selectbox("Sélectionnez une ville :", ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille",
          "Rennes", "Reims", "Le Havre", "Saint-Etienne", "Toulon", "Grenoble", "Dijon", "Nîmes", "Angers", "Dunkerque"])
    weather_data = get_weather(city)
    st.write("Ville sélectionnée :", city)
    st.write("Température actuelle :", weather_data["main"]["temp"],"C°")
    st.write("Température ressentie :", weather_data["main"]["feels_like"],"C°")
    st.write("Température minimale :", weather_data["main"]["temp_min"],"C°")
    st.write("Température maximale :", weather_data["main"]["temp_max"],"C°")
    st.write("Pression :", weather_data["main"]["pressure"],"hPa")
    st.write("Humidité :", weather_data["main"]["humidity"],"%")
    st.write("Vitesse du vent :", weather_data["wind"]["speed"],"m/s")
    st.write("Direction du vent :", weather_data["wind"]["deg"])
    

    # Convertir l'heure du lever et du coucher de soleil en format date
    sunrise_time = datetime.datetime.fromtimestamp(weather_data["sys"]["sunrise"])
    sunset_time = datetime.datetime.fromtimestamp(weather_data["sys"]["sunset"])
    # Afficher l'heure du lever et du coucher de soleil
    st.write("Lever du soleil :", sunrise_time.strftime('%Y-%m-%d %H:%M:%S'))
    st.write("Coucher du soleil :", sunset_time.strftime('%Y-%m-%d %H:%M:%S'))
    
    # Obtenir les coordonnées de la ville
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    lat = location.latitude
    lon = location.longitude
    
    # Créer une carte interactive avec Folium
    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker(location=[lat, lon], popup=city).add_to(m)
    # Afficher la carte sur Streamlit
    folium_static(m)
    
if __name__ == "__main__":
    main()



