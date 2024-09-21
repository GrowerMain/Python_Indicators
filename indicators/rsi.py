import pandas as pd


def calculate_rsi(data: pd.DataFrame, period: int = 14) -> pd.Series:
    """
    Calculate the Relative Strength Index (RSI) for the given data.

    :param data: A Pandas DataFrame containing at least the 'Close' price column.
    :param period: The number of periods for calculating the RSI.
    :return: A Pandas Series representing the RSI values.
    """
    if 'Close' not in data.columns:
        raise ValueError("DataFrame must contain a 'Close' column.")

    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


import pandas as pd


def calculate_sma(data: pd.DataFrame, period: int = 20) -> pd.Series:
    """
    Calculate the Simple Moving Average (SMA) for the given data.

    :param data: A Pandas DataFrame containing at least the 'Close' price column.
    :param period: The number of periods for calculating the moving average.
    :return: A Pandas Series representing the SMA values.
    """
    if 'Close' not in data.columns:
        raise ValueError("DataFrame must contain a 'Close' column.")

    return data['Close'].rolling(window=period).mean()
