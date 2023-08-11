import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def population_country():

    df = pd.read_csv('data.csv')
    pd.read_csv('data.csv')
    search_country = input('Escribe un Pais => ')
    data = df.loc[df['Country/Territory'] == search_country]
    list_population = data[['1970 Population', '1980 Population', '1990 Population', '2000 Population', '2010 Population', '2015 Population', '2020 Population', '2022 Population']]
    print(list_population)

    dict_population = {
        '1970' : int(data['1970 Population']),
        '1980' : int(data['1980 Population']),
        '1990' : int(data['1990 Population']),
        '2000' : int(data['2000 Population']),
        '2010' : int(data['2010 Population']),
        '2015' : int(data['2015 Population']),
        '2020' : int(data['2020 Population']),
        '2022' : int(data['2022 Population']),
    }
    labels = dict_population.keys()
    values = dict_population.values()
    plt.bar(labels, values)
    plt.show()

population_country()