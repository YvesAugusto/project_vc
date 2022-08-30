def threshold_window(window, threshold_min, threshold_max, value):
    thresholded_window = window.copy()
    for idr in range(thresholded_window.shape[0]):
        for idc in range(thresholded_window.shape[1]):
            cond1 = (thresholded_window[idr][idc] > threshold_min)
            cond2 = (thresholded_window[idr][idc] <= threshold_max)
            if cond1 and cond2:
                thresholded_window[idr][idc] = value
    return thresholded_window

def threshold_image(img, thresholds, values):
    image = img.copy()
    for idt, t_pair in enumerate(thresholds):
        image = threshold_window(image, t_pair[0], t_pair[1], values[idt])
    return image