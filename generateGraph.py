import matplotlib.pyplot as plt
from accuracies import getAccuracies

results = getAccuracies()

plt.figure(figsize=(8, 5))
bars = plt.bar(results.keys(), results.values(), color='#54a3e8')
plt.ylabel('Accuracy')
plt.ylim(0.45, 0.59)  
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='-', alpha=0.2)
plt.tight_layout()
plt.savefig("accuracy_comparison.png", format="png", dpi=300)  
plt.show()