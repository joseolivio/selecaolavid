# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:40:23 2020

@author: José Olívio
"""
import pandas as pd
import json

# Questão 2

#Leitura dos dados e salvando em um dataframe do pandas
corpus2 = pd.read_csv("corpus-q2.csv")

def contador_ocorrencias(coluna):
    # Cria um dicionário vazio
    dic = dict() 
    # Itera pelas linhas do dataframe
    for linhas in coluna: 
    # Remove espaços no início e fim da string
        linhas_strip = linhas.strip()    
    # Converte tudo para minúsculos para não dar confusão
        linhas_lower = linhas_strip.lower()  
    # Separa a string nos espaços, ou seja, segrega as palavras
        palavras = linhas_lower.split(" ") 
    # Itera por cada palavra
        for x in palavras: 
        # Verifica se a palavra já se encontra no dicionário
            if x in dic: 
            # Se já estiver, incrementa o contador da palavra.
                dic[x] = dic[x] + 1
            # Se não
            else: 
            # Adiciona a palavra ao dicionário com contador 1
                dic[x] = 1             
            # Cria, ou abre, o arquivo json, em modo de escrita (w)
            with open('q2-resposta.json', 'w') as json_file:
                # Método dump converte a variável de dicionário para json
                # Ensure_ascii=False para não dar problema nos palavras acentuadas
                json.dump(dic, json_file, skipkeys=True, ensure_ascii=False,indent=0,sort_keys=False)
                
# Separando apenas a coluna gr do dataframe corpus2
corpus2_gr = corpus2['gr']
# Executa a função nos dados, gerando o arquivo.
contador_ocorrencias(corpus2_gr)