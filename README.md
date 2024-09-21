
# Trading Indicators Repository

Welcome to the **Trading Indicators** repository! This repository contains a collection of technical indicators commonly used in trading strategies across various markets such as stocks, cryptocurrencies, and forex. The indicators are implemented in Python and can be easily integrated into your trading systems for both backtesting and live trading purposes.

## Features

- A wide range of technical indicators, including:
  - **Moving Averages (SMA, EMA)**: Basic and exponential moving averages to smooth out price data.
  - **Relative Strength Index (RSI)**: A momentum oscillator measuring the speed and change of price movements.
  - **Bollinger Bands**: A volatility indicator using standard deviations to create upper and lower bands around an SMA.
  - **MACD (Moving Average Convergence Divergence)**: A trend-following momentum indicator showing the relationship between two moving averages.
  - **ATR (Average True Range)**: Measures market volatility by analyzing the range between highs and lows.
  - **Stochastic Oscillator**: A momentum indicator comparing a particular closing price to a range of its prices over a period.
  - **Williams %R**: A momentum oscillator similar to the stochastic oscillator that measures overbought and oversold conditions.
  - **Accumulation/Distribution Line (ADL)**: A volume-based indicator that measures money flow into and out of a security.
  - **Parabolic SAR**: A trend-following indicator providing potential reversal points in the market.
  - **Commodity Channel Index (CCI)**: A momentum-based oscillator indicating overbought or oversold conditions.
  - **Chaikin Money Flow (CMF)**: A volume-weighted average of accumulation and distribution over a specific period.
  - **Keltner Channels**: Volatility-based bands set above and below an EMA, with channel width based on ATR.
  - **On-Balance Volume (OBV)**: A momentum indicator using volume flow to predict changes in stock prices.
  - **Donchian Channels**: Formed by the highest high and lowest low over a set period of time.
  - **Chande Momentum Oscillator (CMO)**: A momentum indicator that measures the relative strength of price movements.
  
- Each indicator comes with well-documented code and explanations of how to use it in trading strategies.
- Simple and modular design to allow easy integration into existing trading systems.
- Suitable for both beginner and advanced traders who want to customize their trading algorithms.

## Getting Started

### Prerequisites

Ensure you have the following tools installed:

- Python 3.7 or higher
- Libraries like `pandas`, `numpy`, `matplotlib` (for plotting)


### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/trading-indicators.git
cd trading-indicators
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Each indicator is implemented as a separate Python module, and you can import them into your trading scripts as needed.

#### Example usage for a simple moving average:

```python
from indicators.sma import calculate_sma

# Data is expected to be in a Pandas DataFrame with a 'Close' column
sma = calculate_sma(data['Close'], period=20)
print(sma)
```

#### To calculate multiple indicators:

```python
from indicators.sma import calculate_sma
from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd

sma = calculate_sma(data, period=20)
rsi = calculate_rsi(data, period=14)
macd = calculate_macd(data)
```

### Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy Trading!
