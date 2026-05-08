from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Perceptron
import pandas as pd
from psyke import Extractor
from psyke.utils.dataframe import get_discrete_features_equal_frequency, get_discrete_dataset
from psyke.utils.logic import pretty_theory

x, y = load_iris(return_X_y=True, as_frame=True)
x.columns = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']
iris_features = get_discrete_features_equal_frequency(x, bins=3, output=False)
x = get_discrete_dataset(x, iris_features)
y = pd.DataFrame(y).replace({"target": {0: 'setosa', 1: 'virginica', 2: 'versicolor'}})
dataset = x.join(y)
dataset.columns = [*dataset.columns[:-1], 'iris']
train, test = train_test_split(dataset, test_size=0.5, random_state=0)

for predictor in [ KNeighborsClassifier(n_neighbors=5), Perceptron()]:
    predictor.fit(train.iloc[:, :-1], train.iloc[:, -1])

    (*@\framebreak@*)
    real = Extractor.real(predictor, iris_features)
    theory_from_real = real.extract(train)
    print('Rules extracted via REAL:\n' + pretty_theory(theory_from_real))

    trepan = Extractor.trepan(predictor, iris_features)
    theory_from_trepan = trepan.extract(train)
    print('\Rules extracted via nTrepan:\n' + pretty_theory(theory_from_trepan))

    cart = Extractor.cart(predictor, iris_features)
    theory_from_cart = cart.extract(train)
    print('\Rules extracted via nTrepan:\n' + pretty_theory(theory_from_cart))
