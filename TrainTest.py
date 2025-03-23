import pandas as pd

def trainTestSplit():

    df = pd.read_csv("fullData.csv")

    bettingStats = ["B365H","B365D","B365A","BWH","BWD","BWA","GBH","GBD","GBA","IWH","IWD","IWA","LBH","LBD","LBA","SBH","SBD","SBA","WHH","WHD","WHA","SJH","SJD","SJA","VCH","VCD","VCA","Bb1X2","BbMxH","BbAvH","BbMxD","BbAvD","BbMxA","BbAvA","BbOU","BbMx>2.5","BbAv>2.5","BbMx<2.5","BbAv<2.5","BbAH","BbAHh","BbMxAHH","BbAvAHH","BbMxAHA","BbAvAHA"]
    bettingStatsEx = ["BSH", "BSD", "BSA", "PSA", "PSH", "PSD", "PSCA", "PSCD", "PSCH"]
    genDropInfo = ["Div", "Date", "HomeTeam", "AwayTeam", "Referee"]
    nanFeatures = ['GoalsKPP', 'HomeGoalsKPP', 'AwayGoalsKPP', 'CornersKPP', 'HomeCornersKPP', 'AwayCornersKPP', 'ShotsTargetKPP', 'HomeShotTargetKPP', 'AwayShotTargetKPP', 'Streak', 'HomeStreak', 'AwayStreak', 'WeightedStreak', 'HomeWeightedStreak', 'AwayWeightedStreak']
    preDropFeatures = ["FTHG", "FTAG", "HTHG", "HTAG","HTR","MHTGD", "MATGD"]

    df.drop(bettingStats + bettingStatsEx + genDropInfo + preDropFeatures, axis=1, inplace=True)

    seasons = sorted(df['season'].unique())
    dfs = []
 
    for season in seasons:
        tempDF = df[(df['season'] == (season) )]
        tempDF = tempDF.dropna(subset = nanFeatures)
        dfs.append(tempDF)

    df = pd.concat(dfs)

    Y = df[["FTR"]]
    X = df.drop(columns=["FTR"])

    train_mask = X['season'].isin(['2005-2006', '2006-2007', '2007-2008', 
                                   '2008-2009', '2009-2010', '2010-2011', 
                                   '2011-2012', '2012-2013', '2013-2014'])
    test_mask = X['season'].isin(['2014-2015', '2015-2016'])

    XTrain = X[train_mask].copy()
    XTest = X[test_mask].copy()
    YTrain = Y[train_mask].copy()
    YTest = Y[test_mask].copy()

    XTrain = XTrain.drop(columns=['season'])
    XTest = XTest.drop(columns=['season'])

    return XTrain, XTest, YTrain.values.ravel(), YTest.values.ravel()