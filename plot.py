import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf
import numpy as np
from matplotlib import ticker

filename = 'output_demo_strategy.csv'

data = pd.read_csv(filename)

date = pd.to_datetime(data['date'])
index = data['id']
close = data['close']
open = data['open']
high = data['high']
low = data['low']
sma10 = data['simple_moving_average']
returns = data['returns']
signals = data['signal']
buy = signals[signals == "BUY"]
buy_price = open[signals == "BUY"]
sell = signals[signals == "SELL"]
sell_price = close[signals == "SELL"]


sma10.replace(0, float('nan'), inplace=True)

fig, ax = plt.subplots()
mpf.candlestick2_ochl(ax, open, close, high, low, width=0.2, colorup='r', colordown='green', alpha=1.0)
date = date.apply(lambda x: x.strftime('%Y-%m-%d'))


def format_date(x, pos=None):
    if x < 0 or x > len(date) - 1:
        return ''
    return date[int(x)]


ax.plot(np.arange(0, len(data)), sma10, label=r'sma10')
ax.scatter(buy_price.index, buy_price.values, s=20, c='b', marker='^')
ax.scatter(sell_price.index, sell_price.values, s=20, c='y', marker='v')
ax.set_ylabel('price')
ax.set_xlabel('date')

ax2 = ax.twinx()
ax2.set_ylabel('returns')

ax2.plot(np.arange(0, len(data)), returns, color='b', linewidth=0.5, label=r'returns')
ax2.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))

plt.show()
