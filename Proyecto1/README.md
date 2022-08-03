### Proyecto 2

## Recomendador basado en Slope One

Se trata de un recomendador de una panaderia en linea, toma como base los ratings de los productos tomados.

[Datos a analizar](./data/BasePan.csv)

El :computer: algoritmo :computer:  **Slope One** (Pendiente uno) toma el promedio de la diferencia de cada producto, este es utilizado para los productos no evaluados (los que se van a recomendar).
Estas diferencias se le suman los valores del usuario que vamos a recomendar y se dividen entre la cardinalidad (el numero de diferencias por producto).

Como es pendiente **uno** necesitamos una función **f(x) = mx + b**, donde **m = 1** (la pendiente). Para eso de define la diferencia entre los elementos **i** y **j** entre la cardinalidad de las diferencias entre el producto **i** y sus diferencias con los productos **j**. ejem(concha - todos los panes restantes con calificación)

![dev](./images/dev.png?raw=true)

Donde **itemUsuario** esta dentro del conjunto de entrenamiento **P** (producto seleccionado vs productos calificados), y **card(P** *i*, ***j*** **(X))** es la cardinalidad en conjunto de **i** y **j** dentro del conjunto de entrenamiento (diferencia de tuplas) y **(itemUsuario***i* **- itemUsuario***j* **)** la diferencia de los ratings de los usuarios sobre sus productos. 

Ya que se tiene lo anterior, hay que hacer la suma de de cada desviacion con el dato **!= 0** del usuario al que se va a recomendar y despues la sumas de todas las desviaciones que se lograron obtener y esto se divide entre la cardinalidad de todas las diferencias obtenidas

![total](./images/total.png?raw=true)

***Algunas Ventajas:***

* Es muy facil su implementación.
* Facíl de mantener.
* Funciona con pocos datos.
* Es eficiente.
* Ya que es eficiente nos permite que sea actualizable de forma muy rápida.
* A pesar de ser sencillo su precisión es adecuada dentro de ciertos rangos.

***Ejemplo:***

|Usuario|Dona|Concha|Bolillo|
|:---:|:---:|:---:|:---:|
|Paco| 4| 5|3
|Pepe| 0| 3|4
|Pita| 4| 3|?

Vamos a predecir ***?*** donde *Pita* aún no ha probado el bolillo pero si la Concha y la Dona.
Hay que obtener el promedio de las diferencias, esto será tomando los ratings de los usuarios que han probado los panes que ya probó *Pita*

Es decir tomamos a *Paco* y el *rating de Bolillo*, será nuestra referencia contra la *Dona* y lo mismo con *Pepe*. **[ (3-5) + (4-3) ]**. Ahora sobre la cardinalidad de las diferencias ***(card = 2 )*** **[ (3-5) + (4-3) ]/2**.

Ahora se rpite lo mismo con la *Dona* pero en este caso, no se podrá evaluar contra la *Dona* de Pepe ya que no tiene calificación, por lo tanto será una diferencia. **[ (3-4) ]/1**.

Tenemos que **[ (3-5) + (4-3) ]/2 = -.5** y  **[ (3-4) ]/1 = -1**, entonces a estas diferencias le sumamos los valores de *Pita* a las diferencias correspondientes.
**(-.5) + 4 = 3.5** y **(-1) + 3 = 2**, nos corresponde sumar estos dos datos **3.5 + 2 = 5.5** y lo dividimos sobre la cardinalidad de los productos evaluados **(1/2)(5.5) = 2.25**.

Por lo tanto **2.5 es nuestro posible rating al bolillo**.

Este resultado para una tabla más grande y sin productos evaluados se les obtiene su rating y se recomiendan los productos con ratings calculados mas altos.

![ejemplo](./images/ejemplo.png?raw=true)

***Code:***

[Formato Jupyter para vizualizar el proceso](RecomendadorSlopeOne.ipynb)

[Formato .py para ejecutar](RecomendadorSlopeOne.py)

# **Ejecutar:**
```
$ sudo apt install python
$ python RecomendadorSlopeOne.py
```

***Tecnologías utilizadas***
* Python 3.8
* IPython Notebook


***Bibliografia:***
>Lemire, D., & Maclachlan, A. (2005, April). Slope One Predictors for Online Rating-Based Collaborative Filtering. In SDM (Vol. 5, pp. 1–5).
>Galán Nieto, Sergio Manuel. 2007. Filtrado colaborativo y sistemas de recomendación.
>Xiaoyuan Su y Taghi M. Khoshgoftaar. 2009. A Survey of Collaborative Filtering Techniques.
