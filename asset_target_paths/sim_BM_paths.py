#%%
import numpy as np
import matplotlib.pyplot as plt

def simulate_brownian_motion(paths, steps, mu=0.0, sigma=1.0):
    dt = 1 / steps
    dW = np.sqrt(dt) * np.random.normal(size=(paths, steps))
    W = np.cumsum(dW, axis=1)
    return W
#%% 
# Setting parameters
num_paths = 5
num_steps = 100
brownian_paths = simulate_brownian_motion(num_paths, num_steps)

#%%
# Plot the Brownian Motion paths
plt.figure(figsize=(10, 6))
for path in range(num_paths):
    plt.plot(brownian_paths[path])
plt.title("Standard Brownian Motion Paths")
plt.xlabel("Time Steps")
plt.ylabel("Asset Value")
# plt.show()