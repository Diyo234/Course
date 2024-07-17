import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt

ecg_signal = nk.ecg_simulate(duration=30, sampling_rate=250)
signals, info = nk.ecg_process(ecg_signal, sampling_rate=250)
rpeaks = info["ECG_R_Peaks"]
cleaned_ecg = signals["ECG_Clean"]
plot = nk.events_plot(rpeaks, cleaned_ecg)
#epochs = nk.ecg_segment(cleaned_ecg, rpeaks=None, sampling_rate=250, show=True)
plt.show()  
