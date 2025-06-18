import math
import random

def generate_normal_signal(n, mu=0.0, sigma=1.0):
    samples = []
    while len(samples) < n:
        u1 = random.random()
        u2 = random.random()
        r = math.sqrt(-2.0 * math.log(u1))
        theta = 2.0 * math.pi * u2
        z1 = r * math.cos(theta)
        z2 = r * math.sin(theta)
        samples.append(mu + sigma * z1)
        if len(samples) < n:
            samples.append(mu + sigma * z2)
    return samples
