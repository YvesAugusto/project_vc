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
parser.add_argument('--bins', '-b',  default=1,
                    type=int, help=parse.HELP_BINS)
parser.add_argument('--norm', '-n',  default=0,
                    type=int, help=parse.HELP_NORM)

matplotlib.use('TKAgg')

if __name__ == '__main__':
    args = parser.parse_args()
    img = cv.imread(args.filepath, 0)
    indexes, hist = histogram.calc_histogram_vector(img)
    indexes, hist = histogram.split_histogram(hist, args.bins)
    filename = args.filepath.split("/")[-1].split(".")[0] + "_hist"
    if args.norm:
        hist = histogram.normalize_histogram(hist)
        filename += "_norm"
    axis = histogram.make_axis_y_from_x(hist, indexes, np.arange(256))
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(img, cmap='gray')
    plt.subplots_adjust(wspace=0.25)
    ax[1].plot(np.arange(256), axis)
    plt.xticks(np.arange(0, 256, 25), fontsize=6)
    plt.yticks(fontsize=8)
    plt.show()