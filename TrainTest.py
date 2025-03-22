import pandas as pd
import warnings

warnings.filterwarnings('ignore')

def trainTestSplit():
    try:
        DataFrame = pd.read_csv('./fullData.csv', delimiter=',')

        seasons = [
            '2005-2006', '2006-2007', '2007-2008', '2008-2009', '2009-2010',
            '2010-2011', '2011-2012', '2012-2013', '2013-2014', '2014-2015',
            '2015-2016'
        ]
        
        removedColumns = [
            "B365H", "B365D", "B365A", "BWH", "BWD", "BWA", "IWH", "IWD", "IWA",
            "LBH", "LBD", "LBA", "PSH", "PSD", "PSA", "WHH", "WHD", "WHA",
            "VCH", "VCD", "VCA", "Bb1X2", "BbMxH", "BbAvH", "BbMxD", "BbAvD",
            "BbMxA", "BbAvA", "BbOU", "BbMx>2.5", "BbAv>2.5", "BbMx<2.5", "BbAv<2.5",
            "BbAH", "BbAHh", "BbMxAHH", "BbAvAHH", "BbMxAHA", "BbAvAHA",
            "Div", "Date", "HomeTeam", "AwayTeam", "Referee", "Attendance",
        ]
        DataFrame.drop(columns=removedColumns, errors='ignore', inplace=True)
        
        Y = DataFrame[['FTR', 'season']]
        X = DataFrame.drop('FTR', axis=1)
        
        train_seasons = seasons[:9] 
        test_seasons = seasons[9:] 
        
        YTrain = Y[Y['season'].isin(train_seasons)]
        YTest = Y[Y['season'].isin(test_seasons)]
        YTrain.drop('season', axis=1, inplace=True)
        YTest.drop('season', axis=1, inplace=True)

        XTrain = X[X['season'].isin(train_seasons)]
        XTest = X[X['season'].isin(test_seasons)]
        XTrain.drop('season', axis=1, inplace=True)
        XTest.drop('season', axis=1, inplace=True)
        
        return XTrain, XTest, YTrain, YTest
    
    except FileNotFoundError:
        print("ERRO: Arquivo 'fullData.csv' não encontrado.")
        print("Verifique o caminho e a existência do arquivo.")
        return None, None, None, None
