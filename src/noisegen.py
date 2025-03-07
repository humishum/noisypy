import numpy as np
import numpy.typing as npt
def white_noise(signal:npt.ArrayLike, freq:float):
    noise = np.random.normal(0, 1, len(signal))
    noisy_signal = signal + noise * freq
    return noisy_signal

def pink_noise(signal:npt.ArrayLike, freq:float):
    noise = np.random.randn(len(signal))
    pink_noise_signal = signal + (noise / np.arange(1, signal.__len__+1)) * freq
    return pink_noise_signal
