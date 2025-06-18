import matplotlib.pyplot as plt
from components.core.statistics import calculate_mean, calculate_std
from components.core.snr import calculate_snr

def plot_signal(signal, title="Sinal", color="blue"):
    mean = calculate_mean(signal)
    std = calculate_std(signal)
    snr = calculate_snr(signal)

    plt.figure(figsize=(12, 4))
    plt.plot(signal[:200], color=color)
    plt.title(f"{title} - Primeiros 200 pontos")
    plt.xlabel("Amostras")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 4))
    plt.hist(signal, bins=50, color=color, edgecolor="black", alpha=0.7)
    plt.title(f"Histograma - {title}\nMédia: {mean:.4f}, DP: {std:.4f}, SNR: {snr:.2f} dB")
    plt.xlabel("Valor")
    plt.ylabel("Frequência")
    plt.grid(True)
    plt.tight_layout()
    plt.show()