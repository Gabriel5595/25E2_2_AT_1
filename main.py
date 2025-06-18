from components.core.normal_signal import generate_normal_signal
from components.core.uniform_signal import generate_uniform_signal
from components.core.stats import compute_mean, compute_std
from components.core.snr import compute_snr

# parâmetros
N_SAMPLES = 10_000
MU_X1 = 1.0
SIGMA_X1 = 0.1

# geração
x1 = generate_normal_signal(N_SAMPLES, MU_X1, SIGMA_X1)
x2 = generate_uniform_signal(N_SAMPLES, -1.0, 1.0)

# estatísticas
mean_x1 = compute_mean(x1)
std_x1  = compute_std(x1, mean_x1)
snr_lin_x1, snr_db_x1 = compute_snr(x1, mean_x1, std_x1)

mean_x2 = compute_mean(x2)
std_x2  = compute_std(x2, mean_x2)
snr_lin_x2, snr_db_x2 = compute_snr(x2, mean_x2, std_x2)

# saída
print("===== RESULTADOS =====")
print(f"x1  (Normal): média = {mean_x1:.5f},  desvio-padrão = {std_x1:.5f}")
print(f"                    SNR = {snr_lin_x1:.5f}  ({snr_db_x1:.2f} dB)")
print(f"x2 (Uniforme): média = {mean_x2:.5f},  desvio-padrão = {std_x2:.5f}")
print(f"                    SNR = {snr_lin_x2:.5f}  ({snr_db_x2:.2f} dB)")

# gráficos
if __name__ == "__main__":
    try:
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(1, 2, figsize=(10, 4), tight_layout=True)
        axs[0].hist(x1, bins=60)
        axs[0].set_title("Histograma de x1 (Normal)")
        axs[0].set_xlabel("Amplitude")
        axs[0].set_ylabel("Frequência")

        axs[1].hist(x2, bins=60)
        axs[1].set_title("Histograma de x2 (Uniforme)")
        axs[1].set_xlabel("Amplitude")

        plt.show()
    except ImportError:
        print("\nMatplotlib não encontrado – pulei a geração dos gráficos.")
