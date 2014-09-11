import json
import matplotlib.pyplot as plt


summary = json.load(open("../sample/grand_summary.json", "r"))

for item in summary:
    mean_diameter = summary[item]["mean"]
    giant_component_n = summary[item]["giant_component_n"]
    plt.scatter(giant_component_n, mean_diameter)

plt.axhline(y=0)
plt.xlabel('Largest component n')
plt.ylabel('Mean geodesic distance of largest component')
plt.savefig('ps1-6c2.png')
