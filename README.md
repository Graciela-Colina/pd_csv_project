# Proyecto CVS con pandas

El proyecto consiste en la lectura de un csv usando pandas.
En el csv se encuentra 6 continentes con sus respectivos paises.
Cada pais tiene la poblacion de los años 2022, 2020, 2015, 2010, 2000, 1990, 1980, 1970.
 
En cada modulo hay una busqueda particular

- list_continentes = Permite seleccionar un continente y te dira la lista de paises de ese continente. Lo cual te ayudara en el modulo de population_country.

- population_country = Te permite digitar un pais y arrojara la poblacion de este pais a traves de los años, con una grafica que quuedara guardada.

- max_population = Te permite conocer el TOP10 de los paises con mayor poblacion en el año que digites.

- min_population = Te permite conocer el TOP10 de los paises con menor poblacion en el año que digites.

- popilation_año = Nos facilita una busqueda mas especifica. Digitamos primero el continente, luego un año y despues a partir de que cantidad de poblacion queremos buscar.


## Paso 1: Clonar el repositorio


## Paso 2: Instalar las dependencias del archivo requeriments.txt

``` sh
pip3 install -r requeriments.txt
```

## Paso 2: Buscar la carpeta

``` sh
cd pandacsv
```

## Paso 3: Correr el programa que quieras usar en la terminal 

- lista de continentes
``` sh
python3 list_continentes.py
```

- Poblacion de paises a traves de los años
``` sh
python3 population_country.py
```

- Top 10 Paises con mas poblacion
``` sh
python3 max_population.py
```

- Top 10 Paises con menos poblacion
``` sh
python3 min_population.py
```

- Top 10 Paises de un continente con poblacion mayor a la que elijas
``` sh
python3 popilation_año.py
```