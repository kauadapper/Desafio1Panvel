def rotacionar_texto(rotacao, texto):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_rotacionado = alfabeto[rotacao:] + alfabeto[:rotacao]
    alfabeto += alfabeto.upper()
    alfabeto_rotacionado += alfabeto_rotacionado.upper()
    tabela = str.maketrans(alfabeto, alfabeto_rotacionado)
    return texto.translate(tabela)