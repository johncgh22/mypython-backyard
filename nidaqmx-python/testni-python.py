from platform import mac_ver
import nidaqmx
import matplotlib.pyplot as plt

from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import BridgeConfiguration
from nidaqmx.constants import BridgeElectricalUnits
from nidaqmx.constants import ForceUnits
from nidaqmx.constants import ExcitationSource
from nidaqmx.constants import Edge

plt.ion()
i = 0

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_force_bridge_two_point_lin_chan("cDAQ1Mod4/ai0",
    name_to_assign_to_channel="loadcell",
    min_val=-100.0, max_val=100.0,
    units=ForceUnits.NEWTONS, bridge_config=BridgeConfiguration.FULL_BRIDGE,
    voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, 
    nominal_bridge_resistance=350.0, first_electrical_val=0.0, second_electrical_val=2.0,
    electrical_units=BridgeElectricalUnits.MILLIVOLTS_PER_VOLT, first_physical_val=0.0,
    second_physical_val=100.0, custom_scale_name=None)

    task.timing.cfg_samp_clk_timing(rate=100, active_edge=Edge.RISING,
    sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=100)

    while i<100:
        data = task.read(number_of_samples_per_channel=10)
        plt.scatter(i,data[0],c='r')
        plt.scatter(i,data[1],c='b')
        plt.pause(0.05)
        plt.grid()
        plt.show()
        i=i+1
        print(data) 

