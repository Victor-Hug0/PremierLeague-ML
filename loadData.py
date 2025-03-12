import pandas as pd

def loadDataFrameList():
    
    df0506 = pd.read_csv("premier_league_data/PremierLeague_0506.csv")
    df0607 = pd.read_csv("premier_league_data/PremierLeague_0607.csv")
    df0708 = pd.read_csv("premier_league_data/PremierLeague_0708.csv")
    df0809 = pd.read_csv("premier_league_data/PremierLeague_0809.csv")
    df0910 = pd.read_csv("premier_league_data/PremierLeague_0910.csv")
    df1011 = pd.read_csv("premier_league_data/PremierLeague_1011.csv")
    df1112 = pd.read_csv("premier_league_data/PremierLeague_1112.csv")
    df1213 = pd.read_csv("premier_league_data/PremierLeague_1213.csv")
    df1314 = pd.read_csv("premier_league_data/PremierLeague_1314.csv")
    df1415 = pd.read_csv("premier_league_data/PremierLeague_1415.csv")
    df1516 = pd.read_csv("premier_league_data/PremierLeague_1516.csv")
    df1617 = pd.read_csv("premier_league_data/PremierLeague_1617.csv")
    df1718 = pd.read_csv("premier_league_data/PremierLeague_1718.csv")
    
    dataFramesList = [df0506, df0607, df0708, df0809, df0910, df1011, df1112, df1213, df1314, df1415, df1516, df1617, df1718]
    
    return dataFramesList
