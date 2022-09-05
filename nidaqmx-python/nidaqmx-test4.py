import nidaqmx
import time
import numpy as np
import matplotlib.pyplot as plt

from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import TerminalConfiguration
from nidaqmx.constants import ExcitationSource
from nidaqmx.constants import AccelSensitivityUnits
from nidaqmx.constants import AccelUnits
from nidaqmx.constants import Edge

t = np.linspace(0, 1, 500, endpoint=True)

plt.ion()
i = 0

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_accel_chan("cDAQ1Mod2/ai0",
    name_to_assign_to_channel="accelerometer",
    terminal_config=TerminalConfiguration.DEFAULT,
    min_val=-5.0, max_val=5.0, units=AccelUnits.G,
    sensitivity=1000.0, sensitivity_units=AccelSensitivityUnits.MILLIVOLTS_PER_G,
    current_excit_source=ExcitationSource.INTERNAL,
    current_excit_val=0.004, custom_scale_name=None)

    task.timing.cfg_samp_clk_timing(rate=1000, active_edge=Edge.RISING,
    sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=100)

    while i<100:
        data = task.read(number_of_samples_per_channel=500)
        plt.plot(t, data)
        plt.grid()
        plt.pause(0.01)
        plt.gcf().clear()
        i = i + 1
        print(data)

    plt.close()


    