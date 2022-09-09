import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import cv2 as cv
import itertools

matplotlib.use('TKAgg')

def calc_histogram_vector(img):
    count_vector = np.zeros(256)
    for idr, row in enumerate(img):
        for idc, column in enumerate(row):
            count_vector[img[idr][idc]] += 1
    return np.array([0, 255]), np.array(count_vector)

def split_histogram(histogram_vector, bins):
    splits = np.array_split(histogram_vector, bins)
    indexes = np.array_split(np.arange(len(histogram_vector)),bins)
    histogram = map(np.sum, splits)
    indexes = map(lambda x: [x[0], x[-1]], indexes)
    return np.array(list(indexes)), np.array(list(histogram))

def normalize_histogram(histogram):
    return histogram / np.sum(histogram)

def min_max_scaler(vec):
    # Este método pega os elementos de um vetor qualquer,
    # e os transforma para a escala de (0, 255).
    vec = 255 * (vec - vec.min()) / (vec.max() - vec.min())
    return  vec.astype('uint8')

def make_axis_y_from_x(histogram, indexes, range_values):
    axis = np.zeros(range_values.shape)  
    for idi, index in enumerate(indexes):
        if index[0] == index[1]:
            index[1] += 1
        axis[index[0]: index[1] + 1] = histogram[idi]
    return axis

def cumulative_sum_histogram(hist):
    # Este método efetua a soma cumulativa de uma lista qualquer,
    # atribuindo a cada elemento (i), a soma dos seus antecessores
    # com ele mesmo
    return np.array(list(itertools.accumulate(hist, lambda p, q: p + q)))

def compute_cumulative(img, bins):
    indexes, histogram = calc_histogram_vector(img)
    indexes, histogram = split_histogram(histogram, bins)
    histogram = make_axis_y_from_x(histogram, indexes, np.arange(256))
    cum_sum = cumulative_sum_histogram(histogram)
    scaled = min_max_scaler(cum_sum)
    return scaled

def equalize_hist(img, bins):
    flatten = np.asarray(img).flatten()
    scaled = compute_cumulative(img, bins)
    equalized = scaled[flatten]
    return np.reshape(equalized, img.shape)

def transfer_histogram(origo, terminum):
    transfer_function = compute_cumulative(origo, 255)
    flatten = np.asarray(terminum).flatten()
    transfered = transfer_function[flatten]
    return np.reshape(transfered, terminum.shape)

if __name__ == '__main__':
    image = cv.imread('images/brad.jpg', 0)
    indexes, histogram = calc_histogram_vector(image)
    histogram = normalize_histogram(histogram)
    indexes, histogram = split_histogram(histogram, 20)
    equalized = equalize_hist(image, 20)
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(image, cmap='gray')
    ax[1].imshow(equalized, cmap='gray')
    plt.show()
