import random

def generate_uniform_signal(n, a=-1.0, b=1.0):
    return [random.uniform(a, b) for _ in range(n)]
