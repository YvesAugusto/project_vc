HELP_WINDOW = "Este argumento passa o tamanho da janela"
HELP_STRIDES = "Este argumento determinado a largura do passo da convolução. Exemplo: --strides 2,2"
HELP_FILEPATH = "Este argumento determinado o caminho do arquivo da imagem a ser lida"
HELP_RSZ = "Este argumento determina se a imagem será redimensionada e, caso seja, o novo tamanho de largura"
HELP_PADDING = "Este argumento determinada dois tipos de padding, 'valid' ou 'same'. O primeiro tipo " \
               "não aplica padding e reduz a dimensão da imagem na saída da convolução. O segundo tipo " \
               "aplica padding de modo a manter as dimensões da imagem na saída da convolução"
HELP_SAVE = "Este argumento determina o nome da imagem que será salva com o resultado da operação"
HELP_SIGMA = "Este argumento determina o sigma do filtro gaussiano"
def tuple_type(strings):
    strings = strings.replace("(", "").replace(")", "")
    mapped_int = map(int, strings.split(","))
    return tuple(mapped_int)