import sqlite3

# Connexion à la base de données (si la base de données n'existe pas, elle sera créée)
connexion = sqlite3.connect("weather.db")

# Création d'un curseur pour exécuter les requêtes SQL
curseur = connexion.cursor()

# Création de la table "weather"
curseur.execute("""
                CREATE TABLE weather (
                    ville TEXT,
                    temperature_actuelle REAL, 
                    temperature_ressentie REAL,
                    temperature_minimale REAL,
                    temperature_maximale REAL,
                    pression REAL,
                    humidite REAL,
                    vitesse_vent REAL,
                    direction_vent REAL,
                    lever_soleil TEXT,
                    coucher_soleil TEXT
                )
                """) # le type de données "REAL" (ou "FLOAT" dans d'autres systèmes de gestion de base de données) est utilisé 
                     #pour stocker des nombres à virgule flottante
                     # les types de données "REAL" et "FLOAT" sont en réalité des alias l'un pour l'autre, ce qui signifie qu'ils sont interchangeables.
                     # Par conséquent, vous pouvez utiliser l'un ou l'autre pour stocker des valeurs décimales dans une base de données SQLite.
                     

# Commit des changements dans la base de données
connexion.commit()

# Fermeture de la connexion et du curseur
curseur.close()
connexion.close()