# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# create object
G = nx.star_graph(4)

# illustrate graph
nx.draw_networkx(G, node_color='black', labels={0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}, font_color='white',
                 edge_color='black', font_weight='bold',  node_size=700)
plt.axis('off')
plt.show()

# Uploading the temperature
Temperature_airport = pd.read_csv("weather(lentoasema).csv", dayfirst=True, sep=",",
                                  header=0, decimal=b".", index_col=0,
                                  parse_dates=[[0, 1, 2, 3]], usecols=[0, 1, 2, 3, 5])

# plotting
plt.figure(figsize=(20, 5))
plt.plot(Temperature_airport > 25, color='black', linestyle='-')
plt.title("Node B signals to A at Lappeenranta airport in July, 2018",
          fontsize=20, fontweight="bold")
plt.ylabel("Binary messages", fontweight='bold', fontsize=11)
plt.grid(True)
plt.show()

# Uploading the wind speed
windspeed_airport = pd.read_csv("windspeed(lentoasema).csv", dayfirst=True, sep=",",
                                header=0, decimal=b".", index_col=0,
                                parse_dates=[[0, 1, 2, 3]], usecols=[0, 1, 2, 3, 5])

# plotting
plt.figure(figsize=(20, 5))
plt.plot(windspeed_airport > 5, color='black', linestyle='-')
plt.title("Node C signals to A at Lappeenranta airport in July, 2018",
          fontsize=20, fontweight="bold")
plt.ylabel("Binary messages", fontweight='bold', fontsize=11)
plt.grid(True)
plt.show()

# Uploading the temperature
Temperature_lepola = pd.read_csv("weather(lepola).csv", dayfirst=True, sep=",",
                                 header=0, decimal=b".", index_col=0,
                                 parse_dates=[[0, 1, 2, 3]], usecols=[0, 1, 2, 3, 5])

# plotting
plt.figure(figsize=(20, 5))
plt.plot(Temperature_lepola > 25, color='black', linestyle='-')
plt.title("Node D signals to A at Lappeenranta Lepola station in July, 2018",
          fontsize=20, fontweight="bold")
plt.ylabel("Binary messages", fontweight='bold', fontsize=11)
plt.grid(True)
plt.show()

# Uploading the wind speed
windspeed_lepola = pd.read_csv("windspeed(lepola).csv", dayfirst=True, sep=",",
                               header=0, decimal=b".", index_col=0,
                               parse_dates=[[0, 1, 2, 3]], usecols=[0, 1, 2, 3, 5])

# plotting
plt.figure(figsize=(20, 5))
plt.plot(windspeed_lepola > 5, color='black', linestyle='-')
plt.title("Node E signals to A at Lappeenranta Lepola station in July, 2018",
          fontsize=20, fontweight="bold")
plt.ylabel("Binary messages", fontweight='bold', fontsize=11)
plt.grid(True)
plt.show()

# Plotting risky situations with signals coming from airport area
fig, ax1 = plt.subplots(figsize=(16, 6))
ax1.set_ylabel("Binary signals", color='black')
ax1.plot(Temperature_airport > 25, color='red', marker='o', linestyle='')
# right axis
ax2 = ax1.twinx()
ax2.set_ylabel("Binary signals", color='black', rotation=270, va="bottom")
ax2.plot(windspeed_airport > 5, color='blue', marker='o', linestyle='')
ax1.grid(True)
plt.title(
    "Combined signals coming from node B and node C")
plt.show()

# plotting
aux = (Temperature_airport.values > 25) & (windspeed_airport.values > 5)
plt.figure(figsize=(16, 6))
plt.plot(windspeed_airport.index, aux, color='black', marker='o', linestyle='')
plt.grid(True)
plt.title(
    "Output signals from node A based on the signals coming from node B and node C")
plt.show()

# Plotting risky situations with signals coming from lepola station area
fig, ax1 = plt.subplots(figsize=(16, 6))
# left axis
ax1.set_ylabel("Binary signals", color='black')
ax1.plot(Temperature_lepola > 25, color='red', marker='o', linestyle='')
# right axis
ax2 = ax1.twinx()
ax2.set_ylabel("Binary signals", color='black', rotation=270, va="bottom")
ax2.plot(windspeed_lepola > 5, color='blue', marker='o', linestyle='')
ax1.grid(True)
plt.title(
    "Combined signals coming from node D and node E")
plt.show()

# plotting
aux = (Temperature_lepola.values > 25) & (windspeed_lepola.values > 5)
plt.figure(figsize=(16, 6))
plt.plot(windspeed_lepola.index, aux, color='black', marker='o', linestyle='')
plt.ylim(0, 1)
plt.grid(True)
plt.title(
    "Output signals from node A based on the signals coming from node D and node E")
plt.show()
