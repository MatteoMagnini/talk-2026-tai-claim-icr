from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Perceptron
import pandas as pd
from psyke import Extractor
from psyke.utils.dataframe import get_discrete_features_equal_frequency, get_discrete_dataset
from psyke.utils.logic import pretty_theory

x, y = # TODO load CCPP (https://archive.ics.uci.edu/ml/datasets/combined+cycle+power+plant)
x.columns = ['AT', 'V', 'AP', 'RH', 'PE']
# TODO 
