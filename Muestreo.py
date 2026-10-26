import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Configuración de Parámetros de Muestreo
# ==========================================
Fs = 1000          # Frecuencia de muestreo (1000 Hz)
T = 1.0 / Fs       # Período de muestreo (0.001 s)
N = 1000           # Número total de muestras
t = np.linspace(0.0, N * T, N, endpoint=False) # Vector de tiempo (1 segundo)

# Vector de frecuencias centrado en cero
freqs = np.fft.fftfreq(N, T)
freqs_shifted = np.fft.fftshift(freqs)

def obtener_espectro(senal):
    """Calcula la FFT centrada, magnitud escalada y fase filtrada."""
    X = np.fft.fft(senal)
    X_shift = np.fft.fftshift(X)
    magnitud = np.abs(X_shift) / N
    fase = np.angle(X_shift)
    fase[magnitud < 1e-4] = 0.0  # Limpieza de ruido numérico en fase
    return X_shift, magnitud, fase

# ==========================================
# 2. Generación de Señales Elementales
# ==========================================
# 2.1 Señal Senoidal de 10 Hz
x_seno = np.sin(2 * np.pi * 10 * t)

# 2.2 Pulso Rectangular (Duración de 0.2 s)
x_pulso = np.where((t >= 0.4) & (t <= 0.6), 1.0, 0.0)

# 2.3 Escalón Unitario
x_escalon = np.where(t >= 0.2, 1.0, 0.0)

# ==========================================
# 3. Graficación en Tiempo y Frecuencia
# ==========================================
lista_senales = [
    ("Señal Senoidal (10 Hz)", x_seno),
    ("Pulso Rectangular", x_pulso),
    ("Escalón Unitario", x_escalon)
]

fig, axes = plt.subplots(3, 3, figsize=(14, 9))

for idx, (nombre, senal) in enumerate(lista_senales):
    _, magnitud, fase = obtener_espectro(senal)
    
    # Tiempo
    axes[idx, 0].plot(t, senal, 'b-', linewidth=1.5)
    axes[idx, 0].set_title(f"{nombre} - Tiempo")
    axes[idx, 0].set_xlabel("Tiempo [s]")
    axes[idx, 0].set_ylabel("Amplitud")
    axes[idx, 0].grid(True)
    
    # Magnitud
    axes[idx, 1].plot(freqs_shifted, magnitud, 'r-', linewidth=1.5)
    axes[idx, 1].set_title(f"{nombre} - Magnitud |X(f)|")
    axes[idx, 1].set_xlabel("Frecuencia [Hz]")
    axes[idx, 1].set_ylabel("Magnitud")
    axes[idx, 1].set_xlim(-40, 40)
    axes[idx, 1].grid(True)
    
    # Fase
    axes[idx, 2].plot(freqs_shifted, fase, 'g-', linewidth=1.5)
    axes[idx, 2].set_title(f"{nombre} - Fase Arg(X(f))")
    axes[idx, 2].set_xlabel("Frecuencia [Hz]")
    axes[idx, 2].set_ylabel("Fase [rad]")
    axes[idx, 2].set_xlim(-40, 40)
    axes[idx, 2].grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# 4. Verificación de Propiedades
# ==========================================
# Linealidad: FFT(a*x1 + b*x2) == a*FFT(x1) + b*FFT(x2)
a, b = 2.0, 3.5
x1 = np.sin(2 * np.pi * 5 * t)
x2 = np.sin(2 * np.pi * 15 * t)

comb_lineal = a * x1 + b * x2
fft_directa = np.fft.fft(comb_lineal)
fft_propiedad = a * np.fft.fft(x1) + b * np.fft.fft(x2)

error_linealidad = np.max(np.abs(fft_directa - fft_propiedad))
print(f"Error numérico de linealidad: {error_linealidad:.2e}")