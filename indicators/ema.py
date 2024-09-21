# indicators/ema.py

import pandas as pd


def calculate_ema(data: pd.DataFrame, period: int = 20) -> pd.Series:
    """
    Calculate the Exponential Moving Average (EMA) for the given data.

    :param data: A Pandas DataFrame containing at least the 'Close' price column.
    :param period: The number of periods for calculating the EMA.
    :return: A Pandas Series representing the EMA values.
    """
    if 'Close' not in data.columns:
        raise ValueError("DataFrame must contain a 'Close' column.")

    # Calculate the Exponential Moving Average
    ema = data['Close'].ewm(span=period, adjust=False).mean()

    return ema
