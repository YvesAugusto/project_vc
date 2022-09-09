from tools import histogram, parse
import matplotlib.pyplot as plt
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
    equalized = histogram.equalize_hist(img, args.bins)
    filename = args.filepath.split("/")[-1].split(".")[0] + "_hist_{}_bins.png".format(args.bins)
    fig, ax = plt.subplots(1, 2, sharex=False)
    ax[0].imshow(img, cmap='gray')
    plt.subplots_adjust(wspace=0.5)
    ax[1].imshow(equalized, cmap='gray')
    plt.subplots_adjust(wspace=0.5)
    plt.show()
    cv.imwrite(PATH.format(filename), equalized)
