import math

def compute_mean(signal):
    return sum(signal) / len(signal)

def compute_std(signal, mean=None):
    if mean is None:
        mean = compute_mean(signal)
    variance = sum((x - mean) ** 2 for x in signal) / len(signal)
    return math.sqrt(variance)