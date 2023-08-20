# Code by Ajay K

import numpy as np
from scipy.stats import bernoulli

# Number of samples is 1000, 1 denotes success and 0 denotes failure
sim_len = int(1000)

# Probability of the event ball is red,given transferred is black,
# i.e., X=1 is 16/31
prob = 16/31

bern_dist = bernoulli.rvs(size=sim_len, p=prob)
count_success = np.nonzero(bern_dist == 1)
prob_success = np.size(count_success)/sim_len

success_sim = sim_len*(1-prob_success)
success_act = sim_len*(1-prob)

print("Probability-simulation : ", prob_success,",actual:" ,prob)
print("No. of success: ", success_sim,",actual:", success_act)
print("Sample generated:", bern_dist)
