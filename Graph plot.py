import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File paths
file_paths = [
    r'C:\Users\nawar\Desktop\Fall_2023_Class\ECE437_Operating System\HW_Dec 3\2n7m.csv',
    r'C:\Users\nawar\Desktop\Fall_2023_Class\ECE437_Operating System\HW_Dec 3\4n7m.csv',
    r'C:\Users\nawar\Desktop\Fall_2023_Class\ECE437_Operating System\HW_Dec 3\6n7m.csv',
]

# Read CSV files into Pandas DataFrames
dfs = [pd.read_csv(file_path) for file_path in file_paths]

np_time = np.array(dfs[0]["Time"][:600])  # Use only the first 600 data points
np_c2_arrived = np.array(dfs[0]["Arrived"][:600])
np_c4_arrived = np.array(dfs[1]["Arrived"][:600])
np_c6_arrived = np.array(dfs[2]["Arrived"][:600])

np_c2_wait = np.array(dfs[0]["Waitline"][:600])
np_c4_wait = np.array(dfs[1]["Waitline"][:600])
np_c6_wait = np.array(dfs[2]["Waitline"][:600])

np_c2_rejected = np.array(dfs[0]["Rejected"][:600])
np_c4_rejected = np.array(dfs[1]["Rejected"][:600])
np_c6_rejected = np.array(dfs[2]["Rejected"][:600])

# Plotting
fig, ax = plt.subplots()
plt.plot(np_time, np_c2_arrived, 'r-D', markersize=4, linewidth='.5', label="car = 2, seats = 7")
plt.plot(np_time, np_c4_arrived, 'g-+', markersize=4, linewidth='.5', label="car = 4, seats = 7")
plt.plot(np_time, np_c6_arrived, 'b-s', markersize=4, linewidth='.5', label="car = 6, seats = 7")
plt.title("People Arrival")
plt.ylabel("Arrival #")
plt.ylim([0, 85])
plt.xlabel("Time (minutes)")
plt.xlim([0, 600])
plt.grid(linestyle='dashed')
plt.legend(loc='upper right')

fig, ax = plt.subplots()
plt.plot(np_time, np_c2_wait, 'r-D', markersize=4, linewidth='.5', label="car = 2, seats = 7")
plt.plot(np_time, np_c4_wait, 'g-+', markersize=4, linewidth='.5', label="car = 4, seats = 7")
plt.plot(np_time, np_c6_wait, 'b-s', markersize=4, linewidth='.5', label="car = 6, seats = 7")
plt.title("Waiting Queue")
plt.ylabel("# of persons in waiting")
plt.xlabel("Time (minutes)")
plt.ylim([0, 1000])
plt.xlim([0, 600])
plt.grid(linestyle='dashed')
plt.legend(loc='upper right')

fig, ax = plt.subplots()
plt.plot(np_time, np_c2_rejected, 'r-D', markersize=4, linewidth='.5', label="car = 2, seats = 7")
plt.plot(np_time, np_c4_rejected, 'g-+', markersize=4, linewidth='.5', label="car = 4, seats = 7")
plt.plot(np_time, np_c6_rejected, 'b-s', markersize=4, linewidth='.5', label="car = 6, seats = 7")
plt.title("Go Away People")
plt.ylabel("# of persons in waiting")
plt.xlabel("Time (minutes)")
plt.ylim([0, 70])
plt.xlim([0, 600])
plt.grid(linestyle='dashed')
plt.legend(loc='upper right')

plt.show()
