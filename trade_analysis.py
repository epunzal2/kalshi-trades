# Script for Kalshi markets strategy
from process_csv import *
import matplotlib.pyplot as plt
import numpy as np


# Example usage
csv_file_path = "data/sample_trades.csv"
settlement_data = process_settlement_csv(csv_file_path)

# Print processed data
# for record in settlement_data[:5]:
#     print(record)

# Calculate row profit
# test_rows = settlement_data[:5]
# print([calculate_settlement_profit(row) for row in test_rows])
# print(sum([calculate_settlement_profit(row) for row in test_rows]))

pnls = np.array([calculate_settlement_profit(row) for row in settlement_data])

# Calculate total profit
total_pnl = sum([calculate_settlement_profit(row) for row in settlement_data])
print(f"Total profit: {total_pnl}")

# key metrics
# win rate, avg return
win_rate = np.mean(pnls > 0)
win_rate2 = np.sum(pnls > 0) / len(pnls)
avg_return = np.mean(pnls)
sharpe_ratio = np.mean(pnls) / np.std(pnls)
print(f"Key metrics: win rate: {win_rate:.2f}, avg return: {avg_return:.2f}, sharpe ratio: {sharpe_ratio:.2f}")

# visualization: histogram
plt.hist(pnls, bins=50)
plt.xlabel("PnL ($)")
plt.ylabel("Frequency")
plt.savefig("data/pnl_histogram.png")
