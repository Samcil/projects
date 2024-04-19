#%%
import random 
def estimate_pi(num_darts):
    inside_circle = 0
    for _ in range(num_darts):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_darts

#%%
num_darts = 1_000_000
pi_estimate = estimate_pi(num_darts)
print(f"Estimated value of π: {pi_estimate:.6f}")
#%%
