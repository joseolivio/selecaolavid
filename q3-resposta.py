# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:39:40 2020

@author: José Olívio
"""
import pandas as pd
import re

# Questão 3

# Lê os dados e armazena no dataframe do pandas
corpus3 = pd.read_csv("corpus-q3.csv")
# Separa a coluna gi do dataframe
corpus3_gi = corpus3['gi']
# Lista com as qualificadores de direcionalidade para geração dos dados
lista3 = ['1S','2S','3S','1P','2P','3P']

def text_augmentation(coluna):
    # Duas listas que irão armazenar as frases
    list = []
    list2 = []
    # Percorre as linhas da entrada
    for linhas in coluna:
        # Identifica o caso onde deverá ser substituído e faz o split, separando as partes.
        split = re.split(r'\d\D', linhas)
        # Gera uma nova lista fazendo uma junção da frase anterior segmentada com os qualificadores
        for x in lista3:
            list.append(x.join(split))
        # Itera sobre as frases geradas substituindo os qualificadores para gerar mais casos.
        for y in lista3:
            for frases in list:
                list2.append(re.sub(r'\d\D', y, frases, 1))
        
    # Cria o arquivo e escreve a resposta final, contido em list2
    with open('q3-resposta.txt', 'w') as f:
        for item in list2:
            f.write("%s\n" % item)
        
# Chama a função com a entrada para gerar o arquivo
text_augmentation(corpus3_gi)