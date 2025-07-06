import numpy as np
from scipy.io.wavfile import write
import os

def generate_tone(frequency=13.0, duration=240, sample_rate=44100, amplitude_ratio=0.9, filename=None):
    """
    İstenilen frekansta ve sürede 16-bit PCM WAV dosyası oluşturur.

    Args:
        frequency (float): Tonun frekansı (Hz).
        duration (int or float): Ses süresi (saniye).
        sample_rate (int): Örnekleme hızı (Hz).
        amplitude_ratio (float): Maks amplitude oranı (0.0 - 1.0).
        filename (str or None): Kaydedilecek dosya adı. None ise otomatik isimlendirilir.

    Returns:
        str: Kaydedilen dosyanın tam yolu.
    """

    max_amplitude = 32767  # 16-bit için maksimum değer
    amplitude = max_amplitude * amplitude_ratio

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    signal_int16 = signal.astype(np.int16)

    if filename is None:
        filename = f"smr_{frequency:.2f}hz_{duration}s.wav"

    write(filename, sample_rate, signal_int16)

    return os.path.abspath(filename)

# Örnek kullanım
if __name__ == "__main__":
    path = generate_tone(frequency=14.5, duration=240)
    print(f"Dosya başarıyla oluşturuldu: {path}")
