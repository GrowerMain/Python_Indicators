# example1.py

import os
import pandas as pd

# Import individual indicators
from indicators.adl import calculate_adl
from indicators.atr import calculate_atr
from indicators.bollinger_bands import calculate_bollinger_bands
from indicators.cci import calculate_cci
from indicators.cmf import calculate_cmf
from indicators.cmo import calculate_cmo  # Ensure you have this indicator implemented
from indicators.donchian import calculate_donchian_channels
from indicators.ema import calculate_ema
from indicators.keltner import calculate_keltner_channels
from indicators.macd import calculate_macd
from indicators.obv import calculate_obv
from indicators.parabolic_sar import calculate_parabolic_sar
from indicators.rsi import calculate_rsi
from indicators.sma import calculate_sma
from indicators.stochastic import calculate_stochastic_oscillator
from indicators.williams_r import calculate_williams_r

# Define the path to the price history folder
PRICE_HISTORY_FOLDER = "price_history"

# Variable to point to the specific price history file (update this variable with the filename to use)
price_file = "BNBUSDT.csv"  # Replace with your desired file

def load_price_data(filename):
    """
    Load the price data from a CSV file located in the 'price_history' folder.

    The CSV should contain the following columns:
    - Date
    - Open
    - High
    - Low
    - Close
    - Volume

    :param filename: The name of the CSV file to load.
    :return: A Pandas DataFrame with the required columns.
    """
    # Construct the full path to the CSV file
    file_path = os.path.join(PRICE_HISTORY_FOLDER, filename)

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {filename} not found in {PRICE_HISTORY_FOLDER} folder.")

    # Load the CSV file into a DataFrame
    try:
        df = pd.read_csv(file_path, usecols=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
        return df
    except Exception as e:
        raise ValueError(f"Error loading file {filename}: {e}")

# Sample functions to demonstrate each indicator

def example_sma(data):
    """Example usage of Simple Moving Average (SMA)"""
    data['SMA_20'] = calculate_sma(data, period=20)
    print("\nSimple Moving Average (SMA):")
    print(data[['Date', 'Close', 'SMA_20']].tail(10))

def example_ema(data):
    """Example usage of Exponential Moving Average (EMA)"""
    data['EMA_20'] = calculate_ema(data, period=20)
    print("\nExponential Moving Average (EMA):")
    print(data[['Date', 'Close', 'EMA_20']].tail(10))

def example_rsi(data):
    """Example usage of Relative Strength Index (RSI)"""
    data['RSI_14'] = calculate_rsi(data, period=14)
    print("\nRelative Strength Index (RSI):")
    print(data[['Date', 'Close', 'RSI_14']].tail(10))

def example_bollinger_bands(data):
    """Example usage of Bollinger Bands"""
    bb = calculate_bollinger_bands(data, period=20)
    data = pd.concat([data, bb], axis=1)
    print("\nBollinger Bands:")
    print(data[['Date', 'Close', 'Middle Band', 'Upper Band', 'Lower Band']].tail(10))

def example_macd(data):
    """Example usage of MACD"""
    macd = calculate_macd(data)
    data = pd.concat([data, macd], axis=1)
    print("\nMACD:")
    print(data[['Date', 'MACD Line', 'Signal Line', 'MACD Histogram']].tail(10))

def example_atr(data):
    """Example usage of Average True Range (ATR)"""
    data['ATR_14'] = calculate_atr(data, period=14)
    print("\nAverage True Range (ATR):")
    print(data[['Date', 'ATR_14']].tail(10))

def example_stochastic(data):
    """Example usage of Stochastic Oscillator"""
    stoch = calculate_stochastic_oscillator(data, period=14)
    data = pd.concat([data, stoch], axis=1)
    print("\nStochastic Oscillator:")
    print(data[['Date', '%K', '%D']].tail(10))

def example_williams_r(data):
    """Example usage of Williams %R"""
    data['Williams_%R'] = calculate_williams_r(data, period=14)
    print("\nWilliams %R:")
    print(data[['Date', 'Williams_%R']].tail(10))

def example_adl(data):
    """Example usage of Accumulation/Distribution Line (ADL)"""
    data['ADL'] = calculate_adl(data)
    print("\nAccumulation/Distribution Line (ADL):")
    print(data[['Date', 'ADL']].tail(10))

def example_parabolic_sar(data):
    """Example usage of Parabolic SAR"""
    data['Parabolic_SAR'] = calculate_parabolic_sar(data)
    print("\nParabolic SAR:")
    print(data[['Date', 'Parabolic_SAR']].tail(10))

def example_cci(data):
    """Example usage of Commodity Channel Index (CCI)"""
    data['CCI_20'] = calculate_cci(data, period=20)
    print("\nCommodity Channel Index (CCI):")
    print(data[['Date', 'CCI_20']].tail(10))

def example_cmf(data):
    """Example usage of Chaikin Money Flow (CMF)"""
    data['CMF_20'] = calculate_cmf(data, period=20)
    print("\nChaikin Money Flow (CMF):")
    print(data[['Date', 'CMF_20']].tail(10))

def example_keltner_channels(data):
    """Example usage of Keltner Channels"""
    kc = calculate_keltner_channels(data, ema_period=20, atr_period=14, multiplier=2)
    data = pd.concat([data, kc], axis=1)
    print("\nKeltner Channels:")
    print(data[['Date', 'Middle Channel', 'Upper Channel', 'Lower Channel']].tail(10))

def example_obv(data):
    """Example usage of On-Balance Volume (OBV)"""
    data['OBV'] = calculate_obv(data)
    print("\nOn-Balance Volume (OBV):")
    print(data[['Date', 'OBV']].tail(10))

def example_donchian_channels(data):
    """Example usage of Donchian Channels"""
    dc = calculate_donchian_channels(data, period=20)
    data = pd.concat([data, dc], axis=1)
    print("\nDonchian Channels:")
    print(data[['Date', 'Upper Channel', 'Middle Channel', 'Lower Channel']].tail(10))

def example_cmo(data):
    """Example usage of Chande Momentum Oscillator (CMO)"""
    data['CMO_14'] = calculate_cmo(data, period=14)
    print("\nChande Momentum Oscillator (CMO):")
    print(data[['Date', 'CMO_14']].tail(10))

def main():
    """
    Main execution flow of the script.
    Loads the price data and demonstrates the use of each indicator.
    """
    # Load the price data from the specified CSV file
    try:
        price_data = load_price_data(price_file)
        print(f"Successfully loaded price data from {price_file}.")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return

    # Display the first few rows of the data
    print("First 5 rows of the price data:")
    print(price_data.head())

    # Demonstrate each indicator
    example_sma(price_data.copy())
    example_ema(price_data.copy())
    example_rsi(price_data.copy())
    example_bollinger_bands(price_data.copy())
    example_macd(price_data.copy())
    example_atr(price_data.copy())
    example_stochastic(price_data.copy())
    example_williams_r(price_data.copy())
    example_adl(price_data.copy())
    example_parabolic_sar(price_data.copy())
    example_cci(price_data.copy())
    example_cmf(price_data.copy())
    example_keltner_channels(price_data.copy())
    example_obv(price_data.copy())
    example_donchian_channels(price_data.copy())
    # Uncomment the line below if you have the CMO indicator implemented
    # example_cmo(price_data.copy())

if __name__ == "__main__":
    main()
