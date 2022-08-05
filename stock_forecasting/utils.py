#import requirements
from typing import Tuple
from datetime import timedelta, datetime
import pandas as pd

def slicer(df:pd.DataFrame) -> Tuple[pd.DataFrame, ...]:
    """
    Generates timeseries slicing for training
    """
    startDate = df.index.min()
    endDate = df.index.max()

    percTrain = .7 #porcentaje del subset
    percVal = .2
    percTest = .1

    difDate = (endDate - startDate).days

    startTest = endDate - timedelta(days = difDate*percTest)
    startVal = startTest - timedelta(days = difDate*percVal)

    df_train = df[df.index < startVal].drop(columns="Name")
    df_val = df[(df.index > startVal) & (df.index < startTest)].drop(columns="Name")
    df_test = df[df.index > startTest].drop(columns="Name")

    return (df_train, df_val, df_test)


def load() -> Tuple[pd.DataFrame, ...]:
    """
    Generates dataframes for model training through local csv data loading
    """
    csv_path = "../stock_forecasting/stock_data/Compiled/all_stocks_2006-01-01_to_2018-01-01.csv"
    df = pd.read_csv(csv_path)

    df['Date']=pd.to_datetime(df['Date'])
    resample_df = df.set_index("Date")

    df['Open']=df['Open'].fillna(method='ffill')
    df['High']=df['High'].fillna(method='ffill')
    df['Low']=df['Low'].fillna(method='ffill')

    return (df,resample_df)