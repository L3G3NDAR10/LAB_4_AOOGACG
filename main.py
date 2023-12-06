import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Зчитуємо датасет з файлу
dataset = np.loadtxt('DS8.txt')

# Ділимо датасет на зв'язані області
vor = Voronoi(dataset)

# Знаходимо центри ваги зв'язаних областей
regions = vor.regions
valid_regions = [region for region in regions if -1 not in region and len(region) > 0]
centers = np.array([np.mean(vor.vertices[region], axis=0) for region in valid_regions if len(region) > 0])

# Встановлюємо розміри вікна
fig, ax = plt.subplots(figsize=(960/80, 540/80), dpi=80)

# Відображаємо центри ваги кругами
ax.scatter(centers[:, 0], centers[:, 1], s=5, c='red', marker='o')

# Побудована діаграма Вороного
voronoi_plot_2d(vor, ax=ax)

# Відображаємо точки вихідного датасету
ax.scatter(dataset[:, 0], dataset[:, 1], s=5, c='black', alpha=0.1)

# Зберігаємо результат у файл графічного формату
plt.savefig('output.png')

# Виводимо результат на екран
plt.show()