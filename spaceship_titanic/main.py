import pandas as pd


def load_test_data():
    return load_data("datasets/test.csv")

def load_train_data():
    return load_data("datasets/train.csv")

def load_data(filename):
    return pd.read_csv(filename)