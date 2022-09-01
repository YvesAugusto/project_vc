import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import cv2 as cv
from functools import reduce
import argparse

matplotlib.use('TKAgg')

paddings_map = {
    'same': lambda im, k: (im.shape[0] + k.shape[0] - 1, im.shape[1] + k.shape[1] - 1),
    'valid': lambda im, k: (im.shape[0], im.shape[1])
}

def apply_padding(image, new_shape):
    im = image.copy()

    padded_shape = list(im.shape)
    padded_shape[0] = new_shape[0]
    padded_shape[1] = new_shape[1]
    padded_image = np.zeros(padded_shape)

    delta_y = int((new_shape[0] - im.shape[0])/2)
    delta_x = int((new_shape[1] - im.shape[1])/2)

    padded_image[
        delta_y: padded_shape[0] - delta_y,
        delta_x: padded_shape[1] - delta_x
    ] = im

    return padded_image

def conv_filter_and_window(window, kernel):
    rgb = np.zeros(window.shape[2])
    for c in range(window.shape[2]):
        result = []
        for i in range(window.shape[0]):
            result.append(window[i,:,c].dot(kernel[i,:,c]))
        rgb[c] = np.sum(result)
    return rgb

def define_window(image, center_y, center_x, start_y, start_x):
    cp = image.copy()
    return cp[
             center_y - start_y: center_y + start_y + 1,
             center_x - start_x: center_x + start_x + 1,
             :
    ]

def transform_values_to_absolute(image):
    im = image.copy()
    for c in range(im.shape[2]):
        im[:, :, c] = np.abs(im[:, :, c])
    return im

def stretch_limits(image, min, max):
    im = image.copy()
    for c in range(im.shape[2]):
        im[:, :, c] = 255 * (im[:, :, c] - im[:, :, c].min())/(im[:, :, c].max() - im[:, :, c].min())
    return im

def conv2d(img, kernel, strides=(1,1), 
           padding='same', 
           prod_function=conv_filter_and_window):

    #copy image
    image = img.copy()
    channels = 3
    # se a imagem possui menos que tres canais, reshape
    if len(image.shape) == 2:
        image = np.reshape(image, (image.shape[0], image.shape[1], 1))
        channels = 1
    # se o kernel possui menos que tres canais, reshape
    if len(kernel.shape) == 2:
        kernel = np.reshape(kernel, (kernel.shape[0], kernel.shape[1], 1))
        channels = 1
    # aplica padding
    padded_image = apply_padding(image, paddings_map[padding](image, kernel))
    # calcula os passos na direcao das linhas
    steps_on_y = int(
        np.ceil(
            (padded_image.shape[0] - kernel.shape[0] + 1) / strides[0]
        )
    )
    # calcula os passos na direcao das colunas
    steps_on_x = int(
        np.ceil(
            (padded_image.shape[1] - kernel.shape[1] + 1) / strides[1]
        )
    )
    # calcula ponto de partida nas linhas
    start_y = int((kernel.shape[0] - 1) / 2)
    # calcula ponto de partida nas colunas
    start_x = int((kernel.shape[1] - 1) / 2)
    # gera nova imagem
    new_image_shape = (
        steps_on_y, steps_on_x, channels
    )
    cp = np.zeros(new_image_shape)
    i = 0
    # calcula o ponto de chegada nas linhas
    end_y = start_y + strides[1] * steps_on_y
    for center_y in range(start_y, end_y, strides[1]):
        j = 0
        # calcula o ponto de chegada nas colunas
        end_x = start_x + strides[0] * steps_on_x
        for center_x in range(start_x, end_x, strides[0]):
            # determina janela onde se aplicara convolucao
            window = define_window(padded_image, center_y, 
                                   center_x, start_y, start_x)
            # aplica convolucao do kernel na janela
            cp[i, j, :] = prod_function(window, kernel)
            j += 1
        i += 1

    return cp

if __name__ == '__main__':
    # kernel = np.array([
    #     [0, 1,  0],
    #     [1, -4, 1],
    #     [0, 1,  0]
    # ])
    kernel = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ])
    image = cv.imread('../images/brad.jpg', 0)
    dst = cv.Laplacian(image[0:20, 0:20], cv.CV_8U)
    abs_dst = cv.convertScaleAbs(dst)
    conv_img = conv2d(image[0:20, 0:20], kernel=kernel)
    conv_img = conv_img.clip(0, 255).astype(np.uint8)
    # print(conv_img.shape)
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(abs_dst)
    ax[1].imshow(conv_img)
    plt.show()
