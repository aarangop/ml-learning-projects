import tarfile
import urllib.request
from pathlib import Path

import pandas as pd


def load_housing_data() -> pd.DataFrame:
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))


def column_ratio(X):
    """
    Returns the ratio of the first column to the second column
    :param X: 2-dimensional array
    :return: 2-dimensional array where the second dimension corresponds to the ratio of the first column to the second column
    """
    return X[:, [0]] / X[:, [1]]
