import pandas as pd
import numpy as np
import scipy.stats as sps
from scipy.stats import mannwhitneyu

chat_id = 163596104 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    
    pvalue = mannwhitneyu(x, y, alternative=alternative).pvalue
    
    alpha = 0.06
    return pvalue < alpha

