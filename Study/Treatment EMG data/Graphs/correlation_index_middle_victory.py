import matplotlib.pyplot as plt
from scipy.signal import correlate
from main import data_index, data_middle, data_victory


corr_index_middle = correlate(data_index, data_middle)
corr_index_victory = correlate(data_index, data_victory)
corr_middle_victory = correlate(data_middle, data_victory)

plt.scatter(range(len(corr_index_middle)*15), corr_index_middle, s=1, c='purple')
plt.title('Корреляция между указательным и средним пальцем', fontsize=12)
plt.show()

plt.scatter(range(len(corr_index_victory)*15), corr_index_victory, s=1, c='blue')
plt.title('Корреляция между указательным пальцем и жестом победы', fontsize=12)
plt.savefig('correlation_victory_and_index_all_electrodes.png')
plt.show()

plt.scatter(range(len(corr_middle_victory)*15), corr_middle_victory, s=1, c='red')
plt.title('Корреляция между средним пальцем и жестом победы', fontsize=12)
plt.savefig('correlation_victory_and_middle_all_electrodes.png')
plt.show()
