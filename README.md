# project_vc
Primeiro Trabalho da disciplina de Visão Computacional

## 1. Clone this repository
``` shell
> git clone git@github.com:YvesAugusto/project_vc.git
```
## 2. Install poetry: 
``` shell
> pip install poetry
```
## 3. Activate virtual environment and install dependencies:
``` shell
> poetry shell
> poetry install
```
## Run some examples - low-pass filters
Lets run mean filter on a (3x3) kernel with a (2, 2) strides step, using the default padding. 
``` shell
> python3 media.py --filepath images/brad.jpg --window_size 3,3 --strides 2,2 --padding "same"
```
Lets run median filter on a (5x5) kernel with a (1, 1) strides step, using the default padding. 
``` shell
> python3 mediana.py --filepath images/brad.jpg --window_size 5,5 --strides 1,1 --padding "same"
```
Lets run gaussian filter on a (5x5) kernel with σ = 1.5, using the default padding. 
``` shell
> python3 mediana.py --filepath images/brad.jpg --window_size 5,5 --sigma 1.5
```
## Run some examples - high-pass filters
Lets run prewitt, sobel and laplacian filters on brad pitt image
``` shell
> python3 prewitt.py --filepath images/brad.jpg
> python3 sobel.py --filepath images/brad.jpg
> python3 laplaciano.py --filepath images/brad.jpg
```
## Run some examples - histogram and histogram equalization
Show histogram using 30 bins
``` shell
> python3 show_histogram.py --filepath images/test.jpg --bins 30
```
Equalize image histogram with 50 bins
``` shell
> python3 equalize.py --filepath images/test.jpg --bins 50
```
## Run some examples - multi-thresholding
Set pixels between 0 and 50 to 0, pixels between 50 and 160 to 127 and those ones between 160 and 255 to 255
``` shell
> python3 threshold.py --filepath images/lena.png --limiares 0,50 50,160 160,255 --valores 0 127 255
```
## Run some examples - adaptive thresholding
Apply adaptive thresholding dividing the image onto (32x32) block sizes
``` shell
> python3 adaptive.py --filepath images/test.jpg --block_size 32,32
```
## Run some examples - OTSU thresholding
Apply OTSU thresholding to image
``` shell
> python3 otsu.py --filepath images/test.jpg
```
## If you have doubts, ask for help
You can see the argparse parameters using --help command
``` shell
> python3 mediana.py --help
usage: mediana.py [-h] [--filepath FILEPATH] [--strides STRIDES] [--window_size WINDOW_SIZE]
                  [--resize_width RESIZE_WIDTH] [--sigma SIGMA] [--padding {same,valid}]
                  [--save_filename SAVE_FILENAME]

options:
  -h, --help            show this help message and exit
  --filepath FILEPATH, -f FILEPATH
                        Este argumento determinado o caminho do arquivo da imagem a ser lida
  --strides STRIDES, -s STRIDES
                        Este argumento determinado a largura do passo da convolução. Exemplo: --strides 2,2
  --window_size WINDOW_SIZE, -w WINDOW_SIZE
                        Este argumento passa o tamanho da janela
  --resize_width RESIZE_WIDTH, -rsz RESIZE_WIDTH
                        Este argumento determina se a imagem será redimensionada e, caso seja, o novo tamanho de
                        largura
  --sigma SIGMA, -sig SIGMA
                        Este argumento determina o sigma do filtro gaussiano
  --padding {same,valid}, -p {same,valid}
                        Este argumento determinada dois tipos de padding, 'valid' ou 'same'. O primeiro tipo não
                        aplica padding e reduz a dimensão da imagem na saída da convolução. O segundo tipo aplica
                        padding de modo a manter as dimensões da imagem na saída da convolução
  --save_filename SAVE_FILENAME, -svf SAVE_FILENAME
                        Este argumento determina o nome da imagem que será salva com o resultado da operação
```

