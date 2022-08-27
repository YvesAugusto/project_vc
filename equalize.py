from tools import histogram, parse
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import cv2 as cv
import argparse

PATH = "images/histogram/{}"
parser = argparse.ArgumentParser()
parser.add_argument('--filepath', '-f',
                    type=str, help=parse.HELP_FILEPATH)
parser.add_argument('--bins', '-b',  default=255,
                    type=int, help=parse.HELP_BINS)

matplotlib.use('TKAgg')

if __name__ == '__main__':
    args = parser.parse_args()
    img = cv.imread(args.filepath, 0)
    indexes, hist = histogram.calc_histogram_vector(img)
    indexes, hist = histogram.split_histogram(hist, args.bins)
    equalized = histogram.equalize_hist(img, args.bins)
    print(equalized)
    filename = args.filepath.split("/")[-1].split(".")[0] + "_hist"
    axis = hist
    if args.bins < 255:
        axis = histogram.make_axis_y_from_x(hist, indexes, np.arange(256))
    x_axis = np.arange(axis.shape[0])
    xticks = np.arange(0, axis.shape[0], 25)
    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(img, cmap='gray')
    ax[2].imshow(equalized, cmap='gray')
   
    ax[1].plot(x_axis, axis)
    plt.subplots_adjust(wspace=0.25)
    plt.xticks(xticks, fontsize=6)
    plt.yticks(fontsize=8)
    plt.subplots_adjust(wspace=0.25)
    plt.show()
