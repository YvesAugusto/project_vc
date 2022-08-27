import numpy as np
import cv2 as cv

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

def make_axis_y_from_x(histogram, indexes, range_values):
    axis = np.zeros(range_values.shape)  
    for idi, index in enumerate(indexes):
        if index[0] == index[1]:
            index[1] += 1
        axis[index[0]: index[1] + 1] = histogram[idi]
    return axis

if __name__ == '__main__':
    image = cv.imread('images/brad.jpg', 0)
    indexes, histogram = calc_histogram_vector(image)
    histogram = normalize_histogram(histogram)
    indexes, histogram = split_histogram(histogram, 20)