import matplotlib.pyplot as plt
from main import *

my_dict = {0: [data_thumb, 'Большого'], 1: [data_index, 'Указательного'], 2: [data_middle, 'Среднего'],
           3: [data_ring, 'Безымянного'], 4: [data_little, 'Маленького']}

colors = ['blue', 'red', 'gray', 'pink', 'green']

plt.figure(figsize=(10, 10))
for elem in range(5):
    plt.subplot(5, 1, elem + 1)
    plt.title(f'Показания для {my_dict[elem][1]} пальца')
    plt.plot([i for i in range(len(my_dict[elem][0]))], [i[0] for i in my_dict[elem][0]], color=colors[elem])

plt.subplots_adjust(hspace=1)
plt.show()
