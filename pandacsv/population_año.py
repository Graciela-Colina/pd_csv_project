import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print('Puedes realizar tu estudio eligiendo alguno de estos continentes: Asia, Africa, North America, South America, Europe y Oceania')
print('Los años presentes en el csv son: 2022, 2020, 2015, 2010, 2000, 1990, 1980, 1970')
print('la poblacion mas baja es de 510 y la mas alta mil millones')

def run():
    df = pd.read_csv('data.csv')
    zona = input("Introduce un continente => ")
    years = input("Introduce un año => ")
    cantidad = input("Buscar una poblacion mayor a => ") 
    population = df[(df['Continent'] == zona) & (df[f'{years} Population'] >= int(cantidad))]
    data = population['Country/Territory'].head(10)
    population_years = population[f'{years} Population'].head(10)
 

    plt.bar(data, population_years)
    plt.title(f'Top 10 paises con una poblacion mayor a {cantidad} del contiente {zona}')
    plt.xlabel('Paises')
    plt.ylabel(f'{years} Population')
    plt.savefig(f'paisesde{zona}poblacionmayor{cantidad}en{years}.png')
    plt.show()

run()

