# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:50:47 2020

@author: José Olívio
"""

import pandas as pd
import re


corpus1 = pd.read_csv("corpus-q1-v2.csv")


# Function to clean the names 
def corretor_frases(df): 
    for x in range(len(df)):
    # Inverter P2 -> 2P
    #placeholder
    
    # Simplificar sinais (+++) -> (+)
        # Substitui utilizando metacaracter \ que indica uma sequencia e o método sub
        df.iloc[x,1] = re.sub('\++','+',df.iloc[x,1])

    # Simplificar espaços 'a    b' -> 'ab'
        # Substitui utilizando metacaracter \ que indica uma sequencia e o método sub
        df.iloc[x,1] = re.sub('\s+',' ',df.iloc[x,1])
        
    # Remover hífen entre dígitos '22-22' -> '2222'
        # Primeiro procura os digitos que possuem hífen entre eles
        if(re.findall('\d-+\d',df.iloc[x,1])):
            # Substitui por '', ou seja, remove o hífen
            df.iloc[x,1] = re.sub('\-+','', df.iloc[x,1])
    
    # Remover espaços antes de locais 'Paraiba _estado' -> 'Paraiba_estado'
    
    # Remover espaços após qualificadores pela esquerda 'IS_DAR_ 3P' -> 'IS_DAR_3P'
    
    # Remover espaços à esquerda dos qualificadors de intensidade 'AMAR (+)' -> 'AMAR(+)'
    
    # Adicionar underline pós não 'NÃO QUERO' -> 'NÃO_QUERO'
        # Substitui o string 'NÃO ' por 'NÃO_'
        df.iloc[x,1] = re.sub('NÃO ','NÃO_',df.iloc[x,1])
    
    # Substituir underline por & em famosos 'EINSTEIN_FAMOSO' -> 'EINSTEIN&FAMOSO'
        # Substituição simples
        df.iloc[x,1] = re.sub('_FAMOSO','&FAMOSO',df.iloc[x,1])
    
    # Remover pontos em palavras 'OI.OK' -> 'OI OK'
        # Procura ponto entre palavras
        if(re.findall('\.\D',df.iloc[x,1])):
            # Substitui por espaço
            df.iloc[x,1] = re.sub('^\.',' ', df.iloc[x,1])
    # Acrescentar 0 em números decimais '.92' -> '0.92'
    
    return df
# Chama a função com o dataframe
q1_resposta = corretor_frases(corpus1)         
# Converte pra csv e salva o arquivo
q1_resposta.to_csv('q1_resposta.csv')





