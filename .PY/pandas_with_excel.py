# -*- coding: utf-8 -*-
"""Pandas with excel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pj_OJux4fMrB_WtAT3B8LZiuKacr3PqG
"""

import pandas as pd

cv = pd.read_csv("CPU.xlsx")
print(cv)

cv = cv.sort_values(by='preço')
print(df)

filtro = cv.loc[cv['soquete de cpu'] == 'LGA 1151']
print(filtro)

# Certificar de que a coluna 'preço' é uma string
cv['preço'] = cv['preço'].astype(str)

# Remover caracteres não numéricos e converter para float
cv['preço'] = cv['preço'].str.replace('[^\d.]', '', regex=True).astype(float)

# Calcular a média de preços por soquete de CPU
media_por_soquete = cv.groupby('soquete de cpu')['preço'].mean()

print(media_por_soquete)