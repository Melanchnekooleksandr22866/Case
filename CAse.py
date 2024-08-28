import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('menu.csv')

selected_columns = ['Category', 'Item', 'Calories', 'Total Fat', 'Carbohydrates', 'Protein']
df = df[selected_columns]

df = df.dropna()

plt.figure(figsize=(10, 6))
sns.histplot(df['Calories'], bins=20, kde=True, color='blue', alpha=0.7)
plt.title('Розподіл калорійності страв')
plt.xlabel('Калорії')
plt.ylabel('Види страв')
plt.grid(True)
plt.show()

sns.pairplot(df, hue='Category')

plt.gcf().suptitle('USA |  China |  Europe |  Japan', fontsize=16, y=1.02)
plt.show()
