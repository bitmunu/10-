import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def generate_wave(freq, amp, phase, x):
    return amp * np.sin(2 * np.pi * freq * x + phase)


def update(val):
    x = np.linspace(0, 2 * np.pi, 1000)
    wave1 = generate_wave(freq1.val, amp1.val, 0, x)
    wave2 = generate_wave(freq2.val, amp2.val, 0, x)

    ax_result.clear()
    ax_result.plot(x, wave1 + wave2)
    ax_result.set_title('1 + 2')

    ax_wave1.clear()
    ax_wave1.plot(x, wave1)
    ax_wave1.set_title('волна номер 1')

    ax_wave2.clear()
    ax_wave2.plot(x, wave2)
    ax_wave2.set_title('волна номер 2')

    plt.draw()


fig, (ax_wave1, ax_wave2, ax_result) = plt.subplots(3, 1, figsize=(8, 6), tight_layout=True)
initial_freq1 = 1.0
initial_amp1 = 0.5
initial_freq2 = 3.2
initial_amp2 = 0.6767

freq1 = Slider(ax_wave1, 'частота', 0.1, 10.0, valinit=initial_freq1)
amp1 = Slider(ax_wave1, 'амплитуда', 0.1, 2.0, valinit=initial_amp1)

freq2 = Slider(ax_wave2, 'частота', 0.1, 10.0, valinit=initial_freq2)
amp2 = Slider(ax_wave2, 'амплитуда', 0.1, 2.0, valinit=initial_amp2)

freq1.on_changed(update)
amp1.on_changed(update)
freq2.on_changed(update)
amp2.on_changed(update)

update(None)

plt.show()
