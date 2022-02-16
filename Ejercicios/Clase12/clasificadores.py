# clasificadores.py

# import sklearn
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


iris_dataset = load_iris()
iris_dataframe = sns.load_dataset("iris")

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state = 0)

# Creamos una instancia de la clase KNeighborsClassifier
# la entrenamos con los datos de entrenamiento
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, y_train)

# Predecimos la clase de una nueva flor a partir de sus cuatro medidas
X_new = np.array([[5, 2.9, 1, 0.2]])

# Utilizamos ahora el algoritmo knn entrenado para clasificar el punto X_new
prediction = knn.predict(X_new)

# Utilizamos el 25% de los datos etiquetados que nos guardamos para evaluar cuán bien funciona nuestro clasificador
y_pred = knn.predict(X_test)
# print("Predicciones para el conjunto de Test:\n", y_pred)
# print("Etiquetas originales de este conjunto:\n", y_test)
# print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))


#%% 12.11

clf = DecisionTreeClassifier()

clf.fit(X_train, y_train)
prediction = clf.predict(X_new)
y_pred = clf.predict(X_test)
# print("Test set score: {:.2f}".format(clf.score(X_test, y_test)))


#%% 12.12

def scores(N):
    iris_dataset = load_iris()
    # iris_dataframe = sns.load_dataset("iris")
    knn = KNeighborsClassifier(n_neighbors = 1)
    clf = DecisionTreeClassifier()
    rfc = RandomForestClassifier()
    
    knn_scores = []
    clf_scores = []
    rfc_scores = []
    
    for i in range(N):
        X_train, X_test, y_train, y_test = train_test_split(
            iris_dataset['data'], iris_dataset['target'], random_state = 0)
        
        knn.fit(X_train, y_train)
        # prediction = knn.predict(X_new)
        # y_pred = knn.predict(X_test)
        knn_scores.append(knn.score(X_test, y_test))
        
        clf.fit(X_train, y_train)
        # prediction = clf.predict(X_new)
        # y_pred = clf.predict(X_test)
        clf_scores.append(clf.score(X_test, y_test))
        
        rfc.fit(X_train, y_train)
        # prediction = clf.predict(X_new)
        # y_pred = clf.predict(X_test)
        rfc_scores.append(clf.score(X_test, y_test))
    
    print("Promedio de score KNN: {:.2f}".format(sum(knn_scores) / len(knn_scores)))
    print("Promedio de score CLF: {:.2f}".format(sum(clf_scores) / len(clf_scores)))
    print("Promedio de score RFC: {:.2f}".format(sum(rfc_scores) / len(rfc_scores)))

    return
