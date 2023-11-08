#Need a dataframe for the 2d V1-V2 phase space, no need to analyse current for the capacitors
#Need to consider getting Data for the V-I characteristic of the Chua Diode

import numpy as np
import matplotlib as plt
import pandas as pd

df = pd.read_csv("V1-against-V2 with less data points.xlsx")
print(df)
#names=["Time (s)", "V1 (V)", "V2 (V)"]