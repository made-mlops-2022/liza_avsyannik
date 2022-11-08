import os
import pickle

import click
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


@click.command('train')
@click.option('--input-dir', type=click.Path(),
              help='Path to splitted data')
@click.option('--output-dir', type=click.Path(),
              help='Path to store model')
def train(input_dir: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    X = pd.read_csv(os.path.join(input_dir, 'x_train.csv'))
    y = pd.read_csv(os.path.join(input_dir, 'y_train.csv'))

    model = RandomForestClassifier(max_depth=5)
    model.fit(X, y)

    with open(os.path.join(output_dir, 'rf_model.pkl'), 'wb') as f:
        pickle.dump(model, f)


if __name__ == '__main__':
    train()
