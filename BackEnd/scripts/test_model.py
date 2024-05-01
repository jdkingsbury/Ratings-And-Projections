import os
import pandas as pd
from ludwig.api import LudwigModel


# Load model
def load_model(model_path):
    model = LudwigModel.load(model_path)
    return model


# Load test data
def load_test_data(data_path):
    test_data = pd.read_csv(data_path)
    return test_data


# Make predictions
def make_predictions(model, test_data):
    predictions = model.predict(test_data)
    return predictions


# Evaluate model
def evaluate_model(model, test_data, actual_path):
    actuals = pd.read_csv(actual_path)
    evaluation = model.evaluate(test_data, actuals)
    return evaluation


if __name__ == "__main__":
    # Define paths
    model_path = "./results/model"
    test_data_path = "./data/get_player_game_log_2544_2023-24.csv"
    actuals_path = "./data/lebron_2023-24_actuals.csv"

    # Load model
    model = load_model(model_path)

    # Load test data
    test_data = load_test_data(test_data_path)

    # Make predictions
    predictions = make_predictions(model, test_data)
    print("Predictions: ")
    print(predictions)

    # Evaluate model
    if actuals_path:
        evaluation = evaluate_model(model, test_data, actuals_path)
        print("Evaluation: ")
        print(evaluation)
