# iris_seaborn.py

import sklearn
import pandas as pd
import seaborn as sns


iris_dataset = sklearn.datasets.load_iris()

# iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
# iris_dataframe['target'] = iris_dataset['target']

# pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)

iris_dataframe = sns.load_dataset("iris")

sns.pairplot(iris_dataframe, hue = "species")
