import json
import matplotlib.pyplot as plt


summary = json.load(open("../sample/grand_summary.json", "r"))

for item in summary:
    max_diameter = summary[item]["max"]
    network_size = summary[item]["network_size"]
    plt.scatter(network_size, max_diameter)

plt.axhline(y=0)
plt.xlabel('Network size')
plt.ylabel('Max diameter')
plt.savefig('ps1-6c1.png')
