import matplotlib.pyplot as plt
import numpy as np
import imutils
import argparse
import cv2 as cv

def apply_fourier(orig, modif):
    orig = imutils.resize(orig, width=200)
    modif = imutils.resize(modif, width=200)
    orig_spectrum = np.fft.fftshift(np.fft.fft2(orig))
    mod_spectrum = np.fft.fftshift(np.fft.fft2(modif))

    fig, ax = plt.subplots(2, 2, figsize=(15, 15))
    ax[0, 0].imshow(orig, cmap='gray')
    ax[0, 1].imshow(modif, cmap='gray')
    ax[1, 0].imshow(np.log(abs(orig_spectrum)))
    ax[1, 1].imshow(np.log(abs(mod_spectrum)))

    plt.show()

parser = argparse.ArgumentParser()
parser.add_argument('--img1', type=str, required=True)
parser.add_argument('--img2', type=str, required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    orig = cv.imread(args.img1, 0)
    modif = cv.imread(args.img2, 0)
    apply_fourier(orig, modif)