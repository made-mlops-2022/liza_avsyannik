import json
import os
import pickle

import click
import pandas as pd


@click.command('predict')
@click.option('--input-dir', type=click.Path(),
              help='Path to input data')
@click.option('--model-dir', type=click.Path(),
              help='Path to model')
@click.option('--output-dir', type=click.Path(),
              help='Path to store metrics')
def predict(input_dir: str, model_dir: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    X = pd.read_csv(os.path.join(input_dir, 'train_data.csv'))  # processed data

    with open(os.path.join(model_dir, 'rf_model.pkl'), 'rb') as model_file:
        model = pickle.load(model_file)
    y_pred = model.predict(X)
    pd.DataFrame(y_pred).to_csv(os.path.join(output_dir, 'predictions.csv'), index=False)


if __name__ == '__main__':
    predict()
