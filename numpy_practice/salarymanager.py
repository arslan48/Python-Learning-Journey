import numpy as np

# 3 departments, 4 employees each
salaries = np.array([[25000, 30000, 28000, 32000],  # HR
                     [45000, 50000, 48000, 52000],  # IT
                     [35000, 38000, 36000, 40000]]) # Sales

def give_raise(salaries, raise_amount):
    updated = salaries + raise_amount.reshape(3, 1)
    return updated

def get_stats(salaries):
    return np.mean(salaries,axis= 1)
