#DISCLAIMER: This simulation is part of a lesson in the Data Scientist Carrer Track in Data Camp.

# Suppose you're betting the following with a friend:

# You're in the Empire State Building lobby and you'll throw a dice 100x.

# 1. If you get the number 1, 2 you go one step down
# 2. If you get the number 3, 4 or 5 you go one step up.
# 3. If you get the number 6, you'll throw the dice once more and you'll go x steps up. (x being the number you get)

# There is a 0.1% chance you'll fall down the stairs in the process. If this happens, you'll go to step 0 right away.

# You can't of course go below step 0.

# The bet is that after you throw the dice 100x, you'll be at least in the 60th floor.

# What's the chance of you winning this bet?

# Importing necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating seed for reproducibility
np.random.seed(508)

# Simulating random walk 10.000 times and appending it to all_walks
all_walks = []
for i in range(10000):
    random_walks = [0]
    for x in range(100):
        step = random_walks[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        #adding 0.1% chance of falling down the stairs and going to step 0
        if np.random.rand() <= 0.001:
            step = 0
        random_walks.append(step)
    all_walks.append(random_walks)

# Transforming all_walks into a numpy array
np_all_walks = np.array(all_walks)

# Getting last floor of each random walk within all_walks
ends = np_all_walks[:,100]

# Plotting histogram of ends
plt.hist(ends)
plt.show()

# Calculating chance of winning
success = np.count_nonzero(ends >= 60)
success_chance = success/10000
print(success_chance)