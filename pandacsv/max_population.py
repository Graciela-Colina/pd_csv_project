import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print('Los años presentes en el csv son: 2022, 2020, 2015, 2010, 2000, 1990, 1980, 1970')
print('Escribe uno y mira la lista de paises con mayor poblacion')

def max_population():
    
    df = pd.read_csv('data.csv')
    pd.read_csv('data.csv')
    age = input('Escribe un anio => ')
    data = df.set_index([f'{age} Population'])
    data = df.sort_values(f'{age} Population', ascending=False)
    print(data.head(10))

    plt.bar(data['Country/Territory'].head(10), data[f'{age} Population'].head(10))
    plt.title(f'10 paises con mayor poblacion en {age}')
    plt.xlabel('Paises')
    plt.ylabel(f'{age} Population')
    plt.savefig(f'top10paisesconmayorpoblacion{age}.png')
    plt.show()
    
max_population()

