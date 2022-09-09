from tools import histogram, parse
import matplotlib.pyplot as plt
import matplotlib
import cv2 as cv
import numpy as np
import argparse

PATH = "images/transfer_style/{}"
parser = argparse.ArgumentParser()
parser.add_argument('--origo', '-o',
                    type=str, help=parse.HELP_FILEPATH)
parser.add_argument('--terminum', '-t',
                    type=str, help=parse.HELP_FILEPATH)

matplotlib.use('TKAgg')

if __name__ == '__main__':
    args = parser.parse_args()
    origo = cv.imread(args.origo, 0)
    terminum = cv.imread(args.terminum, 0)
    equalized = histogram.transfer_histogram(origo, terminum)
    filename_origo = args.origo.split("/")[-1].split(".")[0]
    filename_terminum = args.terminum.split("/")[-1].split(".")[0]
    filename = "from_{}_to_{}.png".format(filename_origo, filename_terminum)
    fig, ax = plt.subplots(1, 3, sharex=False)
    ax[0].imshow(terminum, cmap='gray')
    plt.subplots_adjust(wspace=0.5)
    ax[1].imshow(origo, cmap='gray')
    plt.subplots_adjust(wspace=0.5)
    ax[2].imshow(equalized, cmap='gray')
    plt.subplots_adjust(wspace=0.5)
    plt.show()
    cv.imwrite(PATH.format(filename), equalized)
