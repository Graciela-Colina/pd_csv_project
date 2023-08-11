import pandas as pd
import numpy as np


def list_continent():

    df = pd.read_csv('data.csv')
    search_continente = input('Escribe un continente => ')
    continente = df.loc[df['Continent']==search_continente]
    data = continente['Country/Territory']
    print(data)

list_continent()