from scipy import stats
import numpy as np

chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    u_stat, p_value = stats.mannwhitneyu(x, y)
    return p_value < 0.01
