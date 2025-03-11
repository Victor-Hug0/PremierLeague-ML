import os
import pandas as pd
import requests
from io import StringIO

base_url = "https://www.football-data.co.uk/mmz4281/{season}/E0.csv"
seasons = [f"{y-2000:02}{(y+1)-2000:02}" for y in range(2005, 2018)]

os.makedirs("premier_league_data", exist_ok=True)

dataFrames = []

for season in seasons:
    season_url = base_url.format(season=season)
    print(f"Temporada {season} -> {season_url}")
    
    try:
        response = requests.get(season_url)
        response.raise_for_status()
        
        dataFrame = pd.read_csv(StringIO(response.text), on_bad_lines="skip")
        formatted_season = f"20{season[:2]}-20{season[2:]}"
        dataFrame["season"] = formatted_season
        
        dataFrames.append(dataFrame)
        
        path = f"premier_league_data/PremierLeague_{season}.csv"
        dataFrame.to_csv(path, index=False)
        print(f"Salvo em {path}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar {season_url}: {e}")
        
if dataFrames:
    full_data = pd.concat(dataFrames, ignore_index=True)
    full_data.to_csv("premier_league_data/PremierLeague_All_Seasons.csv", index=False)
    print("Todos os dados foram salvos no arquivo: premier_league_data/PremierLeague_All_Seasons.csv")