import pandas as pd
import numpy as np
from loadData import loadDataFrameList
from teamMapping import standardize_team_names

dfs = loadDataFrameList()
processed_dfs = []

for df in dfs:
    teamsRatingFifa = pd.read_csv("TeamsOverInfo/TeamsOverInfo.csv")
    currentSeason = df["season"].unique()[0]
    
    teamsRatingFifa4Season = teamsRatingFifa[teamsRatingFifa["Season"] == currentSeason]
    
    df = standardize_team_names(df, team_columns=['HomeTeam', 'AwayTeam'])
    teamsRatingFifa4Season = standardize_team_names(teamsRatingFifa4Season, team_columns=['Name'])
    
    df['MHTGD'] = df.apply(lambda row: row['FTHG'] - row['FTAG'], axis=1)
    df['MATGD'] = df.apply(lambda row: row['FTAG'] - row['FTHG'], axis=1)
    
    df["OverHome"] = np.nan
    df["OverAway"] = np.nan
    df["AttOverHome"] = np.nan
    df["AttOverAway"] = np.nan
    df["MidOverHome"] = np.nan
    df["MidOverAway"] = np.nan
    df["DefOverHome"] = np.nan
    df["DefOverAway"] = np.nan
    df["GoalsDiffHome"] = np.nan
    df["GoalsDiffAway"] = np.nan
    
    teamsSeason = sorted(df["HomeTeam"].unique(), key=str.lower)
    
    for i in range(len(teamsSeason)):
        team = teamsSeason[i]
        teamGames = df[(df["HomeTeam"] == team) | (df["AwayTeam"] == team)]
        overTeam = teamsRatingFifa4Season[teamsRatingFifa4Season["Name"] == team]
    
        overall = overTeam["Overall"].values[0]
        attack = overTeam["Attack"].values[0]
        midfield = overTeam['Midfield'].values[0]
        defense = overTeam['Defense'].values[0]
        
        gameIndex = teamGames.index.tolist()
        
        homeGameIndex = []
        awayGameIndex = []
        goalsDiffPerGame = []
        goalsDiffCumulative = []
        
        for i, r in teamGames.iterrows():
            if team == r["HomeTeam"]:
                homeGameIndex.append(i)
                goalsDiffPerGame.append(r["MHTGD"])
            elif team == r["AwayTeam"]:
                awayGameIndex.append(i)
                goalsDiffPerGame.append(r["MATGD"])
                
        goalsDiffCumulative = [0]
        goalsDiffAfterFirstMatch = [sum(goalsDiffPerGame[:i]) for i in range(1, len(gameIndex)+1)]
        goalsDiffCumulative += goalsDiffAfterFirstMatch
                
        for m in range(len(gameIndex)):
            if gameIndex[m] in homeGameIndex:
                df.loc[gameIndex[m], "OverHome"] = overall
                df.loc[gameIndex[m], "AttOverHome"] = attack
                df.loc[gameIndex[m], "MidOverHome"] = midfield
                df.loc[gameIndex[m], "DefOverHome"] = defense
                df.loc[gameIndex[m], "GoalsDiffHome"] = goalsDiffCumulative[m]
            elif gameIndex[m] in awayGameIndex:
                df.loc[gameIndex[m], "OverAway"] = overall
                df.loc[gameIndex[m], "AttOverAway"] = attack
                df.loc[gameIndex[m], "MidOverAway"] = midfield
                df.loc[gameIndex[m], "DefOverAway"] = defense
                df.loc[gameIndex[m], "GoalsDiffAway"] = goalsDiffCumulative[m]
    
    
    df["DiffOverall"] = df.apply(lambda r: r["OverHome"] - r["OverAway"], axis=1)
    df["DiffAttack"] = df.apply(lambda r: r["AttOverHome"] - r["AttOverAway"], axis=1)
    df["DiffMidfield"] = df.apply(lambda r: r["MidOverHome"] - r["MidOverAway"], axis=1)
    df["DiffDefense"] = df.apply(lambda r: r["DefOverHome"] - r["DefOverAway"], axis=1)
    df["GoalsDiff"] = df.apply(lambda r: r["GoalsDiffHome"] - r["GoalsDiffAway"], axis=1)
    
    processed_dfs.append(df)

full_data = pd.concat(processed_dfs, ignore_index=True)
full_data.to_csv("./fullData.csv", sep=",", index=False)