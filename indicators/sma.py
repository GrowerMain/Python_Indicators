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
