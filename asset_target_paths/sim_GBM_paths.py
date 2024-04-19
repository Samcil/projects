#%%
# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

#%%
# Define functions
def simulate_gbm(paths, steps, mu, sigma, s0=100):
    dt = 1 / steps
    dW = np.sqrt(dt) * np.random.normal(size=(paths, steps))
    drift = (mu - 0.5 * sigma**2) * dt
    diffusion = sigma * dW
    log_returns = np.cumsum(drift + diffusion, axis=1)
    stock_prices = s0 * np.exp(log_returns)
    return stock_prices

#%%
# Setting parameters
mu = 0.08  # Expected annual return
sigma = 0.2  # Annual volatility
num_paths = 5
num_steps = 100
stock_prices = simulate_gbm(num_paths, num_steps, mu, sigma)

#%%
# Plot simulated stock price paths
plt.figure(figsize=(10, 6))
for path in range(num_paths):
    plt.plot(stock_prices[path])
plt.title("Geometric Brownian Motion (GBM) Paths")
plt.xlabel("Time Steps")
plt.ylabel("Stock Price")
plt.show()

# %%
