from main import data_index, data_middle
import matplotlib.pyplot as plt
from scipy.signal import correlate

# Only for 1 electrode
auto_index_correlate = correlate([i[0] for i in data_index], [i[0] for i in data_index])
index_middle_correlate = correlate([i[0] for i in data_index], [i[0] for i in data_middle])

plt.scatter(range(len(index_middle_correlate)), index_middle_correlate, s=1, c='green')
plt.title('Корреляция указательного и среднего пальцев', fontsize=12)
plt.show()

plt.scatter(range(len(auto_index_correlate)), auto_index_correlate, s=1, c='black')
plt.title('Автокорреляция для указательного пальца', fontsize=12)
plt.show()
