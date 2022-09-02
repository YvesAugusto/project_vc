import adaptive, thresholding
from functools import reduce
import numpy as np

def calcula_prob_foreground(window):
    white_pxl = window[window == 255]
    return len(white_pxl)/(window.shape[0] * window.shape[1])

def calcula_prob_background(window):
    white_pxl = window[window == 0]
    return len(white_pxl)/(window.shape[0] * window.shape[1])

def probs(window):
    return calcula_prob_foreground(window), calcula_prob_background(window)

def calcula_variancia_foreground(window):
    white_pxl = window[window == 255]
    if len(white_pxl) == 0:
        return 0
    N = len(white_pxl)
    mean = np.mean(white_pxl)
    var = int(
        (1/(N-1)) * reduce(lambda x0, xi: x0 + (xi - mean)**2, white_pxl)
    )
    return var

def calcula_variancia_background(window):
    black_pxl = window[window == 0]
    if len(black_pxl) == 0:
        return 0
    N = len(black_pxl)
    mean = np.mean(black_pxl)
    var = int(
        (1/(N-1)) * reduce(lambda x0, xi: x0 + (xi - mean)**2, black_pxl)
    )
    return var

def calc_weighted_variance(window):
    sigma_fg = calcula_variancia_foreground(window)
    sigma_bg = calcula_variancia_background(window)
    prob_fg = calcula_prob_foreground(window)
    prob_bg = calcula_prob_background(window)
    return sigma_fg * prob_fg + sigma_bg * prob_bg

def apply_otsu_window(window, thresholds):
    ponctuations = []
    for thresh in thresholds:
        thresholded_window = thresholding.threshold_image(
            window, [(0, thresh), (thresh, 255)], [0, 255]
        )
        print(thresholded_window)
        value = calc_weighted_variance(thresholded_window)
        ponctuations.append({'threshold': thresh, 'value': value})
    print(ponctuations)
    return sorted(ponctuations, key = lambda x: x['value'])[0]
    

if __name__ == '__main__':
    v = np.array([
        [120, 130, 140],
        [160, 170, 180],
        [190, 200, 200]
    ])
    print(apply_otsu_window(v, [100, 150, 160, 170, 180]))