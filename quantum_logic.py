import random

def quantum_coin_flip(shots=1000):
    counts = {'0': 0, '1': 0}
    for _ in range(shots):
        outcome = random.choice(['0', '1'])  # 50/50 probability
        counts[outcome] += 1
    return counts
