import math
from components.core.stats import compute_mean, compute_std

def compute_snr(signal, mean=None, std=None):
    if mean is None:
        mean = compute_mean(signal)
    if std is None:
        std = compute_std(signal, mean)
    signal_power = mean ** 2
    noise_power = std ** 2
    if noise_power == 0:
        return float('inf'), math.inf
    snr_lin = signal_power / noise_power
    snr_db = 10.0 * math.log10(snr_lin)
    return snr_lin, snr_db
