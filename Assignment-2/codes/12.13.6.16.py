import numpy as np
from scipy.stats import bernoulli

p_black_transferred = 4/7
p_red_transferred = 3/7
p_red_given_black = 4/9
p_black_given_black = 5/9
p_red_given_red = 5/9
p_black_given_red = 4/9

num_simulations = 1000

black_transferred = bernoulli.rvs(p_black_transferred, size=num_simulations)

red_drawn_given_black = np.where(black_transferred == 1, bernoulli.rvs(p_red_given_black, size=num_simulations), 0)
red_drawn_given_red = np.where(black_transferred == 0, bernoulli.rvs(p_red_given_red, size=num_simulations), 0)

black_transferred_and_red_drawn = np.sum(red_drawn_given_black)
red_transferred_and_red_drawn = np.sum(red_drawn_given_red)

p_black_transferred_given_red_drawn = black_transferred_and_red_drawn / (black_transferred_and_red_drawn + red_transferred_and_red_drawn)

print("Simulated probability:", p_black_transferred_given_red_drawn)
