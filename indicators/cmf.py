# indicators/cmf.py

import pandas as pd


def calculate_cmf(data: pd.DataFrame, period: int = 20) -> pd.Series:
    """
    Calculate the Chaikin Money Flow (CMF) for the given data.

    :param data: A Pandas DataFrame containing 'High', 'Low', 'Close', and 'Volume' columns.
    :param period: The number of periods for calculating the CMF.
    :return: A Pandas Series representing the CMF values.
    """
    if not {'High', 'Low', 'Close', 'Volume'}.issubset(data.columns):
        raise ValueError("DataFrame must contain 'High', 'Low', 'Close', and 'Volume' columns.")

    money_flow_multiplier = ((data['Close'] - data['Low']) - (data['High'] - data['Close'])) / (
                data['High'] - data['Low'])
    money_flow_volume = money_flow_multiplier * data['Volume']
    cmf = money_flow_volume.rolling(window=period).sum() / data['Volume'].rolling(window=period).sum()

    return cmf
