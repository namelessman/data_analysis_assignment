import matplotlib.pyplot as plt

import pandas as pd
import os

# load ./Sample_data.csv
data = pd.read_csv(os.path.abspath('') + '/week9/Sample_Data_for_Activity (1).csv')
# Since this is a bunch, create a dataframe
df=pd.DataFrame(data)


# Create histograms for each distribution
plt.figure(figsize=(12, 8))

# Normal Distribution
plt.subplot(2, 2, 1)
plt.hist(df["Normal_Distribution"], bins=30, alpha=0.7, edgecolor="black")
plt.title("Normal Distribution")

# Uniform Distribution
plt.subplot(2, 2, 2)
plt.hist(df["Uniform_Distribution"], bins=30, alpha=0.7, edgecolor="black")
plt.title("Uniform Distribution")

# Exponential Distribution
plt.subplot(2, 2, 3)
plt.hist(df["Exponential_Distribution"], bins=30, alpha=0.7, edgecolor="black")
plt.title("Exponential Distribution")

# Poisson_Distribution
plt.subplot(2, 2, 4)
plt.hist(df["Poisson_Distribution"], bins=30, alpha=0.7, edgecolor="black")
plt.title("Poisson Distribution")

plt.tight_layout()
plt.show()