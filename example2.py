# main.py

import os
import pandas as pd
from indicators.sma import calculate_sma
from indicators.rsi import calculate_rsi
from indicators.ema import calculate_ema
from indicators.bollinger_bands import calculate_bollinger_bands
from indicators.macd import calculate_macd
from indicators.atr import calculate_atr

# Define the path to the price history folder
PRICE_HISTORY_FOLDER = "price_history"

# Variable to point to the specific price history file (update this variable with the filename to use)
price_file = "BNBUSDT.csv"  # Replace with your desired file


# Function to load price data from the specified CSV file
def load_price_data(filename):
    """
    Load the price data from a CSV file located in the 'price_history' folder.

    The CSV should contain the following columns in order:
    - Date
    - Open
    - High
    - Low
    - Close
    - Volume

    Any columns beyond the 6th will be ignored during extraction.

    :param filename: The name of the CSV file to load.
    :return: A Pandas DataFrame with the first 6 columns (Date, Open, High, Low, Close, Volume).
    """
    # Construct the full path to the CSV file
    file_path = os.path.join(PRICE_HISTORY_FOLDER, filename)

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {filename} not found in {PRICE_HISTORY_FOLDER} folder.")

    # Load the CSV file into a DataFrame
    try:
        # Load only the first 6 columns from the CSV file (headers will be auto-detected)
        df = pd.read_csv(file_path, usecols=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
        return df
    except Exception as e:
        raise ValueError(f"Error loading file {filename}: {e}")


# Function to calculate Simple Moving Average (SMA)
def calculate_sma_indicator(data, period=20):
    """
    Calculate and display the SMA for the given data.
    """
    data['SMA'] = calculate_sma(data, period=period)
    print(f"SMA({period}):")
    print(data[['Date', 'SMA']].tail(10))


# Function to calculate Relative Strength Index (RSI)
def calculate_rsi_indicator(data, period=14):
    """
    Calculate and display the RSI for the given data.
    """
    data['RSI'] = calculate_rsi(data, period=period)
    print(f"RSI({period}):")
    print(data[['Date', 'RSI']].tail(10))


# Function to calculate Exponential Moving Average (EMA)
def calculate_ema_indicator(data, period=20):
    """
    Calculate and display the EMA for the given data.
    """
    data['EMA'] = calculate_ema(data, period=period)
    print(f"EMA({period}):")
    print(data[['Date', 'EMA']].tail(10))


# Function to calculate Bollinger Bands
def calculate_bollinger_bands_indicator(data, period=20):
    """
    Calculate and display the Bollinger Bands for the given data.
    """
    bollinger_bands = calculate_bollinger_bands(data, period=period)
    print(f"Bollinger Bands({period}):")
    print(bollinger_bands.tail(10))


# Function to calculate MACD
def calculate_macd_indicator(data):
    """
    Calculate and display the MACD for the given data.
    """
    macd = calculate_macd(data)
    print("MACD:")
    print(macd.tail(10))


# Function to calculate Average True Range (ATR)
def calculate_atr_indicator(data, period=14):
    """
    Calculate and display the ATR for the given data.
    """
    data['ATR'] = calculate_atr(data, period=period)
    print(f"ATR({period}):")
    print(data[['Date', 'ATR']].tail(10))


# Main function to execute the script
def main():
    """
    Main execution flow of the script.
    Loads the price data from the CSV file and demonstrates how to use the individual indicator functions.
    """
    # Step 1: Load the price data from the specified CSV file
    try:
        price_data = load_price_data(price_file)
        print(f"Successfully loaded price data from {price_file}.")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return

    # Step 2: Display the first few rows of the data to verify it's loaded correctly
    print("First 6 rows of the price data:")
    print(price_data.head())

    # Step 3: Calculate indicators separately
    calculate_sma_indicator(price_data, period=20)           # Simple Moving Average
    calculate_rsi_indicator(price_data, period=14)           # Relative Strength Index
    calculate_ema_indicator(price_data, period=20)           # Exponential Moving Average
    calculate_bollinger_bands_indicator(price_data, period=20)  # Bollinger Bands
    calculate_macd_indicator(price_data)                     # MACD
    calculate_atr_indicator(price_data, period=14)           # ATR


# Entry point of the script
if __name__ == "__main__":
    main()
