import nidaqmx
import time
import numpy as np
import matplotlib.pyplot as plt

from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import BridgeConfiguration
from nidaqmx.constants import BridgeElectricalUnits
from nidaqmx.constants import ForceUnits
from nidaqmx.constants import ExcitationSource
from nidaqmx.constants import Edge

Tstop = 5
Ts = 0.05
N = int(Tstop/Ts)
data = []

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_force_bridge_two_point_lin_chan("cDAQ1Mod4/ai0",
    name_to_assign_to_channel="loadcell",
    min_val=-100.0, max_val=100.0,
    units=ForceUnits.NEWTONS, bridge_config=BridgeConfiguration.FULL_BRIDGE,
    voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, 
    nominal_bridge_resistance=350.0, first_electrical_val=0.0, second_electrical_val=2.0,
    electrical_units=BridgeElectricalUnits.MILLIVOLTS_PER_VOLT, first_physical_val=0.0,
    second_physical_val=100.0, custom_scale_name=None)

    task.timing.cfg_samp_clk_timing(rate=10, active_edge=Edge.RISING,
    sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=5)

    file = open("fuerza2.txt", "w")

    def writefiledata(t, x):
        time = str(t)
        value = str(round(x, 2))
        file.write(time + "\t" + value)
        file.write("\n")

    for k in range (N):
        value = task.read()
        print("F: ", round(value,1), "[N]")
        data.append(value)
        time.sleep(Ts)
        writefiledata(k*Ts, value)

    file.close()

t = np.arange(0,Tstop,Ts)
plt.plot(t,data, "-o")
plt.title("Fuerza")
plt.grid()
plt.show()
