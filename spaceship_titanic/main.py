import pandas as pd


def load_test_data():
    return load_data("datasets/test.csv")


def load_train_data():
    return load_data("datasets/train.csv")


def load_data(filename):
    return pd.read_csv(filename)


def split_cabin_feature(titanic_data):
    df = titanic_data.copy()
    _cabin_data = df["Cabin"].str.split("/", expand=True)
    df[["Deck", "CabinNumber", "Side"]] = _cabin_data
    return df


def calculate_total_expenses(titanic_data):
    df = titanic_data.copy()
    df["TotalExpenses"] = df["RoomService"] + df["FoodCourt"] + df[
        "ShoppingMall"] + df["Spa"] + df["VRDeck"]
    return df


def make_expenses_categories(titanic_data, bins, labels):
    df = titanic_data.copy()
    df["ExpenseCat"] = pd.cut(df["TotalExpenses"], bins=bins, labels=labels)
    return df
