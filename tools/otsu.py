from tools import adaptive, thresholding
from functools import reduce
import numpy as np
INFITNITY = 10000000

def calc_num_pixels_window(window):
    prod = 1
    for c in range(len(window.shape)):
        prod *= window.shape[c]
    return prod

def calcula_prob_foreground(window):
    white_pxl = window[window == 255]
    return len(white_pxl)/calc_num_pixels_window(window)

def calcula_prob_background(window):
    white_pxl = window[window == 0]
    return len(white_pxl)/calc_num_pixels_window(window)

def probs(window):
    return calcula_prob_foreground(window), calcula_prob_background(window)

def calcula_variancia_foreground(window):
    white_pxl = window[window == 255]
    if len(white_pxl) == 0:
        return INFITNITY
    N = len(white_pxl)
    mean = np.mean(white_pxl)
    var = int(
        (1/N) * reduce(lambda x0, xi: x0 + (xi - mean)**2, white_pxl)
    )
    return var

def calcula_variancia_background(window):
    black_pxl = window[window == 0]
    if len(black_pxl) == 0:
        return INFITNITY
    N = len(black_pxl)
    mean = np.mean(black_pxl)
    var = int(
        (1/N) * reduce(lambda x0, xi: x0 + (xi - mean)**2, black_pxl)
    )
    return var

def calc_weighted_variance(window):
    if calc_num_pixels_window(window) == 0:
        return INFITNITY
    prob_fg = calcula_prob_foreground(window)
    prob_bg = calcula_prob_background(window)
    if prob_bg * prob_fg == 0:
        return INFITNITY
    sigma_fg = calcula_variancia_foreground(window)
    sigma_bg = calcula_variancia_background(window)
    return sigma_fg * prob_fg + sigma_bg * prob_bg

def apply_otsu_window(window, thresholds):
    ponctuations = []
    for thresh in thresholds:
        thresholded_window = thresholding.threshold_image(
            window, [(0, thresh), (thresh, 255)], [0, 255]
        )
        value = calc_weighted_variance(thresholded_window)
        ponctuations.append({'threshold': thresh, 'value': value})
    return thresholded_window, sorted(ponctuations, key = lambda x: x['value'])[0]

def otsu(img: np.ndarray, block_size: tuple):
    block_info = adaptive.split_image_into_blocks(img, block_size)
    cp = img.copy()
    for info in block_info:
        (start_y, end_y, start_x, end_x) = info['start_y'], info['end_y'], info['start_x'], info['end_x']
        window = cp[start_y: end_y, start_x: end_x]
        if window.shape[0] == 0 or window.shape[1] == 0:
            continue
        best_threshold = otsu_window(
            window
        )
        cp[start_y: end_y, start_x: end_x] = thresholding.threshold_image(
            img=cp[start_y: end_y, start_x: end_x],
            thresholds=[(0, best_threshold), (best_threshold, 255)],
            values=[0,255]
        )
    return cp

def compute_otsu_criteria(im, th):
    thresholded_im = np.zeros(im.shape)
    thresholded_im[im >= th] = 1

    non_black_pixels = im.size
    non_black_pixels1 = np.count_nonzero(thresholded_im)
    w1 = non_black_pixels1 / non_black_pixels
    w0 = 1 - w1

    if w1 == 0 or w0 == 0:
        return INFITNITY

    white_pixels = im[thresholded_im == 1]
    black_pixels = im[thresholded_im == 0]
    var0 = np.var(black_pixels) if len(black_pixels) > 0 else 0
    var1 = np.var(white_pixels) if len(white_pixels) > 0 else 0

    return w0 * var0 + w1 * var1
    
def otsu_window(window):
    threshold_range = range(np.max(window)+1)
    criterias = list(map(lambda th: compute_otsu_criteria(window, th), threshold_range))
    best_threshold = threshold_range[np.argmin(criterias)]
    return best_threshold

if __name__ == '__main__':
    v = np.array([
        [120, 130, 140],
        [160, 170, 180],
        [190, 200, 200]
    ])
    print(otsu(v, (3,3)))